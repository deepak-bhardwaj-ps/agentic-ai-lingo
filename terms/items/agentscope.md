---
title: AgentSCOPE
short_description: A benchmark for checking privacy leaks across the steps of an agent workflow.
category: Evals
tags:
  - agentic-ai
  - evaluation
  - benchmark
  - privacy
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the AgentScope agent framework instead of a separate benchmark.
  - Assuming it only checks the final answer, when it studies intermediate steps too.
related_terms:
  - privacy benchmark
  - agent workflow
  - tool calling
  - contextual integrity
evidence:
  - source_title: AgentSCOPE: Evaluating Contextual Privacy Across Agentic Workflows
    source_url: https://arxiv.org/abs/2603.04902
    source_type: research_paper
    relevance: Primary paper that defines AgentSCOPE.
    key_point: The authors present AgentSCOPE as a benchmark with 62 multi-tool scenarios across eight regulatory domains and ground truth at every pipeline stage.
  - source_title: Evaluating Contextual Privacy Across Agentic Workflows
    source_url: https://arxiv.org/html/2603.04902v1
    source_type: research_paper
    relevance: Full paper text explaining why the benchmark looks at the whole agent pipeline, not just the final output.
    key_point: The paper argues that privacy problems can happen at any step in an agentic pipeline and reports that many violations appear in intermediate tool-response stages.
  - source_title: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Settings
    source_url: https://arxiv.org/html/2606.23217
    source_type: research_paper
    relevance: Later work that cites AgentSCOPE as evidence that intermediate tool-use traces can leak data even when the final answer looks safe.
    key_point: This helps confirm AgentSCOPE is used as a privacy-evaluation reference for agent workflows, not as a general agent framework.
---
AgentSCOPE is a benchmark for checking whether an AI agent leaks private information while it works.

In practice, it tests the steps inside an agent workflow, not just the final answer. That matters because an agent can expose private details while it is looking things up, calling tools, or passing information between steps.

The term matters because a clean final reply does not always mean the whole process was safe. AgentSCOPE is meant to catch privacy leaks that happen in the middle, where they are easy to miss.

It is not the same as the AgentScope agent framework. The names are similar, but AgentSCOPE here refers to the privacy benchmark.
