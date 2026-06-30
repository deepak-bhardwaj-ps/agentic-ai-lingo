---
title: Planning benchmark
short_description: A benchmark that tests how well an AI system can plan a sequence of actions to reach a goal
category: Evals
tags: [benchmark, evals, planning, agents]
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating every task that needs reasoning as a planning benchmark, even when it only tests question answering or summarisation.
  - Assuming one planning score proves an AI system can handle real-world jobs safely.
  - Confusing a planning benchmark with a planner product, a schedule optimiser, or a robot controller.
related_terms:
  - planning
  - agent benchmark
  - benchmark suite
  - reasoning about change
  - task planning
evidence:
  - source_title: PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change
    source_url: https://arxiv.org/abs/2206.10498
    source_type: research_paper
    relevance: This is a foundational paper that defines planning benchmarks for language models and explains why they are needed.
    key_point: The paper says planning benchmarks should test whether models can generate plans and reason about actions and change, rather than just repeat common-sense facts.
  - source_title: TravelPlanner: A Benchmark for Real-World Planning with Language Agents
    source_url: https://proceedings.mlr.press/v235/xie24j.html
    source_type: research_paper
    relevance: This paper shows what a planning benchmark looks like in practice for a real-world task with goals and constraints.
    key_point: TravelPlanner is described as a planning benchmark for travel planning, with a sandbox, tools, many data records, and reference plans to check whether agents can stay on task and manage constraints.
  - source_title: Planet: A Collection of Benchmarks for Evaluating LLMs’ Planning Capabilities
    source_url: https://arxiv.org/html/2504.14773v1
    source_type: research_paper
    relevance: This recent survey shows that planning benchmarks are a broader category, not one single named test.
    key_point: The paper groups planning benchmarks into embodied environments, web navigation, scheduling, games and puzzles, and everyday task automation, which supports treating the term as a benchmark category.
---
Planning benchmark is a test that checks whether an AI system can work out a sequence of steps to reach a goal.

In practice, the system is given a goal and has to choose actions in the right order, often while following rules, limits, or changing conditions. Some planning benchmarks use puzzles or formal planning tasks. Others use real-world settings like travel, web use, or household tasks.

Planning benchmarks matter because good planning is more than giving a fluent answer. A system has to keep track of what has already happened, what still needs to happen, and what constraints it must follow. That helps people compare models on tasks that need long, careful action sequences.

This term is not the same as a planning product or an automatic scheduler. It is also not a general intelligence test. The name is a broad category, and the exact tasks can vary a lot from one benchmark to another.
