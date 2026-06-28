---
slug: agentic-multi-agent-architecture
title: Agentic Multi-Agent Architecture
short_description: A way of building AI systems where several agents share a job and
  coordinate with each other.
category: Protocols
tags:
- agents
- architecture
- orchestration
- coordination
status: Architecture description
aliases:
- multi-agent architecture
- agent orchestration
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating any app with more than one model call as a multi-agent architecture
- Assuming more agents automatically means better results
- Using multiple agents when one agent or a simple workflow would be easier and cheaper
related_terms:
- agent
- orchestration
- workflow
- guardrails
- stateful systems
evidence:
- source_title: How we built our multi-agent research system
  source_url: https://www.anthropic.com/engineering/multi-agent-research-system
  source_type: engineering_blog
  relevance: Shows a real multi-agent design where a lead agent coordinates specialist
    subagents in parallel.
  key_point: Anthropic describes multi-agent systems as an orchestration choice, not
    a default improvement.
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Explains that once multiple agents collaborate, orchestration, tools,
    approvals, and state must be handled explicitly.
  key_point: OpenAI frames agents as systems that can collaborate across specialists
    while keeping enough state to finish work.
- source_title: Orchestration and handoffs
  source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
  source_type: official_docs
  relevance: Describes manager-style workflows where one agent stays responsible and
    calls specialist agents as tools.
  key_point: Multiple agents usually need an explicit controller, handoffs, and a
    clear division of work.
- source_title: LangGraph overview
  source_url: https://docs.langchain.com/oss/python/langgraph/overview
  source_type: official_docs
  relevance: Describes LangGraph as a low-level orchestration framework for long-running,
    stateful agents.
  key_point: The hard part is designing stateful coordination, loops, and control
    flow.
---

An agentic multi-agent architecture is a way of building an AI system where two or more agents share one job and coordinate their work.

In practice, one agent often acts like a manager. It breaks the job into smaller parts, sends those parts to specialist agents, and then combines their answers. The agents may work one after another or at the same time.

This matters when a task has several different skills or when parts of the work can happen in parallel. For example, one agent might search for facts, another might summarise them, and a third might check for mistakes.

It is not the same as simply calling a model twice. It is also not automatically better than a single agent. More agents can mean more cost, more waiting, and more chances for mistakes to spread.

The term is still a bit fuzzy. People use it for anything from a simple manager-and-helper setup to a larger team of agents. The key idea is coordination, not just quantity.
