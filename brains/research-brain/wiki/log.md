---
title: Log
type: overview
description: Append-only chronology of ingests, queries, lints, and schema changes; consult to see what changed and when.
tags: [meta]
sources: []
updated: 2026-10-11
---

# Log

Append-only. Heading format: `## [YYYY-MM-DD] op | Title`.

## [2026-10-09] schema | Wiki initialized
- Created directory layout, `CLAUDE.md` schema, [[index]], [[overview]], and `tools/wiki.py`.

## [2026-10-09] ingest | LLM Wiki
- Created [[llm-wiki]], [[llm-wiki-pattern]], [[rag]], [[wiki-operations]], [[index-and-log]], [[obsidian]], [[qmd]], [[memex]].
- Updated [[index]], [[overview]].

## [2026-10-09] schema | Digest command and raw capture rules
- Added `wiki.py digest` and `/digest`; `CLAUDE.md` now lists all helper subcommands.
- `raw/` is now write-once for the maintainer: new captures allowed with `source`/`captured`/`capture_method` frontmatter, existing files never modified.

## [2026-10-10] schema | description and aliases frontmatter
- `description` is now required on every page (lint errors on missing, empty, or `TODO` placeholder); `aliases` is optional. Added to `CLAUDE.md` and scaffolded by `wiki.py new`.
- Wrote descriptions for all existing pages, including [[index]], [[log]], [[overview]].
- Added `tools/eval/questions.tsv` (16 questions) as the search regression set.

## [2026-10-10] schema | SQLite/FTS5 index
- `tools/wiki.py` now runs on a gitignored, auto-synced `.wiki.db` (FTS5); added `eval`, `reindex`, `doctor`. Search returns section line ranges plus descriptions.
- `CLAUDE.md` updated: helper CLI row, Query workflow (read line ranges), aliases indexed, Lint step for `eval`.
- Eval: hit@1 8/16 -> 14/16, hit@3 13/16 -> 16/16, mean output 1176 -> 857 chars (16 questions; weights provisional).

## [2026-10-10] schema | Portable layout, pattern doc moved, defuddle dropped
- Moved `raw/llm-wiki.md` to the wiki root as `llm-wiki.md` (user-directed exception to write-once); [[llm-wiki]] `raw:` now points there.
- `CLAUDE.md`: removed git instructions (directory is meant to be dropped into host repos); added `llm-wiki.md` and `SETUP.md` to Layers; removed `defuddle` capture method; dropped the rule to copy `capture_method` onto source pages (provenance to be resolved from the index instead).
- Added `SETUP.md`: `.gitignore`, FTS5 check, capture tooling marked as needing an update.

## [2026-10-10] schema | raw/ write-once tracking, captured, provenance
- `tools/wiki.py`: `.wiki.db` now stores mtime/size/sha256 baselines and capture frontmatter for every file under `raw/`. A changed or deleted raw file is a `lint` error; `reindex --accept-raw <path>` re-baselines one file. Added `captured <url>` and `provenance <page>|--all [--method M]`.
- `CLAUDE.md`: tools row, existing-capture check, provenance rule, write-once violation rule.

## [2026-10-10] schema | raw-manifest.tsv
- `raw/` write-once baselines now live in `raw-manifest.tsv` at the wiki root; `.wiki.db` only caches them, so deleting the DB or `reindex --full` no longer accepts raw changes. The manifest wins on disagreement.
- `CLAUDE.md` Layers rows and `SETUP.md` (step 2) updated.

## [2026-10-10] schema | Per-agent wikis: skill, registry, fence hook
- `CLAUDE.md` renamed to `SCHEMA.md` and rewritten for a single owning agent working from the host repository root; ingest and health workflows folded in from the former `/ingest` and `/digest` commands, which were removed.
- Added `WIKI.md` (purpose, scope, capture criteria template), `.claude/skills/wiki/` (`SKILL.md` and `registry.yaml`: agent-to-wiki ownership), and `.claude/hooks/wiki-fence.py` (PreToolUse hook denying non-owners, sweeping searches, and edits to the registry, hook, or settings).
- `SETUP.md` rewritten as install steps for a host repository. Seed content (the [[llm-wiki]] ingest) is kept.

## [2026-10-10] schema | Fence covers all tools
- `wiki-fence.py` now runs for every tool (`"matcher": "*"` in `SETUP.md`); tools other than the built-in file tools and Bash are checked by every input field whose name suggests a path, so plugin and MCP file tools are fenced too.

