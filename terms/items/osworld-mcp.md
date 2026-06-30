---
title: OSWorld-MCP
short_description: A benchmark for testing computer-use agents on GUI actions and MCP tool use.
category: Evals
tags:
- benchmark
- computer-use agents
- MCP
- OSWorld
status: draft
aliases:
- OSWorld MCP
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the MCP standard itself rather than a benchmark that measures MCP tool use inside tasks.
- Treating it as the same thing as OSWorld, when it is an extension of OSWorld with MCP tools added.
related_terms:
- OSWorld
- Model Context Protocol
- computer-use agents
- benchmark
- tool invocation
evidence:
- source_title: OSWorld-MCP Leaderboard
  source_url: https://osworld-mcp.github.io/
  source_type: official_docs
  relevance: Official project page for the benchmark.
  key_point: Says OSWorld-MCP is the first comprehensive benchmark for assessing tool invocation, GUI operation, and decision-making in computer-use agents.
- source_title: OSWorld-MCP: Benchmarking MCP Tool Invocation in Computer-Use Agents
  source_url: https://arxiv.org/abs/2510.24563
  source_type: research_paper
  relevance: Research paper defining the benchmark and its scope.
  key_point: Describes OSWorld-MCP as an extension of OSWorld that adds MCP tools to evaluate computer-use agents more fairly.
- source_title: OSWorld project page
  source_url: https://os-world.github.io/
  source_type: official_docs
  relevance: Establishes the base benchmark that OSWorld-MCP extends.
  key_point: OSWorld is a real computer environment for multimodal agents with execution-based evaluation, which OSWorld-MCP builds on.
- source_title: What is the Model Context Protocol (MCP)?
  source_url: https://modelcontextprotocol.io/docs/getting-started/intro
  source_type: official_docs
  relevance: Defines MCP so the term is not confused with the benchmark itself.
  key_point: MCP is an open standard for connecting AI applications to external systems, so OSWorld-MCP is about testing MCP tool use, not redefining MCP.
---
OSWorld-MCP is a benchmark for testing computer-use agents.

It checks whether an agent can use a computer interface and also choose when to use MCP tools.

In practice, the benchmark gives the agent tasks in a real computer environment and scores how well it completes them. It looks at task success, tool use, and how many steps the agent needs.

This matters because many agents are good at clicking and typing, but weaker at using the right tool at the right time. OSWorld-MCP helps compare those abilities in a more realistic way.

It is not the MCP protocol itself. It is not just a general OSWorld task set. It is a specific evaluation built on OSWorld with MCP tools added.
