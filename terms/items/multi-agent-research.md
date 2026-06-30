---
title: Multi-agent research
short_description: A research workflow where one lead agent splits a question across several specialist agents and then combines their findings.
category: Agentic patterns
tags:
- multi-agent
- research
- orchestration
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal standard term when it is mostly an architectural pattern.
- Using it for any chatbot that does web search, even when there is no coordination between agents.
related_terms:
- multi-agent orchestration
- supervisor agent
- sub-agent swarm
- agent research
- parallel agents
evidence:
- source_title: How we built our multi-agent research system
  source_url: https://www.anthropic.com/engineering/multi-agent-research-system
  source_type: engineering_blog
  relevance: Directly describes a production research system built from a lead agent and subagents.
  key_point: Anthropic says the lead agent breaks a query into subtasks and gives them to subagents, which is a close match for this term.
- source_title: Deep Research API with the Agents SDK
  source_url: https://developers.openai.com/cookbook/examples/deep_research_api/introduction_to_deep_research_api_agents
  source_type: official_docs
  relevance: Shows how research workflows are built with agents, tools, and orchestration rather than a single model call.
  key_point: OpenAI presents agentic research as a workflow that combines planning, tool use, and coordination across steps.
- source_title: Multi-agent
  source_url: https://docs.langchain.com/oss/python/langchain/multi-agent
  source_type: official_docs
  relevance: Gives a general definition of multi-agent systems and when to use them for complex workflows.
  key_point: LangChain says multi-agent systems coordinate specialised components and can run subagents in parallel for difficult tasks.
---

Multi-agent research is a way of doing research with more than one AI agent working together.

Usually, one main agent decides what needs to be found, sends smaller jobs to specialist agents, and then puts their results together.

In practice, this can help when a question is broad and needs several angles at once, such as checking facts, comparing sources, and summarising findings.

The term matters because a single agent can get slow or miss things when a task has many parts. Splitting the work can make the process faster and more organised.

It is not just normal web search, and it is not any system with many agents in it. If there is no clear lead agent or no shared research goal, the term does not really fit.
