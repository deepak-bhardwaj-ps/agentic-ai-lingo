---
title: Antigravity
short_description: Google’s agentic development platform with an editor, a manager view, and agents that work across code, terminal, and browser.
category: Tools and products
tags:
- google
- agentic-development-platform
- cli
- ide
- subagents
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating every Antigravity surface as the same thing, when the name covers the platform and its different interfaces.
- Using it as a generic word for any agentic IDE or CLI.
- Assuming “subagents” or “skills” inside Antigravity mean the same thing everywhere else; the implementation is product-specific.
related_terms:
- agentic development platform
- agent-first IDE
- subagent
- skills
- orchestration
- browser agent
- artifacts
evidence:
  - source_title: Build with Google Antigravity, our new agentic development platform
    source_url: https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/
    source_type: engineering_blog
    relevance: Primary launch announcement that defines Antigravity as Google’s agentic development platform and explains the main surfaces.
    key_point: Antigravity is described as a platform, not just an editor, with an Editor View and a Manager Surface for spawning and observing agents.
  - source_title: Antigravity CLI
    source_url: https://antigravity.google/product/antigravity-2
    source_type: official_docs
    relevance: Confirms the CLI is one part of the broader Antigravity product family and shows how the brand is used in practice.
    key_point: The CLI page presents Antigravity as a product for working with agents in natural language.
  - source_title: Background tasks & subagents - Google Antigravity Documentation
    source_url: https://antigravity.google/docs/cli-subagents
    source_type: official_docs
    relevance: Shows that subagents are a built-in part of Antigravity’s workflow rather than a generic term.
    key_point: Antigravity CLI lets users delegate slower work to parallel background agents while keeping the main coding flow active.
  - source_title: Agent Skills - Google Antigravity Documentation
    source_url: https://antigravity.google/docs/skills
    source_type: official_docs
    relevance: Confirms that Skills are a documented Antigravity feature and helps distinguish them from the general idea of skills in other tools.
    key_point: Skills are an open standard in Antigravity for extending agent capabilities through SKILL.md instructions.
---

Antigravity is Google’s agentic development platform for working with software through agents.

In practice, it gives you different ways to work: a normal editor for hands-on coding, a manager view for spawning and watching agents, and a CLI for giving tasks to agents in plain language.

It matters because it is designed for larger tasks that need planning, background work, and checking results, not just one quick chat reply.

It is not a generic word for any AI coding tool. It is also not the same thing as a subagent, a skill, or a browser agent. Those are parts of the Antigravity system, not the whole thing.
