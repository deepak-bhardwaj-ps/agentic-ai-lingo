---
slug: agent-collective
title: Agent Collective
short_description: A loose term for a group of AI agents that coordinate their work instead of acting alone.
category: Protocols
tags:
- agentic-ai
- multi-agent-systems
- coordination
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it like a formal standard or fixed technical term
- Assuming it always means the agents share memory, follow one leader, or use the same rules
- Using it for agents that simply run one after another without real coordination
related_terms:
- multi-agent system
- agent coordination
- orchestration
- manager pattern
- decentralized multi-agent system
evidence:
  - source_title: A practical guide to building agents
    source_url: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
    source_type: official_docs
    relevance: OpenAI explicitly distinguishes multi-agent systems from single-agent systems and describes them as coordinated agents, which matches the core meaning of this term.
    key_point: Multi-agent systems distribute workflow execution across multiple coordinated agents.
  - source_title: How we built our multi-agent research system
    source_url: https://www.anthropic.com/engineering/multi-agent-research-system
    source_type: engineering_blog
    relevance: Anthropic shows that a multi-agent system is a set of agents working together, often with parallel subagents, and that coordination is a real design problem.
    key_point: Multiple agents can work together, but coordination, state consistency, and error propagation become important challenges.
  - source_title: Towards a science of scaling agent systems: When and why agent systems work
    source_url: https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
    source_type: engineering_blog
    relevance: Google Research shows that adding more agents can help on some tasks and hurt on others, so the value of a collective depends on how the work is split and coordinated.
    key_point: Multi-agent coordination helps parallelisable tasks but can reduce performance on sequential ones.
  - source_title: AI Organizations Can Be More Effective but Less Aligned than Individual Agents
    source_url: https://alignment.anthropic.com/2026/ai-organizations/
    source_type: engineering_blog
    relevance: This paper-style blog defines a group of communicating agents with different roles and a shared goal, which is close to how people use agent collective.
    key_point: An AI organisation is a multi-agent system where agents take on different roles, communicate, and work towards a common goal.
---

An agent collective is a group of AI agents that work together on the same task or goal.

In practice, the agents may split up a job, pass messages, compare answers, or hand work to one another. One agent might gather facts, another might plan, and another might check the result.

The term matters because one agent is often enough for a small task, but several agents can sometimes do better when a job can be divided into parts. That can help with research, review, and other work where different agents can do different pieces at the same time.

It is not a formal standard. It does not automatically mean the agents share memory, have a leader, or use one shared rulebook. It is also not just several agents running one after another without any real coordination.
