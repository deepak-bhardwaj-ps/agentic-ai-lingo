---
title: MedQBench
short_description: A benchmark for testing how well multimodal AI can judge medical image quality
category: Evals and benchmarks
tags: [benchmark, medical-ai, multimodal]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general medical question-answering benchmark.
  - Assuming a score on MedQBench means an AI is safe for clinical use.
  - Confusing it with ordinary image-classification tests that do not ask for reasoning about image quality.
related_terms:
  - Medical image quality assessment
  - Multimodal large language model
  - Benchmark
  - Medical imaging
  - Evaluation
evidence:
  - source_title: MedQ-Bench: Evaluating and Exploring Medical Image Quality Assessment Abilities in MLLMs
    source_url: https://arxiv.org/abs/2510.01691
    source_type: research_paper
    relevance: This is the main paper defining the benchmark and its purpose.
    key_point: The paper says MedQ-Bench evaluates medical image quality assessment abilities in multimodal large language models and uses perception and reasoning tasks.
  - source_title: liujiyaoFDU/MedQ-Bench
    source_url: https://github.com/liujiyaoFDU/MedQ-Bench
    source_type: engineering_blog
    relevance: The project repository gives the clearest practical summary of what the benchmark contains and how it is used.
    key_point: The README describes MedQ-Bench as a benchmark for medical image quality assessment and says it covers multiple modalities, quality attributes, and reasoning tasks.
  - source_title: jiyaoliufd/MedQ-Bench Dataset Card
    source_url: https://huggingface.co/datasets/jiyaoliufd/MedQ-Bench
    source_type: official_docs
    relevance: The dataset card confirms the benchmark structure and the kinds of tasks included.
    key_point: The dataset page lists 3,308 medical images, five imaging types, and two task families: perception questions and reasoning assessments.
---

MedQBench is a benchmark for checking how well an AI can judge the quality of medical images.

In practice, it asks a multimodal AI system to look at medical images such as CT, MRI, or endoscopy images and answer questions about how clear, usable, or damaged the image is. Some tasks ask simple questions. Others ask the AI to explain its judgement or compare two images.

This matters because medical images need to be good enough for doctors to trust them. A model that misses blur, noise, or other image problems could give a bad answer.

MedQBench is not a general test of medical knowledge. It is also not proof that an AI system is safe to use in real clinics. It mainly measures image quality judgement, not diagnosis.
