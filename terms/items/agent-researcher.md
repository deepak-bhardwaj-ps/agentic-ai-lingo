---
title: Agent researcher
short_description: A specialist agent role that gathers, checks, and summarises information for a larger agent system.
category: Roles
tags:
- roles
- agents
- research
status: draft
aliases:
- Research agent
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal, standard job title with one agreed definition.
- Confusing the role with a general chat assistant that only answers questions from memory.
- Assuming it can replace human checking when the sources are weak, missing, or contradictory.
related_terms:
- Deep research
- Research agent
- Agent developer
- Agent orchestrator
- Agent maintainer
evidence:
- source_title: What is Researcher Agent in Microsoft 365 Copilot?
  source_url: https://learn.microsoft.com/en-us/microsoft-365/copilot/researcher-agent
  source_type: official_docs
  relevance: Microsoft’s documentation gives a current, concrete example of a research-focused agent that finds, organises, and cites information for users.
  key_point: Researcher agent handles complex, multi-step research and produces source-cited reports from web and work data.
- source_title: Introducing deep research
  source_url: https://openai.com/index/introducing-deep-research/
  source_type: official_docs
  relevance: OpenAI describes a research agent that independently searches and synthesises many sources, which supports the idea of a dedicated research role inside an agent system.
  key_point: Deep research conducts multi-step web research, analyses many sources, and returns a documented report.
- source_title: How we built our multi-agent research system
  source_url: https://www.anthropic.com/engineering/multi-agent-research-system
  source_type: engineering_blog
  relevance: Anthropic explains research as a multi-agent workflow with a planning agent and parallel search agents, which is the clearest engineering model for this term.
  key_point: A research system can use one agent to plan the search and other agents to gather information in parallel.
---

An agent researcher is a specialist agent role that looks for information, checks it, and turns it into a clear summary for a bigger system.

In practice, an agent researcher may search the web, read documents, compare sources, and collect facts before handing the result to another agent or to a person.

The term matters because some tasks need more than a quick answer. Research work often needs several steps, source checking, and a summary that shows where the information came from.

This is not a standard job title with one fixed meaning. It is also not the same as a normal chatbot, and it should not be treated as a substitute for human judgement when the evidence is weak or conflicting.
