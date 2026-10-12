#!/usr/bin/env python3
"""PreToolUse hook: keep every agent out of wikis it doesn't own.

Ownership comes from .claude/skills/wiki/registry.yaml (agent -> wiki path). The hook is
registered for every tool. Built-in file tools and Bash are checked by their known
fields; any other tool (plugin, MCP server, future built-in) is checked by every input
field whose name suggests a path (path, file, dir, folder, root, cwd, source, target, ...).
Each target path is checked:

- inside a registered wiki: allowed only when the caller's agent_type is that wiki's
  owner. A session with no agent_type (a plain `claude` session) owns nothing.
- Grep/Glob, or a recursive Bash command, rooted above a wiki the caller doesn't own:
  denied, since its results would include that wiki. Narrow the path instead.
- an unknown tool given a directory above a wiki the caller doesn't own: denied, since
  it may list or search inside it.
- the registry, this hook, the skill directory, or a settings file: writes are denied
  for everyone, and Bash and unknown tools may not touch them at all. Reads with the
  Read tool are fine.

No registry file: no fence (template mode). A registry that doesn't parse, or any error
in this hook: deny (fail closed); the human fixes the registry outside Claude.

Bash checks are best-effort: they catch literal and glob paths, `cd` targets, and
recursive tools run from above a wiki, not paths assembled at run time.

`python3 <this file> --selftest` checks every registered wiki without naming any wiki
path: owner allowed, plain session and another agent denied, registry edits denied.
Exit 0 when all pass. The fence allows exactly that command (this file, --selftest), so
an install can verify the fence even while it is live.
"""
import glob
import json
import re
import shlex
import sys
from pathlib import Path

VERSION = "2026-10-10"  # bump on every change, so installs can tell copies apart
HOOK = Path(__file__).resolve()
ROOT = HOOK.parents[2]  # <root>/.claude/hooks/wiki-fence.py
CLAUDE_DIR = ROOT / ".claude"
REGISTRY = CLAUDE_DIR / "skills" / "wiki" / "registry.yaml"
PROTECTED_DIRS = [CLAUDE_DIR / "hooks", CLAUDE_DIR / "skills" / "wiki"]
PROTECTED_FILES = [CLAUDE_DIR / "settings.json", CLAUDE_DIR / "settings.local.json",
                   Path.home() / ".claude" / "settings.json", Path.home() / ".claude" / "settings.local.json"]
PROTECTED_WORDS = ("registry.yaml", "wiki-fence", ".claude/settings")
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
SEARCH_TOOLS = {"Grep", "Glob"}
RECURSIVE_CMDS = {"rg", "find", "fd", "ag", "ack", "tree", "du", "rsync", "tar", "zip"}
RECURSIVE_IF_FLAG = {"grep", "egrep", "ls", "cp", "rm", "chmod", "chown", "mv", "scp"}
RECURSIVE_FLAG = re.compile(r"^-[a-zA-Z]*[rR][a-zA-Z]*$|^--recursive$")
GLOB_CHARS = re.compile(r"[*?\[]")
SEGMENT_SPLIT = re.compile(r"\|\||&&|[|;&\n]")
KNOWN_TOOLS = {"Read", "Bash"} | WRITE_TOOLS | SEARCH_TOOLS
PATH_KEY = re.compile(r"path|file|dir|folder|root|cwd|location|source|dest|target", re.I)


class RegistryError(Exception):
    pass


def load_registry():
    """Returns {wiki_root: owner} or None when there is no registry."""
    if not REGISTRY.exists():
        return None
    entries, cur = [], None
    for n, line in enumerate(REGISTRY.read_text().splitlines(), 1):
        s = line.split("#", 1)[0].rstrip()
        if not s.strip() or s.strip() == "wikis:":
            continue
        m = re.match(r"^\s*(-\s+)?(agent|path):\s*(.+?)\s*$", s)
        if not m:
            raise RegistryError(f"line {n}: expected '- agent: <name>' or 'path: <dir>'")
        if m.group(1):
            cur = {}
            entries.append(cur)
        elif cur is None:
            raise RegistryError(f"line {n}: field outside an entry")
        key, val = m.group(2), m.group(3).strip("'\"")
        if key in cur:
            raise RegistryError(f"line {n}: duplicate '{key}' in one entry")
        cur[key] = val
    wikis, agents = {}, set()
    for e in entries:
        if set(e) != {"agent", "path"}:
            raise RegistryError(f"entry {e} needs both 'agent' and 'path'")
        if Path(e["path"]).is_absolute():
            raise RegistryError(f"path must be relative to the repository root: {e['path']}")
        root = (ROOT / e["path"]).resolve()
        if root == ROOT or ROOT not in root.parents:
            raise RegistryError(f"path must be a directory inside the repository: {e['path']}")
        if e["agent"] in agents:
            raise RegistryError(f"agent '{e['agent']}' owns more than one wiki")
        if root in wikis:
            raise RegistryError(f"wiki '{e['path']}' has more than one owner")
        agents.add(e["agent"])
        wikis[root] = e["agent"]
    for a in wikis:
        for b in wikis:
            if a != b and a in b.parents:
                raise RegistryError(f"wikis may not nest: {a.relative_to(ROOT)} contains {b.relative_to(ROOT)}")
    return wikis


