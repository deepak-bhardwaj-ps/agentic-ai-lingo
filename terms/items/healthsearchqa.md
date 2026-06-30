---
title: HealthSearchQA
short_description: Google’s dataset of commonly searched consumer health questions used in the MultiMedQA benchmark.
category: Evals and benchmarks
tags:
- medical QA
- health benchmarks
- consumer health questions
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating it as a general medical QA term instead of a specific benchmark dataset.
- Assuming it is a clinical diagnosis dataset; it is about consumer health questions, not patient records or doctor notes.
related_terms:
- MultiMedQA
- consumer health question answering
- medical question answering
- LiveQA
- MedicationQA
evidence:
- source_title: Large language models encode clinical knowledge
  source_url: https://www.nature.com/articles/s41586-023-06291-2
  source_type: research_paper
  relevance: Primary publication that defines HealthSearchQA and explains how it fits into the MultiMedQA benchmark.
  key_point: Google introduced HealthSearchQA as a new dataset of 3,173 commonly searched consumer medical questions, curated from search-engine suggestions seeded by medical conditions and symptoms.
- source_title: Large Language Models Encode Clinical Knowledge
  source_url: https://research.google/pubs/large-language-models-encode-clinical-knowledge/
  source_type: official_docs
  relevance: Google Research summary of the same paper, useful for confirming the dataset's purpose and benchmark role.
  key_point: HealthSearchQA is presented as a new dataset of medical questions searched online and used with MultiMedQA to evaluate clinical knowledge and question-answering ability.
- source_title: HealthSearchQA dataset card
  source_url: https://huggingface.co/datasets/katielink/healthsearchqa
  source_type: industry_article
  relevance: Dataset listing that restates the paper's description and confirms the question-only, open-domain format.
  key_point: The dataset contains commonly searched consumer health questions and is formatted as question-only, free-text, open-domain examples.
---

HealthSearchQA is a dataset of commonly searched consumer health questions.

In practice, it is used to test whether a language model can answer everyday health questions that people search for online, such as questions about symptoms, causes, or whether something is serious.

It matters because consumer health questions are different from exam questions. They are often vague, worried, and written in plain language, so a model has to understand what the person really means and answer carefully.

It is not a general term for all health question answering. It is also not the same as clinical records, doctor notes, or diagnosis tasks. It names one specific benchmark dataset used in research.
