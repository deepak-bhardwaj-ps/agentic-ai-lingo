---
title: MedHALT
short_description: A benchmark for testing whether medical AI models make confident but wrong claims.
category: Evals and benchmarks
tags: [benchmark, medical-ai, hallucination, evaluation]
status: active
aliases: [Med-HALT, Medical Domain Hallucination Test]
meaning_type: novel
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating MedHALT as a real medical assistant or diagnosis tool.
  - Assuming it measures every kind of clinical safety problem.
  - Using it as a general medical benchmark when it is focused on hallucination.
related_terms:
  - hallucination
  - medical AI
  - benchmark
  - clinical safety
evidence:
  - source_title: Med-HALT: Medical Domain Hallucination Test for Large Language Models
    source_url: https://aclanthology.org/2023.conll-1.21/
    source_type: research_paper
    relevance: This is the original paper that introduced the term and defines what the benchmark is for.
    key_point: The paper presents Med-HALT as a benchmark and dataset for measuring hallucinations in medical-domain language models.
  - source_title: Med-HALT project site
    source_url: https://medhalt.github.io/
    source_type: official_docs
    relevance: This is the project’s own description and confirms the benchmark naming and purpose.
    key_point: The site describes Med-HALT as a benchmark dataset for testing hallucination in the medical domain.
  - source_title: A framework to assess clinical safety and hallucination rates of LLMs in healthcare
    source_url: https://www.nature.com/articles/s41746-025-01670-7
    source_type: research_paper
    relevance: This later medical-AI paper shows how the term is understood in current clinical-evaluation work and notes its limits.
    key_point: The paper says MedHALT is limited to reasoning questions in a QA format, which helps distinguish it from broader clinical safety evaluation.
---

MedHALT is a benchmark for checking whether a medical AI model says things that sound confident but are wrong.

In practice, MedHALT is used to test how well a model handles medical questions without making up facts. It looks at hallucinations, which means answers that sound plausible but are not supported by evidence.

This matters because medical mistakes can be harmful. A benchmark like MedHALT helps researchers compare models and spot weak points before a system is used in a health setting.

MedHALT is not a doctor, a diagnosis tool, or proof that a medical AI system is safe. It is also not a full test of every clinical risk. It mainly checks hallucination in a question-and-answer setting.
