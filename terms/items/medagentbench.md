---
title: MedAgentBench
short_description: A benchmark that tests medical AI agents in a virtual electronic health record environment.
category: Evals and benchmarks
tags:
  - medical-ai
  - benchmark
  - evaluation
  - agents
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general medical chatbot benchmark instead of a task-based agent benchmark.
  - Assuming it measures medical knowledge alone, when it also tests planning, tool use, and action in an EHR-like setting.
related_terms:
  - agent-benchmark
  - medical-benchmark
  - electronic-health-record-agent
  - evaluation-harness
evidence:
  - source_title: MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents
    source_url: https://stanfordmlgroup.github.io/projects/medagentbench/
    source_type: engineering_blog
    relevance: Official project page from the Stanford team that created MedAgentBench.
    key_point: Says MedAgentBench is a comprehensive evaluation suite for benchmarking agent capabilities in medical records settings, with 300 clinically relevant tasks in a FHIR-compliant environment.
  - source_title: MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents
    source_url: https://arxiv.org/abs/2501.14654
    source_type: research_paper
    relevance: Original paper defining the benchmark and its scope.
    key_point: Describes MedAgentBench as a broad evaluation suite for medical-record contexts, with 300 patient-specific tasks, 100 patient profiles, and an interactive EHR-like environment.
  - source_title: MedAgentBench GitHub repository
    source_url: https://github.com/stanfordmlgroup/medagentbench
    source_type: engineering_blog
    relevance: Implementation repository for the benchmark and its dataset.
    key_point: Confirms that the benchmark is a research codebase built on AgentBench and intended for evaluation, not for production clinical use.
---

MedAgentBench is a benchmark for testing medical AI agents inside a virtual electronic health record, or EHR.

In practice, it gives an agent clinical tasks to complete in a realistic medical-record setting. The point is not just to answer questions. The agent has to plan, choose actions, and use the available record tools correctly.

This matters because a medical agent can look good in a chat window but still fail when it has to work through a real workflow. MedAgentBench helps measure whether the agent can handle those steps in a controlled test.

It is not the same as a general medical question-answering benchmark. It is also not a real hospital system. It is a test environment built to check agent behaviour before anything is used in practice.
