---
title: Open Knowledge Format
short_description: An open standard for storing knowledge as linked Markdown files with YAML frontmatter so people and AI tools can read it.
category: Protocols
tags:
- knowledge-management
- markdown
- yaml
- ai-agents
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as just any Markdown wiki rather than a specific, named format with agreed rules.
- Confusing it with a chat protocol or model format.
related_terms:
- llm wiki
- markdown frontmatter
- knowledge catalog
- llms.txt
evidence:
- source_title: Introducing the Open Knowledge Format
  source_url: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
  source_type: official_docs
  relevance: Google's announcement is the clearest current statement of what OKF is meant to be and why it exists.
  key_point: Google Cloud says OKF is an open, vendor-neutral standard that represents knowledge as a directory of Markdown files with YAML frontmatter.
- source_title: Open Knowledge Format (OKF) Specification v0.1
  source_url: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
  source_type: standards_doc
  relevance: The specification defines the structure and scope of the format, including what it is and what it is not.
  key_point: The spec says OKF is a minimal format for knowledge representation, with Markdown files, YAML frontmatter, portability, and no required SDK or runtime.
---
Open Knowledge Format is a standard for writing knowledge down in a simple, shareable way.

In practice, it means storing information as a folder of Markdown files, where each file describes one idea and has small bits of structured data at the top in YAML frontmatter. The files can link to each other, so the knowledge works like a wiki that both people and AI tools can read.

The term matters because many teams keep important knowledge in places that are hard for tools to use well. OKF is meant to make that knowledge easier to move between systems without needing a special app or a custom database.

It is not just any Markdown page or any wiki. It is a specific format with conventions for how the files are organised and described. It is also not a chat protocol or a model format. It is about storing and sharing knowledge, not talking to a model.
