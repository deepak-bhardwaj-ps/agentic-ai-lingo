---
title: Multi-agent benchmark
short_description: A fixed test for measuring how well a system of several AI agents works together, competes, or coordinates.
category: Evals and benchmarks
tags: [agent, benchmark, evals, multi-agent]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating any test of one agent as a multi-agent benchmark
  - Assuming a high score means the agents will work well in a real product
  - Using the term for any benchmark that merely allows multiple runs, rather than one that measures interaction between agents
related_terms:
  - multi-agent system
  - agent benchmark
  - agent orchestration
  - collaboration
  - coordination
evidence:
  - source_title: Multi-agent collaboration
    source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html
    source_type: official_docs
    relevance: Defines the underlying pattern that benchmarks usually try to measure.
    key_point: AWS says multi-agent collaboration means multiple autonomous agents with different roles coordinate by sharing information and dividing work, which is the behaviour a multi-agent benchmark should test.
  - source_title: MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents
    source_url: https://arxiv.org/abs/2503.01935
    source_type: research_paper
    relevance: Gives a direct example of a benchmark built specifically for multi-agent behaviour.
    key_point: The paper says existing benchmarks miss multi-agent coordination and competition, and introduces a benchmark that measures both task completion and the quality of interaction between agents.
  - source_title: Evaluation and Benchmarking of LLM Agents: A Survey
    source_url: https://arxiv.org/abs/2507.21504
    source_type: research_paper
    relevance: Shows that agent evaluation is still fragmented and that benchmarks for agent behaviour are a distinct area.
    key_point: The survey frames LLM agent evaluation as a separate field and discusses benchmarks that assess sequences of actions and interactions, which supports the idea that multi-agent benchmarks are about coordinated behaviour, not single-turn answers.
---

A multi-agent benchmark is a fixed test that checks how well several AI agents work together, compete, or coordinate on a task.

In practice, it gives the agents the same challenge in a controlled setup and then scores things like whether they finished the task, how well they shared work, and whether they avoided confusion or conflict.

This matters because a group of agents can look fine in a demo but fail when they need to divide tasks, pass information, or recover from mistakes.

It is not the same as a single-agent benchmark. It is also not just any test that happens to involve more than one model run. A true multi-agent benchmark measures interaction between agents, not only individual answers.
