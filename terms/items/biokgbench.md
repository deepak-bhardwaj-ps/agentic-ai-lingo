---
title: BioKGBench
short_description: A benchmark for testing biomedical AI agents on knowledge graph checking and literature-backed claim verification.
category: Evals and benchmarks
tags:
  - benchmark
  - evals
  - biomedical-ai
  - knowledge-graph
  - agentic-ai
status: draft
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating BioKGBench as a general biomedical AI score instead of a specific test for knowledge graph checking.
  - Assuming a strong BioKGBench result proves an agent is safe or accurate in real medical use.
  - Confusing the benchmark with the knowledge graph itself or with general question-answering benchmarks.
related_terms:
  - biomedical benchmark
  - knowledge graph
  - knowledge graph question answering
  - scientific claim verification
  - agent benchmark
evidence:
  - source_title: BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science
    source_url: https://arxiv.org/abs/2407.00466
    source_type: research_paper
    relevance: Original paper that defines the benchmark and explains the tasks it was built to measure.
    key_point: The paper introduces BioKGBench to evaluate biomedical agents on literature understanding and structured knowledge-graph checking through KGQA and scientific claim verification.
  - source_title: westlake-autolab/BioKGBench
    source_url: https://github.com/westlake-autolab/BioKGBench
    source_type: engineering_blog
    relevance: Official project repository showing how the benchmark is packaged and what components it contains.
    key_point: The repository describes BioKGBench as an open-source agent evaluation project and documents its KGCheck, KGQA, and SCV parts.
  - source_title: BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science
    source_url: https://openreview.net/forum?id=I1MKOjNVup
    source_type: standards_doc
    relevance: Conference record for the same benchmark, useful for confirming the formal name and framing.
    key_point: The OpenReview listing identifies BioKGBench as a benchmark for biomedical knowledge graph checking, reinforcing that it is a formal evaluation task rather than a generic term.
---

BioKGBench is a benchmark for testing biomedical AI agents on knowledge graph checking.

In practice, it checks whether an AI can read scientific text, answer questions about a knowledge graph, and spot mistakes in biomedical facts.

This matters because a biomedical AI can sound convincing and still be wrong. A benchmark like this helps people measure whether the system can verify claims instead of just repeating them.

BioKGBench is not a medical tool or proof that an AI is safe to use in hospitals. It is also not the same as a general chatbot test. It is a specific benchmark for biomedical literature and knowledge graph checking.
