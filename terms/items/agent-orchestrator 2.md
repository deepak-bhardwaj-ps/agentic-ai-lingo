---
title: Agent orchestrator
short_description: Software or logic that coordinates one or more AI agents and decides what happens next.
category: Tools and products
tags:
- agents
- orchestration
- workflow
status: active
aliases:
- Agent orchestration tool
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the model itself
- Using it for any chatbot with a few steps
- Assuming more agents automatically means better results
related_terms:
- Agent orchestration
- Agentic workflow
- Workflow orchestration
- Handoffs
- Supervisor agent
evidence:
  - source_title: Agents SDK
    source_url: https://developers.openai.com/api/docs/guides/agents
    source_type: official_docs
    relevance: OpenAI separates the agent from the application layer that owns orchestration, tool execution, approvals, and state, which helps define an orchestrator as coordinating software rather than the model itself.
    key_point: The app can own orchestration, tool execution, approvals, and state.
  - source_title: Orchestration and handoffs
    source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
    source_type: official_docs
    relevance: Shows concrete patterns for manager-style workflows and handoffs, which is the clearest practical meaning of an agent orchestrator.
    key_point: Orchestration decides which agent runs, in what order, and how work is handed off.
  - source_title: Building Effective AI Agents
    source_url: https://www.anthropic.com/research/building-effective-agents
    source_type: engineering_blog
    relevance: Anthropic draws a line between predefined workflows and agents that choose their own actions, which helps explain why an orchestrator is the control layer around agents.
    key_point: Workflows use predefined code paths; agents choose their own tool use more dynamically.
  - source_title: LangGraph overview
    source_url: https://docs.langchain.com/oss/python/langgraph/overview
    source_type: official_docs
    relevance: LangGraph highlights durable execution, streaming, and human-in-the-loop control as core orchestration capabilities, showing what orchestrators need in practice.
    key_point: Orchestration needs state, persistence, and control flow.
---

An agent orchestrator is the software or logic that coordinates one or more AI agents so they work together on a task.

In practice, it decides which agent should act, what information each agent gets, when a handoff happens, and what the next step should be. It may also keep state, wait for human approval, and route work through specialist agents.

This matters because real agent systems often need more than one step. A good orchestrator keeps the work ordered, makes the system easier to follow, and helps avoid agents doing the wrong thing at the wrong time.

It is not the same as the AI model. It is also not just a chatbot with extra prompts. If there is no real control flow, state, or handoff between agents, the term is being used too loosely.
