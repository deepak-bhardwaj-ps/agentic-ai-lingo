---
title: Reliability benchmark
short_description: A benchmark that tests whether an AI system keeps working reliably across repeated runs, wording changes, and failures.
category: Evals
tags:
  - evals
  - benchmarks
  - agents
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating one successful run as proof that a system is reliable.
  - Using it as a loose synonym for any benchmark or test.
  - Confusing reliability with raw accuracy on one fixed prompt.
related_terms:
  - agent evaluation
  - evaluation harness
  - robustness
  - pass@k
  - SWE-bench Verified
evidence:
  - source_title: Testing Agent Skills Systematically with Evals
    source_url: https://developers.openai.com/blog/eval-skills
    source_type: official_docs
    relevance: Shows how OpenAI describes evals as repeatable checks for whether an agent behaves as intended over time.
    key_point: Evals are framed as a way to compare runs and catch regressions, which is the practical purpose of a reliability benchmark.
  - source_title: ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions
    source_url: https://arxiv.org/abs/2601.06112
    source_type: research_paper
    relevance: Gives the clearest current use of the phrase in agent evaluation and defines reliability as consistency, robustness, and fault tolerance.
    key_point: The paper argues that existing benchmarks miss production reliability because they focus too much on single-run success.
  - source_title: Evaluation and Benchmarking of LLM Agents: A Survey
    source_url: https://arxiv.org/abs/2507.21504
    source_type: research_paper
    relevance: Confirms that reliability is a recognised evaluation objective in agent benchmarking, but not a fully standardised term.
    key_point: Reliability means the agent behaves consistently for the same input and robustly when input changes or errors occur.
  - source_title: Introducing SWE-bench Verified
    source_url: https://openai.com/index/introducing-swe-bench-verified/
    source_type: official_docs
    relevance: Shows a real benchmark being improved to better measure whether model performance is trustworthy and not overstated.
    key_point: OpenAI says some benchmark tasks can mislead about real capability, which is why more reliable benchmark design matters.
---
Reliability benchmark is a benchmark that checks whether an AI system keeps giving good results across repeated runs and small changes.

In practice, it is used to see if a system is steady or flaky. A system may solve a task once, but still fail when the same task is asked again, when the wording changes a little, or when a tool or API breaks. A reliability benchmark tries to catch that.

This matters because one lucky result can hide a weak system. If people want to trust an AI agent in real work, they need more than a single score. They need to know whether it keeps working under repeat tests and messy conditions.

It is not the same as a normal accuracy benchmark. It is also not a fixed industry standard, and people may use the term in slightly different ways. In agent work, it usually means a benchmark that checks consistency, robustness, and failure handling.
