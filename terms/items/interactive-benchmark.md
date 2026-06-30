---
title: Interactive benchmark
short_description: A benchmark that tests an AI system through back-and-forth interaction instead of one fixed answer.
category: Evals
tags: [benchmark, evals, interactive, agent-evaluation]
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a formal standard name when it is often just a broad description for benchmarks with interaction.
  - Confusing it with a static benchmark that only asks for one final answer.
  - Assuming any chat-style task is interactive enough to count as an interactive benchmark.
related_terms:
  - agent benchmark
  - multi-turn conversation benchmark
  - tool-use benchmark
  - interactive environment
  - benchmark suite
evidence:
  - source_title: AgentBench: Evaluating LLMs as Agents
    source_url: https://arxiv.org/abs/2308.03688
    source_type: research_paper
    relevance: Shows a clear research use of interactive benchmarking for agents across multiple environments.
    key_point: The paper frames AgentBench as a multi-dimensional benchmark for LLM-as-Agent systems and emphasises interactive environments and multiple turns of action and feedback.
  - source_title: MLPerf Inference 5.1: Benchmarking Small LLMs with Llama3.1-8B
    source_url: https://mlcommons.org/2025/09/small-llm-inference-5-1/
    source_type: official_docs
    relevance: Shows how a major benchmarking body uses an "interactive scenario" to mean low-latency, user-facing evaluation.
    key_point: MLCommons introduces an interactive scenario for cases where responsiveness matters, such as code assistants and real-time creative tools.
  - source_title: Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey
    source_url: https://arxiv.org/html/2503.22458v1
    source_type: research_paper
    relevance: Shows that interactive evaluation often means multi-turn dialogue, context keeping, and tool use.
    key_point: The survey says current evaluation of LLM agents focuses on dialogue coherence, context maintenance, tool use, and memory across multiple turns.
  - source_title: MTR-Bench: A Comprehensive Benchmark for Multi-Turn Reasoning Evaluation
    source_url: https://arxiv.org/html/2505.17123v1
    source_type: research_paper
    relevance: Provides another current example of a benchmark built specifically around interactive, multi-turn evaluation.
    key_point: The paper describes a benchmark for reasoning in multi-turn interactive scenarios and says it uses an automated interactive framework.
---
An interactive benchmark is a test where the AI has to respond step by step instead of giving one answer all at once.

In practice, the system may need to answer, react to new information, use tools, or keep track of what happened in earlier turns. The score depends on how well it handles the interaction, not just on the final reply.

This matters because some AI tasks only make sense when the system can deal with changes over time. A shopping helper, coding helper, or chat assistant may need to ask follow-up questions and adjust its next move.

It is not the same as a static benchmark that checks one fixed prompt and one fixed answer. It is also not a single official standard name. People use it as a broad label for benchmarks that involve interaction, often over multiple turns or actions.
