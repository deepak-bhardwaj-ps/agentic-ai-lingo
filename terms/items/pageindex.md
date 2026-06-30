---
title: PageIndex
short_description: A PageIndex is a tree-shaped retrieval system that organises a document into sections so an AI can search by following the document structure instead of using vector similarity alone.
category: Knowledge and wiki systems
tags:
  - retrieval
  - indexing
  - documents
  - rag
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating PageIndex as a generic term for any page tree
  - Assuming it means a normal vector database or embedding index
  - Saying it is a fixed standard rather than a named product and approach
related_terms:
  - hierarchical tree index
  - vectorless retrieval
  - reasoning-based retrieval
  - document indexing
  - retrieval-augmented generation
evidence:
  - source_title: PageIndex Developer Docs
    source_url: https://docs.pageindex.ai/
    source_type: official_docs
    relevance: This is the main current source for the product and its own definition of how it works.
    key_point: PageIndex says it is a vectorless, reasoning-based retrieval framework that turns documents into a tree structure for context-aware search.
  - source_title: GitHub - VectifyAI/PageIndex
    source_url: https://github.com/VectifyAI/PageIndex
    source_type: engineering_blog
    relevance: The repository README shows the project framing and confirms the product-specific meaning.
    key_point: The project describes PageIndex as a vectorless, reasoning-based RAG engine that avoids vector databases and chunking.
  - source_title: Hierarchical Abstract Tree for Cross-Document Retrieval-Augmented Generation
    source_url: https://arxiv.org/abs/2605.00529
    source_type: research_paper
    relevance: Supports the broader idea that tree-shaped indexes are an active retrieval pattern, not just a marketing phrase.
    key_point: The paper explains that tree-based RAG organises documents into hierarchical indexes so queries can be answered at different levels of detail.
---

PageIndex is a tree-shaped retrieval approach and product that organises a document into sections, then lets an AI move through those sections to find an answer.

In practice, PageIndex turns a long document into a structure that is closer to a table of contents than a pile of text chunks. The system can start at the top, choose a useful branch, then drill down to the most relevant part.

This matters because some documents are easier to search by structure than by word similarity alone. PageIndex is aimed at long, sectioned documents where the layout and order of the content are important.

It is not the same as a normal folder tree, and it is not just another name for embeddings or a vector database. It is also not a fixed industry standard term; it is a specific product and method built around tree-based retrieval.