## [2026-10-10] schema | CLAUDE.md is the install script
- `SETUP.md` merged into `CLAUDE.md`, rewritten as steps for the host repository's agent: owner check, preflight (disabled hooks, formatters, ignore rules, host instructions, Python), `WIKI.md` drafted with the human, skill and hook copied in without overwriting, registry and agent-definition entries, tooling exclusions, a dry run of the fence, cleanup, and a rewrite of `CLAUDE.md` into the owner's entry point. Turning on the fence is the last step, since it locks out the installing session.
- `SCHEMA.md` and `WIKI.md` now refer to `CLAUDE.md` instead of `SETUP.md`.

## [2026-10-10] schema | Install fixes from the first rehearsal
- `wiki-fence.py`: added `--selftest` (checks every registered wiki without naming a wiki path; the fence allows exactly that command), so an install can verify the fence while it is live.
- `CLAUDE.md` install steps reordered: everything inside the wiki happens while it is unregistered, then hook/skill, registry, self-test and settings. Under a live fence, protected changes become an exact to-do list for the human. Preflight now detects a live fence, lists every existing hook (formatters, missing scripts), and checks the owner's `tools:` line; ignore-rule handling covers directory-level patterns; pre-commit merge recipe, host `CLAUDE.md` exception wording, and settings merge of a single object are spelled out.

## [2026-10-10] schema | Live-fence rehearsal and follow-ups
- Rehearsed a real headless install in a host with a live fence: the installer handed protected edits to the human, `--selftest` passed (2 wikis, 0 failures), and afterwards the installer was denied the wiki while the owner (run with `--agent`) read it and was denied the other wiki.
- `CLAUDE.md`: notes on Claude Code permission prompts and narrow searching under a live fence; compare hook copies with Read; don't invent capture criteria. `wiki-fence.py` gained a `VERSION` printed by `--selftest`.

## [2026-10-10] schema | Template guard and development notes
- `CLAUDE.md` template check now keys on the `solinari` repository; added a "Template development" section (search agent, hook `VERSION` bumps, fence re-test checklist, accepted fence limits, search eval baseline, open capture-tooling item). Step 7 removes it from installed copies.

## [2026-10-10] schema | Moved into solinari
- Template moved from `~/repos/astinus` to `solinari/astinus`, where the `CLAUDE.md` template check recognises it; added a row to solinari's `README.md`.

## [2026-10-11] schema | Install rehearsal fixes and human-run fence step
- Rehearsed a full install in a throwaway host (two wikis, Prettier hook, pre-commit `exclude:`, `*.tsv` ignore rule): `--selftest` 0 failures, 20 hand-run hook cases as expected, and real headless sessions showed the owner allowed, a plain session denied, and the owner allowed as a subagent spawned from a plain session.
- `NOT-CLAUDE.md` step 5: the `*.tsv` negation now also covers `tools/eval/questions.tsv`, with a `git check-ignore -v` confirmation. Step 3: the leading HTML comment in `WIKI.md` is deleted once its placeholders are filled.
- `NOT-CLAUDE.md` step 10: turning the fence on is now the human's step. The installer hands over the exact settings change, waits for confirmation, then only verifies it by reading; the report states whether it has been done.

## [2026-10-11] schema | Renamed template from astinus to hesiod
- Directory renamed `astinus/` to `hesiod/`; updated references in solinari's `README.md` and `CLAUDE.md` and in the `sqlite-fts5` agent description. Earlier log entries keep the old name as history.

## [2026-10-11] schema | Installed in mnemosyne
- Owner: `researcher` (`.claude/agents/researcher.md`).
- Changes outside the wiki: copied the `wiki` skill, `wiki-fence.py` (version 2026-10-10) and an empty `registry.yaml` into the host's `.claude/`; registered the wiki in the registry; added `Bash` to the researcher's tools and the owner line to its definition; added a `bash-guard` mode to `scripts/research_check.py` and registered it on `PreToolUse` for `Bash` in `.claude/settings.json`, so the researcher may run only `wiki.py`. The host has no formatters or linters, so no exclusions or ignore-file edits were needed. The existing `SubagentStop` and `PreToolUse` (`Write|Edit`) hooks are unchanged. `WIKI.md` was filled in from a purpose the human approved; unresolved items are marked provisional.
