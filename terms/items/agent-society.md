---
title: Agent Society
short_description: A loose term for a group of AI agents that work together under shared roles, rules, or norms.
category: Protocols
tags:
- agents
- multi-agent
- coordination
- norms
status: emerging
aliases: []
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal standard with one fixed technical meaning.
- Using it for any multi-agent system, even when there are no shared rules or social behaviour.
- Assuming the agents automatically share memory, trust, or security.
related_terms:
- multi-agent system
- agent orchestration
- normative multi-agent system
- agent collaboration
- role-playing agent
evidence:
- source_title: Creating Your First Agent Society
  source_url: https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agents_society
  source_type: official_docs
  relevance: This is one of the clearest current uses of the phrase "agent society" in a real AI framework, and it shows the term being used for agents that communicate to solve tasks.
  key_point: CAMEL says an agent society enables multi-agent communication for task solving and builds it with a RolePlaying setup.
- source_title: How we built our multi-agent research system
  source_url: https://www.anthropic.com/engineering/multi-agent-research-system
  source_type: engineering_blog
  relevance: Anthropic gives a mainstream definition of a multi-agent system, which helps anchor this term as a loose label for several agents working together rather than a separate formal category.
  key_point: A multi-agent system is multiple agents working together, often with one agent planning and spawning specialist subagents.
- source_title: A systematic review of norm emergence in multi-agent systems
  source_url: https://arxiv.org/html/2412.10609v1
  source_type: research_paper
  relevance: This paper explains why rules and norms matter once many agents interact, which matches the "society" part of the term.
  key_point: Norms regulate agent behaviour and help cooperation, coordination, and conflict resolution in multi-agent systems.
---

An agent society is a group of AI agents that work together under shared roles, rules, or norms.

In practice, the agents are not acting alone. They may pass tasks to one another, follow agreed rules, or behave like members of the same group.

The term matters because once many agents are involved, coordination becomes the main problem. You need clear communication, permissions, memory, trust, and control, or the system can become confused and unsafe.

This is not a formal standard. It does not tell you how agents send messages, how they are secured, or whether different systems can connect with each other.

So in plain terms, it is a useful label for a multi-agent system with shared norms, but it is not a technical specification on its own.
