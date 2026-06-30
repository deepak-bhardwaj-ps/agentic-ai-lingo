---
title: Ingest
short_description: Bringing content into a system so it can store, process, index, or search it.
category: Knowledge and wiki systems
tags:
  - knowledge base
  - documents
  - indexing
  - import
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating ingest as the same as reading or understanding content
  - Using it to mean only file upload, when it usually includes processing and indexing too
related_terms:
  - source ingestion
  - import
  - document loader
  - indexing
  - knowledge base
evidence:
  - source_title: Retrieval - Docs by LangChain
    source_url: https://docs.langchain.com/oss/python/langchain/retrieval
    source_type: official_docs
    relevance: This explains ingestion in a modern AI workflow as bringing external data into a retrieval pipeline, which matches how the term is used in knowledge systems.
    key_point: LangChain describes document loaders as a way to ingest data from external sources into standard document objects.
  - source_title: What is a Knowledge Source?
    source_url: https://learn.microsoft.com/en-us/azure/search/agentic-knowledge-source-overview
    source_type: official_docs
    relevance: Azure AI Search uses ingestion as part of how knowledge sources are processed before retrieval, which shows the term includes preparation, not just upload.
    key_point: A knowledge source defines content used in retrieval, and each source is either indexed or remote, which affects how the content is ingested, processed, and queried.
  - source_title: Knowledge
    source_url: https://docs.openwebui.com/features/workspace/knowledge/
    source_type: official_docs
    relevance: Open WebUI describes knowledge as files and collections that the system can search, read, and reason over after they are added, which supports the practical meaning of ingest in a knowledge base.
    key_point: Users upload documents into knowledge collections so the system can use them later for search and answers.
---

Ingest means to bring content into a system so it can be stored, prepared, and used later.

In a knowledge base or wiki system, ingest usually means more than uploading a file. The system may also extract text, split it into pieces, add labels, and index it so it can be found again.

This matters because a system cannot search or reuse content well until the content has been ingested. Good ingest makes later search, question answering, and linking much more reliable.

It is not the same as reading and understanding the content. It is also not just a file copy. In this glossary, ingest is the step that brings source material into the system so other processes can work on it.
