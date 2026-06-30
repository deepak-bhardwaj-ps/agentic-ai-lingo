---
title: Agent orchestration
short_description: The coordination layer that decides which agent, tool, or check should happen next.
category: Agentic patterns
tags:
  - agents
  - orchestration
  - multi-agent
status: draft
aliases:
  - multi-agent orchestration
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating orchestration as the model itself
  - Using the term for any app with one model call and a few tools
  - Assuming more agents automatically means better results
related_terms:
  - Agent runtime
  - Orchestration loop
  - Agentic workflow
  - Multi-agent collaboration
  - Supervisor agent
evidence:
  - source_title: Agents SDK
    source_url: https://developers.openai.com/api/docs/guides/agents
    source_type: official_docs
    relevance: Shows that orchestration belongs to the application layer, not the model call itself.
    key_point: OpenAI says the application can own orchestration, tool execution, approvals, and state.
  - source_title: Orchestration and handoffs
    source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
    source_type: official_docs
    relevance: Gives a concrete example of how specialist agents can be coordinated in practice.
    key_point: OpenAI describes manager-style workflows, agents used as tools, and handoffs between specialists.
  - source_title: Building Effective AI Agents
    source_url: https://www.anthropic.com/research/building-effective-agents
    source_type: engineering_blog
    relevance: Helps distinguish orchestration from a simple prompt or a single autonomous agent.
    key_point: Anthropic contrasts predefined workflows with agents that dynamically direct their own tool use.
  - source_title: LangGraph overview
    source_url: https://docs.langchain.com/oss/python/langgraph/overview
    source_type: official_docs
    relevance: Shows that orchestration usually needs durable execution, streaming, and human-in-the-loop control.
    key_point: LangGraph describes itself as an orchestration runtime for long-running, stateful agents.
---

Agent orchestration is the logic that coordinates one or more AI agents so they work together in the right order.

In practice, it decides which agent should act, what information it gets, when tools are called, whether a human must approve a step, and what happens after each result comes back.

This matters because useful agent systems usually need more than one model reply. They need a way to keep work in order, pass tasks between specialists, store state, and stop loops or dead ends.

It is not the model itself. It is not just a chatbot with extra steps. It is also not a fixed industry standard term, so different teams may use it to mean a runtime, a controller, or the handoff logic between agents.
