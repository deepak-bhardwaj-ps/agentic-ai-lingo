---
title: Agent developer
short_description: A person who designs, builds, and tests AI agents.
category: Roles
tags:
- roles
- agents
- development
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as any software developer who uses chatbots, rather than someone focused on building agent behaviour, tools, and safeguards.
related_terms:
- Agent builder
- Agentic engineer
- Agent orchestrator
- Agent maintainer
evidence:
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: OpenAI’s documentation shows that building agents is a developer task involving code, tools, orchestration, approvals, and state.
  key_point: Agents are applications that plan, call tools, and keep state, so an agent developer works on those building blocks.
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Anthropic’s guidance is aimed at developers and explains practical ways to build agents without treating them as a separate magical category.
  key_point: The article frames agent building as a developer activity and emphasises simple, composable patterns.
- source_title: Agent Framework documentation
  source_url: https://learn.microsoft.com/en-us/agent-framework/
  source_type: official_docs
  relevance: Microsoft’s documentation is explicit that developers build AI agents and multi-agent workflows with its framework.
  key_point: The platform is for building, deploying, and governing agents, which matches the role described here.
---

An agent developer is a person who builds AI agents.

In practice, that means designing what the agent should do, connecting it to tools and data, testing how it behaves, and adding rules so it does not do the wrong thing.

The term matters because AI agents are not just chat boxes. They can plan steps, use tools, and keep track of state, so they need someone who can build and check those parts carefully.

This is not just a general app developer, and it is not the same as someone who only writes prompts. The term is still emerging, so different teams may use nearby names such as agent builder or agentic engineer.
