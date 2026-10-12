---
title: LLM Wiki (source)
type: source
description: Summary of the llm-wiki idea file defining the LLM-maintained wiki pattern; consult for the original claims and the pattern's rationale.
tags: [pattern, knowledge-management]
sources: []
raw: llm-wiki.md
ingested: 2026-10-09
updated: 2026-10-09
---

# LLM Wiki (source)

An abstract "idea file" describing a pattern for personal knowledge bases that an LLM agent builds and maintains. It is intentionally non-prescriptive: the agent and human instantiate the specifics together.

## Key claims
- Conventional RAG re-derives knowledge from raw chunks on every question, so nothing accumulates. The alternative is a persistent wiki the LLM compiles once and keeps current. See [[llm-wiki-pattern]] and [[rag]].
- Three layers: immutable raw sources, an LLM-owned wiki, and a schema document (e.g. CLAUDE.md) that makes the LLM a disciplined maintainer. See [[llm-wiki-pattern]].
- Three operations: ingest, query, lint. Good query answers should be filed back as pages. See [[wiki-operations]].
- Two navigation files: content-oriented `index.md` and chronological, grep-friendly `log.md`. The index replaces embedding search up to roughly 100 sources and hundreds of pages. See [[index-and-log]].
- Optional tooling: a search engine such as [[qmd]] once the index stops being enough; [[obsidian]] as the reading interface (Web Clipper, graph view, Dataview, Marp).
- Wikis fail from bookkeeping burden, not from reading or thinking; LLMs make maintenance cost near zero. The idea is a modern answer to the maintenance problem Bush left open in the [[memex]].

## Notable details
- A single ingest may touch 10-15 pages; the author prefers ingesting one source at a time while staying involved.
- Images should be downloaded locally so the agent can view them; the agent reads text first, then images separately.
- The wiki is just a git repo of markdown, giving history and branching for free.
