---
title: Finance-Agent-Benchmark
short_description: A benchmark for testing finance-focused AI agents on realistic research tasks
category: Evals and benchmarks
tags:
  - benchmark
  - finance
  - agent
  - evals
status: draft
aliases: []
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating a benchmark score as proof that a finance agent is safe or reliable in live use.
  - Confusing this benchmark with a finance chatbot product or a trading system.
  - Assuming one score covers every kind of finance task, when the benchmark only measures the tasks it contains.
related_terms:
  - Agent benchmark
  - Finance agent
  - Agent evaluation
  - Financial research
  - Benchmark suite
evidence:
  - source_title: Finance Agent Benchmark: Benchmarking LLMs on Real-world Financial Research Tasks
    source_url: https://arxiv.org/abs/2508.00828
    source_type: research_paper
    relevance: Original paper that defines the benchmark and explains the task types it covers.
    key_point: The paper presents Finance Agent Benchmark as a testbed for LLM-driven finance agents, using expert-authored questions based on recent SEC filings and tool use.
  - source_title: vals-ai/finance-agent
    source_url: https://github.com/vals-ai/finance-agent
    source_type: engineering_blog
    relevance: Official project repository showing how the benchmark is framed by its maintainers.
    key_point: The repository says the benchmark evaluates LLMs on complex financial questions about companies, financial statements, and SEC filings, which confirms that it is a task benchmark rather than a product.
  - source_title: Finance Agent v2
    source_url: https://www.vals.ai/benchmarks/fabv2
    source_type: engineering_blog
    relevance: Current benchmark page from the same benchmark family, useful for understanding how the benchmark is being used now.
    key_point: Vals AI describes the benchmark as measuring how well AI can help analysts with real research work, showing that the term refers to a practical evaluation suite for finance-agent performance.
---

Finance-Agent-Benchmark is a benchmark suite for checking how well an AI agent can do finance research tasks.

In practice, it gives models the same finance questions and the same rules so their answers can be compared fairly. The tasks usually involve reading company filings, finding facts, doing calculations, and using tools such as search.

It matters because finance work is time-sensitive and detailed. A benchmark like this helps people see whether a system can find the right evidence, keep numbers accurate, and follow a real research workflow.

It is not a finance app, a stock picker, or proof that an AI system is safe in a live business setting. It only measures performance on the tasks built into the benchmark, so a high score does not mean the system can do every finance job well.
