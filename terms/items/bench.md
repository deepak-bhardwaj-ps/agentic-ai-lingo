---
title: τ-bench
short_description: A benchmark for testing how AI agents handle realistic tool use and user interaction.
category: Evals
tags:
  - benchmark
  - agent
  - tool-use
  - user-interaction
status: active
aliases:
  - tau-bench
  - TAU-bench
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as a general score for all AI agents instead of a specific benchmark with fixed tasks and rules.
  - Confusing the original τ-bench with the newer τ²-bench and τ³-bench versions.
related_terms:
  - agent benchmark
  - tool-use benchmark
  - interactive benchmark
  - benchmark suite
evidence:
  - source_title: τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains
    source_url: https://arxiv.org/abs/2406.12045
    source_type: research_paper
    relevance: Original paper that defines the term and explains its core design.
    key_point: τ-bench tests whether an agent can handle dynamic conversations with a simulated user, use domain-specific tools, and follow policy rules.
  - source_title: τ-bench
    source_url: https://taubench.com/
    source_type: official_docs
    relevance: Official project site for the benchmark.
    key_point: The site presents τ-bench as benchmarking AI agents in collaborative real-world scenarios, which supports the term’s current framing.
  - source_title: GitHub - sierra-research/tau-bench
    source_url: https://github.com/sierra-research/tau-bench
    source_type: official_docs
    relevance: Official repository showing the benchmark structure and its current maintenance status.
    key_point: The repository states that the original tasks are outdated and points users to τ³-bench for the latest fixed tasks and new domains, which matters for using the term accurately today.
---
τ-bench is a benchmark for testing AI agents that have to talk with a user and use tools to finish a task.

In practice, it gives the agent a realistic job, like handling a customer request in a domain such as travel or retail. The agent must follow rules, choose the right tool actions, and keep the conversation on track.

It matters because these agents are not being judged only on one answer. They are being judged on whether they can act correctly over several steps, which is much closer to how real helper systems work.

It is not a general AI intelligence score. It is also not the same as a real workplace system, because the tasks are controlled and the user is simulated. The original τ-bench has also been followed by newer versions such as τ²-bench and τ³-bench, so people should check which version they mean.
