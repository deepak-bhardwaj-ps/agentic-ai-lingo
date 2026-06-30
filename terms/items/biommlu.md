---
title: BioMMLU
short_description: A biomedical subset of MMLU used to test language models on medicine and biology questions.
category: Evals
tags:
  - benchmark
  - biomedical-ai
  - evals
aliases:
  - Biomedical MMLU
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating BioMMLU as a separate benchmark family instead of a biomedical slice of MMLU.
  - Assuming it covers all medical AI evaluation.
  - Using a BioMMLU score as proof that a model is safe or clinically reliable.
related_terms:
  - MMLU
  - biomedical benchmark
  - medical benchmark
  - multiple-choice benchmark
  - domain-specific benchmark
evidence:
  - source_title: Measuring Massive Multitask Language Understanding
    source_url: https://arxiv.org/abs/2009.03300
    source_type: research_paper
    relevance: This is the original MMLU paper, which BioMMLU reuses as its base benchmark.
    key_point: MMLU is a 57-task multiple-choice benchmark for measuring broad language-model knowledge and reasoning.
  - source_title: Improving Domain Adaptation through Extended-Text Reading Comprehension
    source_url: https://arxiv.org/pdf/2401.07284
    source_type: research_paper
    relevance: This paper explicitly names BioMMLU and explains how it is constructed.
    key_point: The authors describe BioMMLU as biomedicine subjects selected from MMLU for evaluating domain-specific performance.
  - source_title: MoRA: High-Rank Updating for Parameter-Efficient Fine-Tuning
    source_url: https://arxiv.org/pdf/2405.12130
    source_type: research_paper
    relevance: This later paper uses BioMMLU in biomedical evaluation, confirming the term is used as a domain-specific benchmark label in recent research.
    key_point: The paper reports BioMMLU alongside PubMedQA, USMLE, and RCT as part of biomedical task evaluation.
---
BioMMLU is a biomedical subset of MMLU.

In practice, it is used to check how well a language model answers multiple-choice questions in biomedicine, rather than across all subjects in MMLU.

The term matters because models can do well on general questions but still be weak in medicine and biology. A BioMMLU score gives a narrow view of domain knowledge in that area.

BioMMLU is not the same as all medical AI evaluation. It does not show whether a model is safe for clinical use, gives good advice, or can handle real patients. It is also not a full benchmark for every biomedical task.
