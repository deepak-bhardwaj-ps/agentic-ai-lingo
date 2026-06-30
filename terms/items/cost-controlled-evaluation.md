---
title: Cost-controlled evaluation
short_description: An evaluation that compares systems under a fixed or clearly stated cost budget.
category: Evals and benchmarks
tags:
  - evaluation
  - benchmarks
  - cost
  - agent-evaluation
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the same thing as being cheap overall
  - Comparing agents by accuracy alone without reporting the cost needed to reach it
  - Using different budgets or run settings and then treating the results as directly comparable
related_terms:
  - agent evaluation
  - benchmark
  - cost-performance tradeoff
  - Pareto frontier
  - evaluation budget
evidence:
  - source_title: AI Agents That Matter
    source_url: https://arxiv.org/abs/2407.01502
    source_type: research_paper
    relevance: This is the clearest source for the term itself and explains why agent benchmarks should account for cost, not just accuracy.
    key_point: The paper argues that agent evaluation should jointly optimise accuracy and cost, because accuracy-only benchmarking can reward needlessly expensive systems.
  - source_title: Practices for Automated Benchmark Evaluations of Language Models
    source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-2.ipd.pdf
    source_type: standards_doc
    relevance: This current NIST draft gives practical guidance that evaluation results should report both performance and the costs used to achieve it.
    key_point: NIST says evaluators should balance statistical power against budget and should report costs alongside performance when systems are not uniformly cost controlled.
  - source_title: Evaluation best practices
    source_url: https://developers.openai.com/api/docs/guides/evaluation-best-practices
    source_type: official_docs
    relevance: This official guide supports the broader idea that evaluation should be designed around clear objectives and metrics instead of vague scoring.
    key_point: OpenAI recommends defining the evaluation objective and metrics up front, which is necessary if cost is one of the things being controlled.
---

Cost-controlled evaluation is an evaluation that compares systems under a fixed or clearly stated cost budget.

In practice, it means the test does not just ask, “Which system got the best score?” It also asks, “What did that score cost to produce?” The cost might be extra model calls, more retries, more tool use, or a larger amount of compute.

The point is to stop expensive systems from looking better just because they spent more. This matters because two agents can get similar results, but one may use far more time or money to get there.

It is not the same as “cheap evaluation”. It is also not a formal universal standard with one fixed formula. The main idea is to compare quality and cost together so the result reflects real use, not just leaderboard performance.
