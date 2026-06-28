---
slug: agent-marketplace
title: Agent Marketplace
short_description: A catalogue where people can find, compare, and install AI agents
  or skills from different creators.
category: Protocols
tags:
- agentic-ai
- marketplace
- distribution
- governance
status: draft
aliases:
- agent store
- agent catalogue
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating the marketplace itself as a safety check
- Assuming listed agents are trusted or high quality
- Confusing a marketplace with the agent software itself
related_terms:
- agent
- agent skill
- MCP registry
- provenance
- supply chain
evidence:
- source_title: Plugins
  source_url: https://developers.openai.com/codex/plugins
  source_type: official_docs
  relevance: Shows a real product pattern where reusable agent capabilities are discovered
    through a marketplace and then installed.
  key_point: Users can browse, install, and manage plugins from a marketplace-style
    directory.
- source_title: Build plugins
  source_url: https://developers.openai.com/codex/plugins/build
  source_type: official_docs
  relevance: Defines the marketplace as a catalogue of reusable items rather than
    the agent itself.
  key_point: A marketplace is described as a JSON catalog of plugins that can be curated
    for a team or personal workflow.
- source_title: The MCP Registry
  source_url: https://modelcontextprotocol.io/registry/about
  source_type: official_docs
  relevance: Shows how a central catalogue helps people discover agent-adjacent tools.
  key_point: The registry is metadata for discovery and installation, not proof that
    a tool is safe or trustworthy.
- source_title: Registry Charter
  source_url: https://modelcontextprotocol.io/community/working-groups/registry
  source_type: official_docs
  relevance: Explains why catalogues need moderation and evaluation.
  key_point: The registry is meant to help users discover, evaluate, and install servers
    with confidence.
- source_title: LLM01:2025 Prompt Injection
  source_url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  source_type: standards_doc
  relevance: Supports the warning that a listed tool can still be unsafe.
  key_point: Trust boundaries matter between the model, outside inputs, and tools,
    so a marketplace is not a security boundary.
---

An agent marketplace is a place where people can find, compare, and install AI agents or skills made by different creators.

In practice, it works like an app store for agent tools. You look through a list, see what each one claims to do, and choose whether to install it. Some marketplaces also help with updates, permissions, and sharing inside a team.

The term matters because it makes useful agent tools easier to reuse. Instead of building everything from scratch, a team can pick from a shared catalogue.

An agent marketplace is not the agent itself. It is also not a safety check. A listing can still be badly made, misleading, or unsafe, so you still need to check who made it and what access it asks for.
