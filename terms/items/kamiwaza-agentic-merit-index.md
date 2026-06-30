---
title: Kamiwaza Agentic Merit Index
short_description: Kamiwaza’s benchmark and leaderboard for testing how well AI agents handle enterprise-style tasks.
category: Evals
tags:
  - benchmark
  - leaderboard
  - agentic-ai
  - evaluation
status: draft
aliases:
  - KAMI
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general score for all AI models, rather than a benchmark for specific agent-style tasks.
  - Assuming a high score means a model will work well in every real-world setting.
  - Confusing the benchmark itself with the leaderboard page that shows results.
related_terms:
  - agentic benchmark
  - model evaluation
  - benchmark contamination
  - leaderboard
  - tool use
evidence:
  - source_title: Agentic Merit Index | Kamiwaza Docs
    source_url: https://docs.kamiwaza.ai/research/agentic-merit-index
    source_type: official_docs
    relevance: This is Kamiwaza’s own definition of the term and shows that it is also used as the name of a public leaderboard.
    key_point: Kamiwaza says the Agentic Merit Index is “the definitive leaderboard for enterprise agentic AI performance,” powered by the KAMI benchmark.
  - source_title: KAMI v0.1: Enterprise-Relevant Agentic AI Benchmark
    source_url: https://docs.kamiwaza.ai/research/papers/kami-v0-1
    source_type: official_docs
    relevance: This explains what the benchmark measures and why it exists.
    key_point: Kamiwaza describes KAMI v0.1 as an enterprise-focused benchmark for agentic evaluation and contamination resistance, aimed at tasks like multi-step tool use and decision-making under uncertainty.
  - source_title: Testing What Models Can Do, Not What They've Seen: PICARD
    source_url: https://docs.kamiwaza.ai/research/papers/picard
    source_type: official_docs
    relevance: This shows the evaluation method behind the benchmark family and why randomised tests matter.
    key_point: Kamiwaza says PICARD generates unique, randomised test instances to reduce memorisation and better measure genuine agentic capability.
  - source_title: Benchmark Data Contamination of Large Language Models: A Survey
    source_url: https://arxiv.org/html/2406.04244v1
    source_type: research_paper
    relevance: This supports the need for contamination-resistant benchmarks in modern model evaluation.
    key_point: The survey explains that benchmark contamination can make evaluation scores unreliable, which is one of the problems KAMI says it is trying to avoid.
---
Kamiwaza Agentic Merit Index is a benchmark and leaderboard for checking how well AI agents do on enterprise-style tasks.

In practice, it is used to test models on work that needs several steps, tool use, and decisions made with incomplete information. Kamiwaza says the benchmark is designed to be harder to game by memorisation, so it tries to measure what a model can really do.

It matters because a model can score well on ordinary tests and still perform badly when it has to carry out real tasks such as file handling, database work, or other multi-step jobs. KAMI is meant to help people compare models for that kind of work.

It is not a general “IQ score” for AI. It does not prove a model is best at every task, and it should not be treated as a universal measure of intelligence.
