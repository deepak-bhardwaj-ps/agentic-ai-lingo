---
title: Markdown graph
short_description: A visual map of how Markdown files or notes link to each other.
category: Knowledge and wiki systems
tags:
  - markdown
  - graph view
  - links
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: low
maturity_level: emerging
common_misuse:
  - Treating it as a Mermaid diagram or any chart written in Markdown.
  - Using it for any graph data structure, instead of a view of links between Markdown files or notes.
related_terms:
  - graph view
  - backlinks
  - internal links
  - wikilinks
  - knowledge graph
evidence:
  - source_title: Graph view - Obsidian Help
    source_url: https://obsidian.md/help/plugins/graph
    source_type: official_docs
    relevance: This is the clearest current description of a Markdown-note graph view in a widely used markdown-based knowledge tool.
    key_point: The graph view visualises relationships between notes in a vault, with lines representing internal links between nodes.
  - source_title: Internal links - Obsidian Help
    source_url: https://obsidian.md/help/links
    source_type: official_docs
    relevance: Shows the link type that such graphs are built from, which helps define what the graph is actually showing.
    key_point: Internal links connect notes and create a network of knowledge, which is the structure a markdown graph visualises.
  - source_title: markdown-links
    source_url: https://github.com/tchayen/markdown-links
    source_type: engineering_blog
    relevance: A concrete implementation of the same idea outside Obsidian, showing the term family is about link relationships between Markdown files.
    key_point: It displays a graph of local links between Markdown files to help understand the structure of a wiki or documentation set.
---

Markdown graph is a visual map of how Markdown files or notes link to each other.

In practice, it shows the connections between pages in a wiki, notes in a vault, or files in a documentation set. Each dot usually stands for a note or file, and each line shows a link between them.

This matters because it helps you see which notes are central, which topics are isolated, and how ideas connect across a collection of Markdown files.

It is not the same as a Mermaid diagram, a chart made inside Markdown, or any general graph data structure. It is specifically a view of links between Markdown-based notes or files.
