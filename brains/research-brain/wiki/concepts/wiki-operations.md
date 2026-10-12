---
title: Wiki Operations
type: concept
description: The ingest, query, and lint operations that make up the wiki's working loop; consult for how each operation is meant to work.
tags: [workflow, ingest, query, lint]
sources: [llm-wiki]
updated: 2026-10-09
---

# Wiki Operations

Three operations from [[llm-wiki]], used in the [[llm-wiki-pattern]]:

- **Ingest**: add a source; the LLM reads it, discusses takeaways, writes a summary page, updates the index, entity and concept pages, and the log. One source can touch 10-15 pages. One-at-a-time with human involvement is preferred; batch ingest is possible with less supervision.
- **Query**: search the wiki (index first, see [[index-and-log]]), synthesize an answer with citations. Answers can be pages, tables, slide decks, charts. Valuable answers should be filed back as new pages so explorations compound.
- **Lint**: periodic health check for contradictions, stale claims, orphan pages, concepts lacking pages, missing cross-references, and data gaps; also a source of new questions and sources to seek.
