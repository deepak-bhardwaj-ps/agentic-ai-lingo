---
title: QF-Bench
short_description: A benchmark for testing AI agents on quantitative finance tasks
category: Evals and benchmarks
tags: [benchmark, evals, finance, quantitative-finance, agent-evals]
status: active
aliases: [QuantitativeFinance-Bench]
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it like a general finance quiz or a trading system.
  - Confusing it with FinanceBench, which is a different benchmark for financial question answering.
related_terms:
  - FinanceBench
  - benchmark
  - AI agent
  - quantitative finance
  - sandbox
evidence:
  - source_title: QFBench | Quantitative Finance Benchmark for AI Agents
    source_url: https://qfbench.com/
    source_type: official_docs
    relevance: Official project site that names the benchmark and explains its purpose in the project’s own words.
    key_point: QFBench is presented as a benchmark for AI agents in quantitative finance, with tasks that require real code and verifiable outputs.
  - source_title: QuantitativeFinance-Bench README
    source_url: https://github.com/QF-Bench/QuantitativeFinance-Bench
    source_type: official_docs
    relevance: Repository README that gives the clearest technical description of what the benchmark actually tests.
    key_point: The project describes QF-Bench as a state-aware, interactive benchmark for financial and quantitative agent tasks that runs in a secure sandbox.
  - source_title: Task Contribution Guide
    source_url: https://github.com/QF-Bench/QuantitativeFinance-Bench/blob/main/docs/task_contribution.md
    source_type: official_docs
    relevance: Shows how the maintainers define a good task, which helps pin down the benchmark’s meaning.
    key_point: Tasks must be state-aware, use real data, and be programmatically verifiable, so the benchmark is about interactive quantitative work rather than simple question answering.
---

QF-Bench is a benchmark for checking how well an AI agent can do quantitative finance tasks.

In practice, this means the agent has to work through real finance problems, often by running code, reading files, and producing answers that can be checked automatically.

It matters because finance work needs correct numbers, careful reasoning, and outputs that can be verified. A benchmark like this helps people compare systems more fairly.

QF-Bench is not a general finance quiz, and it is not a trading bot or investing app. It is also not the same as FinanceBench, which focuses on question answering about financial documents rather than interactive quantitative work.
