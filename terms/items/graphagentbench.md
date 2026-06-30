---
title: GraphAgentBench
short_description: A benchmark term for testing AI agents on graph tasks.
category: Evals
tags: [benchmark, agent, graph, evals]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as one fixed, official benchmark when the name is sometimes used loosely for different graph-agent evaluation sets.
  - Confusing graph-agent evaluation with general graph reasoning benchmarks that do not use agent tools or multi-step actions.
related_terms:
  - Agent benchmark
  - Graph reasoning
  - Tool use
  - Multi-step task benchmark
  - Graph agent
evidence:
  - source_title: GraphAgent: Agentic Graph Language Assistant
    source_url: https://arxiv.org/html/2412.17029v1
    source_type: research_paper
    relevance: Shows a graph-agent system being evaluated on multiple graph-related prediction and generation tasks, which is the closest published framing for this term.
    key_point: The paper evaluates GraphAgent on graph-based predictive tasks and graph-enhanced text generation, showing that "graph agent" benchmarks can cover both structured graph tasks and language tasks that depend on graph context.
  - source_title: GDS Agent for Graph Algorithmic Reasoning
    source_url: https://arxiv.org/html/2508.20637v2
    source_type: research_paper
    relevance: Introduces named benchmark sets for graph-agent evaluation and shows how these benchmarks score tool calls and final answers.
    key_point: The paper defines new benchmarks, including graph-agent-bench-ln-v0, to evaluate graph agents on intermediate tool calls and answer quality, confirming that graph-agent benchmarking is about step-by-step graph task solving, not just final answers.
  - source_title: Scalable and Accurate Graph Reasoning with LLM-Based Multi-Agent Systems
    source_url: https://arxiv.org/html/2410.05130v3
    source_type: research_paper
    relevance: Helps distinguish graph-agent benchmarking from ordinary graph reasoning by showing agent-based graph evaluation at larger scales.
    key_point: The paper presents GraphAgent-Reasoner for graph reasoning and reports benchmark results across graph tasks, reinforcing that this area is still developing and has several nearby but distinct benchmark names.
---
GraphAgentBench is a benchmark for testing how well an AI agent can work with graphs.

In practice, it usually means a set of graph tasks where the agent has to follow links, use tools, or answer questions that depend on graph structure.

It matters because graphs are full of connected steps, so they test more than a single answer. They can show whether an agent can plan, choose the right next move, and use the graph correctly.

This is not the same as a general graph theory test, and it is not a fully settled standard name. Different papers may use similar names for related but different benchmark sets.
