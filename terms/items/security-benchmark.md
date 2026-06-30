---
title: Security benchmark
short_description: A fixed test that measures how well an AI system handles security tasks, risks, or defences.
category: Evals and benchmarks
tags: [benchmark, evals, security, cybersecurity]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating any benchmark with "security" in the name as the same thing
  - Assuming a security benchmark proves a system is safe in real use
  - Confusing defensive security tests with offensive vulnerability-exploitation tests
related_terms:
  - cybersecurity benchmark
  - safety benchmark
  - red-team benchmark
  - vulnerability benchmark
  - agentic benchmark
evidence:
  - source_title: CYBERSECEVAL 2: A Wide-Ranging Cybersecurity Evaluation Suite for Large Language Models
    source_url: https://ai.meta.com/research/publications/cyberseceval-2-a-wide-ranging-cybersecurity-evaluation-suite-for-large-language-models/
    source_type: official_docs
    relevance: Shows a current official use of a security benchmark for measuring LLM security risks and capabilities.
    key_point: Meta says CYBERSECEVAL 2 is a benchmark to quantify LLM security risks and capabilities, including prompt injection and code interpreter abuse.
  - source_title: GPT-5.5 System Card - Cybersecurity evaluations
    source_url: https://deploymentsafety.openai.com/gpt-5-5/cybersecurity
    source_type: official_docs
    relevance: Shows that security benchmarks can test whether a model can identify, exploit, or defend against real vulnerabilities.
    key_point: OpenAI describes CVE-Bench as a benchmark that tasks models with identifying and exploiting real-world web-application vulnerabilities in a sandbox.
  - source_title: Project Glasswing: Securing critical software for the AI era
    source_url: https://www.anthropic.com/glasswing
    source_type: official_docs
    relevance: Shows a defensive security benchmark used to evaluate AI on real security workflows, not just attack generation.
    key_point: Anthropic refers to CTI-REALM as an open-source security benchmark and uses it to assess end-to-end detection engineering.
---

A security benchmark is a fixed test that checks how well an AI system handles security work.

In practice, it may ask the system to spot a vulnerability, resist a harmful prompt, generate a detection rule, or carry out another security-related task in a controlled setting. Different security benchmarks can focus on different parts of security, so the term is broad.

It matters because security mistakes can cause real harm. A benchmark helps people compare systems more fairly and see where they still fail.

It is not proof that a system is safe in the real world. It is also not one single agreed test. Some security benchmarks check defence, while others check offensive capability or misuse risk.
