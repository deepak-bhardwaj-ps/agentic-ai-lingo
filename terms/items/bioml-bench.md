---
title: BioML-bench
short_description: A benchmark suite for testing AI agents on end-to-end biomedical machine learning tasks.
category: Evals
tags:
  - biomedical-ai
  - benchmark
  - evals
  - agent-evaluation
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general term for biomedical machine learning instead of a specific benchmark suite.
  - Assuming it is a medical diagnosis tool rather than a way to measure agent performance.
related_terms:
  - MLE-bench
  - biomedical machine learning
  - AI agent benchmark
  - bioinformatics benchmark
evidence:
  - source_title: BioML-bench repository README
    source_url: https://github.com/science-machine/biomlbench
    source_type: official_docs
    relevance: The project’s own README states what BioML-bench is, what tasks it covers, and that it is still a pre-release version.
    key_point: BioML-bench is a benchmark suite for biomedical machine learning tasks and is built on top of MLE-bench.
  - source_title: BioML-bench: Evaluation of AI Agents for End-to-End Biomedical ML
    source_url: https://www.biorxiv.org/content/10.1101/2025.09.01.673319v2
    source_type: research_paper
    relevance: The paper is the main research description of the benchmark and defines the scope more precisely than secondary summaries.
    key_point: It presents BioML-bench as a benchmark for evaluating AI agents on end-to-end biomedical ML tasks across multiple domains.
  - source_title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
    source_url: https://arxiv.org/abs/2410.07095
    source_type: research_paper
    relevance: BioML-bench is explicitly described as being built on top of MLE-bench, so this paper explains the benchmark lineage and evaluation style.
    key_point: MLE-bench is a benchmark for measuring how well AI agents perform at machine learning engineering, which BioML-bench adapts for biomedicine.
---
BioML-bench is a benchmark suite for checking how well AI agents can do end-to-end biomedical machine learning tasks.

In practice, it gives an agent a biomedical task, a dataset, and rules for producing a result. The agent has to work through the problem, build a solution, and be scored against a standard.

The term matters because it helps compare different agents on the same kinds of biology and health-data problems. It is meant for evaluation, not for making medical decisions.

BioML-bench is not the same thing as biomedical machine learning in general. It is also not a drug, a diagnosis system, or a single dataset. It is a test suite used to measure performance.
