---
title: PubMedQA
short_description: A biomedical question-answering dataset and benchmark built from PubMed abstracts.
category: Evals
tags: [benchmark, dataset, biomedical-qa, medical-qa]
status: draft
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as a general medical knowledge test instead of a benchmark built from research abstracts.
  - Assuming it measures clinical diagnosis in real patients.
  - Confusing the dataset name with the broader field of biomedical question answering.
related_terms:
  - biomedical question answering
  - BioASQ
  - MedQA
  - benchmark suite
evidence:
  - source_title: PubMedQA: A Dataset for Biomedical Research Question Answering
    source_url: https://aclanthology.org/D19-1259/
    source_type: research_paper
    relevance: Original paper that defines the term and describes the dataset structure.
    key_point: PubMedQA is a biomedical QA dataset collected from PubMed abstracts, using yes/no/maybe answers and a long-answer field from the abstract conclusion.
  - source_title: PubMedQA GitHub repository
    source_url: https://github.com/pubmedqa/pubmedqa
    source_type: official_docs
    relevance: Official project repository that confirms the task format used for evaluation and submission.
    key_point: The repository shows that answers are scored as yes, no, or maybe, which makes clear that PubMedQA is a benchmark with a fixed answer format.
  - source_title: PubMedQA: A Dataset for Biomedical Research Question Answering
    source_url: https://arxiv.org/abs/1909.06146
    source_type: research_paper
    relevance: ArXiv version of the original paper, useful for the dataset summary and stated evaluation setting.
    key_point: The paper says PubMedQA is the first QA dataset where reasoning over biomedical research texts, especially quantitative contents, is required.
---
PubMedQA is a biomedical question-answering dataset and benchmark built from PubMed abstracts.

It gives a research question and a matching abstract, then asks a model to answer yes, no, or maybe.

In practice, PubMedQA checks whether a system can read a medical research abstract and use the evidence in it to reach the right answer. The abstract usually acts like the clue sheet, and the answer is meant to follow from that text.

This matters because it tests reading and reasoning over biomedical research, not just memorised facts. Teams use it to compare models on a fixed task with a fixed answer format.

It is not the same as a doctor making a real diagnosis. It is also not a broad test of all medical knowledge. PubMedQA is a specific benchmark built around PubMed abstracts and a small set of answer choices.
