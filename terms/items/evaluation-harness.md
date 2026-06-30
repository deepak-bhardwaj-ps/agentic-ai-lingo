---
title: Evaluation harness
short_description: Software that runs the same evaluation the same way each time so results can be compared fairly.
category: Evals and benchmarks
tags:
  - evaluation
  - benchmarking
  - testing
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating it as the model itself
  - Using it to mean a benchmark dataset only
  - Assuming one score from one run tells the full story
related_terms:
  - Agent evaluation
  - Agentic harness
  - Benchmark suite
  - Grader
  - Test runner
evidence:
  - source_title: Working with evals
    source_url: https://developers.openai.com/api/docs/guides/evals
    source_type: official_docs
    relevance: Shows that evaluation work on the OpenAI platform is built from repeatable pieces such as datasets, graders, and evaluation runs, which is the operational shape of an evaluation harness.
    key_point: OpenAI says evals test model outputs against criteria you define and are used to compare model behaviour reliably over time.
  - source_title: Realtime Eval Guide
    source_url: https://developers.openai.com/cookbook/examples/realtime_eval_guide
    source_type: official_docs
    relevance: Uses the exact term and describes the harness as the repeatable system that makes evaluation results robust.
    key_point: OpenAI describes an eval harness as one of the core parts of a reusable evaluation setup, alongside the dataset and graders.
  - source_title: Demystifying evals for AI agents
    source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    source_type: engineering_blog
    relevance: Shows that for agent systems, the surrounding harness affects the result, so the harness is part of what must be evaluated or controlled.
    key_point: Anthropic says the harness is the system that processes inputs, orchestrates tool calls, and returns results, and that agent evaluation covers the harness and the model together.
  - source_title: Evaluate your AI agents
    source_url: https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent
    source_type: official_docs
    relevance: Confirms the practical use of agent evaluation setups for repeatable quality and safety checks before release.
    key_point: Microsoft describes agent-targeted evaluations as a way to establish baselines and pass/fail thresholds before deploying an agent.
---

An evaluation harness is the software that runs tests on a model or agent in the same way each time.

In practice, it feeds inputs into the system, collects the outputs, scores them with rules or graders, and records the results. A good harness makes it easier to compare one version with another and to spot when a change helped or hurt.

This matters because AI systems can behave differently from one run to the next. A harness gives you a repeatable way to check quality, safety, and reliability before users see the system.

It is not the model itself. It is also not just a dataset, and it is not the same as a benchmark name. The harness is the machinery that runs the evaluation.
