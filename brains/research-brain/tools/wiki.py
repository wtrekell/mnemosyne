#!/usr/bin/env python3
"""Helper CLI for the LLM wiki, backed by a derived SQLite/FTS5 index.

The wiki root is the directory containing tools/ (it may sit inside any host repository, or
none). Markdown under wiki/ is the source of truth. `.wiki.db` (wiki root) is a disposable index:
every command first syncs it (mtime+size, then content hash, per file; deleted files are
dropped), so answers are never stale. Delete the file or run `reindex --full` at any time;
nothing is stored only in the DB. raw/ write-once baselines live in raw-manifest.tsv (wiki root,
plain text, meant to be versioned with the directory); the DB only caches them (see below).

Usage:
  wiki.py search <terms...> [-n 10] [-s] [--all] [--prefix] [--type T] [--tag T] [--all-chunks] [--no-cutoff]
                                      ranked FTS5/BM25 search, one line per page:
                                      path:line_start-line_end  heading  description
                                      -s adds a snippet line; --all requires every term (AND);
                                      --prefix makes terms prefix matches; --all-chunks lists
                                      every matching section instead of the best per page.
                                      Read the line range, not the whole file.
  wiki.py lint [files...]             structural health check (exit 1 on errors), including
                                      raw/ write-once violations; with files, report only
                                      problems in those files
  wiki.py new <type> <slug> [-t T]    create a page with valid frontmatter
  wiki.py backlinks <page>            list pages linking to <page>
  wiki.py status [path]               list unprocessed raw files; path may be a file
                                      or directory under raw/ (default: all of raw/)
  wiki.py captured <url-or-path>...   already captured? one line per matching raw file:
                                      raw/path  captured=D  method=M  page=wiki/sources/x.md|-
                                      exit 1 if any argument has no capture
  wiki.py provenance <page>... | --all [--method M]
                                      capture_method of every raw file behind a page, via its
                                      sources: list (a source page uses its own raw:):
                                      path  slug=method ...  (unknown = no capture_method)
  wiki.py log [-n 5]                  show the last N log entries
  wiki.py digest [--days 30]          read-only health report: queue, lint, stale pages,
                                      unsupported pages, recent activity
  wiki.py eval [-v]                   run tools/eval/questions.tsv through `search`:
                                      hit@1, hit@3, mean output size
  wiki.py reindex [--full] [--accept-raw PATH...]
                                      force a sync; --full drops and rebuilds the whole index
                                      (raw/ baselines are reloaded from raw-manifest.tsv, so
                                      violations survive); --accept-raw re-baselines the named
                                      raw files (globs work) in the manifest and the cache.
                                      There is deliberately no accept-everything flag.
  wiki.py doctor                      integrity-check the index, re-hash every raw file, and
                                      compare the index to the files

Index tables: pages, aliases, tags, sources, chunks (one row per heading section, with line
range), links (wikilinks by filename stem; unresolved targets kept), fts (FTS5 over
title/aliases/description/heading/body, rowid = chunks.id; it is the only copy of chunk text).
Seam for sqlite-vec: add a vec0 table keyed by chunks.id and reuse vectors across rebuilds
via chunks.hash; not built.

raw-manifest.tsv (source of truth for raw/ baselines): header line, then one row per tracked
raw file sorted by path: path, size, sha256, source, captured, capture_method (tab-separated,
empty = absent; \t \n \r \\ escaped). Tracked = every file under raw/ except dotfiles;
raw/assets/ is included so binary captures are write-once checked too (assets are never
"unprocessed" and have no frontmatter). capture_method is never defaulted. size is
informational; sha256 is the check. It is created on first run (header-only when raw/ is empty,
so its presence shows tracking is active and its loss is visible to version control) and written
atomically (temp file + rename).

raw_files caches the manifest plus the last observed mtime_ns/size/hash. Sync is mtime+size
first, sha256 only when those differ; nothing depends on today's date. Reconciliation: a
manifest row always wins over the cache; a cached baseline absent from the manifest is written
back from the cache (never from current content); a file never seen before is baselined from
its content and appended (the normal capture path, no extra step). If a file no longer matches
its baseline, `seen_hash` records it and lint (error) / doctor report a write-once violation;
the baseline is NOT updated. A deleted file keeps its row (missing=1), also a violation. Because
baselines come from the manifest, a raw file edited while .wiki.db was gone is still a violation
after the rebuild. The only re-baseline is `reindex --accept-raw PATH...`. If the manifest does
not parse, lint/doctor report it, the cache is used as is, and nothing is written until it is
fixed. Limit: if both the manifest and .wiki.db are lost, current content becomes the baseline.

Source normalization (for `captured`): trim whitespace; for URLs lowercase the scheme and host
and drop trailing "/" from the path (query and fragment kept verbatim; http/https, www. and
default ports are NOT unified); for local paths drop a trailing "/". Nothing else.

A source page's `raw:` may point outside raw/ (e.g. `raw: llm-wiki.md`, a document kept at the
wiki root). That is valid when the file exists; it is reported as `not-a-capture` by provenance
and is not write-once tracked.
"""
import argparse
import hashlib
import os
import posixpath
import re
import sqlite3
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
MANIFEST = ROOT / "raw-manifest.tsv"
MANIFEST_COLS = ("path", "size", "sha256", "source", "captured", "capture_method")
DB_PATH = ROOT / ".wiki.db"
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
WORD_RE = re.compile(r"\w+")
REQUIRED_FM = ("title", "type", "description", "tags", "sources", "updated")
TYPES = {"source", "entity", "concept", "analysis", "overview"}
SPECIAL = {"index", "log"}
FOLDERS = {"source": "sources", "entity": "entities", "concept": "concepts", "analysis": "analyses"}

# --- index configuration (changing TOKENIZER / CHUNK_* / META_ALL triggers an automatic rebuild) ---
TOKENIZER = "porter unicode61 remove_diacritics 2"
WEIGHTS = (10.0, 10.0, 3.0, 3.0, 1.0)  # bm25 weights: title, aliases, description, heading, body
META_ALL = True       # True: title/aliases/description are indexed on every chunk, else only the first
MIN_REL = 0.1         # drop hits scoring below this fraction of the best score (token saver); 0 = off
CHUNK_MAX = 60        # sections longer than this many lines are split at a blank line
CHUNK_SPLIT_AT = 40
SCHEMA_VERSION = "2"
RAW_SCHEMA_VERSION = "2"  # raw_files is a cache of raw-manifest.tsv; bumping it reloads from there
STOPWORDS = frozenset(
    "a an and are as at be by can did do does for from how i in is it of on or should that the "
    "then this to was what when which who why with".split()
)


