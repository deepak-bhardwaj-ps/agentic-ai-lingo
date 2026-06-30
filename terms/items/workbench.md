---
title: WorkBench
short_description: A benchmark for testing AI agents on realistic workplace tasks with tools and changing database state
category: Evals and benchmarks
tags: [benchmark, evals, agentic-ai, tool-use, workplace]
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating WorkBench as a general workplace tool instead of a benchmark for evaluation.
  - Assuming a good score means an AI agent is safe or reliable in real office work.
  - Confusing it with unrelated products or any generic workbench used for building things.
related_terms:
  - benchmark
  - agent evaluation
  - tool use
  - sandbox environment
  - workplace agents
  - outcome-centric evaluation
evidence:
  - source_title: WorkBench: a Benchmark Dataset for Agents in a Realistic Workplace Setting
    source_url: https://arxiv.org/abs/2405.00823
    source_type: research_paper
    relevance: This is the original paper that defines WorkBench and explains what kind of agent tasks it measures.
    key_point: The paper presents WorkBench as a benchmark for evaluating agents in a realistic workplace setting, with tools, databases, and tasks such as sending emails and scheduling meetings.
  - source_title: olly-styles/WorkBench
    source_url: https://github.com/olly-styles/WorkBench
    source_type: engineering_blog
    relevance: This maintained repository shows how the benchmark is packaged and used in practice, including the sandbox and scoring approach.
    key_point: The repository describes WorkBench as an open-source benchmark for realistic workplace tasks and says tasks are graded by comparing the sandbox's final state against the ground truth.
  - source_title: WorkBench Revisited: Workplace Agents Two Years On
    source_url: https://arxiv.org/abs/2606.13715
    source_type: research_paper
    relevance: This follow-up paper confirms the term is still used for the same benchmark and shows current framing in the literature.
    key_point: The paper revisits WorkBench as a benchmark for workplace agents and reports newer model results on the same task set.
---

WorkBench is a benchmark for testing AI agents on realistic workplace tasks.

In practice, it gives an AI tools, databases, and tasks such as sending emails or scheduling meetings. The AI has to choose actions and make changes in the right place, and the result is checked against the expected outcome.

It matters because simple question tests do not show whether an AI can handle a job-like task from start to finish. WorkBench checks planning, tool use, and whether the agent causes the right change without making the wrong one.

WorkBench is not a workplace app and it is not proof that an AI is safe to use in real office work. It is a test environment for measuring agents, not a system for doing the work itself.
