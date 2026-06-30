---
title: Vectorless retrieval
short_description: Retrieval that avoids vector embeddings and instead uses document structure, tree search, or lexical methods to find information.
category: Knowledge and wiki systems
tags:
  - retrieval
  - search
  - documents
  - rag
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a settled industry standard with one fixed definition
  - Using it to mean any search system that is not semantic search
  - Assuming it always means no ranking, no search index, or no LLM involvement
related_terms:
  - PageIndex
  - reasoning-based retrieval
  - hierarchical tree index
  - tree search
  - lexical search
  - retrieval-augmented generation
evidence:
  - source_title: PageIndex Developer Docs
    source_url: https://docs.pageindex.ai/
    source_type: official_docs
    relevance: This is the clearest current source for the exact phrase as used by a live product, so it anchors the term’s most common modern meaning.
    key_point: PageIndex defines itself as a vectorless, reasoning-based retrieval framework that turns documents into a tree and uses LLM reasoning over that tree instead of vector similarity search.
  - source_title: VectifyAI/PageIndex GitHub Repository
    source_url: https://github.com/VectifyAI/PageIndex
    source_type: engineering_blog
    relevance: The project README gives a concise engineering description of how the approach works in practice and confirms the product-specific meaning.
    key_point: The repository says PageIndex builds a hierarchical tree index from long documents and uses LLMs to reason over it, with no vector DBs or chunking.
  - source_title: Vectorless Reasoning-Based RAG: A New Approach to Retrieval-Augmented Generation
    source_url: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/vectorless-reasoning-based-rag-a-new-approach-to-retrieval-augmented-generation/4502238
    source_type: engineering_blog
    relevance: This independent engineering write-up shows the phrase being used in the wider field, not only by the PageIndex project itself.
    key_point: Microsoft describes vectorless approaches as structured document navigation for long, structured documents, rather than vector-based similarity search.
  - source_title: Hierarchical Abstract Tree for Cross-Document Retrieval-Augmented Generation
    source_url: https://arxiv.org/abs/2605.00529
    source_type: research_paper
    relevance: This paper shows that tree-based, non-vector retrieval is an active research direction, which supports treating the term as emerging rather than settled.
    key_point: The paper states that tree-based RAG organises documents into hierarchical indexes to support queries at multiple granularities.
---

Vectorless retrieval means finding information without turning the text into vector embeddings first.

In practice, the system looks at the document structure, words, headings, or tree-like sections to find the best part to read. Some versions also use an AI model to move through that structure step by step.

The term matters because some documents are easier to search by structure than by hidden numeric meaning. Long reports, manuals, and other sectioned documents can sometimes be easier to retrieve from when the system keeps the original layout.

It is not a fixed standard term. In current use, it most often points to PageIndex-style tree search or other structured retrieval methods, not to plain keyword search in general and not to semantic search with embeddings.
