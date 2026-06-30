---
title: MD-Bench
short_description: A synthetic benchmark for testing multi-document reasoning in language models
category: Evals and benchmarks
tags: [benchmark, evals, reasoning, long-context, documents]
status: draft
aliases: [MDBench]
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a benchmark for all “MD” tasks. In this term, MD means multi-document reasoning.
  - Assuming a good score means a model can do real research well in any setting.
  - Confusing MD-Bench with unrelated tools or benchmarks that happen to use the same letters.
related_terms:
  - Multi-document reasoning
  - Long-context benchmark
  - Question answering
  - Benchmark suite
  - Synthetic benchmark
evidence:
  - source_title: MDBench: A Synthetic Multi-Document Reasoning Benchmark Generated with Knowledge Guidance
    source_url: https://aclanthology.org/2025.findings-acl.1312/
    source_type: research_paper
    relevance: Original paper that introduces the benchmark and states exactly what it is for.
    key_point: The paper defines MDBench as a new dataset for evaluating large language models on multi-document reasoning, built with synthetic generation to create challenging question-answer examples.
  - source_title: jpeper/MDBench
    source_url: https://github.com/jpeper/MDBench
    source_type: engineering_blog
    relevance: Official repository for the benchmark, useful for confirming the project name and how it is packaged.
    key_point: The repository describes MDBench as a multi-document reasoning benchmark generated with knowledge-guided prompting, which confirms that the term refers to a specific benchmark suite rather than a general idea.
  - source_title: MDBench: A Synthetic Multi-Document Reasoning Benchmark Generated with Knowledge Guidance
    source_url: https://arxiv.org/abs/2506.14927
    source_type: research_paper
    relevance: Preprint version of the same work, useful as a second independent record of the benchmark’s purpose and scope.
    key_point: The abstract says MDBench evaluates models on multi-document reasoning and exists because this kind of benchmark is hard to build with hand annotation.
---

MD-Bench is a benchmark for testing how well a language model can reason across more than one document.

In practice, the benchmark gives a model several related documents and asks questions that need information from more than one of them. It is meant to check whether the model can pull details together, follow links between documents, and answer correctly after reading a set of texts.

This matters because some tasks are easy in a single short passage but much harder when the answer is spread across multiple documents. MD-Bench helps researchers see whether a model can handle that kind of reasoning instead of only answering from one source.

MD-Bench is not a general test of intelligence, and it is not the same as doing real research in the wild. It is also not a benchmark for every meaning of “MD”; in this term, MD stands for multi-document. The benchmark is useful, but a strong score does not prove the model will always reason well outside the test.
