---
title: HealthBench
short_description: OpenAI's benchmark for testing how well AI models handle realistic health conversations safely and clearly.
category: Evals and benchmarks
tags:
  - healthcare
  - evaluation
  - benchmark
status: active
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as a medical chatbot or product rather than a test used to judge models.
  - Thinking it measures medical knowledge alone, when it also checks safety, communication, and judgement.
related_terms:
  - healthcare benchmark
  - model evaluation
  - rubric-based evaluation
  - HealthBench Professional
  - clinical safety
evidence:
  - source_title: Introducing HealthBench
    source_url: https://openai.com/index/healthbench/
    source_type: official_docs
    relevance: Primary source from the team that introduced the benchmark.
    key_point: Says HealthBench is a benchmark for evaluating AI systems on realistic health conversations, built with physicians and scored with physician-written rubrics.
  - source_title: HealthBench: Evaluating Large Language Models Towards Improved Human Health
    source_url: https://arxiv.org/abs/2505.08775
    source_type: research_paper
    relevance: Peer-reviewed-style technical description of the benchmark design and scope.
    key_point: Describes HealthBench as an open-source benchmark with 5,000 multi-turn health conversations and rubric-based scoring by 262 physicians.
  - source_title: OpenAI for Healthcare
    source_url: https://openai.com/index/openai-for-healthcare/
    source_type: official_docs
    relevance: Confirms how OpenAI positions HealthBench in its healthcare evaluation stack.
    key_point: Explains that HealthBench measures behaviour in realistic medical scenarios, including accuracy, safety, uncertainty handling, and communication quality.
---

HealthBench is a benchmark for checking how well an AI model handles health questions and conversations.

In practice, that means people use it to test whether a model gives clear, safe, and useful answers in realistic medical situations. It is not a medical tool itself. It is a scorecard used to compare models and track improvement over time.

The term matters because health advice is high stakes. A model can sound fluent and still give a weak or unsafe answer, so a benchmark like HealthBench tries to measure more than just factual recall.

HealthBench is not the same as a real doctor, a hospital system, or a general chat benchmark. It is also not a claim that a model is medically trustworthy on its own.
