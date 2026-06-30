---
title: Gold set
short_description: A small, carefully checked reference set used to judge whether an evaluation is working.
category: Evals and benchmarks
tags: [evals, benchmark, ground-truth, reference-set]
status: draft
aliases: []
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
  - Treating a gold set like a benchmark score instead of the small reference set used to score the benchmark.
  - Assuming one gold set proves the system is ready for real use.
  - Using "gold" to mean perfect or final, when it really means carefully checked against a chosen standard.
related_terms:
  - ground truth
  - gold standard dataset
  - benchmark
  - eval dataset
  - reference answer
evidence:
  - source_title: Evaluation best practices
    source_url: https://developers.openai.com/api/docs/guides/evaluation-best-practices
    source_type: official_docs
    relevance: OpenAI explains that evals often use a reference or "gold standard" answer as the benchmark for grading model outputs.
    key_point: The guide frames gold-standard answers as the reference point used to score a response, which matches how a gold set works in evaluation.
  - source_title: Working with evals
    source_url: https://developers.openai.com/api/docs/guides/evals
    source_type: official_docs
    relevance: OpenAI describes evals as tests that compare outputs against ideal answers, showing that a gold set is part of the scoring setup, not the product itself.
    key_point: The guide says evals use input prompts plus ideal answers, which is the practical role of a gold set.
  - source_title: Realtime Eval Guide
    source_url: https://developers.openai.com/cookbook/examples/realtime_eval_guide
    source_type: official_docs
    relevance: OpenAI recommends starting with a small "gold" seed set when building a benchmark, which is a direct use of the term in current practice.
    key_point: The guide says to start with a gold seed set and have humans review it, showing that gold sets are small, curated examples used to bootstrap evaluation.
  - source_title: Demystifying evals for AI agents
    source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    source_type: engineering_blog
    relevance: Anthropic describes evals as tests with inputs and grading logic, and discusses gold-standard human judgements as the reference for evaluating agent behaviour.
    key_point: The post supports the idea that a gold set is the trusted reference against which automated or human scoring is compared.
---

A gold set is a small set of examples that people have checked carefully and use as the reference for scoring an evaluation.

In practice, a gold set is the answer key for a test. If the model gives the same answer as the gold set, the result can be counted as correct. Teams use it to check whether a model, prompt, or agent is getting better or worse over time.

It matters because AI systems can be inconsistent. A gold set helps people compare runs in a fair way and spot mistakes such as wrong facts, missed steps, or unsafe replies.

A gold set is not the whole benchmark and not proof that a system is ready for real life. It is also not a perfect set of truth. It is only as good as the people who made and checked it, and it can become outdated if the task changes.
