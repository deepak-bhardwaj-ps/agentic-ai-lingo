---
title: Raw source
short_description: Original material kept unchanged so a knowledge base can build from it later.
category: Knowledge and wiki systems
tags:
  - knowledge base
  - source material
  - wiki workflow
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating raw source as the finished wiki page instead of the original input
  - Editing raw source in place when the point is to keep the original unchanged
  - Using it to mean any data at all, rather than the specific source material that feeds a knowledge base
related_terms:
  - source ingestion
  - ingest
  - source material
  - source of truth
  - compiled wiki
evidence:
  - source_title: llm-wiki
    source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
    source_type: industry_article
    relevance: This is the clearest primary description of the Karpathy-style wiki pattern the glossary term comes from, and it explains the role of raw sources in that system.
    key_point: Raw sources are the curated source documents, kept immutable, and treated as the source of truth.
  - source_title: Knowledge Base Documentation
    source_url: https://docs.senso.ai/docs/knowledge-base
    source_type: official_docs
    relevance: This shows a current product implementation that accepts raw files and raw text before processing them into a knowledge base, which supports the practical meaning of the term.
    key_point: Raw content can come from files or directly from text, and it is then parsed, chunked, and embedded for later querying.
  - source_title: llmwiki
    source_url: https://github.com/microsoft/llmwiki
    source_type: engineering_blog
    relevance: This Microsoft project uses the same three-layer structure and reinforces that raw sources are the unmodified input layer in a self-maintaining wiki.
    key_point: Raw sources are immutable source documents; the LLM reads them but does not modify them.
---

Raw source is the original material that a knowledge base or wiki is built from.

In practice, it means the untouched files, notes, articles, papers, images, or transcripts that are collected before anything is summarised or rewritten.

This matters because the raw source stays as the evidence layer. The wiki or summary can change over time, but the raw source lets you check where the information came from.

It is not the finished wiki page. It is also not the same as every piece of data in a system. In this glossary, raw source means the original input that should stay unchanged while other layers are built from it.
