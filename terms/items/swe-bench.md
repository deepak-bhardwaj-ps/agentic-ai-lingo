---
title: SWE-bench
short_description: A benchmark that tests whether AI can fix real software bugs from GitHub issues.
category: Evals and benchmarks
tags:
  - benchmark
  - evals
  - software-engineering
status: active
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating SWE-bench as a measure of general intelligence instead of a software-fixing benchmark.
  - Assuming a high score means an AI will work well on real projects without human help.
  - Confusing SWE-bench with SWE-bench Verified, which is a human-checked subset of the benchmark.
related_terms:
  - agent benchmark
  - agentic evaluation
  - benchmark suite
  - software engineering benchmark
  - SWE-bench Verified
evidence:
  - source_title: SWE-bench: Can Language Models Resolve Real-world GitHub Issues?
    source_url: https://arxiv.org/abs/2310.06770
    source_type: research_paper
    relevance: Original paper that defines the benchmark and its task format.
    key_point: SWE-bench uses real GitHub issues and pull requests from open-source repositories, and asks a model to produce a code patch that fixes the issue.
  - source_title: SWE-bench GitHub repository
    source_url: https://github.com/swe-bench/SWE-bench
    source_type: official_docs
    relevance: Official project page that describes how the benchmark is used today.
    key_point: The repository frames SWE-bench as a benchmark for evaluating large language models on real-world software issues collected from GitHub.
  - source_title: Introducing SWE-bench Verified
    source_url: https://openai.com/index/introducing-swe-bench-verified/
    source_type: official_docs
    relevance: Explains the verified subset and helps distinguish the base benchmark from its curated version.
    key_point: OpenAI says SWE-bench Verified is a human-validated subset made to more reliably evaluate models on real software issues, which shows that the base benchmark and the verified subset are related but not identical.
---

SWE-bench is a benchmark for checking whether an AI system can fix real software bugs.

It gives the system a real GitHub issue and the related code base, then asks it to make a patch that solves the problem. In other words, the AI is tested on a task that looks like a small software repair job.

This matters because it measures a useful skill for coding assistants: finding what is wrong and changing code so the project works again. It is not just a quiz about facts or a test of how well the AI can talk about code.

SWE-bench is not a general intelligence score. A good result does not mean the system can handle every programming task, every repository, or every real-world engineering rule. People also sometimes mean SWE-bench Verified, which is a curated subset of the benchmark with human checking.
