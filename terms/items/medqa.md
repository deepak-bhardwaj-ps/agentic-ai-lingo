---
title: MedQA
short_description: A medical question-answering benchmark built from professional board-exam questions.
category: Evals
tags:
- medical
- question-answering
- benchmark
- evaluation
status: draft
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating MedQA as any medical Q&A system or any medical QA dataset.
- Confusing it with PubMedQA or MedMCQA, which are different benchmarks built from different sources.
related_terms:
- PubMedQA
- MedMCQA
- medical benchmark
- multiple-choice question answering
evidence:
- source_title: What Disease does this Patient Have? A Large-scale Open Domain Question Answering Dataset from Medical Exams
  source_url: https://arxiv.org/abs/2009.13081
  source_type: research_paper
  relevance: Original paper that introduced MedQA and defined the benchmark.
  key_point: MedQA is presented as a free-form multiple-choice open-domain QA dataset collected from professional medical board exams, with English, simplified Chinese, and traditional Chinese versions.
- source_title: jind11/MedQA
  source_url: https://github.com/jind11/MedQA
  source_type: engineering_blog
  relevance: Official repository for the dataset and baseline code.
  key_point: Confirms that MedQA is the code and data release for the paper and that the dataset includes US, Mainland China, and Taiwan question sets plus an official train/dev/test split.
- source_title: MedQA: Medical exam Q&A benchmark
  source_url: https://github.com/UKGovernmentBEIS/inspect_evals
  source_type: official_docs
  relevance: Shows how MedQA is used today in an evaluation harness.
  key_point: Describes MedQA as a Q&A benchmark with questions collected from professional medical board exams and notes that the Inspect eval uses only the English subset.
---
MedQA is a benchmark for asking and scoring answers to medical exam questions.

It was built from real professional medical board-exam questions. In practice, people use it to test whether a model can answer medical multiple-choice questions and do basic medical reasoning.

It matters because medical questions are hard and often need careful reasoning, not just memorising facts. A strong score on MedQA suggests a model can handle some exam-style medical knowledge, but it does not mean the model is safe to use for real medical advice.

MedQA is not a doctor, a clinical decision tool, or a general medical chat system. It is a test set used to measure performance. It is also not the same thing as PubMedQA or MedMCQA, which are separate medical QA benchmarks with different source material.