def resolve(p, cwd):
    p = Path(str(p)).expanduser()
    return (p if p.is_absolute() else cwd / p).resolve()


def rel(p):
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


class Denied(Exception):
    pass


def deny(reason):
    raise Denied(reason)


def emit_deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}))


class Fence:
    def __init__(self, wikis, agent):
        self.agent = agent
        self.foreign = {root: owner for root, owner in wikis.items() if owner != agent}

    def who(self):
        return f"agent '{self.agent}'" if self.agent else "this session (no agent)"

    def check_inside(self, p):
        for root, owner in self.foreign.items():
            if p == root or root in p.parents:
                deny(f"{rel(p)} is inside wiki {rel(root)}, which belongs to agent '{owner}'; "
                     f"{self.who()} has no access. Ask that agent instead.")

    def check_covers(self, p):
        for root, owner in self.foreign.items():
            if p in root.parents:
                deny(f"Searching {rel(p)} would include wiki {rel(root)} (owned by '{owner}'). "
                     f"Narrow the path to exclude it.")

    def check_protected_write(self, p):
        if is_protected(p):
            deny(f"{rel(p)} is protected (wiki registry, fence hook, or settings); only the human edits it.")


def is_protected(p):
    return p in PROTECTED_FILES or any(p == d or d in p.parents for d in PROTECTED_DIRS)


def path_tokens(segment):
    try:
        toks = shlex.split(segment, comments=True)
    except ValueError:
        toks = segment.split()
    out = []
    for t in toks:
        t = t.lstrip("<>(&0123456789") if re.match(r"^\d*[<>]", t) else t
        if "=" in t and t.startswith("-"):
            t = t.split("=", 1)[1]
        if t:
            out.append(t)
    return out


def looks_like_path(t, cwd):
    if t.startswith("-"):
        return False
    return "/" in t or t in (".", "..", "~") or t.startswith("~") or GLOB_CHARS.search(t) or (cwd / t).exists()


SELFTEST_CMD = re.compile(r"""\s*python3\s+(["']?)([^\s"';|&<>]*wiki-fence\.py)\1\s+--selftest\s*""")


def check_bash(cmd, cwd, fence):
    m = SELFTEST_CMD.fullmatch(cmd)
    if m and resolve(m.group(2), cwd) == HOOK:
        return  # running this hook's read-only self-test
    if any(w in cmd for w in PROTECTED_WORDS):
        deny("Commands may not reference the wiki registry, fence hook, or settings files; "
             "use the Read tool to view them. Only the human edits them.")
    fence.check_inside(cwd)
    for root in fence.foreign:
        for form in {str(root), rel(root)}:
            if form in cmd:
                fence.check_inside(root)
    for seg in SEGMENT_SPLIT.split(cmd):
        toks = path_tokens(seg)
        if not toks:
            continue
        while toks and re.match(r"^\w+=", toks[0]):  # leading VAR=value
            toks.pop(0)
        if toks and toks[0] in ("sudo", "env", "command", "exec", "nohup", "time", "xargs"):
            toks.pop(0)
        if not toks:
            continue
        name = Path(toks[0]).name
        args = toks[1:]
        if name == "git" and args[:1] == ["grep"]:
            recursive, args = True, args[1:]
        else:
            recursive = name in RECURSIVE_CMDS or (
                name in RECURSIVE_IF_FLAG and any(RECURSIVE_FLAG.match(a) for a in args))
        paths = []
        for a in args:
            if not looks_like_path(a, cwd):
                continue
            if GLOB_CHARS.search(a):
                base = a if Path(a).expanduser().is_absolute() else str(cwd / a)
                matches = glob.glob(str(Path(base).expanduser()), recursive=True)
                paths.extend(resolve(m, cwd) for m in matches)
                prefix = GLOB_CHARS.split(a, maxsplit=1)[0]
                if "/" in prefix:  # a bare pattern like *.py names no directory
                    paths.append(resolve(prefix.rsplit("/", 1)[0] or "/", cwd))
                recursive = recursive or "**" in a
            else:
                paths.append(resolve(a, cwd))
        if name == "cd" and not args:
            paths.append(Path.home())
        for p in paths:
            if is_protected(p):
                deny(f"Commands may not touch {rel(p)} (wiki registry, fence hook, or settings); "
                     "use the Read tool to view it. Only the human edits it.")
            fence.check_inside(p)
        if name in ("cd", "pushd") and paths:
            cwd = paths[0]  # later segments run from here
        if recursive:
            for p in paths or [cwd]:
                fence.check_covers(p)


