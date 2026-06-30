---
title: GraphArena
short_description: A benchmark for testing large language models on graph problems.
category: Evals and benchmarks
tags:
  - benchmark
  - evals
  - graph-reasoning
  - large-language-models
status: draft
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating GraphArena as a general AI score instead of a benchmark for graph computation.
  - Assuming a good result means the model can solve all graph problems well.
  - Confusing it with graph databases, knowledge graphs, or graph visualisation tools.
related_terms:
  - graph reasoning
  - graph benchmark
  - large language model evaluation
  - algorithmic reasoning
  - benchmark dataset
evidence:
  - source_title: GraphArena: Evaluating and Exploring Large Language Models on Graph Computation
    source_url: https://arxiv.org/abs/2407.00379
    source_type: research_paper
    relevance: Original paper that defines GraphArena and explains what kinds of graph tasks it measures.
    key_point: GraphArena is a benchmark for real-world graph computation, including polynomial-time tasks and NP-complete challenges, used to test LLM reasoning on graphs.
  - source_title: GraphArena: Evaluating and Exploring Large Language Models on Graph Computation
    source_url: https://openreview.net/forum?id=Y1r9yCMzeA
    source_type: standards_doc
    relevance: Formal conference record that confirms the name, framing, and evaluation purpose of the benchmark.
    key_point: The OpenReview listing presents GraphArena as a comprehensive benchmark for assessing and improving LLM reasoning on graph computational problems.
  - source_title: squareRoot3/GraphArena
    source_url: https://github.com/squareRoot3/GraphArena
    source_type: engineering_blog
    relevance: Official repository showing the released benchmark code, tasks, and evaluation workflow.
    key_point: The repository documents GraphArena as the official implementation of the paper and lists the graph tasks and benchmarking scripts used to run evaluations.
---

GraphArena is a benchmark for testing large language models on graph problems.

In practice, it gives a model graph tasks to solve, such as finding shortest paths or handling harder graph problems where the answer is not easy to compute.

It matters because graph problems check more than word guessing. They test whether a model can follow links, search carefully, and avoid making up answers.

GraphArena is not a graph database, a knowledge graph, or a general AI score. It is a specific test suite for graph computation and graph reasoning in language models.
