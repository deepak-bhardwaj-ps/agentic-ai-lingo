---
title: CRM-bench
short_description: A benchmark for testing AI agents on CRM tasks such as sales and customer service work.
category: Evals and benchmarks
tags: [benchmark, evals, crm, agentic-ai]
status: active
aliases: [CRM benchmark]
meaning_type: novel
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as a general CRM product or a score for all AI systems, rather than a specific benchmark for CRM tasks.
  - Confusing it with the old Unix `bench` command or with generic “CRM benchmarking”.
related_terms:
  - CRMArena
  - CRMArena-Pro
  - agent benchmark
  - tool-use benchmark
  - sales assistant
  - customer support automation
evidence:
  - source_title: Agentic Benchmark for CRM
    source_url: https://www.salesforceairesearch.com/crm-benchmark
    source_type: official_docs
    relevance: Official Salesforce AI Research page for the benchmark name used in this glossary term.
    key_point: Describes a benchmark for evaluating agents on enterprise CRM use cases, with measures such as accuracy, cost, speed, trust and safety, and sustainability.
  - source_title: Salesforce Announces the World's First LLM Benchmark for CRM
    source_url: https://www.salesforce.com/news/stories/crm-benchmark/
    source_type: official_docs
    relevance: Salesforce’s announcement explains what the benchmark covers and why it exists.
    key_point: Says the benchmark is designed for common sales and service tasks like prospecting, lead nurturing, and case summaries, which makes the CRM focus concrete.
  - source_title: CRMArena: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks in Realistic Environments
    source_url: https://arxiv.org/html/2411.02305v1
    source_type: research_paper
    relevance: Research paper showing the earlier benchmark framing for CRM agent evaluation.
    key_point: Defines CRMArena as a benchmark for realistic CRM tasks in a sandbox built around Salesforce-like structures, supporting the idea that CRM-bench refers to agent evaluation rather than CRM software itself.
  - source_title: CRMArena-Pro: Holistic Assessment of LLM Agents Across Diverse Business Scenarios and Interactions
    source_url: https://arxiv.org/html/2505.18878v1
    source_type: research_paper
    relevance: Newer paper showing how the CRM benchmark line has expanded.
    key_point: Shows the benchmark family has grown beyond basic customer service into sales, CPQ, B2B and B2C tasks, which matters for using the term today.
---

CRM-bench is a benchmark for testing how well an AI agent can do CRM work, such as sales and customer service tasks.

In practice, it usually means a controlled test set where an agent is asked to carry out CRM-style jobs and is scored on how well it performs. The work may include looking up customer information, handling sales steps, or summarising service cases.

The term matters because CRM work is not just about answering questions. It is about doing the right actions, in the right order, while keeping cost, speed, and safety in mind.

It is not the same as a real CRM system. It is also not a general score for all AI. If someone uses the term loosely, they are usually talking about a specific benchmark for CRM tasks, not customer relationship management software itself.
