---
title: Drug discovery benchmark
short_description: A fixed test used to compare AI or machine learning methods on drug-discovery tasks.
category: Evals and benchmarks
tags: [drug-discovery, benchmark, evals, chemistry, molecules]
status: draft
aliases: []
meaning_type: overloaded_buzzword
novelty_level: low
maturity_level: established
common_misuse:
  - Treating one benchmark score as proof that a model will find a real medicine
  - Calling any chemistry dataset a drug discovery benchmark, even when it was not built for fair comparison
  - Ignoring how the task split, metric, or dataset choice can make results look better than they really are
related_terms:
  - molecular property prediction benchmark
  - ADMET benchmark
  - virtual screening
  - hit identification
  - lead optimisation
  - molecular benchmark
evidence:
  - source_title: MoleculeNet: a benchmark for molecular machine learning
    source_url: https://pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc02664a
    source_type: research_paper
    relevance: Foundational benchmark paper for molecular machine learning, which is a core part of drug discovery benchmarking.
    key_point: MoleculeNet was built to provide a standard platform for comparing models on molecular tasks, with shared datasets, metrics, and splits.
  - source_title: Therapeutics Data Commons
    source_url: https://tdcommons.ai/
    source_type: official_docs
    relevance: Shows the modern broader meaning of drug-discovery benchmarking across many therapeutic tasks, not just one dataset.
    key_point: TDC curates datasets, tasks, benchmarks, metrics, and public leaderboards for therapeutic science.
  - source_title: Lo-Hi: Practical ML Drug Discovery Benchmark
    source_url: https://openreview.net/forum?id=H2Yb28qGLV
    source_type: research_paper
    relevance: Shows that newer drug-discovery benchmarks are trying to better match real discovery work and that older benchmarks can be unrealistic.
    key_point: The paper argues that common benchmarks may be too far from real drug-discovery practice and introduces tasks for hit identification and lead optimisation.
  - source_title: WelQrate: Defining the Gold Standard in Small Molecule Drug Discovery Benchmarking
    source_url: https://openreview.net/forum?id=IjiIPQcLbV
    source_type: research_paper
    relevance: Shows that the field still debates what a good benchmark should look like, which is why the term is broad and uneven.
    key_point: The paper proposes a new benchmark standard because current benchmarking practice is still seen as incomplete for small-molecule drug discovery.
---

A drug discovery benchmark is a fixed test used to compare how well models help with parts of finding and improving medicines.

In practice, it usually means a curated dataset, a scoring rule, and a shared test setup so different methods can be judged fairly. The task might ask a model to predict a molecule property, find promising compounds, or estimate safety.

This matters because drug discovery is slow and expensive. Benchmarks let researchers check ideas before they spend time and money on lab work.

A drug discovery benchmark is not the same as a real drug trial. A strong score does not mean the model will find a working medicine in people.

The term is broad. There is no single drug discovery benchmark, so the exact meaning depends on which task or dataset is being named.
