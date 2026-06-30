---
title: BioAgentBench
short_description: A benchmark suite for testing AI agents on bioinformatics workflows
category: Evals
tags: [agent, benchmark, bioinformatics, evals]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating BioAgentBench as a general biology or biomedical benchmark rather than a benchmark for bioinformatics agent workflows.
  - Assuming a strong score means an agent will be reliable on real lab or clinical work.
  - Confusing BioAgentBench with broader benchmark suites for biology, medicine, or biosecurity.
related_terms:
  - Agent benchmark
  - Bioinformatics
  - Agent evaluation
  - Benchmark suite
  - Computational biology
evidence:
  - source_title: BioAgent Bench: An AI Agent Evaluation Suite for Bioinformatics
    source_url: https://arxiv.org/abs/2601.21800
    source_type: research_paper
    relevance: Original paper defining the term and describing what the benchmark measures.
    key_point: The paper presents BioAgent Bench as an evaluation suite for AI agents on common bioinformatics tasks, including end-to-end workflows such as RNA-seq, variant calling, and metagenomics.
  - source_title: bioagent-bench/bioagent-bench
    source_url: https://github.com/bioagent-bench/bioagent-bench
    source_type: engineering_blog
    relevance: Official project repository showing the benchmark’s intended use and task style.
    key_point: The repository frames BioAgent Bench as a benchmark for evaluating LLM agents in bioinformatics and includes concrete workflow tasks and grading material.
  - source_title: BioAgent Bench: An AI Agent Evaluation Suite for Bioinformatics
    source_url: https://openreview.net/forum?id=fAk5JqgZp2
    source_type: standards_doc
    relevance: Conference record confirming the published framing of the benchmark.
    key_point: The OpenReview entry describes BioAgent Bench as an evaluation suite for measuring performance and robustness on common bioinformatics tasks, which helps distinguish it from looser uses of the name.
---
BioAgentBench is a benchmark suite for testing AI agents on bioinformatics tasks.

In practice, it gives agents the same kinds of biology data-workflow tasks and checks how well they can carry them out. The tasks include multi-step work such as analysing sequencing data, building pipelines, and producing the requested output files.

It matters because bioinformatics work is often long, technical, and easy to get wrong in small ways. A benchmark like this helps people see whether an agent can keep going through a real workflow, not just answer a biology question.

BioAgentBench is not a general test of all biology AI, and it is not the same as a clinical safety benchmark or a biosecurity benchmark. A good score does not prove the agent is safe, reliable, or ready for real laboratory use.
