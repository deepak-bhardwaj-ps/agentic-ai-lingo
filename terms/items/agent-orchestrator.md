---
title: Agent orchestrator
short_description: Software that coordinates one or more AI agents, their tools, and the order of work.
category: Tools and products
tags:
  - orchestration
  - multi-agent
  - runtime
status: draft
aliases:
  - Agent orchestration tool
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the model itself
  - Using it as a vague name for any AI app
  - Assuming every team means the same thing by it
related_terms:
  - Agent orchestration
  - Orchestration loop
  - Agent runtime
  - Multi-agent orchestration
  - Workflow orchestration
evidence:
  - source_title: Agents SDK
    source_url: https://developers.openai.com/api/docs/guides/agents
    source_type: official_docs
    relevance: Shows that orchestration is an application-layer job separate from the model call.
    key_point: OpenAI says the application can own orchestration, tool execution, approvals, and state.
  - source_title: Sandbox Agents
    source_url: https://developers.openai.com/api/docs/guides/agents/sandboxes
    source_type: official_docs
    relevance: Defines the harness around the model as the control plane that owns the agent loop and related coordination work.
    key_point: OpenAI describes the harness as owning model calls, tool routing, handoffs, approvals, tracing, recovery, and run state.
  - source_title: LangGraph overview
    source_url: https://docs.langchain.com/oss/python/langgraph/overview
    source_type: official_docs
    relevance: Shows a widely used agent framework that explicitly focuses on orchestration.
    key_point: LangGraph describes itself as a low-level orchestration framework and runtime for long-running, stateful agents.
  - source_title: Workflow orchestration agents
    source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html
    source_type: standards_doc
    relevance: Gives a clear multi-agent pattern where a central orchestrator coordinates specialist agents.
    key_point: AWS describes workflow agents as coordinating multistep tasks across systems and delegating to subagents.
---

An agent orchestrator is software that decides how an AI agent job should move from one step to the next.

In practice, it may send prompts to a model, call tools, pass results along, wait for approval, and choose whether to stop, retry, or hand work to another agent.

This matters because useful agent systems often need more than one model reply. Someone or something has to keep the work in order, manage state, and stop the system from looping or drifting.

It is not the model itself. It is also not a fixed industry standard term. People may use it to mean a full agent runtime, a multi-agent controller, or just the part that routes work between steps.
