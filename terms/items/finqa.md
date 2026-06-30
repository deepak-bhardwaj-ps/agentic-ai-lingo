---
title: FinQA
short_description: A benchmark dataset for testing numerical reasoning over financial reports
category: Evals
tags: [benchmark, finance, evals, question-answering, numerical-reasoning]
status: active
aliases: [FINQA]
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating FinQA as a general finance app, model, or product instead of a benchmark dataset.
  - Assuming it covers all kinds of financial questions, when it is mainly about numerical reasoning over reports.
  - Assuming a strong score on FinQA means a model is ready for real financial work.
related_terms:
  - financial question answering
  - numerical reasoning
  - benchmark dataset
  - financial reports
  - ConvFinQA
  - DocFinQA
evidence:
  - source_title: FinQA
    source_url: https://finqasite.github.io/
    source_type: official_docs
    relevance: This is the project site for the benchmark and gives the clearest plain-language description of what FinQA is.
    key_point: The site says FinQA is a large-scale dataset with 2.8k financial reports and 8k question-answer pairs for studying numerical reasoning with structured and unstructured evidence.
  - source_title: FinQA: A Dataset of Numerical Reasoning over Financial Data
    source_url: https://aclanthology.org/2021.emnlp-main.300/
    source_type: research_paper
    relevance: This is the original paper that defines the dataset and explains the task it was built to study.
    key_point: The paper describes FinQA as a new large-scale dataset with question-answer pairs over financial reports, written by financial experts, with gold reasoning programs for explainability.
  - source_title: FinQA GitHub repository
    source_url: https://github.com/czyssrs/FinQA
    source_type: engineering_blog
    relevance: This repository confirms how the benchmark is packaged and named for reuse by other researchers.
    key_point: The repository identifies FinQA as the dataset and code for the EMNLP 2021 paper, reinforcing that it is a research benchmark rather than a product.
---
FinQA is a benchmark dataset for testing how well a model can answer questions that need number handling from financial reports.

In practice, FinQA gives a model questions about financial documents and checks whether it can work out the answer from the evidence. The questions are not just about reading words. They often need the model to add, subtract, compare, or combine numbers from tables and text.

It matters because financial reports are full of details that must be handled exactly. FinQA helps researchers see whether a model can do that kind of reasoning instead of guessing or making up an answer.

FinQA is not a finance app, and it is not proof that a model is safe for real investment, accounting, or compliance work. It is also not the same as every financial question-answering benchmark, because it focuses on numerical reasoning over reports with supporting evidence.