# ---------------------------------------------------------------- parsing

def parse_page(text):
    """Return (frontmatter dict, body start line index, lines). Values are str or list[str]."""
    lines = text.split("\n")
    fm = {}
    if lines[0].rstrip() != "---":
        return fm, 0, lines
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip() == "---"), None)
    if end is None:
        return fm, 0, lines
    key = None
    for line in lines[1:end]:
        m = re.match(r"\s+-\s+(.*)$", line)
        if m and key is not None:
            if not isinstance(fm[key], list):
                fm[key] = []
            fm[key].append(m.group(1).strip().strip("'\""))
        elif ":" in line and not line.startswith((" ", "\t")):
            k, v = line.split(":", 1)
            key, v = k.strip(), v.strip()
            if v.startswith("[") and v.endswith("]"):
                fm[key] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
            else:
                fm[key] = v[1:-1] if len(v) > 1 and v[0] == v[-1] and v[0] in "'\"" else v
    return fm, end + 1, lines


def as_list(v):
    if isinstance(v, list):
        return v
    return [v] if v else []


def make_chunks(lines, start):
    """Heading sections as (heading, level, line_start, line_end), 1-based inclusive lines."""
    cuts = []
    fence = None
    for i in range(start, len(lines)):
        ln = lines[i]
        s = ln.lstrip()
        if s.startswith(("```", "~~~")):
            fence = None if fence == s[:3] else (fence or s[:3])
            continue
        if fence:
            continue
        m = HEADING_RE.match(ln)
        if m:
            cuts.append((i, len(m.group(1)), m.group(2)))
    sections = [("", 0, start, cuts[0][0] if cuts else len(lines))]
    for j, (i, lvl, h) in enumerate(cuts):
        sections.append((h, lvl, i, cuts[j + 1][0] if j + 1 < len(cuts) else len(lines)))
    out = []
    for h, lvl, a, b in sections:
        while a < b and not lines[a].strip():
            a += 1
        while b > a and not lines[b - 1].strip():
            b -= 1
        if a >= b:
            continue
        while b - a > CHUNK_MAX:
            cut = next((k for k in range(a + CHUNK_SPLIT_AT, b) if not lines[k].strip()), None)
            if cut is None:
                break
            out.append((h, lvl, a + 1, cut))
            a = cut
            while a < b and not lines[a].strip():
                a += 1
        out.append((h, lvl, a + 1, b))
    return out


# ---------------------------------------------------------------- index

def check_fts5():
    try:
        sqlite3.connect(":memory:").execute("create virtual table t using fts5(x)")
    except sqlite3.Error as e:
        sys.exit(f"wiki.py: this Python's SQLite ({sqlite3.sqlite_version}) lacks FTS5 ({e}). "
                 "Use a Python built against a SQLite with FTS5.")


SCHEMA = [
    """CREATE TABLE pages(
  id INTEGER PRIMARY KEY, path TEXT NOT NULL UNIQUE, stem TEXT NOT NULL, title TEXT, type TEXT,
  description TEXT, updated TEXT, raw TEXT, ingested TEXT,
  fm_keys TEXT, mtime_ns INTEGER, size INTEGER, hash TEXT)""",
    "CREATE INDEX pages_stem ON pages(stem)",
    "CREATE TABLE aliases(pid INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE, alias TEXT)",
    "CREATE TABLE tags(pid INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE, tag TEXT)",
    "CREATE TABLE sources(pid INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE, source TEXT)",
    "CREATE INDEX aliases_alias ON aliases(alias)",
    "CREATE INDEX tags_tag ON tags(tag)",
    """CREATE TABLE chunks(
  id INTEGER PRIMARY KEY, pid INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE,
  heading TEXT, level INTEGER, line_start INTEGER, line_end INTEGER, hash TEXT)""",
    "CREATE INDEX chunks_pid ON chunks(pid)",
    """CREATE TABLE links(
  pid INTEGER NOT NULL REFERENCES pages(id) ON DELETE CASCADE, dst_stem TEXT NOT NULL, line INTEGER)""",
    "CREATE INDEX links_dst ON links(dst_stem)",
    "CREATE VIRTUAL TABLE fts USING fts5(title, aliases, description, heading, body, tokenize='%s')",
]


RAW_SCHEMA = [
    """CREATE TABLE raw_files(
  path TEXT PRIMARY KEY, mtime_ns INTEGER, size INTEGER, hash TEXT NOT NULL, seen_hash TEXT,
  missing INTEGER NOT NULL DEFAULT 0, source TEXT, source_norm TEXT, captured TEXT, capture_method TEXT,
  base_size INTEGER)""",
    "CREATE INDEX raw_files_source ON raw_files(source_norm)",
]


def config_sig():
    return f"{SCHEMA_VERSION}|{TOKENIZER}|{META_ALL}|{CHUNK_MAX}|{CHUNK_SPLIT_AT}"


def connect(full=False):
    check_fts5()
    if full:
        for suffix in ("", "-wal", "-shm"):
            Path(str(DB_PATH) + suffix).unlink(missing_ok=True)
    conn = sqlite3.connect(DB_PATH, isolation_level=None, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA busy_timeout=10000")
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY, value TEXT)")
    get = lambda k: (conn.execute("SELECT value FROM meta WHERE key=?", (k,)).fetchone() or [None])[0]
    if get("config") != config_sig():
        reset_schema(conn)
    have_raw = get("raw_config")
    if have_raw == "1":  # v1 had no manifest: keep its baselines so sync_raw can export them
        conn.execute("ALTER TABLE raw_files ADD COLUMN base_size INTEGER")
        conn.execute("UPDATE raw_files SET base_size=size")
        conn.execute("UPDATE meta SET value=? WHERE key='raw_config'", (RAW_SCHEMA_VERSION,))
    elif have_raw != RAW_SCHEMA_VERSION:
        reset_raw_schema(conn)
    return conn


