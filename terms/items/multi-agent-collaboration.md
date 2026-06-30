---
title: Multi-agent collaboration
short_description: Two or more AI agents working together on the same task by splitting work, sharing results, or handing off parts of the job.
category: Agentic patterns
tags:
  - multi-agent
  - collaboration
  - orchestration
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating any system with more than one agent as “collaboration” even when the agents do not coordinate.
  - Using it as a fancy name for a single agent that only calls tools.
  - Assuming it always means a fixed team structure; in practice it can be loose, centralised, or parallel.
related_terms:
  - multi-agent system
  - multi-agent orchestration
  - supervisor agent
  - sub-agent swarm
  - agent handoff
evidence:
  - source_title: Orchestration and handoffs
    source_url: https://developers.openai.com/api/docs/guides/agents/orchestration
    source_type: official_docs
    relevance: Shows the manager-style pattern where one agent stays responsible while calling specialist agents, which is a common form of collaboration.
    key_point: OpenAI describes using agents as tools so a main agent can stay in charge and collaborate with specialists.
  - source_title: Multi-agent
    source_url: https://docs.langchain.com/oss/python/langchain/multi-agent
    source_type: official_docs
    relevance: Defines the main coordination patterns used in practice, including subagents and handoffs.
    key_point: LangChain explains that a main agent can coordinate subagents as tools and route control between agents.
  - source_title: How we built our multi-agent research system
    source_url: https://www.anthropic.com/engineering/multi-agent-research-system
    source_type: engineering_blog
    relevance: Gives a real production example of agents working in parallel and then combining results.
    key_point: Anthropic describes multiple agents exploring parts of a research task at the same time under a lead agent.
  - source_title: Multi-Agent Collaboration Mechanisms: A Survey of LLMs
    source_url: https://arxiv.org/abs/2501.06322
    source_type: research_paper
    relevance: Shows that the term sits inside a broader, still-developing research area with many collaboration styles.
    key_point: The survey treats collaboration as a field with different actors, structures, strategies, and coordination protocols.
---

Multi-agent collaboration means two or more AI agents working together on the same job.

In practice, one agent may split the work into smaller parts, give tasks to other agents, collect their results, and combine them into one answer. Sometimes the agents work in parallel. Sometimes one agent hands off to another when a different skill is needed.

This matters because some tasks are easier and more reliable when different agents focus on different parts of the problem. It can help with speed, specialisation, and keeping each agent's context smaller.

It is not just any system with many agents. If the agents do not coordinate, it is not really collaboration. It is also not the same as a single agent using tools, unless there is a real second agent doing separate work.

The term is useful, but not fully settled. Different products and teams use it in slightly different ways, so any real system should explain exactly how the agents work together.
