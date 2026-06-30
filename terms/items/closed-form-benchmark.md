---
title: Closed-form benchmark
short_description: A benchmark with exact answers that can be checked automatically, often used in maths and other tasks with a fixed final result
category: Evals
tags: [benchmark, evals, exact-answer, maths, verification]
status: review
aliases: []
meaning_type: overloaded_buzzword
novelty_level: low
maturity_level: emerging
common_misuse:
  - Treating any benchmark with a neat final answer as closed-form, even when the scoring is still subjective or human-judged.
  - Using it for open-ended tasks that need a long explanation or multiple valid outputs.
related_terms:
  - exact-answer benchmark
  - verifiable benchmark
  - short-answer benchmark
  - math benchmark
evidence:
  - source_title: FrontierMath: LLM Benchmark for Advanced AI Math Reasoning
    source_url: https://epoch.ai/frontiermath/tiers-1-4/about
    source_type: official_docs
    relevance: Shows a current benchmark that relies on closed-form answers which can be checked automatically.
    key_point: Epoch says closed-form math problems can be automatically verified, and FrontierMath uses solutions expressed as closed-form mathematical expressions.
  - source_title: Benchmarking AI on unsolved math problems
    source_url: https://epoch.ai/frontiermath/open-problems/about
    source_type: official_docs
    relevance: Shows that benchmark problems can be designed so candidate answers are verifiable by a program rather than by opinion.
    key_point: Epoch says FrontierMath open-problem tasks are included only when proposed solutions can be verified programmatically.
  - source_title: BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents
    source_url: https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf
    source_type: research_paper
    relevance: Shows the same evaluation pattern outside maths: short, checkable reference answers are what make a hard benchmark practical to score.
    key_point: OpenAI says BrowseComp’s predicted answers are short and easily verifiable against reference answers.
  - source_title: Introducing SimpleQA
    source_url: https://openai.com/index/introducing-simpleqa/
    source_type: official_docs
    relevance: Shows that short, fact-seeking benchmarks are built around answers that can be judged against a known reference.
    key_point: OpenAI describes SimpleQA as a factuality benchmark for short, fact-seeking questions, which fits the same exact-answer style of evaluation.
---
Closed-form benchmark is a benchmark where the answer has a fixed final form and can be checked automatically.

In practice, this usually means the task has one correct answer, or a small set of acceptable answers, and the score can be computed by a rule or a program. These benchmarks are common in maths, factual question answering, and some other tasks where the final result is easy to compare with a reference answer.

The term matters because automatic scoring makes it easier to compare models fairly and at scale. It also reduces the need for human judgement, which is slower and can be inconsistent.

It is not the same as an open-ended benchmark, where many answers might be reasonable and a human or judge model has to decide what is good. It is also not the same as every benchmark with a final answer written as a formula. If the answer still needs subjective scoring, it is not really a closed-form benchmark.