def reset_schema(conn):
    """Rebuild the wiki-page tables. raw_files (the write-once baselines) is left alone."""
    conn.execute("BEGIN IMMEDIATE")
    conn.execute("DROP TABLE IF EXISTS fts")
    for name in ("links", "chunks", "sources", "tags", "aliases", "pages"):
        conn.execute(f"DROP TABLE IF EXISTS {name}")
    for stmt in SCHEMA:
        conn.execute(stmt % TOKENIZER if "%s" in stmt else stmt)
    conn.execute("INSERT OR REPLACE INTO meta VALUES('config', ?)", (config_sig(),))
    conn.execute("COMMIT")


def reset_raw_schema(conn):
    conn.execute("BEGIN IMMEDIATE")
    conn.execute("DROP TABLE IF EXISTS raw_files")
    for stmt in RAW_SCHEMA:
        conn.execute(stmt)
    conn.execute("INSERT OR REPLACE INTO meta VALUES('raw_config', ?)", (RAW_SCHEMA_VERSION,))
    conn.execute("COMMIT")


def delete_page(conn, pid):
    conn.execute("DELETE FROM fts WHERE rowid IN (SELECT id FROM chunks WHERE pid=?)", (pid,))
    conn.execute("DELETE FROM pages WHERE id=?", (pid,))


def index_page(conn, rel, text, st, digest):
    old = conn.execute("SELECT id FROM pages WHERE path=?", (rel,)).fetchone()
    if old:
        delete_page(conn, old[0])
    fm, start, lines = parse_page(text)
    title = str(fm.get("title", ""))
    aliases = as_list(fm.get("aliases"))
    desc = str(fm.get("description", ""))
    cur = conn.execute(
        "INSERT INTO pages(path, stem, title, type, description, updated, raw, ingested,"
        " fm_keys, mtime_ns, size, hash) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (rel, Path(rel).stem, title, str(fm.get("type", "")), desc, str(fm.get("updated", "")),
         norm_rel(str(fm.get("raw", ""))), str(fm.get("ingested", "")),
         " ".join(fm), st.st_mtime_ns, st.st_size, digest))
    pid = cur.lastrowid
    conn.executemany("INSERT INTO aliases VALUES (?,?)", [(pid, a) for a in aliases])
    conn.executemany("INSERT INTO tags VALUES (?,?)", [(pid, t) for t in as_list(fm.get("tags"))])
    conn.executemany("INSERT INTO sources VALUES (?,?)", [(pid, s) for s in as_list(fm.get("sources"))])
    seen = set()
    for i, ln in enumerate(lines, 1):
        for m in LINK_RE.findall(ln):
            if (m.strip(), i) not in seen:
                seen.add((m.strip(), i))
                conn.execute("INSERT INTO links VALUES (?,?,?)", (pid, m.strip(), i))
    chunks = make_chunks(lines, start) or [("", 0, start + 1, max(start + 1, len(lines)))]
    meta = (title, " ".join(aliases), desc)
    for n, (h, lvl, a, b) in enumerate(chunks):
        body = "\n".join(lines[a - 1:b])
        c = conn.execute("INSERT INTO chunks(pid, heading, level, line_start, line_end, hash) VALUES (?,?,?,?,?,?)",
                         (pid, h, lvl, a, b, hashlib.sha1(body.encode()).hexdigest()[:12]))
        m = meta if (n == 0 or META_ALL) else ("", "", "")
        conn.execute("INSERT INTO fts(rowid, title, aliases, description, heading, body) VALUES (?,?,?,?,?,?)",
                     (c.lastrowid, *m, h, body))


def sync(conn):
    """Bring the index in line with wiki/*.md. Returns (added, updated, removed)."""
    known = {r["path"]: r for r in conn.execute("SELECT id, path, mtime_ns, size, hash FROM pages")}
    todo, touch, present = [], [], set()
    for p in sorted(WIKI.rglob("*.md")):
        rel = str(p.relative_to(ROOT))
        present.add(rel)
        st = p.stat()
        r = known.get(rel)
        if r and r["mtime_ns"] == st.st_mtime_ns and r["size"] == st.st_size:
            continue
        text = p.read_text()
        digest = hashlib.sha1(text.encode()).hexdigest()
        if r and r["hash"] == digest:
            touch.append((st.st_mtime_ns, st.st_size, r["id"]))
        else:
            todo.append((rel, text, st, digest, r is not None))
    gone = [r["id"] for path, r in known.items() if path not in present]
    if not (todo or touch or gone):
        return 0, 0, 0
    conn.execute("BEGIN IMMEDIATE")
    try:
        conn.executemany("UPDATE pages SET mtime_ns=?, size=? WHERE id=?", touch)
        for pid in gone:
            delete_page(conn, pid)
        for rel, text, st, digest, _ in todo:
            index_page(conn, rel, text, st, digest)
        conn.execute("COMMIT")
    except BaseException:
        conn.execute("ROLLBACK")
        raise
    updated = sum(1 for t in todo if t[4])
    return len(todo) - updated, updated, len(gone)


def norm_rel(path):
    """Normalize a wiki-root-relative path from frontmatter ('./raw/x.md' -> 'raw/x.md'); '' stays ''."""
    path = path.strip()
    return posixpath.normpath(path) if path else ""


def root_rel(arg):
    """A CLI path (cwd-relative or absolute) as a wiki-root-relative posix path; falls back to
    treating it as wiki-root-relative when it does not resolve under the wiki root."""
    try:
        return Path(arg).resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return norm_rel(arg)


def norm_source(src):
    """Minimal source normalization; see module docstring. '' -> None."""
    s = (src or "").strip()
    if not s:
        return None
    m = re.match(r"([A-Za-z][A-Za-z0-9+.-]*)://([^/?#]*)([^?#]*)(.*)$", s, re.S)
    if m:
        scheme, auth, path, rest = m.groups()
        user, at, host = auth.rpartition("@")
        return f"{scheme.lower()}://{user}{at}{host.lower()}{path.rstrip('/')}{rest}"
    return s.rstrip("/") or s


def raw_files_on_disk():
    """Every non-dot file under raw/, as wiki-root-relative posix paths."""
    if not RAW.is_dir():
        return {}
    out = {}
    for p in sorted(RAW.rglob("*")):
        rel = p.relative_to(ROOT)
        if p.is_file() and not any(part.startswith(".") for part in rel.parts):
            out[rel.as_posix()] = p
    return out


