---
title: WorkArena-Lite
short_description: A lighter name for the basic WorkArena task set, usually meaning the low-level ServiceNow benchmark tasks.
category: Evals
tags: [benchmark, evals, web-agents, browser-automation, enterprise-software]
status: active
aliases: [WorkArena-L1]
meaning_type: overloaded_buzzword
novelty_level: low
maturity_level: emerging
common_misuse:
  - Treating WorkArena-Lite as a separate benchmark family when it is usually just the simpler WorkArena task set.
  - Assuming it means a small or toy dataset rather than a benchmark for real enterprise UI tasks.
  - Using it as a synonym for WorkArena++ or for the full WorkArena benchmark without checking which task level is meant.
related_terms:
  - WorkArena
  - WorkArena++
  - BrowserGym
  - web-agent benchmark
  - enterprise software
evidence:
  - source_title: ServiceNow/WorkArena repository
    source_url: https://github.com/ServiceNow/workarena
    source_type: official_docs
    relevance: The project repository is the primary source for how the benchmark is named and structured today.
    key_point: The repo describes WorkArena as a benchmark for knowledge-work tasks and says the WorkArena-L1 set contains 19,912 instances from 33 atomic ServiceNow tasks.
  - source_title: WorkArena project website
    source_url: https://servicenow.github.io/WorkArena/
    source_type: official_docs
    relevance: This is the current public project page and gives the plain-language definition used by the authors.
    key_point: It describes WorkArena as browser-based tasks for routine knowledge-worker work on the ServiceNow platform, which matches the meaning behind the lite/basic task set.
  - source_title: WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?
    source_url: https://arxiv.org/abs/2403.07718
    source_type: research_paper
    relevance: This is the original paper and the most authoritative source for the benchmark’s scope and task design.
    key_point: The paper defines WorkArena as a remote-hosted benchmark on ServiceNow for evaluating web agents on common knowledge-work tasks, with low-level atomic tasks as the base benchmark.
  - source_title: BrowserGym repository
    source_url: https://github.com/servicenow/browsergym
    source_type: official_docs
    relevance: BrowserGym is the main evaluation environment that now packages WorkArena, so it helps confirm how the benchmark is used in practice.
    key_point: The repository lists WorkArena as one of the default BrowserGym benchmarks and shows that the atomic WorkArena task set is the basic level, distinct from higher-composition variants.
---
WorkArena-Lite is the lighter name for the basic WorkArena benchmark. It usually means the simpler, low-level ServiceNow tasks that make up the “atomic” task set.

In practice, these tasks ask an agent to do routine office-style work in a browser, such as finding information, filling forms, filtering lists, using menus, or ordering items from a service catalogue. The point is to check whether an agent can carry out common work steps correctly on enterprise software.

The term matters because “lite” suggests a smaller or easier version, but it is still a real benchmark for browser agents. It is used to measure whether a system can handle basic office workflows before moving on to harder tasks.

It is not a general term for all WorkArena benchmarks. It is also not the same as WorkArena++, which adds more complex, multi-step planning tasks.
