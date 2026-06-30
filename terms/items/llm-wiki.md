---
title: LLM wiki
short_description: A wiki that an LLM helps build and maintain from source notes and documents.
category: Knowledge and wiki systems
tags:
  - knowledge-management
  - wiki
  - llm
  - personal-knowledge-base
status: draft
aliases:
  - Karpathy LLM wiki
  - Karpathy-style LLM wiki
meaning_type: novel
novelty_level: high
maturity_level: emerging
common_misuse:
  - Treating it as a general synonym for a normal wiki or for RAG
  - Assuming the LLM only answers questions, rather than also writing and maintaining the pages
related_terms:
  - knowledge base
  - wiki
  - backlinks
  - RAG
  - raw source
evidence:
  - source_title: LLM Wiki
    source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
    source_type: engineering_blog
    relevance: This is the clearest primary source for the term and explains the pattern Karpathy means by it.
    key_point: The wiki is a persistent, interlinked markdown knowledge base that the LLM incrementally compiles and maintains from raw sources.
  - source_title: Internal links - Obsidian Help
    source_url: https://obsidian.md/help/links
    source_type: official_docs
    relevance: Obsidian is a common file-based wiki environment for this pattern, and its docs explain the link style the term relies on.
    key_point: Obsidian uses wikilinks to connect notes into a network of knowledge, which matches the linked-page structure of an LLM wiki.
  - source_title: The Missing Data Layer in LLM Knowledge Bases
    source_url: https://xata.io/blog/llm-knowledge-bases
    source_type: engineering_blog
    relevance: Confirms how the pattern is used in practice and distinguishes it from a plain retrieval system.
    key_point: The LLM writes and maintains the wiki, which is treated as compiled knowledge rather than just a retrieval index.
---

An LLM wiki is a wiki that an LLM helps build and keep up to date from source notes, articles, or files.

In practice, the LLM reads new material, pulls out important ideas, links related pages, and updates the wiki when something changes.

This matters because the knowledge can grow over time instead of being re-checked from scratch every time you ask a question.

It is not just a normal wiki, and it is not the same as RAG. A normal wiki is written by people. RAG mainly looks up chunks of text and answers from them. An LLM wiki uses the model to do the writing and organising as well.