def input_paths(value, key=""):
    """Yields string values held under path-like keys, at any depth."""
    if isinstance(value, dict):
        for k, v in value.items():
            yield from input_paths(v, str(k))
    elif isinstance(value, list):
        for v in value:
            yield from input_paths(v, key)
    elif isinstance(value, str) and PATH_KEY.search(key):
        v = value.strip()
        if v.startswith("file://"):
            v = v[len("file://"):]
        if v and "://" not in v and "\n" not in v:
            yield v


def check_other_tool(tool, ti, cwd, fence):
    for v in input_paths(ti):
        p = resolve(v, cwd)
        if is_protected(p):
            deny(f"{tool} may not touch {rel(p)} (wiki registry, fence hook, or settings); "
                 "use the Read tool to view it. Only the human edits it.")
        fence.check_inside(p)
        if p.is_dir():
            fence.check_covers(p)


def evaluate(data):
    """Raises Denied(reason) to block the call; returns normally to allow it."""
    tool = data.get("tool_name", "")
    ti = data.get("tool_input") or {}
    cwd = Path(data.get("cwd") or ".").resolve()
    try:
        wikis = load_registry()
    except RegistryError as e:
        deny(f"Wiki registry {rel(REGISTRY)} is invalid ({e}); all file access is blocked until the human fixes it.")
    if wikis is None:
        return
    fence = Fence(wikis, data.get("agent_type") or None)

    if tool == "Bash":
        check_bash(ti.get("command", ""), cwd, fence)
        return
    if tool in SEARCH_TOOLS:
        p = resolve(ti.get("path") or str(cwd), cwd)
        if tool == "Glob":  # the search root is path + the pattern's literal directory prefix
            pattern = ti.get("pattern", "")
            prefix = GLOB_CHARS.split(pattern, maxsplit=1)[0]
            if "/" in prefix:
                p = resolve(prefix.rsplit("/", 1)[0] or "/", p)
            for m in glob.glob(str(resolve(ti.get("path") or str(cwd), cwd) / pattern), recursive=True)[:5000]:
                fence.check_inside(Path(m).resolve())
        fence.check_inside(p)
        fence.check_covers(p)
        return
    if tool not in KNOWN_TOOLS:
        check_other_tool(tool, ti, cwd, fence)
        return
    target = ti.get("file_path") or ti.get("notebook_path")
    if target:
        p = resolve(target, cwd)
        if tool in WRITE_TOOLS:
            fence.check_protected_write(p)
        fence.check_inside(p)


def selftest():
    print(f"wiki-fence {VERSION} at {rel(HOOK)}")
    try:
        wikis = load_registry()
    except RegistryError as e:
        print(f"FAIL  registry {rel(REGISTRY)} is invalid: {e}")
        return 1
    if not wikis:
        print(f"no wikis registered in {rel(REGISTRY)}; nothing is fenced")
        return 1
    failures = 0

    def expect(want, label, data):
        nonlocal failures
        try:
            evaluate({"cwd": str(ROOT), **data})
            got = "allow"
        except Denied:
            got = "deny"
        ok = got == want
        failures += not ok
        print(f"{'ok  ' if ok else 'FAIL'}  {want:5}  {label}")

    reg = {"tool_name": "Edit", "tool_input": {"file_path": str(REGISTRY), "old_string": "a", "new_string": "b"}}
    for root, owner in sorted(wikis.items()):
        w = rel(root)
        read = {"tool_name": "Read", "tool_input": {"file_path": str(root / "CLAUDE.md")}}
        bash = {"tool_name": "Bash", "tool_input": {"command": f"cat {w}/CLAUDE.md"}}
        expect("allow", f"{w}: owner '{owner}' reads", {**read, "agent_type": owner})
        expect("deny", f"{w}: plain session reads", read)
        expect("deny", f"{w}: another agent reads", {**read, "agent_type": "__selftest_other__"})
        expect("deny", f"{w}: plain session cats via Bash", bash)
        expect("deny", f"{w}: owner edits the registry", {**reg, "agent_type": owner})
    print(f"{len(wikis)} wikis, {failures} failures")
    return 1 if failures else 0


def main():
    if sys.argv[1:] == ["--selftest"]:
        sys.exit(selftest())
    try:
        evaluate(json.load(sys.stdin))
    except Denied as d:
        emit_deny(str(d))
    except Exception as e:  # fail closed
        emit_deny(f"wiki-fence hook error ({type(e).__name__}: {e}); call blocked. Report this to the human.")


if __name__ == "__main__":
    main()
