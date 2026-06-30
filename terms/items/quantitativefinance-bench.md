---
title: QuantitativeFinance-Bench
short_description: A state-aware benchmark for testing AI agents on quantitative finance tasks.
category: Evals
tags: [benchmark, evals, finance, agent, quantitative-finance]
status: draft
aliases: [QFBench]
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a simple finance question-answering benchmark.
  - Assuming a high score means an agent can trade profitably in the real world.
related_terms:
  - agent benchmark
  - agent evaluation
  - financial benchmark
  - quantitative finance
  - interactive benchmark
evidence:
  - source_title: QFBench | Quantitative Finance Benchmark for AI Agents
    source_url: https://qfbench.com/
    source_type: official_docs
    relevance: The project site is the clearest current public description of the benchmark and its intended use.
    key_point: It describes Quantitative Finance-Bench, also branded as QFBench, as a benchmark for AI agents in quantitative finance with real code and verifiable outputs.
  - source_title: QF-Bench/QuantitativeFinance-Bench
    source_url: https://github.com/QF-Bench/QuantitativeFinance-Bench
    source_type: official_docs
    relevance: The repository explains the benchmark’s mechanics and confirms that it is interactive and state-aware, not just a static quiz.
    key_point: The README says it evaluates agents in stateful environments, handling dirty data, runtime errors, and numeric outputs inside a secure sandbox.
  - source_title: QuantEval: A Benchmark for Financial Quantitative Tasks in Large Language Models
    source_url: https://arxiv.org/abs/2601.08689
    source_type: research_paper
    relevance: This newer paper shows the broader research direction for quantitative-finance evaluation and helps distinguish coding-and-reasoning benchmarks from ordinary finance QA.
    key_point: It frames quantitative finance evaluation around knowledge QA, mathematical reasoning, and strategy coding with execution-based backtesting, which matches the kind of skills this term targets.
---
QuantitativeFinance-Bench is a benchmark that tests whether an AI agent can handle real quantitative finance tasks.

In practice, it gives the agent finance problems that need code, calculations, debugging, and careful checking of numbers. The tasks are meant to behave more like real quant work than like a normal quiz.

The term matters because an agent can sound convincing and still be wrong on the maths. A benchmark like this helps show whether the system can produce outputs that are actually correct and repeatable.

It is not just a finance question-answering set. It is also not proof that a model can make money in live markets, because benchmark results do not remove real-world trading risks.
