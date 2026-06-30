---
title: Outlinks
short_description: Links that leave a note and point to other notes or pages.
category: Knowledge and wiki systems
tags:
  - wiki links
  - note linking
  - knowledge management
status: draft
aliases:
  - outgoing links
  - outbound links
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating outlinks as backlinks, which are links coming into a note instead of leaving it.
  - Counting unlinked mentions as outlinks, even when no actual link exists.
  - Using the term for any external web link, when many note tools use it mainly for links between notes in the same system.
related_terms:
  - internal links
  - backlinks
  - wikilinks
  - linked mentions
evidence:
  - source_title: Outgoing links - Obsidian Help
    source_url: https://obsidian.md/help/plugins/outgoing-links
    source_type: official_docs
    relevance: This is the clearest current definition in a widely used note app and matches how the term is used in practice.
    key_point: Outgoing links shows the links from the active note and separates them from backlinks, which are incoming links.
  - source_title: Metadata on Pages - Dataview
    source_url: https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-pages/
    source_type: official_docs
    relevance: This gives a concrete data-model definition used by note tooling, which helps avoid guessing from UI wording alone.
    key_point: file.outlinks means all outgoing links from a file, or all links the file contains.
  - source_title: Help:Links - MediaWiki
    source_url: https://www.mediawiki.org/wiki/Help:Links
    source_type: official_docs
    relevance: This shows the wider wiki tradition behind the term: links inside a page point to other pages in the same system.
    key_point: Internal wiki links connect pages in the same wiki and are the basic structure that outlinks describe from the source page side.
---

Outlinks are the links that leave a note or page and point to other notes or pages.

In practice, if one note contains links to three other notes, those three links are its outlinks. Many note apps show them in a panel so you can see what the current note refers to and jump to those targets.

Outlinks matter because they show how ideas connect. They help you browse a wiki, follow references, and see which other pages a note depends on.

Outlinks are not backlinks. Backlinks point to the current note from other notes. Outlinks point away from the current note. They are also not the same as unlinked mentions, which are just matching words without a real link.
