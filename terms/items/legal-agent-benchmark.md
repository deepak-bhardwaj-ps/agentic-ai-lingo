---
title: Legal Agent Benchmark
short_description: Harvey’s open benchmark for testing AI agents on long legal work tasks.
category: Evals and benchmarks
tags: [agent benchmark, legal AI, legal work, Harvey, LAB]
status: draft
aliases: [LAB]
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as any benchmark about law, instead of a benchmark for agents doing legal work
  - Thinking a strong score means the system can safely replace a lawyer
  - Confusing it with short legal question-answer tests that do not involve tools, files, or multi-step work
related_terms:
  - agent benchmark
  - legal benchmark
  - legal agent
  - LegalBench
  - BigLaw Bench
  - contract review benchmark
evidence:
  - source_title: Open-Sourcing Harvey’s Long Horizon Legal Agent Benchmark
    source_url: https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
    source_type: official_docs
    relevance: This is Harvey’s launch post and the clearest source for the term itself.
    key_point: Harvey says LAB is an open-source benchmark for legal agents, built to evaluate long-horizon legal work using an instruction, a client matter with materials, and a required work product.
  - source_title: Harvey LAB repository
    source_url: https://github.com/harveyai/harvey-labs
    source_type: official_docs
    relevance: Confirms the benchmark structure and that it is an ongoing open-source project.
    key_point: The repo describes LAB as a benchmark for real legal work, made of task datasets plus an execution harness, and notes that the task set and harness will keep evolving.
  - source_title: Moritz Hardt has contributed to the Legal Agent Benchmark launched by Harvey
    source_url: https://is.mpg.de/en/news/moritz-hardt-has-contributed-to-the-legal-agent-benchmark-launched-by-harvey
    source_type: industry_article
    relevance: Independent confirmation that this is a benchmark for long-horizon legal-agent work, not just a product feature.
    key_point: MPI-IS describes it as an open benchmark for measuring AI agents on long-horizon legal work and says it is intended to measure multi-document, open-ended assignments.
  - source_title: Harvey’s Legal Agent Benchmark on Vals AI
    source_url: https://www.vals.ai/benchmarks/hlab
    source_type: industry_article
    relevance: Provides a current third-party summary of how the benchmark is used and what kinds of tools it tests.
    key_point: Vals AI says the benchmark tests an agent’s ability to complete legal work using documents, spreadsheets, presentations, and file-system tools.
---

Legal Agent Benchmark is Harvey’s benchmark for testing AI agents on long legal tasks.

In practice, it gives an agent legal work to do, along with files and instructions, and checks whether the result meets the rules for that task. It is meant to look more like real law-firm work than a simple quiz.

This matters because legal work often takes many steps and depends on reading several documents, using tools, and producing careful written work. A benchmark like this helps people compare different systems in a more realistic way.

It is not a general law exam, and it is not proof that an AI system can safely do legal work by itself. It is also not the same as a simple legal question-answer test.
