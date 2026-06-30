---
title: FinBen
short_description: A finance benchmark for evaluating large language models across many financial tasks
category: Evals and benchmarks
tags:
  - benchmark
  - finance
  - evals
  - llm
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating FinBen as a finance app, model, or dataset rather than a benchmark for evaluation.
  - Assuming a good score on FinBen means an AI system is safe for real financial work.
  - Confusing FinBen with narrower finance question-answering benchmarks.
related_terms:
  - finance benchmark
  - financial question answering
  - stock trading evaluation
  - retrieval-augmented generation
evidence:
  - source_title: FinBen: A Holistic Financial Benchmark for Large Language Models
    source_url: https://arxiv.org/abs/2402.12659
    source_type: research_paper
    relevance: This is the original paper that introduces FinBen and defines its scope.
    key_point: FinBen is presented as an open-source benchmark covering 36 datasets and 24 financial tasks, including information extraction, question answering, forecasting, and decision-making.
  - source_title: The-FinAI/FinBen
    source_url: https://github.com/The-FinAI/FinBen
    source_type: official_docs
    relevance: This is the project repository maintained for the benchmark and confirms how the authors describe it in practice.
    key_point: The repository describes FinBen as a comprehensive benchmark suite for evaluating large language models in financial contexts.
  - source_title: FinBen: a holistic financial benchmark for large language models
    source_url: https://dl.acm.org/doi/10.5555/3737916.3740949
    source_type: research_paper
    relevance: This later publication record helps confirm that FinBen is a formal benchmark name, not a casual nickname.
    key_point: The paper record shows FinBen as a benchmark spanning 24 financial tasks, which supports the term as a broad finance evaluation suite.
---

FinBen is a benchmark for testing how well a large language model handles financial tasks.

In practice, it gives models many finance-related tasks, such as reading financial text, answering questions, doing calculations, and reasoning about risk or decisions. Researchers use it to compare models in a fair way.

It matters because finance work needs accurate facts, careful number handling, and sensible judgement. A benchmark like FinBen helps show where a model is useful and where it still makes mistakes.

FinBen is not a finance product, and it is not proof that a model is safe to use with money. It is also not just one small quiz about finance. It is a broad evaluation suite, so people should not treat it as the final word on financial ability.
