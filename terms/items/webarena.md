---
title: WebArena
short_description: A benchmark for testing web agents on realistic, self-hosted websites
category: Evals and benchmarks
tags: [benchmark, evals, web-agents, browser-automation]
status: active
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating WebArena as a browser tool, agent framework, or product instead of a benchmark.
  - Assuming a good score on WebArena means an agent will work reliably on the open internet.
  - Using WebArena as a synonym for all web-agent tests, including newer variants like VisualWebArena.
related_terms:
  - web-agent benchmark
  - browser automation
  - multimodal agent
  - VisualWebArena
  - evaluation harness
evidence:
  - source_title: WebArena project website
    source_url: https://webarena.dev/
    source_type: official_docs
    relevance: This is the current project home page and gives the simplest official description of the term.
    key_point: WebArena is described as a suite of benchmarks for building autonomous web agents.
  - source_title: WebArena: A Realistic Web Environment for Building Autonomous Agents
    source_url: https://arxiv.org/abs/2307.13854
    source_type: research_paper
    relevance: This is the original paper that introduced the benchmark and explains its scope and purpose.
    key_point: The paper defines WebArena as a realistic, reproducible web environment with tasks on common websites and says it is used to evaluate long-horizon web agents.
  - source_title: web-arena-x/webarena
    source_url: https://github.com/web-arena-x/webarena
    source_type: engineering_blog
    relevance: The repository shows how the benchmark is packaged and used in practice, which helps distinguish it from a general product.
    key_point: The repo describes WebArena as a standalone, self-hostable web environment for building autonomous agents and notes that it is the canonical implementation of the benchmark.
---

WebArena is a benchmark for testing web agents on realistic websites that are set up to be self-hosted and reproducible.

In practice, it gives an agent tasks to do on websites such as shopping, forums, software development, maps, or content management. The agent must use the site, follow instructions, and finish the task correctly. The score is based on whether the final result matches the goal.

The term matters because web agents can look good in simple demos but fail on longer, messier tasks. WebArena helps researchers compare agents on the same kind of work and see whether they can handle real website behaviour, not just short question-answer steps.

WebArena is not a browser, a chatbot, or an agent framework. It is also not the same as the open internet. It is a controlled test environment for measuring how well a web agent can complete tasks.
