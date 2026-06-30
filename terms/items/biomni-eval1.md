---
title: Biomni-Eval1
short_description: A benchmark dataset for testing Biomni and other biomedical agents on fixed biology tasks.
category: Evals
tags:
  - benchmark
  - biomedical
  - agent-evaluation
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general biology score that proves an AI can handle all biomedical work.
  - Confusing the benchmark with the Biomni agent itself.
  - Assuming one result on Biomni-Eval1 means the system is safe or reliable in real research or clinical use.
related_terms:
  - Biomni
  - biomedical benchmark
  - agent benchmark
  - evaluation dataset
evidence:
  - source_title: Biomni: A General-Purpose Biomedical AI Agent
    source_url: https://github.com/snap-stanford/biomni
    source_type: official_docs
    relevance: The project README is the clearest official description of Biomni-Eval1 and shows how the term is used by the builders themselves.
    key_point: Biomni-Eval1 is described as a comprehensive evaluation benchmark with 433 instances across 10 biological reasoning tasks, including gene identification, diagnosis, and lab-bench questions.
  - source_title: Biomni-Eval1
    source_url: https://huggingface.co/datasets/biomni/Eval1
    source_type: official_docs
    relevance: The dataset page confirms that Biomni-Eval1 is a real, packaged evaluation dataset with fixed rows, task names, and answer formats.
    key_point: The dataset card shows 433 rows and gives task-specific scoring rules, which makes it clear this is a standardised benchmark rather than an informal test.
  - source_title: Biomni: A General-Purpose Biomedical AI Agent
    source_url: https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1
    source_type: research_paper
    relevance: The paper provides the research framing for Biomni and explains why the team released an evaluation suite alongside the agent.
    key_point: The paper presents Biomni as a general-purpose biomedical AI agent and uses Biomni-Eval1 as its benchmark for measuring biomedical reasoning and task execution.
---
Biomni-Eval1 is a benchmark dataset for testing biomedical AI agents on fixed biology tasks.

In practice, it gives the same set of tasks to every system and checks whether the answers match the expected results. The tasks include things like finding the right gene, choosing a variant, answering lab questions, and identifying rare diseases.

It matters because biomedical work is detailed and easy to get wrong. A benchmark like this helps people compare systems in a fair way and see whether an agent can do specific research-style jobs, not just talk about biology.

It is not the same as the Biomni agent itself. It is also not proof that a system is safe, useful, or correct in real research or clinical work. The term is specific to Biomni’s evaluation suite, so it should not be used as a general name for any biology test.
