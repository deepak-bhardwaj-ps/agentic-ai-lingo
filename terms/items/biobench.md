---
title: BioBench
short_description: 'A benchmark suite for evaluating computer vision models on biology and ecology image tasks.'
category: Evals and benchmarks
tags:
  - biology
  - ecology
  - computer-vision
  - benchmark
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating BioBench as a general biology or biomedical benchmark rather than a specific computer vision benchmark for ecology-related image tasks.
  - Confusing it with other similarly named biology benchmarks, especially ones for language models or bioinformatics.
related_terms:
  - benchmark-suite
  - computer-vision-benchmark
  - ecology-ai
  - scientific-ml-benchmark
  - image-classification
evidence:
  - source_title: BioBench Leaderboard
    source_url: https://imageomics.github.io/biobench/
    source_type: official_docs
    relevance: The project site states the benchmark measures ecology tasks and gives the current task count, modalities, and scoring setup.
    key_point: BioBench is presented as 9 field tasks across 6 imaging modalities, using frozen backbones and simple classifiers with macro-F1 scoring.
  - source_title: Imageomics/biobench README
    source_url: https://github.com/Imageomics/biobench
    source_type: official_docs
    relevance: The repository README defines the scope and explains what kinds of models and tasks the benchmark is meant to compare.
    key_point: BioBench is described as a biology-related computer vision benchmark built to evaluate models, add tasks, and compare meaningful performance differences.
  - source_title: BioBench: A Blueprint to Move Beyond ImageNet for Scientific ML Benchmarks
    source_url: https://ar5iv.org/abs/2511.16315
    source_type: research_paper
    relevance: The paper explains why the benchmark exists and what problem it is trying to solve in scientific computer vision.
    key_point: BioBench is an ecology vision benchmark designed to measure performance on real scientific images where ImageNet-style scores stop predicting downstream usefulness.
---

BioBench is a benchmark suite for testing computer vision models on biology and ecology image tasks.

In practice, it gives a set of real-looking image tasks and checks how well a model handles them. The benchmark is mainly about ecological images such as camera-trap photos, microscope images, specimen photos, drone footage, and other scientific pictures.

It matters because a model that does well on everyday web photos does not always do well on scientific images. BioBench helps researchers see whether a model is actually useful for biology work, not just good at standard image tests.

BioBench is not a general biology exam, a medical benchmark, or a language-model benchmark. It is specifically a computer vision benchmark for ecology-related tasks.
