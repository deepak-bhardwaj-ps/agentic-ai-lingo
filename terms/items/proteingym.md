---
title: ProteinGym
short_description: Benchmark suite for testing models that predict how protein mutations change protein function.
category: Evals
tags:
  - benchmark
  - biology
  - protein
  - evals
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating ProteinGym as a single model, tool, or dataset instead of a benchmark suite.
  - Assuming it measures all protein work, when it mainly focuses on mutation effect and protein fitness prediction.
related_terms:
  - protein fitness prediction
  - deep mutational scanning
  - mutation effect prediction
  - protein design
  - clinical variant benchmarking
evidence:
  - source_title: ProteinGym
    source_url: https://proteingym.org/
    source_type: official_docs
    relevance: The project website states the term’s current purpose in plain language.
    key_point: ProteinGym is a collection of benchmarks for comparing models that predict the effects of protein mutations.
  - source_title: GitHub - OATML-Markslab/ProteinGym
    source_url: https://github.com/OATML-Markslab/ProteinGym
    source_type: official_docs
    relevance: The repository README gives the clearest operational definition and shows what data the benchmark actually contains.
    key_point: ProteinGym combines deep mutational scanning assays and annotated human clinical variants for substitution and indel benchmarks.
  - source_title: ProteinGym: Large-Scale Benchmarks for Protein Fitness Prediction and Design
    source_url: https://papers.nips.cc/paper_files/paper/2023/hash/cac723e5ff29f65e3fcbb0739ae91bee-Abstract-Datasets_and_Benchmarks.html
    source_type: research_paper
    relevance: The NeurIPS paper is the original research description and explains the benchmark’s scope and intent.
    key_point: The paper presents ProteinGym v1.0 as a large-scale benchmark for protein fitness prediction and design, built from over 250 deep mutational scanning assays plus curated clinical datasets.
---
ProteinGym is a benchmark suite for checking how well models predict what happens when a protein changes.

In practice, it gives models the same protein mutation tasks and compares their scores under the same rules. The tasks are based on real experimental data, including deep mutational scanning assays and curated clinical variants.

It matters because protein changes can affect health, medicines, and bioengineering. A benchmark like ProteinGym helps researchers compare methods more fairly and see which ones work better on different kinds of protein mutations.

ProteinGym is not a single model and not a real-world lab test. It is also not the whole field of protein science. It is a benchmark suite for a specific job: predicting the effects of protein mutations.
