---
title: Risk benchmark
short_description: A benchmark that measures how risky an AI system’s behaviour is in a given situation.
category: Evals and benchmarks
tags:
  - benchmark
  - safety
  - risk
  - evals
status: active
aliases:
  - AI risk benchmark
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general performance score instead of a safety or harm-focused test
  - Assuming one risk benchmark covers every danger, setting, or user group
  - Using it to mean any benchmark with a scary-sounding name
related_terms:
  - AI risk
  - AI safety
  - safety benchmark
  - benchmark
  - red teaming
  - evaluation
evidence:
  - source_title: Framing Risk - AIRC - NIST AI Resource Center
    source_url: https://airc.nist.gov/airmf-resources/airmf/1-sec-risk/
    source_type: standards_doc
    relevance: This gives the base meaning of risk in NIST’s AI guidance, which is the right starting point for any benchmark that claims to measure risk.
    key_point: NIST defines risk as the combination of how likely something is and how serious the consequence would be.
  - source_title: AIR-Bench - Holistic Evaluation of Language Models (HELM)
    source_url: https://crfm.stanford.edu/helm/air-bench/v1.0.0/
    source_type: official_docs
    relevance: This is a current, explicit example of a risk benchmark in AI safety, showing the term used for prompt sets organised around risk categories.
    key_point: AIR-Bench aligns prompts with risk categories drawn from regulations and company policies, so it measures safety risk rather than ordinary task accuracy.
  - source_title: The Assessing Risks and Impacts of AI (ARIA) Program Companion Document
    source_url: https://ai-challenges.nist.gov/aria/docs/ARIA_Program_Companion_Document_Dec20.pdf
    source_type: standards_doc
    relevance: This explains why risk measurement needs scenarios and field-style testing, which supports the idea that risk benchmarks look beyond simple accuracy.
    key_point: NIST says AI risk measurement needs evidence about whether risks actually happen in realistic conditions and what impacts they cause.
  - source_title: Risk Management for Mitigating Benchmark Failure Modes: BenchRisk
    source_url: https://arxiv.org/abs/2510.21460
    source_type: research_paper
    relevance: This shows a newer, different use of “risk benchmark” as a benchmark about benchmark reliability, which is a common source of confusion.
    key_point: The paper frames “benchmark risk” as the chance that benchmark failure modes lead users to wrong or unsupported conclusions.
---

Risk benchmark is a benchmark that tries to show how risky an AI system is in a specific situation.

In practice, it usually asks whether a model or agent might say harmful things, encourage unsafe actions, leak private data, or behave badly under pressure. The benchmark then scores those outcomes against named risk categories.

This matters because a model can look good on normal tasks and still be unsafe in the real world. A risk benchmark helps people check for harm before they trust the system.

It is not the same as a general performance benchmark. It also is not one single agreed standard. Some people use the phrase for safety tests of AI systems, while others use it for benchmarks that judge how reliable other benchmarks are.
