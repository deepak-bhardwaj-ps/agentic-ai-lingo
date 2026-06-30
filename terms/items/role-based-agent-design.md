---
title: Role-based agent design
short_description: A way of building an agent system by giving different agents different jobs, such as researcher, checker, planner, or writer.
category: Agentic patterns
tags:
- agentic-ai
- multi-agent-systems
- orchestration
- delegation
status: active
aliases: []
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: maturing
common_misuse:
- Treating it as a formal standard instead of a loose design pattern
- Thinking the role name gives the agent extra intelligence rather than just a narrower job
- Confusing role design with permission design
related_terms:
- multi-agent system
- orchestrator
- subagent
- specialized agent
- delegation
evidence:
- source_title: How we built our multi-agent research system
  source_url: https://www.anthropic.com/engineering/multi-agent-research-system
  source_type: engineering_blog
  relevance: Shows a current production system split into a lead agent and specialised subagents with different jobs.
  key_point: Anthropic describes a multi-agent system where a lead agent creates parallel subagents with separate prompts, tools, and exploration paths.
- source_title: Building a Multi-Agent System
  source_url: https://codelabs.developers.google.com/codelabs/production-ready-ai-roadshow/1-building-a-multi-agent-system/building-a-multi-agent-system
  source_type: engineering_blog
  relevance: Gives a concrete example of agents assigned different roles in one workflow.
  key_point: Google’s codelab builds a researcher, judge, content builder, and orchestrator, showing role-based splitting of work.
- source_title: Agent Builder
  source_url: https://developers.openai.com/api/docs/guides/agent-builder
  source_type: official_docs
  relevance: Shows that agent workflows can route work to specialised agents inside one system.
  key_point: OpenAI documents workflows that take questions, reframe them, route them to other specialised agents, and return an answer.
- source_title: Multi-Agent Collaboration Mechanisms: A Survey of LLMs
  source_url: https://arxiv.org/html/2501.06322v1
  source_type: research_paper
  relevance: Supports the idea that role-based collaboration is a recognised strategy in multi-agent research, even if the exact term is not standard.
  key_point: The survey explicitly lists role-based strategies as one way to organise collaboration in multi-agent systems.
---

Role-based agent design is a way of building an agent system where different agents have different jobs.

One agent might search for information, another might check the answer, and another might turn the result into something the user can read. The idea is to split a hard task into smaller parts and give each part to the agent best suited for it.

In practice, this often means an orchestrator agent or workflow sends work to specialist agents with clear roles. The roles help the system stay organised and make the overall result more reliable.

It matters because one general agent can struggle with big, messy jobs. Special roles can make a system faster to understand, easier to test, and better at handling complex work.

This is not a formal standard. It is a design pattern, and different teams may use different names for it.

It is not the same as giving an agent a human personality. It is also not the same as access control. A role describes what the agent is supposed to do, not what it is allowed to reach.
