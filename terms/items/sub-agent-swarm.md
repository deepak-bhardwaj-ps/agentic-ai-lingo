---
slug: sub-agent-swarm
title: Sub-Agent Swarm
short_description: A sub-agent swarm is a group of smaller agents that a main agent
  coordinates to split up work.
category: Runtime
tags:
- multi-agent
- orchestration
- subagents
- runtime
status: emerging
aliases:
- subagent swarm
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it like a formal standard term when it is usually informal shorthand.
- Using it to mean any multi-agent system, even when there is no clear coordinator
  or task split.
- Assuming a swarm always means many agents; in practice it can mean just a few specialists.
related_terms:
- multi-agent system
- orchestration
- supervisor agent
- subagent
- agent handoff
evidence:
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Explains why parallel work and task decomposition are useful in agent
    systems.
  key_point: Anthropic describes parallelisation as useful when subtasks can be split
    across separate model calls.
- source_title: How we built our multi-agent research system
  source_url: https://www.anthropic.com/engineering/multi-agent-research-system
  source_type: engineering_blog
  relevance: Shows a real system using subagents to explore different parts of a problem
    at the same time.
  key_point: Subagents operate in parallel with separate context windows and are merged
    by a lead agent.
- source_title: Subagents - Docs by LangChain
  source_url: https://docs.langchain.com/oss/python/langchain/multi-agent/subagents
  source_type: official_docs
  relevance: Describes the supervised worker pattern that this phrase usually refers
    to.
  key_point: A central supervisor agent coordinates specialised worker agents.
- source_title: Orchestration and handoffs | OpenAI API
  source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
  source_type: official_docs
  relevance: Confirms the broader design pattern of using a main agent with specialist
    agents as tools.
  key_point: A manager-style workflow can keep the main agent responsible while calling
    specialists as helpers.
---

A sub-[[Agent Swarm|agent swarm]] is a group of smaller agents that a main agent coordinates to split up a task.

In practice, the main agent gives each sub-agent a smaller job. The sub-agents may work at the same time, each looking at a different part of the problem, and then the main agent combines what they found.

This matters because some jobs are too big for one agent to do well in one pass. Breaking the work into parts can make the system faster and more careful.

It is not a strict technical standard. Peop[[Context Collapse|l]]e use the phrase in different ways, so it should be defined clearly in any real system. It is also not just “many agents together”; without a clear coordinator and shared goal, it is not really a sub-[[Agent Swarm|agent swarm]].
