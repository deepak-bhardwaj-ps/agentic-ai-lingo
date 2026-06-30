---
title: SWE-bench verified
short_description: A human-validated subset of SWE-bench used to test coding agents on real software issues.
category: Evals and benchmarks
tags: [benchmark, evals, coding-agents, software-engineering]
status: active
aliases: [SWE-Bench Verified]
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: established
common_misuse:
  - Treating it as a general coding test for all programming tasks, rather than a specific benchmark built from GitHub issues.
  - Assuming a score on SWE-bench Verified proves a model can handle any real software project.
  - Confusing the verified subset with the original SWE-bench test set or with other SWE-bench variants such as Lite.
related_terms:
  - SWE-bench
  - coding agent
  - software engineering benchmark
  - issue resolution
  - unit tests
evidence:
  - source_title: Introducing SWE-bench Verified
    source_url: https://openai.com/index/introducing-swe-bench-verified/
    source_type: official_docs
    relevance: OpenAI’s announcement gives the clearest explanation of why the verified subset exists and what was changed.
    key_point: Describes SWE-bench Verified as a human-validated subset of SWE-bench created to more reliably evaluate models on real-world software issues.
  - source_title: SWE-bench Verified
    source_url: https://www.swebench.com/verified.html
    source_type: official_docs
    relevance: The benchmark’s own page confirms the size, purpose, and human review step.
    key_point: Says it is a human-validated subset of 500 instances from SWE-bench, with annotators checking that problems are clear, test patches are correct, and tasks are solvable.
  - source_title: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
    source_url: https://arxiv.org/abs/2310.06770
    source_type: research_paper
    relevance: The original paper defines SWE-bench itself, which is necessary context for understanding the verified subset.
    key_point: Defines SWE-bench as a benchmark of software engineering problems drawn from real GitHub issues and pull requests, showing that SWE-bench Verified is a curated version of an existing benchmark.
---

SWE-bench Verified is a human-checked subset of SWE-bench used to test how well an AI system can fix real software issues.

In practice, a model gets a code repository and an issue description, then tries to make a code change that solves the problem. The result is judged by tests and other checks.

The term matters because coding agents can look helpful while still missing details, breaking tests, or fixing the wrong thing. A verified benchmark makes the comparison fairer by removing some unclear or badly specified cases.

It is not a general programming exam, and it is not proof that a model can work safely on any real project. It is also not the same as the original SWE-bench test set or every other SWE-bench variant.
