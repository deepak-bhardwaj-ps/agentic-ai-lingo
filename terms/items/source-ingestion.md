---
title: Source ingestion
short_description: Bringing source material into a knowledge system so it can be prepared for search, reuse, or indexing.
category: Knowledge and wiki systems
tags:
  - knowledge base
  - source material
  - indexing
  - retrieval
status: active
aliases:
  - ingest
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as only file upload, when it usually includes text extraction, chunking, and indexing
  - Using it to mean the same thing as understanding the source, when it only prepares content for later use
  - Using it as a broad data-engineering term without the knowledge-system context
related_terms:
  - ingest
  - raw source
  - document loader
  - indexing
  - retrieval
evidence:
  - source_title: Document loader integrations - Docs by LangChain
    source_url: https://docs.langchain.com/oss/python/integrations/document_loaders
    source_type: official_docs
    relevance: This shows how source material is brought from external systems into a standard form before later retrieval steps, which matches the knowledge-system meaning of source ingestion.
    key_point: Document loaders read data from sources such as Slack, Notion, or Google Drive into LangChain's Document format so it can be handled consistently.
  - source_title: What is a Knowledge Source? - Azure AI Search
    source_url: https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-overview
    source_type: official_docs
    relevance: This gives a current, concrete example of ingestion in an agentic retrieval system and shows that ingestion includes processing before query time.
    key_point: Indexed knowledge sources ingest content into a search index before query time.
  - source_title: Knowledge - Open WebUI
    source_url: https://docs.openwebui.com/features/workspace/knowledge/
    source_type: official_docs
    relevance: This shows a current product workflow where uploaded files become searchable knowledge, which supports the practical meaning of source ingestion in a wiki or knowledge base.
    key_point: Files and collections are uploaded so the system can search, read, and reason over them later.
---

Source ingestion is the step where source material is brought into a knowledge system so it can be prepared for later use.

In practice, this usually means the system reads the source, extracts text, splits it into smaller pieces, adds metadata, and indexes it so search or retrieval can work well.

This matters because a knowledge base cannot reuse content properly until the source has been ingested. Good source ingestion makes later search, question answering, and linking more reliable.

It is not the same as understanding the source, and it is not just a file upload. In this glossary, source ingestion means the preparation step that turns raw source material into something the system can work with.
