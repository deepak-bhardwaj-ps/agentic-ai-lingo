---
title: MedBench
short_description: A Chinese medical benchmark and open evaluation platform for testing medical large language models
category: Evals
tags: [benchmark, medical-ai, medical-llm, evals]
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating MedBench as a generic name for any medical benchmark.
  - Confusing it with unrelated projects that use the same name in other languages or regions.
  - Assuming a high score on MedBench proves a model is safe for real clinical use.
related_terms:
  - Medical benchmark
  - Clinical benchmark
  - Biomedical benchmark
  - Large language model benchmark
  - Evaluation platform
evidence:
  - source_title: MedBench: A Large-Scale Chinese Benchmark for Evaluating Medical Large Language Models
    source_url: https://arxiv.org/abs/2312.12806
    source_type: research_paper
    relevance: This is the original paper that introduced MedBench and shows the term’s first clear meaning.
    key_point: The paper defines MedBench as a comprehensive benchmark for the Chinese medical domain, built from exam questions and real clinic cases to test medical knowledge and reasoning.
  - source_title: MedBench: A Comprehensive, Standardized, and Reliable Benchmarking System for Evaluating Chinese Medical Large Language Models
    source_url: https://arxiv.org/abs/2407.10990
    source_type: research_paper
    relevance: This later paper shows the term being used as an updated benchmarking system, not just a single dataset.
    key_point: The paper says MedBench is a standardised, automated benchmarking system for Chinese medical large language models, with a much larger question set and dynamic evaluation.
  - source_title: MedBench
    source_url: https://medbench.opencompass.org.cn/home
    source_type: official_docs
    relevance: The current project site shows how MedBench is presented today and confirms it is still an active evaluation platform.
    key_point: The site describes MedBench as a scientific, fair, rigorous Chinese medical model evaluation system and open platform for real medical scenarios.
---
MedBench is a Chinese medical benchmark and open evaluation platform for testing medical language models.

In practice, it gives models a set of medical questions and tasks to answer under the same rules. The goal is to see how well a model understands medical language, medical facts, reasoning, and safety-related cases.

This matters because a medical model can sound confident and still be wrong. A benchmark like MedBench helps people compare models more fairly and spot weak areas before the model is used in serious settings.

MedBench is not the same as proof that a model is safe for patients. It is also not a general name for every medical benchmark. In the sources, it refers to a specific Chinese benchmark and evaluation platform, and the term has changed a little as the project has grown.
