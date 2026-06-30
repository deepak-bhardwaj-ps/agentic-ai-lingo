---
title: Durable wiki
short_description: A wiki made to last: kept in plain text, linked, and updated over time instead of treated like a one-off summary.
category: Knowledge and wiki systems
tags:
  - wiki
  - knowledge base
  - markdown
status: draft
aliases: []
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: emerging
common_misuse:
  - Treating it as a chat transcript or a single summary that is never revised.
  - Using it to mean any wiki, even when the point is long-term upkeep and link structure.
related_terms:
  - interlinked wiki
  - wiki compiler
  - knowledge base
  - local-first
  - wikilinks
evidence:
  - source_title: LLM Wiki
    source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
    source_type: standards_doc
    relevance: This is the clearest source for the term family used in modern agentic knowledge-base work.
    key_point: It describes a persistent, compounding wiki made from structured markdown files that is updated as new sources arrive, rather than rebuilt from scratch on each question.
  - source_title: LLM Wiki - Obsidian Plugin
    source_url: https://community.obsidian.md/plugins/llm-wiki
    source_type: official_docs
    relevance: Shows how the term is used in current tooling, which helps distinguish it from a generic wiki.
    key_point: It describes turning raw notes, clippings, and chat exports into an interlinked personal wiki with YAML frontmatter, confidence scores, and graph edges, all maintained automatically.
  - source_title: Obsidian - Sharpen your thinking
    source_url: https://obsidian.md/
    source_type: official_docs
    relevance: Confirms the underlying durable format and link-based structure that make a wiki last over time.
    key_point: Obsidian stores notes locally as plain text Markdown files, supports links between notes, and can publish notes as an online wiki or knowledge base.
  - source_title: Help:Links
    source_url: https://www.mediawiki.org/wiki/Help%3ALinks
    source_type: official_docs
    relevance: Gives the classic wiki model for internal links, which is the structural base of a durable wiki.
    key_point: MediaWiki uses internal links, commonly called wikilinks, to connect pages inside the same wiki.
---

Durable wiki is a wiki that is meant to last and keep growing over time.

In practice, it is usually stored in plain text files, connected with links, and updated as new information arrives. The pages are not treated as throwaway notes. They are kept as a living reference that can be revised, cross-linked, and reused later.

The point of a durable wiki is that knowledge does not disappear into old chat messages or one-off summaries. It becomes a structured place where important ideas, decisions, and source-backed notes can be found again and improved.

It is not just any wiki, and it is not the same as a chat transcript. The word durable means the content is expected to survive changes, stay readable, and remain useful over time.
