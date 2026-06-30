---
title: Hierarchical tree index
short_description: A tree-shaped index that organises content into levels so a system can move from broad sections to smaller details.
category: Knowledge and wiki systems
tags:
  - search
  - retrieval
  - indexing
  - documents
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a standard industry term with one fixed definition
  - Confusing it with a simple folder tree or table of contents
  - Assuming it always uses embeddings or vector search
related_terms:
  - tree index
  - hierarchical retrieval
  - document indexing
  - table of contents
  - retrieval-augmented generation
evidence:
  - source_title: Tree Index - LlamaIndex Developer Documentation
    source_url: https://developers.llamaindex.ai/python/framework/module_guides/indexing/index_guide/
    source_type: official_docs
    relevance: Shows a current production library using the exact idea of building a hierarchical tree for retrieval.
    key_point: LlamaIndex says its tree index builds a hierarchical tree from nodes and traverses from root to leaves during querying.
  - source_title: PageIndex - Vectorless, Reasoning-based RAG
    source_url: https://github.com/VectifyAI/PageIndex
    source_type: engineering_blog
    relevance: Shows a recent engineering implementation that uses the same phrase for document retrieval.
    key_point: PageIndex describes a hierarchical tree index built from long documents and used for reasoning-based retrieval without a vector database.
  - source_title: Hierarchical Abstract Tree for Cross-Document Retrieval-Augmented Generation
    source_url: https://arxiv.org/abs/2605.00529
    source_type: research_paper
    relevance: Confirms that tree-based indexing is an active research pattern for organising documents at multiple levels of detail.
    key_point: The paper says tree-based RAG organises documents into hierarchical indexes to support queries at different granularities.
---

A hierarchical tree index is an index arranged like a tree, with broad sections near the top and smaller pieces underneath.

In practice, this lets a system start with a big topic, then drill down through child sections until it reaches the most relevant detail. It is often used for documents, notes, or knowledge bases that have natural structure.

The term matters because tree-shaped indexes can make retrieval easier to explain and easier to navigate than a flat list of chunks. They can also help a system answer questions by moving through the document structure instead of searching everything the same way.

It is not a single fixed standard, and it is not the same as a normal folder tree. It also is not always the same as a vector index or full-text search index, although some systems combine those ideas.
