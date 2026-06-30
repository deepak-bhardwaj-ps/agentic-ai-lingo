---
title: MLE-bench
short_description: A benchmark for testing how well AI agents can do machine learning engineering tasks.
category: Evals
tags:
  - benchmark
  - evals
  - machine-learning
  - agents
status: draft
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a machine learning product or toolkit instead of a test for AI agents.
  - Assuming one score on MLE-bench proves an agent can do machine learning engineering in real life.
  - Using it as a general ML benchmark when it is focused on engineering tasks drawn from Kaggle competitions.
related_terms:
  - agentic benchmark
  - machine learning engineering
  - Kaggle benchmark
  - benchmark suite
evidence:
  - source_title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
    source_url: https://openai.com/index/mle-bench/
    source_type: official_docs
    relevance: OpenAI’s announcement is the clearest current definition from the team that introduced the term.
    key_point: OpenAI says MLE-bench measures how well AI agents perform at machine learning engineering and is built from 75 Kaggle competitions.
  - source_title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
    source_url: https://arxiv.org/abs/2410.07095
    source_type: research_paper
    relevance: The paper gives the formal research framing and explains what kinds of tasks the benchmark covers.
    key_point: The abstract describes MLE-bench as a benchmark for ML engineering tasks such as training models, preparing datasets, and running experiments.
  - source_title: openai/mle-bench
    source_url: https://github.com/openai/mle-bench
    source_type: engineering_blog
    relevance: The repository documents how the benchmark is packaged and used in practice.
    key_point: The README says the dataset is a collection of 75 Kaggle competitions used to evaluate AI systems’ ML engineering capabilities.
---
MLE-bench is a benchmark for testing how well AI agents can do machine learning engineering.

In practice, it gives an agent real competition-style tasks, mostly based on Kaggle, and checks whether it can work through them well enough to score highly. The tasks include things like preparing data, training models, and running experiments.

The term matters because machine learning engineering is more than answering questions about AI. It asks whether an agent can do the messy work of building and improving models, which is much closer to real technical work.

MLE-bench is not a machine learning product, and it is not a promise that an agent can do ML work safely in a real job. It is also not every ML benchmark. It is a specific evaluation built around Kaggle-style engineering tasks.
