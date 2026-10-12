---
name: wiki
description: Use your own registered wiki (your "second brain") as a reference bank. Look things up in it, capture material that meets its criteria, ingest sources dropped into its raw/ folder, and keep it healthy. Use whenever an agent that owns a wiki needs background knowledge it may already have filed, finds something worth keeping, is asked to ingest or capture, or is asked about the wiki's state. Not for agents without a registered wiki; they have no access.
---

# Wiki

Each wiki in this repository belongs to exactly one agent. `registry.yaml` (next to this file) records which. A hook blocks every other agent and session from that wiki's directory, and blocks everyone from changing the registry.

## 1. Find your wiki
Read `registry.yaml` in this skill's directory. Find the entry whose `agent` is your agent name; its `path` (relative to the repository root) is your wiki. If there is no entry for you, you have no wiki: stop and say so. Don't look for one, and don't try another wiki's path.

## 2. Load its rules (once per session, before any other wiki work)
- `<wiki>/SCHEMA.md`: how the wiki is built and maintained (layers, page conventions, capture rules, workflows). It governs everything below.
- `<wiki>/WIKI.md`: this wiki's purpose, scope, and capture criteria.

Run every tool command as `python3 <wiki>/tools/wiki.py ...`.

## 3. Pick the workflow (all defined in SCHEMA.md)
| You need to | Workflow |
| --- | --- |
| Answer a question from what you've filed | Query: `index.md` first, then `search`, then read only the returned line ranges |
| Keep something you found (host file, URL, conversation) | Capture rules: check `WIKI.md` criteria, then `captured`, then a write-once file in `raw/` |
| Process files waiting in `raw/` | Ingest: `status` for the queue, one source at a time |
| Report on the wiki's state | Health: `digest`, read-only |
| Fix problems or tidy up | Lint |

## Ground rules
- You are the wiki's only writer. Don't delegate wiki work to subagents; the hook blocks them.
- Stay inside your own wiki. A denied call means a path belongs to another agent; narrow your path, don't work around the denial.
- Never edit `registry.yaml`, the hook, or settings files. Changes to ownership go through the human.
