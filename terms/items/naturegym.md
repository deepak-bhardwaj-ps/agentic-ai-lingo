---
title: NatureGym
short_description: A pipeline that turns Nature-family papers into reproducible benchmark tasks for AI coding agents
category: Evals
tags: [benchmark, evals, scientific-research, coding-agents]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: high
maturity_level: emerging
common_misuse:
  - Treating NatureGym as the benchmark itself instead of the task-construction pipeline behind NatureBench.
  - Assuming it is a general science benchmark for any research topic.
  - Reading it as a fitness or outdoor-training brand because of the name.
related_terms:
  - NatureBench
  - Agent benchmark
  - Agent evaluation
  - Reproducible environment
  - Scientific discovery
evidence:
  - source_title: NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?
    source_url: https://arxiv.org/abs/2606.24530
    source_type: research_paper
    relevance: Primary source for the benchmark that introduced NatureGym.
    key_point: The paper says NatureGym is an automated pipeline that turns a Nature-family paper into a containerized task package with a brief, dataset, held-out test set, and evaluator.
  - source_title: NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?
    source_url: https://arxiv.org/html/2606.24530v1
    source_type: research_paper
    relevance: Gives the clearest in-paper description of how NatureGym works.
    key_point: The paper explains that NatureGym standardises different papers into one reproducible format and uses an information firewall so agents must discover solutions rather than copy the source method.
  - source_title: NatureBench / naturegym README
    source_url: https://github.com/FrontisAI/NatureBench/blob/main/naturegym/README.md
    source_type: engineering_blog
    relevance: Official repository documentation confirming the project's own wording.
    key_point: The README describes NatureGym as the automated pipeline that turns a published Nature-family paper into a runnable NatureBench task package and says it is the construction half of NatureBench.
---
NatureGym is the pipeline that turns a Nature-family research paper into a benchmark task an AI coding agent can try to solve.

In practice, NatureGym takes a paper, its data, and an evaluation rule, then packages them into one repeatable task. The idea is to make different research papers look more alike so they can be tested in a fair way.

It matters because scientific tasks are usually messy and hard to compare. A pipeline like NatureGym helps researchers build benchmark tasks that are reproducible and harder to game.

NatureGym is not the benchmark name itself. It is also not a general science platform or a fitness term. In this glossary, it refers to the task-building system used by NatureBench.
