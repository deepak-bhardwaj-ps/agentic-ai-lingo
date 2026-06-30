---
title: FinanceBench
short_description: A benchmark for testing how well AI models answer finance questions using real company documents
category: Evals and benchmarks
tags: [benchmark, finance, evals, question-answering]
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
  - Treating FinanceBench as a finance app or dataset name rather than a benchmark for evaluation.
  - Assuming a strong score on FinanceBench proves an AI model is safe or reliable in real financial work.
related_terms:
  - financial question answering
  - benchmark suite
  - retrieval-augmented generation
  - SEC filings
evidence:
  - source_title: FinanceBench: A New Benchmark for Financial Question Answering
    source_url: https://arxiv.org/abs/2311.11944
    source_type: research_paper
    relevance: This is the original paper that defines the term and shows how it is used in research.
    key_point: FinanceBench is presented as a benchmark for open-book financial question answering, with 10,231 questions about public companies and evidence strings for answers.
  - source_title: patronus-ai/financebench
    source_url: https://github.com/patronus-ai/financebench
    source_type: engineering_blog
    relevance: This is the project repository for the benchmark and confirms how the dataset is packaged and described for use.
    key_point: The repository says FinanceBench is a test suite for open-book financial QA and that the open-source sample contains annotated examples, answers, and evidence.
---

FinanceBench is a benchmark for testing how well an AI model answers finance questions by using real company documents and evidence.

In practice, it gives the model questions about public companies and checks whether the answer matches the evidence. The idea is to see if the model can find and use the right facts instead of guessing.

It matters because finance work depends on exact details. A benchmark like this helps people compare models in a fair way and spot mistakes such as wrong numbers, made-up answers, or missed evidence.

FinanceBench is not a finance product, and it is not proof that a model is safe to use in real investing, reporting, or compliance work. It is also not the same as every finance benchmark, because it focuses on open-book question answering with supporting evidence.
