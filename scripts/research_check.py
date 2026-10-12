#!/usr/bin/env python3
"""Hooks for the researcher agent.

  stop    SubagentStop: checks the report the researcher wrote last and blocks
          until it passes. On a pass, copies the report into
          brains/research-brain/raw/ and writes a search log and a .json file
          linking the log to that copy in _logs/research/.
  guard   PreToolUse for Write and Edit: the researcher may not write outside
          the repository.
  bash-guard
          PreToolUse for Bash: the researcher may run only the wiki's own tool,
          `python3 brains/research-brain/tools/wiki.py <subcommand> ...`, with
          no shell syntax and no path outside the wiki.

Both read the hook JSON on stdin. No network, no model calls.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import re
import shlex
import shutil
import sys
from pathlib import Path

AGENT = "researcher"
WIKI_REL = Path("brains/research-brain")
RAW_REL = WIKI_REL / "raw"
LOG_REL = Path("_logs/research")
REQUIRED_SECTIONS = ("Findings", "Conflicts", "Appendix A", "Appendix B")
EVIDENCE_TOOL_PREFIXES = ("WebSearch", "WebFetch", "mcp__")
URL_RE = re.compile(r"https?://[^\s|)>\]\"'`\\]+")


# --- report ------------------------------------------------------------------


def split_front_matter(text):
    m = re.match(r"---\n(.*?)\n---[ \t]*\n?(.*)\Z", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fm[key.strip()] = value.strip()
    return fm, m.group(2)


def section_headings(body):
    headings, fenced = [], False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced and line.startswith("## "):
            headings.append(line[3:].strip())
    return headings


def appendix_b(body):
    m = re.search(r"^## Appendix B.*?(?=^## |\Z)", body, re.S | re.M)
    return m.group(0) if m else ""


def normalize_url(url):
    url = url.strip().rstrip(".,;:")
    url = re.sub(r"^https?://", "", url, flags=re.I)
    url = re.sub(r"^www\.", "", url, flags=re.I)
    return url.split("#", 1)[0].rstrip("/").lower()


def check_report(text, seen):
    problems = []
    fm, body = split_front_matter(text)
    if fm is None:
        return ["Front matter: the file must start with a --- block."]
    for key in ("created", "updated"):
        try:
            datetime.date.fromisoformat(fm.get(key, ""))
        except ValueError:
            problems.append("Front matter: '%s' must be a real date as YYYY-MM-DD." % key)
    headings = section_headings(body)
    for name in REQUIRED_SECTIONS:
        if not any(h.lower().startswith(name.lower()) for h in headings):
            problems.append("Sections: '## %s' is missing." % name)
    for url in URL_RE.findall(appendix_b(body)):
        if normalize_url(url) not in seen:
            problems.append("Provenance: this URL never appeared in this run's searches, fetches or request: %s" % url)
    return problems


# --- transcript --------------------------------------------------------------


def read_transcript(path):
    entries = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            try:
                entries.append(json.loads(line))
            except ValueError:
                continue
    return entries


def blocks(entry):
    content = (entry.get("message") or {}).get("content")
    return content if isinstance(content, list) else []


def tool_uses(entries):
    """Yield (timestamp, tool name, input, tool_use_id) in order."""
    for e in entries:
        if e.get("type") == "assistant":
            for b in blocks(e):
                if b.get("type") == "tool_use":
                    yield e.get("timestamp", ""), b.get("name", ""), b.get("input") or {}, b.get("id", "")


def flatten(content):
    if isinstance(content, str):
        return content
    if isinstance(content, dict):
        return "\n".join(flatten(v) for v in content.values())
    if isinstance(content, list):
        return "\n".join(flatten(v) for v in content)
    return "" if content is None else str(content)


def is_evidence_tool(name):
    return name.startswith(EVIDENCE_TOOL_PREFIXES)


def seen_urls(entries):
    """URLs from the request and from web and MCP tool traffic. The agent's own
    text and its Write, Edit and Read traffic are left out, so a URL it wrote
    into the report does not vouch for itself."""
    names = {tid: name for _, name, _, tid in tool_uses(entries)}
    chunks = [flatten(inp) for _, name, inp, _ in tool_uses(entries) if is_evidence_tool(name)]
    for e in entries:
        if e.get("type") != "user":
            continue
        content = (e.get("message") or {}).get("content")
        if isinstance(content, str):
            chunks.append(content)
        for b in blocks(e):
            if b.get("type") == "tool_result" and is_evidence_tool(names.get(b.get("tool_use_id"), "")):
                chunks.append(flatten(b.get("content")))
            elif b.get("type") == "text":
                chunks.append(b.get("text", ""))
    return {normalize_url(u) for u in URL_RE.findall("\n".join(chunks))}


def find_report_path(entries):
    """The last .md file the agent wrote that opens with front matter holding 'topic'."""
    found = None
    for _, name, inp, _ in tool_uses(entries):
        path = str(inp.get("file_path", ""))
        if name == "Write" and path.endswith(".md"):
            fm, _ = split_front_matter(str(inp.get("content", "")))
            if fm and "topic" in fm:
                found = path
    return found


def search_log(entries, title):
    errors = {}
    for e in entries:
        if e.get("type") == "user":
            for b in blocks(e):
                if b.get("type") == "tool_result":
                    errors[b.get("tool_use_id")] = bool(b.get("is_error"))
    rows, last = [], ""
    for ts, name, inp, tid in tool_uses(entries):
        if not is_evidence_tool(name):
            continue
        if name == "WebSearch":
            kind, what = "search", inp.get("query", "")
        elif name == "WebFetch":
            kind, what = "fetch", inp.get("url", "")
        else:
            kind, what = name.split("__")[-1], flatten(inp).replace("\n", " ")
        rows.append("| %s | %s | %s | %s |" % (
            ts[:19].replace("T", " ") or "?", kind, str(what).replace("|", "\\|"),
            "failed" if errors.get(tid) else "ok"))
        last = ts
    return "\n".join([
        "# Search log: %s" % title,
        "",
        "As of: %s (UTC)." % (last[:10] or "no searches"),
        "",
        "| Time (UTC) | Kind | Query or URL | Status |",
        "| --- | --- | --- | --- |",
    ] + rows) + "\n"


# --- stop hook ---------------------------------------------------------------


def ensure_raw_copy(report, root):
    """Copy the report into raw/ unless an identical file is already there."""
    raw = Path(root) / RAW_REL
    report = Path(report).resolve()
    raw.mkdir(parents=True, exist_ok=True)
    if raw.resolve() in report.parents:
        return report
    data = report.read_bytes()
    for p in raw.rglob("*"):
        if p.is_file() and p.stat().st_size == len(data) and p.read_bytes() == data:
            return p
    dest = raw / report.name
    if dest.exists():
        dest = raw / ("%s-%s%s" % (report.stem, hashlib.sha256(data).hexdigest()[:8], report.suffix))
    shutil.copyfile(str(report), str(dest))
    return dest


def write_log(entries, copy, root):
    root = Path(root).resolve()
    log_dir = root / LOG_REL
    log_dir.mkdir(parents=True, exist_ok=True)
    log = log_dir / (Path(copy).stem + ".log.md")
    log.write_text(search_log(entries, Path(copy).name), encoding="utf-8")
    link = log_dir / (Path(copy).stem + ".json")
    link.write_text(json.dumps({
        "log": str(log.relative_to(root)),
        "report": str(Path(copy).resolve().relative_to(root)),
    }, indent=2) + "\n", encoding="utf-8")


def run_stop(payload, root):
    """Return a block reason, or None when the agent may finish."""
    if payload.get("agent_type") not in (None, AGENT):
        return None
    tpath = os.path.expanduser(payload.get("agent_transcript_path") or "")
    if not os.path.isfile(tpath):
        return None
    entries = read_transcript(tpath)
    report = find_report_path(entries)
    if not report or not os.path.isfile(report):
        return None
    problems = check_report(Path(report).read_text(encoding="utf-8"), seen_urls(entries))
    if problems:
        return ("The report at %s failed these checks. Fix each one in the file, then finish.\n- %s"
                % (report, "\n- ".join(problems)))
    write_log(entries, ensure_raw_copy(report, root), root)
    return None


# --- guard hook --------------------------------------------------------------


def guard_decision(payload, root):
    """Return a deny reason when the researcher writes outside the repository."""
    if payload.get("agent_type") != AGENT or payload.get("tool_name") not in ("Write", "Edit"):
        return None
    path = (payload.get("tool_input") or {}).get("file_path")
    if not path:
        return None
    base, target = Path(root).resolve(), Path(path).resolve()
    if target == base or base in target.parents:
        return None
    return "The researcher may write only inside the repository (%s); %s is outside it." % (base, target)


# --- bash-guard hook ---------------------------------------------------------

WIKI_SUBCOMMANDS = {"search", "lint", "new", "backlinks", "status", "captured",
                    "provenance", "log", "eval", "digest", "reindex", "doctor"}
SHELL_SYNTAX = re.compile(r"[;&|<>$`\\\n\r(){}*?\[\]~!]")


def inside(path, base):
    return path == base or base in path.parents


def bash_decision(payload, root):
    """Return a deny reason unless the researcher runs only the wiki tool, as one plain command."""
    if payload.get("agent_type") != AGENT or payload.get("tool_name") != "Bash":
        return None
    cmd = (payload.get("tool_input") or {}).get("command", "")
    wiki = (Path(root) / WIKI_REL).resolve()
    tool = wiki / "tools" / "wiki.py"
    usage = "The researcher may run only: python3 %s <subcommand> ..." % tool.relative_to(Path(root).resolve())
    if SHELL_SYNTAX.search(cmd):
        return "%s Shell syntax (; & | < > $ ` \\ ( ) { } * ? [ ] ~ ! or a newline) is not allowed." % usage
    try:
        argv = shlex.split(cmd)
    except ValueError:
        return "%s The command has unbalanced quotes." % usage
    cwd = Path(payload.get("cwd") or root)
    if len(argv) < 3 or argv[0] != "python3" or (cwd / argv[1]).resolve() != tool:
        return usage
    if argv[2] not in WIKI_SUBCOMMANDS:
        return "%s Unknown subcommand '%s'." % (usage, argv[2])
    if "--accept-raw" in argv[3:]:
        return "--accept-raw re-baselines write-once raw files and needs the human's agreement."
    for arg in argv[3:]:
        if arg.startswith("-") or "/" not in arg or re.match(r"[a-z][a-z0-9+.-]*://", arg, re.I):
            continue
        if not (inside((cwd / arg).resolve(), wiki) or inside((wiki / arg).resolve(), wiki)):
            return "The path '%s' is outside %s." % (arg, wiki)
    return None


def project_root():
    env = os.environ.get("CLAUDE_PROJECT_DIR")
    return Path(env) if env else Path(__file__).resolve().parent.parent


def main(argv):
    if len(argv) != 2 or argv[1] not in ("stop", "guard", "bash-guard"):
        sys.exit("usage: research_check.py stop|guard|bash-guard")
    payload = json.load(sys.stdin)
    if argv[1] == "stop":
        reason = run_stop(payload, project_root())
        if reason:
            print(json.dumps({"decision": "block", "reason": reason}))
    else:
        reason = (bash_decision if argv[1] == "bash-guard" else guard_decision)(payload, project_root())
        if reason:
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason}}))


if __name__ == "__main__":
    main(sys.argv)
