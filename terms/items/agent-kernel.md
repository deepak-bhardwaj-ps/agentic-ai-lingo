---
slug: agent-kernel
title: Agent Kernel
short_description: The small runtime loop that lets an agent keep state, choose its
  next step, and use tools.
category: Runtime
tags:
- agents
- kernel
- runtime
- orchestration
- state
status: emerging
aliases:
- kernel
- agent runtime core
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it like a formal standard when teams mostly use it informally.
- Using it to mean the whole agent platform instead of the small loop that runs one
  agent.
related_terms:
- agent loop
- agent runtime
- orchestration
- state
- guardrails
- tools
evidence:
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Describes agents as systems that plan, call tools, collaborate, and keep
    state, which supports the idea of a core runtime loop.
  key_point: OpenAI says agents keep enough state to complete multi-step work and
    that orchestration, tool execution, approvals, and state are application-owned
    concerns.
- source_title: Building effective agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Shows that effective agents are usually built from simple, explicit patterns
    rather than one giant hidden framework.
  key_point: Anthropic recommends simple, composable agent patterns and a clear agent
    loop.
- source_title: LangGraph overview
  source_url: https://docs.langchain.com/oss/python/langgraph/overview
  source_type: official_docs
  relevance: Shows that stateful agent systems are often built with explicit control
    flow and persistent state.
  key_point: LangGraph is designed for long-running, stateful workflows and agents
    with explicit structure.
---

An agent kernel is the small part of an agent that decides the next step, uses tools when needed, and updates what the agent knows.

In practice, it is the loop inside the agent that checks the current state, chooses an action, carries it out, and then saves the result so the next step can use it.

This matters because the loop has to stay clear and reliable. If it is poorly designed, the agent can forget what it was doing, pick the wrong action, or use a tool badly.

It is not the whole agent system. It does not mean the app screen, hosting, logs, databases, or extra services around the agent. The term is also not used in one fixed way across the industry, so people may mean slightly different things by it.
