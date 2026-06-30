---
title: Full-text search
short_description: A way to search the words inside documents and rank the best matches.
category: Knowledge and wiki systems
tags:
- search
- indexing
- retrieval
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating it as the same as keyword search on a title or tag field
- Assuming it only finds exact word matches
- Using it to mean semantic search, which is a different approach
related_terms:
- inverted index
- keyword search
- semantic search
- document retrieval
- relevance ranking
evidence:
  - source_title: Chapter 12. Full Text Search
    source_url: https://www.postgresql.org/docs/current/textsearch.html
    source_type: official_docs
    relevance: PostgreSQL’s current documentation gives a precise, widely used definition of full-text search as searching natural-language documents and ranking matches by relevance.
    key_point: Full-text search identifies documents that satisfy a query and can sort them by relevance.
  - source_title: How full-text search works | Elastic Docs
    source_url: https://www.elastic.co/docs/solutions/search/full-text/how-full-text-works
    source_type: official_docs
    relevance: Elastic explains the core mechanism behind modern full-text search, especially how text is broken into tokens and stored in an inverted index.
    key_point: Full-text search typically uses an inverted index that maps each token to the documents containing it.
  - source_title: Apache Lucene 10.3.0 Documentation
    source_url: https://lucene.apache.org/core/10_3_0/
    source_type: official_docs
    relevance: Lucene is the search library behind many search systems, so its documentation shows how the term is used in production search tooling.
    key_point: Lucene is a full-text search engine library, not a complete app, which shows the term refers to a search capability rather than one product.
---

Full-text search is a way to search the words inside documents, not just exact labels or titles. It looks through the text of a page, note, article, or record and finds the ones that best match what was typed.

In practice, the text is usually split into smaller parts called tokens, then stored in a structure that makes searching fast. The search system can also rank results, so the most relevant matches appear first.

This matters because people often need to find information buried inside long text. Full-text search is useful for articles, notes, help pages, manuals, and other documents where the important words may be anywhere in the content.

It is not the same as keyword search on a tag or title, and it is not the same as semantic search. Full-text search usually still depends on the words in the text, even if it can ignore small differences like plurals or word forms.
