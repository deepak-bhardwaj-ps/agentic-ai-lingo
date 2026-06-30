---
title: State-aware benchmark
short_description: A benchmark that checks a system against the state it should have after a change
category: Evals and benchmarks
tags:
  - benchmark
  - evals
  - machine-unlearning
  - state
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general benchmark about any kind of system state, instead of a benchmark that checks a specific expected state after an intervention.
  - Assuming it is the same as a retrain-from-scratch comparison, when newer work argues for retrain-free evaluation.
  - Using it as if it were a product feature rather than a test method.
related_terms:
  - Machine unlearning
  - Retrain-free evaluation
  - Counterfactual oracle
  - Evaluation benchmark
  - Unlearning metrics
evidence:
  - source_title: Form and Function: Machine Unlearning as a Problem of Misaligned States
    source_url: https://arxiv.org/abs/2605.17590
    source_type: research_paper
    relevance: This is the clearest source using the exact state-aware framing and shows the term in its likely home area: machine unlearning.
    key_point: The paper describes a state-aware benchmark for deletion interventions and compares them against a counterfactual oracle model, which supports defining the term as evaluation against the state a model should have after deletion.
  - source_title: MU-Bench: A Multitask Multimodal Benchmark for Machine Unlearning
    source_url: https://arxiv.org/html/2406.14796v1
    source_type: research_paper
    relevance: This paper shows how machine-unlearning benchmarks are built around the original model, deleted samples, and a chosen evaluation target rather than simple accuracy alone.
    key_point: MU-Bench defines machine unlearning as removing the influence of selected training data and argues for retrain-free evaluation, which matches the idea behind a state-aware benchmark.
  - source_title: Gone but Not Forgotten: Improved Benchmarks for Machine Unlearning
    source_url: https://arxiv.org/html/2405.19211v1
    source_type: research_paper
    relevance: This paper explains why basic benchmark checks are not enough and why stronger, state-focused evaluation is needed in unlearning.
    key_point: The authors propose improved machine-unlearning benchmarks that use stronger privacy tests, update-leakage checks, and iterative evaluation, showing that benchmark quality depends on the target state and attack setting.
---

State-aware benchmark is a benchmark that checks whether a system ends up in the right state after something changes.

In machine unlearning, that usually means checking whether a model looks like it should after some training data has been removed. The benchmark compares the actual result with a target state, often a counterfactual one, instead of only checking one output score.

This matters because some changes are about more than one answer. If a model is supposed to forget data, a plain accuracy score may miss whether the unwanted influence is still there.

It is not the same as a general benchmark for any system that has state. In current AI use, the term is most clearly tied to machine unlearning and similar evaluation settings where the expected end state matters.
