---
title: Query
short_description: A search request or search string used to ask a knowledge system to find matching notes, pages, or documents.
category: Knowledge and wiki systems
tags:
  - search
  - retrieval
  - indexing
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating a query as the same thing as the result list
  - Confusing a search query with a filter, which only narrows results
  - Assuming every system uses the same query syntax
related_terms:
  - search
  - search term
  - filter
  - index
  - retrieval
evidence:
  - source_title: Search - Obsidian Help
    source_url: https://obsidian.md/help/plugins/search
    source_type: official_docs
    relevance: Obsidian is a current wiki-style knowledge tool, and its help page shows how queries are entered as search terms with operators.
    key_point: Obsidian defines a search term as the word or phrase entered into the search field, and it uses operators like quotes, AND, and OR to narrow results.
  - source_title: Querying in Azure AI Search
    source_url: https://learn.microsoft.com/en-us/azure/search/search-query-overview
    source_type: official_docs
    relevance: This shows that a query is the input sent to a search system, not the answer itself, and that different query types exist.
    key_point: Microsoft describes queries as constructs that run over a search index and can be free-form text, structured patterns, or vector search requests.
  - source_title: Query options overview
    source_url: https://learn.microsoft.com/en-us/odata/concepts/queryoptions-overview
    source_type: official_docs
    relevance: This is useful because it shows another common meaning of query in software: a request that tells a service how to return data.
    key_point: OData defines query options as URL parameters that control filtering, sorting, and related data returned by a service.
---

A query is the words or instructions you type into a search system to ask it to find matching notes, pages, or documents.

In a wiki or knowledge app, a query can be a simple word search, an exact phrase in quotes, or a search with operators like AND and OR. The system looks through its index or content and returns the items that match best.

Queries matter because they help you find the right information quickly in a large collection.

A query is not the answer itself. It is also not the same as a filter, which only narrows results. In other software, query can mean a database command or a URL parameter, so the exact meaning depends on the system.
