---
title: MiniWoB++
short_description: A benchmark suite of small web-browser tasks used to test whether an AI agent can click, type, drag, and fill forms correctly.
category: Evals and benchmarks
tags:
  - web-benchmarks
  - agent-evals
  - browser-automation
status: draft
aliases:
  - MiniWob++
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
  - Treating it as a single app instead of a suite of many small browser tasks.
  - Assuming it measures general intelligence rather than task performance on scripted web actions.
  - Confusing it with newer, harder web benchmarks that test longer or more realistic workflows.
related_terms:
  - MiniWoB
  - WebArena
  - WorkArena
  - WebShop
evidence:
  - source_title: MiniWoB++ Documentation
    source_url: https://miniwob.farama.org/index.html
    source_type: official_docs
    relevance: The project’s current documentation defines the living benchmark and its interface, so it is the best source for what MiniWoB++ is today.
    key_point: The library contains over 100 web interaction environments and provides JavaScript and Python interfaces for programmatic browser interaction.
  - source_title: Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration
    source_url: https://arxiv.org/pdf/1802.08802
    source_type: research_paper
    relevance: This is the paper that introduced MiniWoB++ and explains why it was created as an extension of the earlier MiniWoB benchmark.
    key_point: MiniWoB++ was released as a benchmark of web tasks designed to test harder web-agent behaviours such as longer time horizons, soft natural-language reasoning, and changing layouts.
  - source_title: World of Bits: An Open-Domain Platform for Web-Based Agents
    source_url: https://proceedings.mlr.press/v70/shi17a.html
    source_type: research_paper
    relevance: This earlier paper explains the original MiniWoB family and shows the lineage from World of Bits to MiniWoB and then MiniWoB++.
    key_point: The benchmark family is built around agents completing web tasks with low-level keyboard and mouse actions in browser-like environments.
  - source_title: A Data-Driven Approach for Learning to Control Computers
    source_url: https://proceedings.mlr.press/v162/humphreys22a/humphreys22a.pdf
    source_type: research_paper
    relevance: This later paper shows how MiniWoB++ is used in current agent research and confirms the practical task range.
    key_point: MiniWoB++ is described as a suite of browser-based tasks ranging from simple button clicking to more complex form filling.
---

MiniWoB++ is a benchmark suite of small web-browser tasks.

In practice, it gives an AI agent a short instruction and a browser page, then checks whether the agent can do the right actions, such as clicking buttons, typing into fields, dragging items, or filling in forms.

It matters because researchers use it to measure how well an agent can handle simple web interactions before trying harder real-world tasks. It is useful for comparing models and testing whether an agent can follow instructions inside a browser.

It is not a single app, and it is not a general test of intelligence. It is also not the same as newer web benchmarks that focus on longer, messier, more realistic workflows.
