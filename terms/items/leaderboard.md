---
title: Leaderboard
short_description: A ranked list that compares models or systems using scores from the same benchmark or evaluation.
category: Evals
tags:
  - evals
  - benchmark
status: active
aliases: []
meaning_type: overloaded_buzzword
novelty_level: low
maturity_level: established
common_misuse:
  - Treating the top-ranked system as the best choice for every real-world task.
  - Assuming one leaderboard score proves a model is safe, cheap, fast, or generally reliable.
  - Confusing a leaderboard with the benchmark or test set it is based on.
related_terms:
  - Benchmark
  - Benchmark suite
  - Evaluation
  - Eval suite
  - Model ranking
  - Score normalisation
evidence:
  - source_title: Leaderboards and Evaluations
    source_url: https://huggingface.co/docs/leaderboards/index
    source_type: official_docs
    relevance: Gives a current, direct explanation of how leaderboards are used in AI to rank models and show benchmark results.
    key_point: Hugging Face describes leaderboards as a way to evaluate and rank models and says benchmark results are shown as scores on model pages or in leaderboard views.
  - source_title: Evaluation best practices
    source_url: https://developers.openai.com/api/docs/guides/evaluation-best-practices
    source_type: official_docs
    relevance: Explains that benchmark-style evals compare models in isolation and that scores alone do not tell the whole story.
    key_point: OpenAI notes that industry benchmarks are used for comparing models in isolation and warns that evaluation should not rely only on a single score.
  - source_title: MLPerf Training
    source_url: https://mlcommons.org/benchmarks/training/
    source_type: official_docs
    relevance: Shows how benchmark results are collected and displayed as published results that people can review and compare.
    key_point: MLCommons presents benchmark results in a dashboard and uses official rules as the source of truth, which is the common structure behind many leaderboards.
---
A leaderboard is a ranked list that shows how different models or systems scored on the same benchmark or evaluation.

In practice, each entry gets a score, and the list is ordered from higher to lower. People use leaderboards to compare models quickly and to see which ones do well on a particular test.

Leaderboards matter because they make comparison easier. They can help teams track progress, spot strong models, and notice when a change improves or hurts performance.

A leaderboard is not the same as real life. A model can rank first on one leaderboard and still be a poor choice for your own task, because the test may be too narrow, outdated, or different from the job you care about.

It is also not proof that a model is safe, cheap, fast, or best overall. It only tells you how it performed on the benchmark behind that list.
