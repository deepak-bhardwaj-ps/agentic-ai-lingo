---
title: Wikilinks
short_description: Double-bracket links used inside notes or wiki pages to jump to other pages, headings, or blocks.
category: Knowledge and wiki systems
tags:
  - note-taking
  - wiki
  - links
 status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating wikilinks as the same thing as standard Markdown links, when some tools support both and others do not.
  - Assuming every wiki uses the same wikilink syntax, when some use page names, slugs, headings, or block references.
related_terms:
  - internal links
  - Markdown links
  - backlinks
  - wiki pages
evidence:
  - source_title: Internal links - Obsidian Help
    source_url: https://obsidian.md/help/links
    source_type: official_docs
    relevance: Shows the most common modern note-app meaning of wikilinks as `[[...]]` internal links, plus options for linking to headings and blocks.
    key_point: Obsidian treats wikilinks as a compact internal link format, alongside standard Markdown links, and uses them to connect notes in a vault.
  - source_title: Wiki-specific Markdown | GitLab Docs
    source_url: https://docs.gitlab.com/user/project/wiki/markdown/
    source_type: official_docs
    relevance: Shows that wiki systems often use double brackets for page links and may support extra wiki-only link syntax.
    key_point: GitLab wiki pages support double-bracket wiki-style links and other wiki-specific link forms, which shows the term is broader than one app.
  - source_title: WikiLinks - Python-Markdown documentation
    source_url: https://python-markdown.github.io/extensions/wikilinks/
    source_type: standards_doc
    relevance: Shows that wikilinks are a recognised link pattern in markdown tooling, usually written as double brackets.
    key_point: Python-Markdown defines WikiLinks as bracketed words in double brackets that are converted into links, confirming the core syntax.
---

Wikilinks are links written with double brackets, like `[[Page Name]]`, so you can jump from one note or wiki page to another.

In practice, wikilinks are used in note apps and wikis to connect ideas quickly. Some tools let you link to a whole page, while others also let you link to a heading or even a smaller piece of text inside a page.

They matter because they make a collection of notes easier to move through. Instead of copying the same idea into many places, you can point back to one page and build a web of connected notes.

Wikilinks are not the same as standard Markdown links. Some apps support both, but not all. They are also not one single universal standard, so the exact syntax and behaviour can change between tools.
