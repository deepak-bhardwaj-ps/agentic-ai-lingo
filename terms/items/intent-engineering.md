---
slug: intent-engineering
title: Intent Engineering
short_description: Intent engineering is the work of turning a person’s goal into
  a clear, testable task that a system can carry out.
category: Protocols
tags:
- ai
- agents
- prompts
- context
- workflows
status: emerging
aliases:
- Intent Engineering
meaning_type: emerging_unsettled
novelty_level: high
maturity_level: emerging
common_misuse:
- Treating it as a formal standard or protocol
- Confusing it with prompt engineering
- Using it as a catch-all label for planning, requirements, and tool orchestration
related_terms:
- Prompt Engineering
- Context Engineering
- Model Context Protocol
- AI Agents
evidence:
- source_title: Effective context engineering for AI agents
  source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  source_type: engineering_blog
  relevance: Shows that modern agent work is about shaping the full context and goal
    state, not just writing a prompt.
  key_point: Anthropic describes context engineering as curating the right information
    for the model so it can behave as intended over multiple turns.
- source_title: What is the Model Context Protocol (MCP)?
  source_url: https://modelcontextprotocol.io/docs/getting-started/intro
  source_type: official_docs
  relevance: Establishes MCP as a standard for connecting AI applications to tools,
    data, and workflows.
  key_point: MCP standardises how AI applications connect to external systems and
    perform tasks, but it does not define "intent engineering" as a protocol term.
- source_title: Specification
  source_url: https://modelcontextprotocol.io/specification/2025-11-25
  source_type: official_docs
  relevance: Gives the protocol boundary for what counts as a real interoperability
    standard.
  key_point: MCP is an open protocol with defined requirements for connecting LLM
    applications to external data sources and tools.
- source_title: Prompt Engineering for AI Guide
  source_url: https://cloud.google.com/discover/what-is-prompt-engineering
  source_type: industry_article
  relevance: Provides a mainstream definition of prompt engineering for contrast.
  key_point: Prompt engineering is about designing prompts to guide model output;
    intent engineering is a broader and less standard label.
---

Intent engineering is the work of turning a person’s goal into a clear task that a system can carry out and check.

In practice, it means making the goal specific enough that a model, agent, or workflow knows what success looks like, what limits it must follow, and how to tell if it has finished.

This matters because people often ask for something vague. A good system cannot act well on vague instructions. It needs the real goal, the important rules, and the result you expect.

It is not the same as prompt engineering, which focuses on writing good instructions for a model. It is also not a formal protocol on its own. If a system claims to support intent engineering, check whether it has a real task format, clear rules, and a way to verify results.

The term is still unsettled. People use it to describe a useful idea, but there is no single agreed standard for it.
