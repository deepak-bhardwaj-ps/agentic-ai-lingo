---
title: AgentBench
short_description: A benchmark suite for testing how well language models can act as agents in interactive tasks
category: Evals
tags: [agent, benchmark, evals, interactive-tasks]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Using AgentBench as if it were a general score for all agent behaviour, rather than a specific benchmark suite with its own tasks and rules.
  - Treating a good AgentBench result as proof that an agent will work well in real use.
  - Confusing AgentBench with the broader idea of an agent benchmark.
related_terms:
  - Agent benchmark
  - Agent evaluation
  - Benchmark suite
  - Interactive benchmark
  - Multi-step task benchmark
evidence:
  - source_title: AgentBench: Evaluating LLMs as Agents
    source_url: https://arxiv.org/abs/2308.03688
    source_type: research_paper
    relevance: Original paper defining AgentBench and explaining what it measures.
    key_point: The paper presents AgentBench as a multi-dimensional benchmark for evaluating language models as agents across interactive environments, with tasks that test reasoning and decision-making over multiple turns.
  - source_title: THUDM/AgentBench
    source_url: https://github.com/THUDM/AgentBench
    source_type: engineering_blog
    relevance: Official project repository showing the benchmark’s scope and how it is packaged for use.
    key_point: The repository describes AgentBench as a comprehensive benchmark for LLM-as-Agent and shows that it includes multiple environments rather than one single test.
  - source_title: AgentBench: Evaluating LLMs as Agents
    source_url: https://openreview.net/forum?id=zAdUB0aCTQ
    source_type: standards_doc
    relevance: Conference record confirming the paper’s framing and helping distinguish the benchmark from informal uses of the name.
    key_point: The OpenReview record presents AgentBench as a benchmark for evaluating agents in interactive settings, reinforcing that it is a formal evaluation suite.
---
AgentBench is a benchmark suite for testing how well a language model can act like an agent in interactive tasks.

In practice, it gives the same kinds of tasks to different models so their behaviour can be compared fairly. The tasks are not just one answer at a time. They can involve several steps, using tools, and making choices as the situation changes.

It matters because agent systems are judged by what they do over time, not only by how they answer a question. A benchmark like AgentBench helps people see whether a system can plan, follow instructions, and keep working through a task.

AgentBench is not the same as a real job or a real app in production. A strong score does not prove the agent will be reliable, safe, or useful in every situation. It is also not the same as the general idea of an agent benchmark, which can refer to many different tests.
