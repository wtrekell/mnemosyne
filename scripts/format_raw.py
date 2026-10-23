#!/usr/bin/env python3
"""PostToolUse hook: when a file is written under brains/research-brain/raw/, run prettier over all of raw/
and re-baseline every raw file it changed, so wiki.py lint reports no write-once violations.

Order matters: new files are baselined first (unformatted), then formatted, then the changed ones are
re-baselined with `wiki.py reindex --accept-raw`. The human asked for this re-baselining explicitly."""

import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

WIKI_REL = Path("brains/research-brain")


def digests(raw):
    return {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(raw.rglob("*")) if p.is_file()}


def run(cmd, root):
    result = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
    if result.returncode:
        sys.stderr.write("%s failed:\n%s%s" % (" ".join(map(str, cmd[:3])), result.stdout, result.stderr))
        sys.exit(2)
    return result


def main():
    payload = json.load(sys.stdin)
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parent.parent)
    wiki = Path(os.environ.get("FORMAT_RAW_WIKI") or root / WIKI_REL)
    raw = wiki / "raw"
    target = (payload.get("tool_input") or {}).get("file_path")
    if not target:
        return
    target = Path(target).resolve()
    if raw.resolve() not in target.parents:
        return

    wiki_py = [sys.executable, str(wiki / "tools/wiki.py")]
    # Homebrew's Prettier; hooks may run without Homebrew on PATH.
    prettier = shutil.which("prettier") or "/opt/homebrew/bin/prettier"
    empty_ignore = wiki / ".prettier-ignore-none"  # prettier otherwise skips gitignored brains/
    empty_ignore.write_text("")
    try:
        run(wiki_py + ["reindex"], root)
        before = digests(raw)
        run([prettier, "--write", "--log-level", "warn", "--ignore-path", str(empty_ignore), str(raw)], root)
        after = digests(raw)
    finally:
        empty_ignore.unlink(missing_ok=True)
    changed = [str(p.relative_to(wiki)) for p in after if before.get(p) != after[p]]
    if changed:
        run(wiki_py + ["reindex", "--accept-raw", *changed], root)
        print("prettier reformatted and re-baselined %d raw file(s)" % len(changed), file=sys.stderr)


if __name__ == "__main__":
    main()
