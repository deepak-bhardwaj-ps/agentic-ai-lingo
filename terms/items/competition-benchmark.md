---
title: Competition benchmark
short_description: A benchmark built from a competition, usually with fixed tasks, fixed scoring, and a hidden test set.
category: Evals
tags:
  - benchmark
  - competition
  - evals
status: draft
aliases: []
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
  - Treating any leaderboard or contest as a benchmark, even when the task, data, or scoring is not fixed.
  - Assuming the benchmark score proves real-world performance outside the competition setting.
  - Confusing a competition benchmark with a general benchmark that is not built around a contest or leaderboard.
related_terms:
  - benchmark dataset
  - challenge benchmark
  - leaderboard
  - hidden test set
  - evaluation metric
evidence:
  - source_title: The life cycle of challenges and benchmarks
    source_url: https://ai-competitions-book.github.io/chapters/chapter1.pdf
    source_type: standards_doc
    relevance: Gives a clear, general description of what makes a competition-style benchmark work.
    key_point: Benchmarking competitions usually have a stated problem, public training data, and a scoring method that evaluates predictions on a private hidden test set.
  - source_title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
    source_url: https://arxiv.org/pdf/2410.07095
    source_type: research_paper
    relevance: Shows a modern AI benchmark built directly from real Kaggle competitions.
    key_point: MLE-bench is an offline Kaggle competition benchmark, where each task includes competition data, grading code, and a leaderboard snapshot for comparing agents with human participants.
  - source_title: Find Benchmarks | Kaggle
    source_url: https://www.kaggle.com/benchmarks
    source_type: official_docs
    relevance: Shows current platform usage of the term benchmark in a competition setting.
    key_point: Kaggle describes benchmarks as something people can build, run, and share for evaluating AI models and agents.
---
A competition benchmark is a benchmark made from a competition.

It usually gives everyone the same task, the same data, and the same scoring rules. In many cases, the real test answers are kept hidden, so people cannot simply copy the right output from the training data.

This matters because it lets people compare different models or teams fairly. It is a common way to see which approach performs best on a real task, not just in theory.

It is not the same as a general benchmark that was not built around a contest. It is also not proof that a system will work well in the real world. A strong score only means it did well under that competition's rules.
