---
title: Retrieval-Augmented Generation (RAG)
type: concept
description: Retrieval-augmented generation and why the llm-wiki source criticizes it; consult when contrasting query-time retrieval with compiled knowledge.
tags: [contrast, retrieval]
sources: [llm-wiki]
updated: 2026-10-09
---

# Retrieval-Augmented Generation (RAG)

Upload documents, retrieve relevant chunks at query time, generate an answer. [[llm-wiki]] criticizes it because the LLM rediscovers knowledge from scratch on every question, so synthesis across many documents is redone each time and nothing is built up. It cites NotebookLM and ChatGPT file uploads as examples. The [[llm-wiki-pattern]] is proposed as the accumulating alternative.