def raw_capture_fm(data):
    """(source, captured, capture_method) from a capture's frontmatter; None for absent/empty fields."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return None, None, None
    fm, _, _ = parse_page(text)
    vals = []
    for k in ("source", "captured", "capture_method"):
        v = fm.get(k)
        v = ", ".join(v) if isinstance(v, list) else v
        vals.append(v or None)
    return tuple(vals)


class ManifestError(Exception):
    pass


def _tsv_esc(v):
    v = "" if v is None else str(v)
    return v.replace("\\", "\\\\").replace("\t", "\\t").replace("\n", "\\n").replace("\r", "\\r")


def _tsv_unesc(v):
    return re.sub(r"\\(.)", lambda m: {"t": "\t", "n": "\n", "r": "\r"}.get(m.group(1), m.group(1)), v)


def read_manifest():
    """{path: (size, sha256, source, captured, capture_method)} with None for empty fields, or None when
    the file does not exist. Raises ManifestError with a line number on anything malformed."""
    if not MANIFEST.exists():
        return None
    try:
        lines = MANIFEST.read_text(encoding="utf-8").split("\n")
    except (OSError, UnicodeDecodeError) as e:
        raise ManifestError(f"unreadable: {e}")
    if lines and lines[-1] == "":
        lines.pop()
    if not lines or lines[0] != "\t".join(MANIFEST_COLS):
        raise ManifestError("line 1: header must be: " + " <tab> ".join(MANIFEST_COLS))
    out = {}
    for n, line in enumerate(lines[1:], 2):
        f = line.split("\t")
        if len(f) != len(MANIFEST_COLS):
            raise ManifestError(f"line {n}: expected {len(MANIFEST_COLS)} tab-separated fields, got {len(f)}")
        path, size, digest, src, cap, meth = (_tsv_unesc(x) for x in f)
        if not path.startswith("raw/") or path != norm_rel(path):
            raise ManifestError(f"line {n}: path must be a normalized raw/ path: {path!r}")
        if not size.isdigit():
            raise ManifestError(f"line {n}: size is not a non-negative integer: {size!r}")
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ManifestError(f"line {n}: sha256 is not 64 lowercase hex digits")
        if path in out:
            raise ManifestError(f"line {n}: duplicate path {path}")
        out[path] = (int(size), digest, src or None, cap or None, meth or None)
    return out


def render_manifest(rows):
    """rows: {path: (size, sha256, source, captured, capture_method)} -> file text, sorted by path."""
    body = ["\t".join(MANIFEST_COLS)]
    body += ["\t".join(_tsv_esc(x) for x in (path, *rows[path])) for path in sorted(rows)]
    return "\n".join(body) + "\n"


def write_manifest(text):
    tmp = MANIFEST.with_name(MANIFEST.name + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, MANIFEST)


def db_baselines(conn):
    return {r["path"]: (r["base_size"], r["hash"], r["source"], r["captured"], r["capture_method"])
            for r in conn.execute("SELECT * FROM raw_files")}


def note(msg):
    print(f"{MANIFEST.name}: {msg}", file=sys.stderr)


def sync_raw(conn):
    """Bring raw_files in line with raw-manifest.tsv and raw/.

    raw-manifest.tsv holds the baselines; raw_files caches them plus the last observed mtime/size/hash.
    1. Reconcile: a manifest row always wins over the cache (the cached row is replaced and re-hashed).
       A cached baseline missing from the manifest is written back from the cache, never from current
       file content, so dropping a manifest row cannot silently accept an edit. If the manifest does
       not parse, the cache is used as is and nothing is written (lint/doctor report the error).
    2. Scan raw/: files never seen before are baselined from their current content and appended to the
       manifest (the normal capture path). Changed or deleted files are flagged via seen_hash / missing.
    Returns (added, flagged, restored)."""
    try:
        man, man_err = read_manifest(), None
    except ManifestError as e:
        man, man_err = None, e
    cache = db_baselines(conn)
    load, writeback = {}, []
    if man is not None:
        load = {p: v for p, v in man.items() if cache.get(p) != v}
        writeback = sorted(p for p in cache if p not in man)
    known = {r["path"]: r for r in conn.execute("SELECT * FROM raw_files")}
    for path in load:
        known.pop(path, None)  # force a re-hash against the manifest baseline
    disk = raw_files_on_disk()
    new, upd = [], []
    added = flagged = restored = 0
    for rel, p in disk.items():
        st = p.stat()
        r = known.get(rel)
        if r and not r["missing"] and r["mtime_ns"] == st.st_mtime_ns and r["size"] == st.st_size:
            continue
        data = p.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        base = load[rel][1] if rel in load else (r["hash"] if r else None)
        if base is None:
            src, cap, meth = raw_capture_fm(data)
            new.append((rel, st.st_mtime_ns, st.st_size, digest, src, norm_source(src), cap, meth, st.st_size))
            added += 1
            continue
        seen = None if digest == base else digest
        if seen and (r is None or seen != r["seen_hash"]):
            flagged += 1
        if r and not seen and (r["seen_hash"] or r["missing"]):
            restored += 1
        upd.append((st.st_mtime_ns, st.st_size, seen, rel))
    gone = [(rel,) for rel in set(known) | set(load) if rel not in disk
            and (rel in load or not known[rel]["missing"])]
    if new or upd or gone or load:
        conn.execute("BEGIN IMMEDIATE")
        try:
            conn.executemany(
                "INSERT OR REPLACE INTO raw_files(path, base_size, hash, source, source_norm, captured,"
                " capture_method, missing) VALUES (?,?,?,?,?,?,?,0)",
                [(p, v[0], v[1], v[2], norm_source(v[2]), v[3], v[4]) for p, v in load.items()])
            conn.executemany("INSERT INTO raw_files(path, mtime_ns, size, hash, source, source_norm, captured,"
                             " capture_method, base_size) VALUES (?,?,?,?,?,?,?,?,?)", new)
            conn.executemany("UPDATE raw_files SET mtime_ns=?, size=?, seen_hash=?, missing=0 WHERE path=?", upd)
            conn.executemany("UPDATE raw_files SET missing=1 WHERE path=?", gone)
            conn.execute("COMMIT")
        except BaseException:
            conn.execute("ROLLBACK")
            raise
    if man_err is None:
        text = render_manifest(db_baselines(conn))
        current = MANIFEST.read_text(encoding="utf-8") if man is not None else None
        if text != current:
            try:
                write_manifest(text)
            except OSError as e:
                note(f"could not write ({e}); baselines are only in the index cache")
            else:
                if man is None:
                    n = len(cache)
                    note(f"created ({n} baselines from the index cache, {added} from current raw/ content)"
                         if n or added else "created (no raw files yet)")
        stale = sorted(p for p in load if p in cache)
        if stale:
            note(f"index cache disagreed on {len(stale)} baseline(s); the manifest wins: {', '.join(stale)}")
        if writeback:
            note(f"{len(writeback)} cached baseline(s) were missing from the manifest and were written back:"
                 f" {', '.join(writeback)}")
    return added, flagged + len(gone), restored


def manifest_findings(conn):
    """Manifest problems as lint-style error messages (after sync)."""
    try:
        man = read_manifest()
    except ManifestError as e:
        return [f"{MANIFEST.name}: does not parse ({e}); restore it from version control. Until it is "
                "fixed, baselines (including new captures) live only in the index cache"]
    if man is None:
        return [f"{MANIFEST.name}: missing and could not be created"]
    cache = db_baselines(conn)
    out = []
    for path in sorted(set(man) | set(cache)):
        if man.get(path) != cache.get(path):
            where = "only in manifest" if path not in cache else "only in index" if path not in man else "differs"
            out.append(f"{MANIFEST.name}: disagrees with the index cache for {path} ({where})")
    return out


def raw_violations(conn):
    """Write-once violations as lint-style messages, sorted by path."""
    out = []
    for r in conn.execute("SELECT path, hash, seen_hash, missing FROM raw_files"
                          " WHERE missing=1 OR seen_hash IS NOT NULL ORDER BY path"):
        what = ("file deleted or moved" if r["missing"] else
                f"content changed since baseline (sha256 {r['hash'][:12]} -> {r['seen_hash'][:12]})")
        out.append(f"{r['path']}: write-once violation: {what}; restore it, or re-baseline with "
                   f"`wiki.py reindex --accept-raw {r['path']}`")
    return out


def open_db():
    conn = connect()
    sync(conn)
    sync_raw(conn)
    return conn


def sort_key(path):
    return Path(path).parts


# ---------------------------------------------------------------- search

def build_query(terms, all_terms=False, prefix=False):
    """Plain words in, safe FTS5 expression out. Returns (expr or None, kept words)."""
    words = [w for t in terms for w in WORD_RE.findall(t.lower())]
    kept = [w for w in words if w not in STOPWORDS] or words
    kept = list(dict.fromkeys(kept))
    if not kept:
        return None, []
    star = "*" if prefix else ""
    return (" AND " if all_terms else " OR ").join(f'"{w}"{star}' for w in kept), kept


def search_hits(conn, terms, n=10, all_terms=False, prefix=False, type_=None, tag=None, all_chunks=False,
                weights=None, snippet=False, min_rel=None):
    q, kept = build_query(terms, all_terms, prefix)
    if q is None:
        return [], kept
    w = ", ".join(str(float(x)) for x in (weights or WEIGHTS))
    sql = (f"SELECT p.path, p.stem, c.heading, c.line_start, c.line_end, p.description, bm25(fts, {w}) AS score, "
           + ("snippet(fts, 4, '[', ']', '...', 14) AS snip " if snippet else "'' AS snip ")
           + "FROM fts JOIN chunks c ON c.id = fts.rowid JOIN pages p ON p.id = c.pid WHERE fts MATCH ?")
    args = [q]
    if type_:
        sql += " AND p.type = ?"
        args.append(type_)
    if tag:
        sql += " AND EXISTS (SELECT 1 FROM tags t WHERE t.pid = p.id AND t.tag = ?)"
        args.append(tag)
    sql += " ORDER BY score, p.path, c.line_start LIMIT 500"
    rows = conn.execute(sql, args).fetchall()
    if not all_chunks:
        seen, best = set(), []
        for r in rows:
            if r["path"] not in seen:
                seen.add(r["path"])
                best.append(r)
        rows = best
    min_rel = MIN_REL if min_rel is None else min_rel
    if rows and min_rel:
        floor = rows[0]["score"] * min_rel  # scores are negative; more negative = better
        rows = [r for r in rows if r["score"] <= floor]
    return rows[:n], kept


def cmd_search(args):
    conn = open_db()
    rows, kept = search_hits(conn, args.terms, args.n, args.all, args.prefix, args.type, args.tag,
                             args.all_chunks, snippet=args.snippet,
                             min_rel=0 if args.no_cutoff else None)
    if not rows:
        mode = "all terms required" if args.all else "any term"
        print(f"no matches for: {' '.join(kept) or ' '.join(args.terms)} ({mode}). "
              "Try synonyms, aliases, fewer terms, or --prefix.")
        return 0
    for r in rows:
        print(f"{r['path']}:{r['line_start']}-{r['line_end']}  {r['heading'] or '(lead)'}  {r['description']}")
        if args.snippet:
            print("  " + " ".join(r["snip"].split()))
    return 0


# ---------------------------------------------------------------- lint / digest

def lint_findings(conn):
    """Returns (page_count, errors, warnings), same wording and order as the pre-index implementation."""
    errors, warnings = [], []
    pages = sorted(conn.execute("SELECT * FROM pages"), key=lambda r: sort_key(r["path"]))
    names = {}
    for p in pages:
        if p["stem"] in names:
            errors.append(f"duplicate filename: {p['path']} and {names[p['stem']]}")
        else:
            names[p["stem"]] = p["path"]
    links = {}
    for r in conn.execute("SELECT pid, dst_stem FROM links"):
        links.setdefault(r["pid"], set()).add(r["dst_stem"])
    srcs = {}
    for r in conn.execute("SELECT pid, source FROM sources"):
        srcs.setdefault(r["pid"], []).append(r["source"])
    source_stems = {p["stem"] for p in pages if p["type"] == "source"}
    inbound = Counter()
    index_links = set()
    for p in pages:
        rel = p["path"]
        keys = set(p["fm_keys"].split())
        for key in REQUIRED_FM:
            if key not in keys:
                errors.append(f"{rel}: missing frontmatter '{key}'")
        if "description" in keys and (not p["description"] or p["description"].startswith("TODO")):
            errors.append(f"{rel}: empty or placeholder 'description'")
        if p["type"] and p["type"] not in TYPES:
            errors.append(f"{rel}: unknown type '{p['type']}'")
        if p["type"] == "source" and "raw" not in keys:
            errors.append(f"{rel}: source page missing 'raw' path")
        elif p["raw"] and (p["raw"].startswith("../") or p["raw"].startswith("/")):
            errors.append(f"{rel}: raw path outside the wiki root: {p['raw']}")
        elif p["raw"] and not (ROOT / p["raw"]).exists():
            errors.append(f"{rel}: raw file not found: {p['raw']}")
        for slug in srcs.get(p["id"], ()):
            if slug not in source_stems:
                warnings.append(f"{rel}: sources lists '{slug}', which is not a source page")
        for target in sorted(links.get(p["id"], ())):
            if target not in names:
                errors.append(f"{rel}: broken link [[{target}]]")
            elif target != p["stem"]:
                inbound[target] += 1
                if p["stem"] == "index":
                    index_links.add(target)
    for stem, path in names.items():
        if stem in SPECIAL:
            continue
        if stem not in index_links:
            errors.append(f"{path}: not listed in index")
        if inbound[stem] == 0:
            warnings.append(f"{path}: orphan (no inbound links)")
    errors += manifest_findings(conn) + raw_violations(conn)
    return len(pages), errors, warnings


def cmd_lint(args):
    n, errors, warnings = lint_findings(open_db())
    if args.files:
        scope = tuple(str(Path(f).resolve().relative_to(ROOT)) + ":" for f in args.files)
        errors = [e for e in errors if e.startswith(scope)]
        warnings = [w for w in warnings if w.startswith(scope)]
    for w in warnings:
        print("warn ", w)
    for e in errors:
        print("error", e)
    print(f"{n} pages, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def cmd_new(args):
    if args.type not in FOLDERS:
        print(f"type must be one of: {', '.join(FOLDERS)}", file=sys.stderr)
        return 2
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", args.slug):
        print("slug must be lowercase-kebab-case", file=sys.stderr)
        return 2
    if open_db().execute("SELECT 1 FROM pages WHERE stem=?", (args.slug,)).fetchone():
        print(f"a page named '{args.slug}' already exists", file=sys.stderr)
        return 1
    path = WIKI / FOLDERS[args.type] / f"{args.slug}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    title = args.title or args.slug.replace("-", " ").title()
    today = date.today().isoformat()
    extra = f"raw: raw/FILENAME\ningested: {today}\n" if args.type == "source" else ""
    path.write_text(
        f"---\ntitle: {title}\ntype: {args.type}\ndescription: TODO what this page covers and when to consult it\n"
        f"tags: []\nsources: []\n"
        f"{extra}updated: {today}\n---\n\n# {title}\n\n"
    )
    print(path.relative_to(ROOT))
    return 0


def cmd_backlinks(args):
    target = args.page.removesuffix(".md")
    rows = open_db().execute(
        "SELECT DISTINCT p.path FROM links l JOIN pages p ON p.id = l.pid WHERE l.dst_stem = ? AND p.stem != ?",
        (target, target)).fetchall()
    if not rows:
        print("no backlinks")
        return 0
    for path in sorted((r["path"] for r in rows), key=sort_key):
        print(path)
    return 0


def unprocessed(conn, path=None):
    """Raw files (outside raw/assets/) with no source page. Returns (files, error_message)."""
    done = {r[0] for r in conn.execute("SELECT raw FROM pages WHERE type='source' AND raw != ''")}
    scope = Path(path).resolve() if path else RAW
    if not scope.exists() or not (scope == RAW or RAW in scope.parents):
        return None, f"not found under raw/: {path}"
    pre = scope.relative_to(ROOT).as_posix()
    todo = [
        ROOT / r["path"] for r in conn.execute("SELECT path FROM raw_files WHERE missing=0")
        if (r["path"] == pre or r["path"].startswith(pre + "/"))
        and not r["path"].startswith("raw/assets/") and r["path"] not in done
    ]
    return sorted(todo), None


def cmd_status(args):
    todo, err = unprocessed(open_db(), args.path)
    if err:
        print(err, file=sys.stderr)
        return 2
    for f in todo:
        print(f.relative_to(ROOT))
    print(f"{len(todo)} unprocessed", file=sys.stderr)
    return 0


def source_pages_by_raw(conn):
    out = {}
    for r in conn.execute("SELECT raw, path FROM pages WHERE type='source' AND raw != '' ORDER BY path"):
        out.setdefault(r["raw"], []).append(r["path"])
    return out


def cmd_captured(args):
    conn = open_db()
    pages = source_pages_by_raw(conn)
    status = 0
    for arg in args.source:
        key = norm_source(arg)
        rows = conn.execute("SELECT * FROM raw_files WHERE source_norm=? ORDER BY path", (key,)).fetchall()
        if not rows:
            print(f"not captured: {key or arg}")
            status = 1
        for r in rows:
            flag = "  MISSING" if r["missing"] else ("  MODIFIED" if r["seen_hash"] else "")
            print(f"{r['path']}  captured={r['captured'] or '-'}  method={r['capture_method'] or 'unknown'}"
                  f"  page={','.join(pages.get(r['path'], [])) or '-'}{flag}")
    return status


def provenance(conn, page_row):
    """[(source slug, label)] for every source behind a page. Label is the raw file's capture_method,
    'unknown' (capture without capture_method), 'not-a-capture' (raw: outside raw/), or a problem:
    'no-source-page', 'no-raw', 'raw-missing'. '!modified' is appended on write-once violations."""
    if page_row["type"] == "source":
        slugs = [page_row["stem"]]
    else:
        slugs = [r[0] for r in conn.execute("SELECT source FROM sources WHERE pid=?", (page_row["id"],))]
    out = []
    for slug in dict.fromkeys(slugs):
        sp = conn.execute("SELECT raw FROM pages WHERE stem=? AND type='source' ORDER BY path", (slug,)).fetchone()
        if sp is None:
            out.append((slug, "no-source-page"))
        elif not sp["raw"]:
            out.append((slug, "no-raw"))
        elif not sp["raw"].startswith("raw/"):
            out.append((slug, "not-a-capture" if (ROOT / sp["raw"]).is_file() else "raw-missing"))
        else:
            rf = conn.execute("SELECT * FROM raw_files WHERE path=?", (sp["raw"],)).fetchone()
            if rf is None or rf["missing"]:
                out.append((slug, "raw-missing"))
            else:
                out.append((slug, (rf["capture_method"] or "unknown") + ("!modified" if rf["seen_hash"] else "")))
    return out


def cmd_provenance(args):
    conn = open_db()
    if args.all:
        rows = conn.execute("SELECT * FROM pages WHERE stem NOT IN ('index', 'log')").fetchall()
    else:
        rows = []
        for name in args.pages:
            stem = Path(name).name.removesuffix(".md")
            r = conn.execute("SELECT * FROM pages WHERE stem=? ORDER BY path", (stem,)).fetchone()
            if r is None:
                print(f"no such page: {name}", file=sys.stderr)
                return 2
            rows.append(r)
        if not rows:
            print("give page names or --all", file=sys.stderr)
            return 2
    shown = 0
    for r in sorted(rows, key=lambda r: sort_key(r["path"])) if args.all else rows:
        prov = provenance(conn, r)
        if args.method and not any(lbl.split("!")[0] == args.method for _, lbl in prov):
            continue
        shown += 1
        print(f"{r['path']}  " + ("  ".join(f"{s}={l}" for s, l in prov) or "(no sources)"))
    if args.method and not shown:
        print(f"no pages depend on capture_method={args.method}")
    return 0


def cmd_log(args):
    text = (WIKI / "log.md").read_text()
    entries = re.split(r"(?m)^(?=## \[)", text)[1:]
    for e in entries[-args.n:]:
        print(e.rstrip() + "\n")
    return 0


def cmd_digest(args):
    """Read-only report. Sections with nothing to say are omitted."""
    conn = open_db()
    _, errors, warnings = lint_findings(conn)
    cutoff = date.today() - timedelta(days=args.days)
    by_type, stale, unsupported = Counter(), [], []
    rows = sorted(conn.execute(
        "SELECT p.path, p.type, p.updated, (SELECT COUNT(*) FROM sources s WHERE s.pid = p.id) AS nsrc "
        "FROM pages p WHERE p.stem NOT IN ('index', 'log')"), key=lambda r: sort_key(r["path"]))
    for r in rows:
        t = r["type"] or "?"
        by_type[t] += 1
        try:
            if date.fromisoformat(r["updated"]) < cutoff:
                stale.append(f"{r['path']} (updated {r['updated']})")
        except ValueError:
            pass
        if t in ("entity", "concept", "analysis") and r["nsrc"] == 0:
            unsupported.append(r["path"])
    queue, _ = unprocessed(conn)
    log = (WIKI / "log.md").read_text()
    recent = []
    for m in re.finditer(r"(?m)^## \[(\d{4}-\d{2}-\d{2})\] (.+)$", log):
        try:
            if date.fromisoformat(m.group(1)) >= cutoff:
                recent.append(f"{m.group(1)} {m.group(2)}")
        except ValueError:
            pass

    def section(title, items):
        if items:
            print(f"\n## {title} ({len(items)})")
            for i in items:
                print(f"- {i}")

    print(f"# Wiki digest {date.today().isoformat()} (window: {args.days} days)")
    section("Attention: lint errors", errors)
    section("Attention: raw sources awaiting ingest (run /ingest)", [str(f.relative_to(ROOT)) for f in queue])
    section("Orphan pages", [w.split(": ")[0] for w in warnings if "orphan" in w])
    section("Pages with no supporting sources", unsupported)
    section(f"Stale pages (not updated in {args.days} days)", stale)
    section("Recent activity", recent)
    print("\n## Totals")
    print(f"- {sum(by_type.values())} pages: " + ", ".join(f"{n} {t}" for t, n in sorted(by_type.items())))
    print(f"- {len(errors)} lint errors, {len(warnings)} warnings, {len(queue)} unprocessed raw files")
    return 0


# ---------------------------------------------------------------- index maintenance

def cmd_reindex(args):
    conn = connect(full=args.full)
    if args.accept_raw:
        rels = [root_rel(p) for p in args.accept_raw]
        try:
            man = read_manifest() or {}
        except ManifestError as e:
            print(f"{MANIFEST.name} does not parse ({e}); fix it before accepting raw changes", file=sys.stderr)
            return 2
        known = {r[0] for r in conn.execute("SELECT path FROM raw_files")} | set(man)
        bad = [p for p in rels if p not in known]
        if bad:
            print(f"not a tracked raw file: {', '.join(bad)}", file=sys.stderr)
            return 2
        # drop the baseline from both the manifest and the cache; sync_raw re-baselines files that
        # still exist from their current content and appends them to the manifest again
        if MANIFEST.exists():
            write_manifest(render_manifest({k: v for k, v in man.items() if k not in rels}))
        conn.execute("BEGIN IMMEDIATE")
        conn.executemany("DELETE FROM raw_files WHERE path=?", [(p,) for p in rels])
        conn.execute("COMMIT")
        for p in rels:
            print("re-baselined", p + ("" if (ROOT / p).exists() else " (deleted; baseline dropped)"))
    a, u, r = sync(conn)
    ra, rv, _ = sync_raw(conn)
    if args.full:
        conn.execute("INSERT INTO fts(fts) VALUES('optimize')")
    n = conn.execute("SELECT COUNT(*) FROM pages").fetchone()[0]
    c = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    print(f"{DB_PATH.name}: {n} pages, {c} chunks (added {a}, updated {u}, removed {r})")
    nr = conn.execute("SELECT COUNT(*) FROM raw_files WHERE missing=0").fetchone()[0]
    print(f"raw: {nr} files (baselined {ra}), {len(raw_violations(conn))} write-once violations")
    return 0


def cmd_doctor(args):
    conn = open_db()
    problems = []
    try:
        conn.execute("INSERT INTO fts(fts, rank) VALUES('integrity-check', 1)")
    except sqlite3.Error as e:
        problems.append(f"fts integrity-check: {e}")
    ic = conn.execute("PRAGMA integrity_check").fetchone()[0]
    if ic != "ok":
        problems.append(f"sqlite integrity_check: {ic}")
    problems += [f"foreign key violation: {tuple(r)}" for r in conn.execute("PRAGMA foreign_key_check")]
    files = {str(p.relative_to(ROOT)) for p in WIKI.rglob("*.md")}
    paths = {r[0] for r in conn.execute("SELECT path FROM pages")}
    problems += [f"file not indexed: {p}" for p in sorted(files - paths)]
    problems += [f"indexed but missing on disk: {p}" for p in sorted(paths - files)]
    # full re-hash of raw/: catches edits that preserved both mtime and size
    disk = raw_files_on_disk()
    for rf in conn.execute("SELECT path, hash, seen_hash FROM raw_files WHERE missing=0").fetchall():
        if rf["path"] in disk:
            digest = hashlib.sha256(disk[rf["path"]].read_bytes()).hexdigest()
            seen = None if digest == rf["hash"] else digest
            if seen != rf["seen_hash"]:
                conn.execute("UPDATE raw_files SET seen_hash=? WHERE path=?", (seen, rf["path"]))
    tracked = {r[0] for r in conn.execute("SELECT path FROM raw_files")}
    problems += [f"raw file not tracked: {p}" for p in sorted(set(disk) - tracked)]
    problems += manifest_findings(conn) + raw_violations(conn)
    nc = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    nf = conn.execute("SELECT COUNT(*) FROM fts").fetchone()[0]
    if nc != nf:
        problems.append(f"chunks ({nc}) != fts rows ({nf})")
    for p in problems:
        print("problem", p)
    print(f"sqlite {sqlite3.sqlite_version}, {len(paths)} pages, {nc} chunks, {len(problems)} problems")
    return 1 if problems else 0


# ---------------------------------------------------------------- eval

def cmd_eval(args):
    """Run tools/eval/questions.tsv through `search`; report hit rank and output size.

    Rank = position of the expected page among distinct pages in the printed output.
    Tokens are estimated as chars/4 (no tokenizer in stdlib).
    """
    import contextlib
    import io
    qfile = ROOT / "tools" / "eval" / "questions.tsv"
    rows = [l.split("\t") for l in qfile.read_text().splitlines()[1:] if l.strip()]
    ns = argparse.Namespace(terms=[], n=args.n, snippet=False, all_chunks=False, all=False, prefix=False,
                            type=None, tag=None, no_cutoff=False)
    h1 = h3 = total = 0
    heads = [0, 0]
    for row in rows:
        q, want = row[0], row[1]
        want_heading = row[2].strip().lower() if len(row) > 2 else ""
        ns.terms = q.split()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            cmd_search(ns)
        out = buf.getvalue()
        stems, first_line = [], {}
        for line in out.splitlines():
            m = re.match(r"wiki/(?:[^/\s:]+/)*([^/\s:]+)\.md:", line)
            if m and m.group(1) not in stems:
                stems.append(m.group(1))
                first_line[m.group(1)] = line
        rank = stems.index(want) + 1 if want in stems else 0
        h1 += rank == 1
        h3 += 1 <= rank <= 3
        total += len(out)
        note = ""
        if want_heading:
            heads[1] += 1
            ok = rank and want_heading in first_line[want].lower()
            heads[0] += bool(ok)
            note = f" heading={'ok' if ok else 'MISS'}"
        if args.v or rank != 1:
            print(f"rank={rank or '-'} chars={len(out):4d}  want={want}{note}  {q}")
    n = len(rows)
    extra = f" heading_ok={heads[0]}/{heads[1]}" if heads[1] else ""
    print(f"questions={n} hit@1={h1}/{n} ({h1 / n:.0%}) hit@3={h3}/{n} ({h3 / n:.0%}) "
          f"mean_chars={total / n:.0f} mean_tokens~{total / n / 4:.0f}{extra}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("terms", nargs="+")
    s.add_argument("-n", type=int, default=10)
    s.add_argument("-s", "--snippet", action="store_true")
    s.add_argument("--all", action="store_true", help="require every term (AND); default is OR")
    s.add_argument("--prefix", action="store_true", help="treat terms as prefixes")
    s.add_argument("--type", choices=sorted(TYPES))
    s.add_argument("--tag")
    s.add_argument("--no-cutoff", action="store_true", help="also show weak matches (score < 10%% of best)")
    s.add_argument("--all-chunks", action="store_true", help="one line per matching section, not per page")
    s.set_defaults(fn=cmd_search)
    li = sub.add_parser("lint")
    li.add_argument("files", nargs="*")
    li.set_defaults(fn=cmd_lint)
    nw = sub.add_parser("new")
    nw.add_argument("type")
    nw.add_argument("slug")
    nw.add_argument("-t", "--title")
    nw.set_defaults(fn=cmd_new)
    bl = sub.add_parser("backlinks")
    bl.add_argument("page")
    bl.set_defaults(fn=cmd_backlinks)
    st = sub.add_parser("status")
    st.add_argument("path", nargs="?")
    st.set_defaults(fn=cmd_status)
    cp = sub.add_parser("captured", help="is a URL or path already captured under raw/?")
    cp.add_argument("source", nargs="+")
    cp.set_defaults(fn=cmd_captured)
    pv = sub.add_parser("provenance", help="capture_method of the raw files behind pages")
    pv.add_argument("pages", nargs="*")
    pv.add_argument("--all", action="store_true", help="every page except index and log")
    pv.add_argument("--method", help="only pages with a source of this capture_method (or unknown, ...)")
    pv.set_defaults(fn=cmd_provenance)
    l = sub.add_parser("log")
    l.add_argument("-n", type=int, default=5)
    l.set_defaults(fn=cmd_log)
    ev = sub.add_parser("eval")
    ev.add_argument("-n", type=int, default=10)
    ev.add_argument("-v", action="store_true", help="print every question, not just misses")
    ev.set_defaults(fn=cmd_eval)
    dg = sub.add_parser("digest")
    dg.add_argument("--days", type=int, default=30)
    dg.set_defaults(fn=cmd_digest)
    ri = sub.add_parser("reindex")
    ri.add_argument("--full", action="store_true",
                    help="drop and rebuild the index; raw/ baselines are reloaded from raw-manifest.tsv")
    ri.add_argument("--accept-raw", nargs="+", metavar="PATH", help="re-baseline these raw files only")
    ri.set_defaults(fn=cmd_reindex)
    dr = sub.add_parser("doctor")
    dr.set_defaults(fn=cmd_doctor)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
