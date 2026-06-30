---
title: Agent orchestration
short_description: Coordination logic that decides which agent runs, in what order, and what happens next.
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
- Using the term for any app with one agent and a few tool calls
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
    relevance: OpenAI describes agents as applications that may own orchestration, tool execution, approvals, and state, which makes orchestration a separate application layer rather than the model itself.
    key_point: The app, not the model, can control how agent work is coordinated across steps.
  - source_title: Orchestration and handoffs
    source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
    source_type: official_docs
    relevance: Shows concrete agent-orchestration patterns such as manager-style workflows and agents used as tools, which helps pin down what the term means in practice.
    key_point: Orchestration is about which agents run, in what order, and how handoffs happen.
  - source_title: Building Effective AI Agents
    source_url: https://www.anthropic.com/research/building-effective-agents
    source_type: engineering_blog
    relevance: Anthropic separates simple workflow patterns from agentic control, which helps distinguish orchestration from a plain prompt or a single model call.
    key_point: Effective agent systems use simple, composable control patterns instead of one large autonomous blob.
  - source_title: LangGraph overview
    source_url: https://docs.langchain.com/oss/python/langgraph/overview
    source_type: official_docs
    relevance: LangGraph explicitly describes the capabilities needed for agent orchestration, especially durable execution, streaming, and human-in-the-loop control.
    key_point: Orchestration needs state, persistence, and control flow, not just model output.
---

Agent orchestration is the logic that coordinates one or more AI agents so they work as a system.

In practice, it decides which agent should act, when it should act, what information it gets, and what happens after it finishes. The orchestration can be written in code, partly chosen by the model, or split between the two.

This matters because useful agent systems usually need more than one model reply. They may need a planner, a specialist agent, a checker, and a human approval step. Orchestration keeps that work in order and stops the system from becoming chaotic.

It is not the same as the model itself. It is also not just a chatbot with extra steps. If there is no real control flow, state, or handoff between agents, the term is being used too loosely.
