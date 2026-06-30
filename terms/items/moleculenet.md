---
title: MoleculeNet
short_description: A benchmark suite for comparing machine learning methods on molecular tasks.
category: Evals and benchmarks
tags: [drug-discovery, benchmark, chemistry, molecules, deepchem]
status: draft
aliases: []
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
  - Treating MoleculeNet as one single dataset instead of a suite of datasets and tasks
  - Assuming a strong score on MoleculeNet means a model will work well in real drug discovery
  - Using the name for any chemistry dataset, even if it was not part of the MoleculeNet suite
related_terms:
  - drug discovery benchmark
  - molecular machine learning
  - molecular property prediction
  - benchmark suite
  - DeepChem
evidence:
  - source_title: MoleculeNet: a benchmark for molecular machine learning
    source_url: https://pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc02664a
    source_type: research_paper
    relevance: This is the original paper that defined MoleculeNet and explains what the benchmark suite is for.
    key_point: The paper says MoleculeNet is a large-scale benchmark for molecular machine learning that curates public datasets, evaluation metrics, and standard implementations.
  - source_title: MoleculeNet documentation in DeepChem
    source_url: https://deepchem.readthedocs.io/en/latest/api_reference/moleculenet.html
    source_type: official_docs
    relevance: This is the main software documentation for the suite and shows how the benchmark is organised in practice.
    key_point: DeepChem describes MoleculeNet as a curated collection of datasets loaded into convenient dataset objects for training and benchmarking.
  - source_title: MoleculeNet dataset documentation in PyTorch Geometric
    source_url: https://pytorch-geometric.readthedocs.io/en/2.6.1/generated/torch_geometric.datasets.MoleculeNet.html
    source_type: official_docs
    relevance: Confirms that the name is still used today as a benchmark collection and shows its scope across molecular tasks.
    key_point: PyTorch Geometric calls MoleculeNet a benchmark collection from the paper and says it covers datasets from physical chemistry, biophysics, and physiology.
---

MoleculeNet is a benchmark suite for testing machine learning models on molecular tasks.

In practice, that means it is a grouped set of datasets and scoring rules that researchers use to compare different models in a fairer way. The tasks usually involve molecules, such as predicting a property of a molecule or judging how it might behave.

It matters because chemical research is slow and expensive. A shared benchmark helps scientists see whether one method is better than another before they spend time on lab work.

MoleculeNet is not one single dataset, and it is not proof that a model will discover a real medicine. It is a test set for comparison, not a final answer about real-world drug success.
