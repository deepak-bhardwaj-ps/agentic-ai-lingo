---
title: Offensive security benchmark
short_description: A test used to measure how well an AI system can carry out offensive cyber tasks in a controlled setting
category: Evals and benchmarks
tags: [benchmark, evals, cybersecurity, offensive-security, ai-agents]
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it like a real hacking tool instead of a controlled test.
  - Assuming it measures all of cybersecurity, when it usually focuses on attack-style tasks such as finding or exploiting weaknesses.
  - Using it as proof that a model is safe or unsafe in the real world.
related_terms:
  - Cybersecurity benchmark
  - Red teaming
  - Capture the Flag (CTF)
  - Vulnerability exploitation
  - Agent benchmark
evidence:
  - source_title: Cybench
    source_url: https://cybench.github.io/
    source_type: official_docs
    relevance: The project’s own description shows the common benchmark framing for offensive cybersecurity evaluation.
    key_point: Cybench is described as a benchmark for evaluating the cybersecurity capabilities and risks of language models, using CTF tasks and graded subtasks.
  - source_title: NYU CTF Bench
    source_url: https://nyu-llm-ctf.github.io/
    source_type: official_docs
    relevance: This official site uses the exact benchmark idea for offensive security in LLM evaluation.
    key_point: The benchmark is presented as a way to test LLM cybersecurity capabilities with difficult real-world CTF challenges.
  - source_title: CVE-Bench: A Benchmark for AI Agents’ Ability to Exploit Real-World Web Application Vulnerabilities
    source_url: https://github.com/uiuc-kang-lab/cve-bench
    source_type: official_docs
    relevance: This benchmark extends the idea beyond CTF tasks to real-world web application exploits, showing how the term is used in practice.
    key_point: CVE-Bench evaluates AI agents on exploiting real web vulnerabilities in a sandbox, which matches the offensive-security benchmark pattern.
---

An offensive security benchmark is a controlled test that checks how well an AI system can do attack-style cybersecurity tasks.

In practice, that usually means tasks such as solving Capture the Flag challenges, finding weaknesses, or trying to exploit a known vulnerability inside a safe sandbox. The point is to measure capability, not to let the system attack real targets.

It matters because these benchmarks help researchers compare models and see whether a system can reason through hard security tasks. They also help spot where a model is weak, such as getting stuck, missing a step, or failing to exploit a flaw it identified.

It is not the same as real offensive hacking, a red-team exercise against live systems, or proof that a model is safe to deploy. The term is also not fully standardised, so different projects may use it for slightly different benchmark setups.
