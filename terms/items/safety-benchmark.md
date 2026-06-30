---
title: Safety benchmark
short_description: A fixed test used to check whether an AI system behaves safely on risky or harmful cases.
category: Evals and benchmarks
tags:
  - benchmark
  - evals
  - safety
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating one safety benchmark score as proof that a system is safe in the real world.
  - Assuming there is one standard safety benchmark for every AI system.
  - Confusing safety benchmarks with general capability tests that do not focus on harm, refusal, or risky behaviour.
related_terms:
  - safety evaluation
  - benchmark suite
  - red-team benchmark
  - model safety
  - evaluation harness
evidence:
  - source_title: Practices for Automated Benchmark Evaluations of Language Models
    source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-2.ipd.pdf
    source_type: standards_doc
    relevance: NIST’s current guidance frames benchmark evaluations as useful but limited, which is important for explaining what a safety benchmark can and cannot tell you.
    key_point: NIST says benchmark-style evaluations are an important tool, but their results can be hard to interpret and should not be treated as a complete picture of system performance or safety.
  - source_title: Working with evals
    source_url: https://developers.openai.com/api/docs/guides/evals
    source_type: official_docs
    relevance: OpenAI’s eval guidance shows how teams build repeatable tests for specific behaviours, including safety checks, which matches how the term is used in practice.
    key_point: OpenAI describes evals as running test inputs against criteria you define, with safety checks as one kind of evaluation, which supports the idea of a safety benchmark as a fixed, criteria-based test.
  - source_title: SafetyBench: Evaluating the Safety of Large Language Models
    source_url: https://arxiv.org/abs/2309.07045
    source_type: research_paper
    relevance: This paper uses the term in the core LLM safety sense and shows that safety benchmarks are usually built from standardised harmful or risky prompts.
    key_point: The paper presents SafetyBench as a benchmark for evaluating LLM safety, confirming that the term usually refers to a standardised test set for unsafe or harmful behaviour.
  - source_title: Sabotage evaluations for frontier models
    source_url: https://www.anthropic.com/research/sabotage-evaluations
    source_type: engineering_blog
    relevance: Anthropic explains why frontier models go through safety evaluations for dangerous capabilities, which helps bound the practical purpose of safety benchmarks.
    key_point: Anthropic says new AI models are tested with safety evaluations for harmful capabilities such as helping create biological or chemical weapons, showing that safety benchmarks are about specific risky behaviours rather than general ability.
---

A safety benchmark is a fixed test used to check whether an AI system behaves safely when it faces risky or harmful cases.

In practice, it usually gives the system the same kinds of prompts, tasks, or scenarios every time, then checks for things like unsafe advice, harmful instructions, dangerous actions, or failure to refuse when it should.

This matters because teams need a repeatable way to spot safety problems before release and to compare changes over time.

It is not proof that a system is safe in real life. It is also not a full safety review, and there is no single agreed safety benchmark for every AI system. The term is usually an umbrella label for benchmarks that focus on harmful or risky behaviour.
