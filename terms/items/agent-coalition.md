---
slug: agent-coalition
name: Agent Coalition
title: Agent Coalition
category: Protocols
aliases: []
short_description: A loose term for several separate agents that coordinate on one goal.
status: emerging
tags:
  - multi-agent-systems
  - coordination
  - interoperability
 meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a formal standard with one agreed technical meaning.
  - Confusing it with one orchestrator splitting work across sub-agents under a single owner.
related_terms:
  - multi-agent system
  - agent orchestration
  - handoff
  - agent swarms
  - Agent2Agent (A2A) protocol
evidence:
  - source_title: A practical guide to building AI agents
    source_url: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
    source_type: official_docs
    relevance: Shows that multi-agent systems are a recognised pattern where work is distributed across coordinated agents.
    key_point: OpenAI describes multi-agent systems as workflows split across multiple coordinated agents.
  - source_title: How we built our multi-agent research system
    source_url: https://www.anthropic.com/engineering/multi-agent-research-system
    source_type: engineering_blog
    relevance: Explains that multiple agents can work together while keeping separate roles and tool use.
    key_point: Anthropic describes a multi-agent system as multiple agents working together, with one agent spawning parallel specialist agents.
  - source_title: Introduction to A2A
    source_url: https://google.github.io/adk-docs/a2a/intro/
    source_type: official_docs
    relevance: Shows the newer push for agents that can communicate and collaborate across systems, which is the closest formal idea to this term.
    key_point: Google’s A2A docs say the protocol lets specialised agents collaborate to solve a problem.
  - source_title: A review of cooperation in multi-agent learning
    source_url: https://arxiv.org/html/2312.05162v1
    source_type: research_paper
    relevance: Provides the older research background for agents coordinating and cooperating towards shared goals.
    key_point: The review frames cooperation as agents coordinating effectively when goals are aligned.
---

An agent coalition is a group of separate agents that work together on one goal.

In practice, each agent still keeps its own job, limits, and rules. They do not become one single agent. They may split up tasks, pass work to each other, or combine their results.

The term matters because real systems are often built from parts made by different teams or companies. It is a useful way to describe agents that cooperate without being merged into one system.

This is not a strict technical standard with one fixed meaning. It is also not the same as one app controlling a set of sub-agents. When people use the phrase, they usually mean coordinated agents, not a new kind of single agent.
