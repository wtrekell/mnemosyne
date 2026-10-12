---
title: Index and Log
type: concept
description: The two navigation files, index.md and log.md, their roles and formats; consult when deciding how to navigate or what to record.
tags: [navigation, conventions]
sources: [llm-wiki]
updated: 2026-10-09
---

# Index and Log

Two special files from [[llm-wiki]]:

- **index.md**: content-oriented catalog of every page with a link and one-line summary, grouped by category. Updated on every ingest and read first when answering queries. Works at moderate scale (~100 sources, hundreds of pages) without embedding-based search; beyond that consider [[qmd]].
- **log.md**: append-only chronology of ingests, queries, and lint passes. A consistent heading prefix such as `## [2026-04-02] ingest | Title` makes it parseable with unix tools, e.g. `grep "^## \[" log.md | tail -5`.

Part of the [[llm-wiki-pattern]]; used by all [[wiki-operations]].
