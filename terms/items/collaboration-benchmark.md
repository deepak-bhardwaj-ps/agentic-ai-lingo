---
title: Collaboration benchmark
short_description: A benchmark that measures how well a person and an AI system work together on a task.
category: Evals and benchmarks
tags:
  - benchmark
  - evaluation
  - human-ai-collaboration
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general model benchmark when the task is really about teamwork between a human and an AI system.
  - Assuming one score proves the system works well in real life.
  - Using it as a vague label for any test that involves more than one step.
related_terms:
  - Human-AI collaboration
  - Human-AI teaming
  - Interactive benchmark
  - Agent evaluation
  - Benchmark suite
evidence:
  - source_title: A Survey on Human-AI Collaboration with Large Foundation Models
    source_url: https://arxiv.org/html/2403.04931v3
    source_type: research_paper
    relevance: Provides the broader research framing for human-AI collaboration and shows why evaluation is needed for interactive work, not just one-shot answers.
    key_point: The survey treats human evaluation as part of an iterative collaboration loop and shows that collaboration work is evaluated differently from plain model output.
  - source_title: HAI-Eval: Measuring Human-AI Synergy in Collaborative Coding
    source_url: https://arxiv.org/html/2512.04111v1
    source_type: research_paper
    relevance: Shows a concrete benchmark built specifically to measure human-AI collaboration, not solo model skill.
    key_point: The paper introduces a benchmark for human-AI synergy in coding and designs tasks that require collaboration rather than standalone solving.
  - source_title: A Benchmark to Assess Common Ground in Human-AI Collaboration
    source_url: https://arxiv.org/abs/2602.21337
    source_type: research_paper
    relevance: Shows that collaboration benchmarks often measure shared understanding, coordination, and repair during interaction.
    key_point: The paper defines a benchmark for human-AI collaboration around common ground, joint action, and repair, which are core parts of collaborative work.
---

Collaboration benchmark is a test that measures how well a person and an AI system work together.

In practice, it checks things like whether the AI understands the person's intent, whether both sides can stay coordinated, and whether they can fix mistakes during the task. The task is often interactive, which means the result depends on back-and-forth communication, not just one final answer.

This matters because some AI tools are only useful if they can work smoothly with people. A collaboration benchmark helps compare systems on teamwork, not just on raw output quality.

It is not a general benchmark for all AI performance. It is also not the same as a simple chatbot test, because the point is to measure cooperation, shared understanding, and task repair across multiple steps.
