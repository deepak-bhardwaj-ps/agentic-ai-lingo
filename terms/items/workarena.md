---
title: WorkArena
short_description: A benchmark for testing web agents on common knowledge-work tasks in ServiceNow.
category: Evals and benchmarks
tags:
  - benchmark
  - evals
  - web-agents
  - service-now
  - knowledge-work
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating WorkArena as a general AI test instead of a benchmark for browser-based work tasks.
  - Assuming a high score means an agent can handle all office work safely or reliably.
  - Confusing WorkArena with WorkArena++, which is a later extension with more complex tasks.
related_terms:
  - benchmark
  - agent benchmark
  - web agent
  - knowledge work
  - BrowserGym
  - WorkArena++
evidence:
  - source_title: WorkArena: A Benchmark for Evaluating Agents on Knowledge Work Tasks
    source_url: https://github.com/ServiceNow/workarena
    source_type: engineering_blog
    relevance: Official project page that defines WorkArena in the benchmark authors’ own words.
    key_point: The repository describes WorkArena as a suite of browser-based tasks for testing web agents on routine knowledge-worker tasks in ServiceNow.
  - source_title: WorkArena: How Capable Are Web Agents at Solving Common Knowledge Work Tasks?
    source_url: https://arxiv.org/abs/2403.07718
    source_type: research_paper
    relevance: Primary research paper defining the benchmark, its task count, and its purpose.
    key_point: The paper says WorkArena is a remote-hosted benchmark of 33 tasks built on ServiceNow to measure how well agents perform typical enterprise knowledge-work tasks.
  - source_title: WorkArena paper HTML version
    source_url: https://arxiv.org/html/2403.07718v5
    source_type: research_paper
    relevance: Confirms the benchmark’s scale and that it covers many unique task instances, not just one-off examples.
    key_point: The paper describes WorkArena as a realistic benchmark of enterprise-related tasks with 19,912 unique task instances.
  - source_title: WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks
    source_url: https://openreview.net/forum?id=PCjK8dqrWW
    source_type: research_paper
    relevance: Shows the related follow-up benchmark, which helps distinguish WorkArena from its extension.
    key_point: The follow-up paper extends the WorkArena idea towards more complex planning and reasoning tasks, showing that WorkArena is the original benchmark rather than the more advanced variant.
---

WorkArena is a benchmark for testing how well an AI agent can do common knowledge-work tasks in a browser, usually in ServiceNow.

In practice, it gives the agent tasks that look like real office work, such as moving through forms, dashboards, lists, and service requests. The point is to see whether the agent can complete multi-step work in a real business system, not just answer questions.

It matters because many agents can sound capable but still struggle with the messy steps needed to finish real work. WorkArena helps researchers compare agents on tasks that are closer to day-to-day enterprise use.

It is not a general test of all AI systems. It is not proof that an agent is ready for any company job. It is also not the same as WorkArena++, which is a later benchmark built to test more complex planning and reasoning tasks.
