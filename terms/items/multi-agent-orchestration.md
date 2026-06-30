---
title: Multi-agent orchestration
short_description: Coordination logic that manages how several AI agents share work.
category: Agentic patterns
tags:
- agents
- orchestration
- multi-agent
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal standard term with one fixed meaning
- Using it for any system that simply calls a model more than once
- Confusing it with governance, which is about rules and oversight rather than turn-taking
related_terms:
- Agent orchestration
- Multi-agent system
- Handoff orchestration
- Group chat orchestration
- Supervisor agent
evidence:
  - source_title: Orchestration and handoffs
    source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
    source_type: official_docs
    relevance: OpenAI shows that orchestration is the application-level logic that decides which agent owns the reply, which specialists to call, and how work moves between them.
    key_point: Multi-agent orchestration is about coordinating specialists, not about the model itself.
  - source_title: Group Chat orchestration
    source_url: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/group-chat
    source_type: official_docs
    relevance: Microsoft defines a current multi-agent orchestration pattern where an orchestrator manages speaker selection and conversation flow in a shared thread.
    key_point: A multi-agent system can be orchestrated as a shared conversation with controlled turn-taking.
  - source_title: How we built our multi-agent research system
    source_url: https://www.anthropic.com/engineering/multi-agent-research-system
    source_type: engineering_blog
    relevance: Anthropic gives a real-world example of a lead agent coordinating specialist subagents in parallel, showing that orchestration is a design choice for dividing work.
    key_point: Multi-agent orchestration often uses a lead agent plus specialist agents working in parallel or sequence.
  - source_title: LangGraph overview
    source_url: https://docs.langchain.com/oss/python/langgraph/overview
    source_type: official_docs
    relevance: LangGraph describes the infrastructure needed for long-running, stateful agent work, which helps explain why orchestration is more than a prompt.
    key_point: Orchestration needs state, control flow, and persistence to coordinate agents reliably.
---

Multi-agent orchestration is the logic that coordinates two or more AI agents so they can work on the same task.

In practice, it decides which agent should act, when they should act, what each one should see, and how the result moves to the next agent or back to a person. Sometimes one agent acts like a manager. Sometimes the agents share one conversation. Sometimes they work one after another.

The term matters because splitting work across agents can help with hard tasks, such as research, checking, planning, or comparing different viewpoints. But it also adds cost, delay, and more chances for confusion if the coordination is poor.

It is not the same as the model itself. It is not just “using AI more than once”. It is also not the same as governance, which is about rules, safety checks, and oversight around the agents.
