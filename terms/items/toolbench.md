---
title: ToolBench
short_description: Benchmark and dataset for testing how well language models can use external tools and APIs.
category: Evals
tags: [benchmark, evals, tool-use, agent]
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating ToolBench as a model instead of a benchmark and dataset.
  - Using it as proof that a system works well in the real world without checking live performance.
  - Confusing it with any general agent benchmark that does not focus on tool calls and API use.
related_terms:
  - Tool use
  - Tool learning
  - Tool-use benchmark
  - Agent benchmark
  - StableToolBench
evidence:
  - source_title: On the Tool Manipulation Capability of Open-source Large Language Models
    source_url: https://arxiv.org/abs/2305.16504
    source_type: research_paper
    relevance: Original paper that introduces ToolBench and explains what it is for.
    key_point: The paper says ToolBench is a tool manipulation benchmark made of diverse software tools for real-world tasks, designed to evaluate tool use.
  - source_title: ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs
    source_url: https://arxiv.org/abs/2307.16789
    source_type: research_paper
    relevance: Shows ToolBench as the dataset and evaluation base for tool-use training and testing.
    key_point: The paper describes ToolBench as an instruction-tuning dataset for tool use, built from many real-world APIs, with single-tool and multi-tool tasks.
  - source_title: OpenBMB/ToolBench
    source_url: https://github.com/OpenBMB/ToolBench
    source_type: engineering_blog
    relevance: Project repository that confirms the benchmark is an open platform for training, serving, and evaluating tool-learning systems.
    key_point: The repository presents ToolBench as an open platform for tool learning and includes the data, tool environment, and evaluation code.
  - source_title: StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models
    source_url: https://arxiv.org/abs/2403.07714
    source_type: research_paper
    relevance: Explains a limitation of ToolBench and why later work needed to stabilise it.
    key_point: The paper says ToolBench-based evaluation can be unstable because real APIs change, which is why StableToolBench adds caching, simulators, and steadier scoring.
---
ToolBench is a benchmark and dataset for testing whether a language model can use external tools such as APIs.

In practice, it gives a model tasks that need tool calls, not just a single text answer. The model has to choose the right tool, use it in the right way, and follow the task to the end.

It matters because many AI systems only look smart when they can talk. ToolBench checks whether they can also act, which is closer to how assistant systems work in real products.

It is not a general intelligence test. It is not the same as a chatbot benchmark that only scores one reply. It is also not proof that a model will work reliably in every live tool system, because real APIs can change and break old results.
