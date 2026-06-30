---
title: AgentSecBench
short_description: A short name for Agent Security Bench (ASB), a benchmark for testing security failures in LLM-based agents.
category: Evals
tags:
  - agent
  - benchmark
  - evals
  - security
  - prompt-injection
status: active
aliases:
  - Agent Security Bench
  - ASB
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general agent benchmark instead of a security-focused one
  - Assuming it measures all risks in agent systems
  - Confusing the benchmark name with the broader topic of agent security
related_terms:
  - agentic security
  - prompt injection
  - indirect prompt injection
  - tool misuse
  - agent safety benchmark
evidence:
  - source_title: Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents
    source_url: https://arxiv.org/abs/2410.02644
    source_type: research_paper
    relevance: This is the original paper that defines the benchmark and its scope, so it is the main source for what the term means.
    key_point: ASB is a benchmark for formalising and evaluating attacks and defences for LLM-based agents.
  - source_title: Agent Security Bench (ASB) GitHub repository
    source_url: https://github.com/agiresearch/asb
    source_type: official_docs
    relevance: This is the official code repository, which confirms the project name, acronym, and intended use as a benchmark for agent security testing.
    key_point: The repository says ASB is the official code for the paper and aims to evaluate adversarial attacks and defences across multiple scenarios.
  - source_title: OpenReview record for Agent Security Bench (ASB)
    source_url: https://openreview.net/forum?id=V4y0CpX4hK
    source_type: research_paper
    relevance: This conference record confirms the term as a research benchmark and helps verify that it is used in published academic work.
    key_point: OpenReview describes ASB as a framework for benchmarking attacks and defences of LLM-based agents.
---
AgentSecBench is a short name for Agent Security Bench, often written as ASB.

It is a benchmark for testing how secure an LLM-based agent is when it can use tools, follow instructions, and act on a person’s behalf.

In practice, ASB is used to check whether an agent can be tricked into doing the wrong thing, leaking private information, or using a tool it should not use.

This matters because agents can take real actions, not just write text. A security benchmark helps researchers compare defences and find weak spots before the agent is used in the real world.

It is not a general “how smart is the agent” score. It is also not the same as ordinary cybersecurity software, because it focuses on failures that happen when an AI system itself is making decisions.
