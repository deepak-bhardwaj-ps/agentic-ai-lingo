---
title: Handoff orchestration
short_description: A handoff orchestration pattern lets one agent transfer control to a more suitable agent, and the new agent takes over the task.
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
- Treating handoff orchestration as the same thing as a supervisor pattern
- Assuming a central manager always stays in control
- Using it for fixed pipelines where the next agent is known in advance
related_terms:
- Handoff
- Agent orchestration
- Multi-agent orchestration
- Supervisor agent
- Sequential orchestration
- Dynamic teaming
evidence:
  - source_title: Orchestration and handoffs
    source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
    source_type: official_docs
    relevance: OpenAI gives a current product definition of handoffs and explicitly contrasts them with agent-as-tools, which helps separate ownership transfer from helper-style delegation.
    key_point: Handoffs are best when a specialist should own the next response, and the routing surface should stay narrow and concrete.
  - source_title: Handoff orchestration
    source_url: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/handoff
    source_type: official_docs
    relevance: Microsoft’s framework docs describe handoff orchestration as direct transfer of control between agents, including the fact that the receiving agent takes full ownership.
    key_point: In handoff orchestration, one agent transfers the conversation to another agent with the right expertise, and control moves fully to that agent.
  - source_title: AI Agent Orchestration Patterns
    source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
    source_type: standards_doc
    relevance: This architecture guide places handoff alongside sequential and concurrent orchestration, and states the pattern is for dynamic delegation when the best agent is not known upfront.
    key_point: Handoff orchestration is also called routing, triage, transfer, dispatch, or delegation, and it is used when control moves between specialised agents one at a time.
  - source_title: Multi-agent systems
    source_url: https://mastra.ai/guides/concepts/multi-agent-systems
    source_type: official_docs
    relevance: Mastra provides a clear distinction from a supervisor pattern, which helps avoid a common confusion in glossary terms.
    key_point: A handoff pattern transfers control from one agent to another, and the first agent does not stay in charge for the full task.
---

Handoff orchestration is a way for one AI agent to pass control of a task to another agent that is better suited to continue.

In practice, one agent starts the work, decides it has reached its limit, and transfers the conversation or task to a specialist. The second agent then takes over and continues from the shared context.

This matters because not every task should be handled by one general agent. Handoff orchestration lets a system use the right specialist at the right time, which can make complex or mixed-domain tasks easier to handle.

It is not the same as a supervisor pattern, where one lead agent stays in charge and calls helpers. It is also not the same as a fixed pipeline, where the next step is known in advance. The key idea is that ownership moves from one agent to another.
