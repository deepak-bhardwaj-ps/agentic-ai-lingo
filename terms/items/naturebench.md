---
title: NatureBench
short_description: A benchmark for testing AI coding agents on scientific tasks drawn from Nature-family papers
category: Evals and benchmarks
tags: [benchmark, evals, scientific-research, coding-agents]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: high
maturity_level: emerging
common_misuse:
  - Treating NatureBench as a general benchmark for all AI systems.
  - Assuming a good score means the agent can do scientific research in the real world.
  - Confusing NatureBench with NatureGym, which is the pipeline used to build the tasks.
related_terms:
  - Agent benchmark
  - Agent evaluation
  - Benchmark suite
  - Scientific discovery
  - Reproducibility
evidence:
  - source_title: NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?
    source_url: https://arxiv.org/abs/2606.24530
    source_type: research_paper
    relevance: Primary source defining NatureBench, its task count, and its purpose.
    key_point: The paper says NatureBench is a cross-discipline benchmark of 90 tasks taken from peer-reviewed Nature-family publications, meant to test whether AI coding agents can move from reproduction to discovery.
  - source_title: FrontisAI/NatureBench
    source_url: https://github.com/FrontisAI/NatureBench
    source_type: engineering_blog
    relevance: Official project repository with the benchmark description and release materials.
    key_point: The repository describes NatureBench as 90 tasks across six scientific domains and explains that each task is scored against the source paper's reported state of the art.
  - source_title: NatureGym README
    source_url: https://github.com/FrontisAI/NatureBench/blob/main/naturegym/README.md
    source_type: engineering_blog
    relevance: Clarifies the related pipeline name, which is easy to confuse with the benchmark itself.
    key_point: The README says NatureGym is the automated pipeline that turns a published paper into a containerized NatureBench task package, making it the construction system rather than the benchmark name.
---

NatureBench is a benchmark for checking how well an AI coding agent can solve scientific tasks taken from Nature-family research papers.

In practice, it gives the agent a set of paper-based problems and scores the result against the paper’s reported best performance. The tasks are built to see whether the agent can go beyond copying a known method and actually make progress on a real research problem.

It matters because many AI systems can answer questions or write code, but that does not mean they can help with scientific work. NatureBench is meant to test that harder step.

It is not a general test of all AI. It is not proof that an agent can do science in the real world. It is also not the same thing as NatureGym, which is the pipeline used to build the benchmark tasks.
