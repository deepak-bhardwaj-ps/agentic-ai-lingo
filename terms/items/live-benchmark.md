---
title: Live benchmark
short_description: A benchmark that keeps adding or refreshing tasks over time so it stays current and harder to memorise.
category: Evals
tags:
- benchmark
- evals
- contamination
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as any benchmark that is simply public or online
- Assuming it always means a streaming leaderboard rather than an updated test set
- Using it as proof that a model works well in real life
related_terms:
- static benchmark
- contamination
- benchmark suite
- continuous evaluation
- contamination-resistant benchmark
evidence:
- source_title: LiveBench
  source_url: https://github.com/livebench/livebench
  source_type: official_docs
  relevance: Shows a current benchmark project that defines itself around monthly updates, fresh questions, and contamination control. This anchors the term in practice.
  key_point: LiveBench says it limits contamination by releasing new questions monthly and using recently released datasets, arXiv papers, news articles, and IMDb synopses.
- source_title: LiveXiv - A Multi-Modal Live Benchmark Based on Arxiv Papers Content
  source_url: https://arxiv.org/html/2410.10783v3
  source_type: research_paper
  relevance: Explains the core idea behind a live benchmark as an evolving benchmark that can be updated from current web data and re-evaluated over time.
  key_point: The paper says a live benchmark should be updated frequently, consistently, and automatically, and it uses changing arXiv content to test models on the latest version.
- source_title: SWE-bench Goes Live!
  source_url: https://arxiv.org/html/2505.23419v2
  source_type: research_paper
  relevance: Shows the term being used for a benchmark that is continuously refreshed to reduce contamination and better reflect current tasks.
  key_point: The paper describes SWE-bench-Live as a live benchmark with an automated, scalable update method and frames it as contamination-resistant.
---
Live benchmark is a benchmark that is kept up to date by adding new tasks or refreshing old ones over time.

In practice, that usually means the test does not stay frozen. New questions are taken from current sources, and old questions may be replaced or updated. The point is to make the test less easy to memorise and less likely to overlap with training data.

This matters because a static benchmark can stop being useful once models have seen it too often. A live benchmark gives a more current check on what a model can do now, not just what it learned long ago.

It is not the same as any public benchmark. It is also not just a live leaderboard. The important part is that the test itself keeps changing in a controlled way.

The term is not perfectly standard, so people sometimes use it a bit differently. But the usual meaning is a benchmark that is regularly refreshed to stay current and reduce contamination.
