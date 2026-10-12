---
title: LLM Wiki Pattern
type: concept
description: The core pattern of an LLM incrementally building a persistent interlinked markdown wiki instead of retrieving chunks at query time; consult when reasoning about this wiki's design.
tags: [pattern, architecture]
sources: [llm-wiki]
updated: 2026-10-09
---

# LLM Wiki Pattern

The LLM incrementally builds and maintains a persistent, interlinked markdown wiki between the human and the raw sources, instead of retrieving chunks at query time ([[rag]]). Knowledge is compiled once and kept current; cross-references and flagged contradictions are already in place when a question arrives. Source: [[llm-wiki]].

## Layers
- **Raw sources**: curated, immutable; the LLM reads but never modifies them.
- **Wiki**: LLM-generated pages (summaries, entities, concepts, comparisons, overview). The LLM owns this layer entirely.
- **Schema**: a document such as CLAUDE.md defining structure, conventions, and workflows. Co-evolved by human and LLM.

## Division of labor
The human sources, explores, and asks questions. The LLM summarizes, cross-references, files, and does bookkeeping. Analogy from the source: [[obsidian]] is the IDE, the LLM is the programmer, the wiki is the codebase.

## Operations and navigation
See [[wiki-operations]] and [[index-and-log]].
