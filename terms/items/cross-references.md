---
title: Cross-references
short_description: Links inside documentation or wiki content that point readers to related pages, sections, or other named targets.
category: Knowledge and wiki systems
tags:
  - wiki links
  - documentation
  - navigation
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating cross-references as tags or summaries instead of links that point to a specific target.
  - Using the term for any citation or footnote, even though cross-references usually point to pages, sections, figures, or other document targets.
related_terms:
  - internal links
  - wikilinks
  - backlinks
  - outlinks
  - references
evidence:
  - source_title: How to use cross-references with Sphinx
    source_url: https://docs.readthedocs.com/platform/stable/guides/cross-referencing-with-sphinx.html
    source_type: official_docs
    relevance: Directly defines cross-references in documentation systems and shows they can point to pages, sections, figures, and code blocks.
    key_point: Cross-references are links to different elements of a document, with references pointing to targets elsewhere in the docs.
  - source_title: Markdown links
    source_url: https://docusaurus.io/docs/markdown-features/links
    source_type: official_docs
    relevance: Shows how modern docs systems use relative links to connect pages in the same documentation set.
    key_point: Documentation links can point to other pages by file path or URL path, which is the basic behaviour cross-references rely on.
  - source_title: Help:Links
    source_url: https://www.mediawiki.org/wiki/Help:Links
    source_type: official_docs
    relevance: Defines wiki links as the standard internal links used to connect pages inside a wiki, which is the closest wiki-system equivalent of cross-references.
    key_point: Internal wiki links reference pages in the same wiki and can also link to sections or anchors within a page.
---

Cross-references are links that point from one place in a document or wiki to another place in the same system.

In practice, a cross-reference can take a reader to another page, a section heading, a figure, a code example, or another named target. It helps people move between related ideas without repeating the same explanation in several places.

Cross-references matter because they make documentation easier to follow and keep it shorter. They also help readers trace how ideas connect across a knowledge base.

Cross-references are not the same as tags. They are not just labels, and they are not the same as a citation unless the link is specifically pointing to a source or reference entry. In wiki systems, the same idea is often called an internal link or a wikilink.
