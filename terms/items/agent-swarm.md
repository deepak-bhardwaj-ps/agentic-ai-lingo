---
slug: agent-swarm
name: Agent Swarm
title: Agent Swarm
short_description: A loose term for several AI agents working together on one task, often by splitting work and sharing results.
category: Runtime
tags: []
status: informal
aliases: []
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Using it as a fancy name for any multi-agent system, even when the agents do not really coordinate.
  - Assuming it always means many agents; in practice it can mean a small team of specialised agents.
  - Confusing it with simple parallel runs that never combine their results.
related_terms:
  - multi-agent system
  - multi-agent collaboration
  - sub-agent swarm
  - agent orchestration
  - supervisor agent
evidence:
  - source_title: Multi-agent
    source_url: https://docs.langchain.com/oss/python/langchain/multi-agent
    source_type: official_docs
    relevance: Shows the practical meaning of a multi-agent setup as specialised components coordinating on a workflow, which is the closest stable meaning behind "agent swarm".
    key_point: LangChain says multi-agent systems coordinate specialised components, but also warns that a single agent is often enough.
  - source_title: How we built our multi-agent research system
    source_url: https://www.anthropic.com/engineering/multi-agent-research-system
    source_type: engineering_blog
    relevance: Gives a concrete production example of multiple agents working in parallel under a lead agent, which matches how people usually mean swarm in agent systems.
    key_point: Anthropic describes a lead agent creating parallel agents that search for information at the same time.
  - source_title: Multi-agent patterns
    source_url: https://learn.microsoft.com/en-us/agents/architecture/multi-agent-patterns
    source_type: official_docs
    relevance: Confirms that multi-agent systems are usually built around explicit coordination, task splitting, and governance rather than just many agents at once.
    key_point: Microsoft recommends simple orchestration, least privilege, and clear coordination for multi-agent workflows.
  - source_title: Multi-agent architectures
    source_url: https://learn.microsoft.com/en-us/dynamics365/guidance/resources/contact-center-multi-agent-architecture-design
    source_type: official_docs
    relevance: Explains why teams use multiple agents in the first place and shows that coordination can be centralised, decentralised, or hybrid.
    key_point: Microsoft says multi-agent architectures use multiple autonomous agents with unique capabilities that cooperate, compete, or work independently.
---

An agent swarm is a loose term for several AI agents working together on one task.

In practice, the agents usually split the work. One may search, another may draft, and another may check the answer. Sometimes one agent leads and assigns jobs. Sometimes the group is more decentralised, with agents sharing results and reacting to each other.

The term matters because dividing work can help an AI system handle bigger or more complex jobs than one agent could handle well on its own. It can also make the system faster when agents work in parallel.

It is not a strict technical standard. People often use it to mean any multi-agent setup, even when there is no clear swarm-like behaviour. It is also not the same as just running many agents at once. If they do not coordinate or combine their work, "swarm" is mostly just a label.
