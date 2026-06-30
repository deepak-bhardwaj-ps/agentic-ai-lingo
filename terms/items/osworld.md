---
title: OSWorld
short_description: A benchmark for testing how well multimodal agents can complete real computer tasks across desktop apps and operating systems.
category: Evals and benchmarks
tags:
  - benchmark
  - computer-use agents
  - multimodal agents
  - GUI
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating OSWorld as the operating system itself, rather than a benchmark that runs on real computer environments.
  - Treating one OSWorld score as proof that an agent will work well for all computer tasks.
  - Confusing OSWorld with other computer-use benchmarks that build on it or use a similar name.
related_terms:
  - computer-use agent
  - multimodal agent
  - GUI grounding
  - execution-based evaluation
  - benchmark suite
evidence:
  - source_title: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments
    source_url: https://arxiv.org/abs/2404.07972
    source_type: research_paper
    relevance: Original paper that defines OSWorld and explains what it is meant to measure.
    key_point: Presents OSWorld as a scalable real computer environment for multimodal agents, with 369 tasks across web and desktop apps, file operations, and multi-application workflows.
  - source_title: OSWorld project page
    source_url: https://os-world.github.io/
    source_type: official_docs
    relevance: Official benchmark page with the clearest plain-language description of the environment and tasks.
    key_point: Describes OSWorld as a real computer environment for multimodal agents across Ubuntu, Windows, and macOS, and shows that it uses execution-based evaluation.
  - source_title: xlang-ai/OSWorld
    source_url: https://github.com/xlang-ai/OSWorld
    source_type: engineering_blog
    relevance: Official repository for the benchmark, useful for confirming it is an active maintained project rather than a one-off paper result.
    key_point: States that OSWorld is the official repository for the benchmark and notes later updates such as OSWorld-Verified, which shows the term refers to a living benchmark family.
---

OSWorld is a benchmark that tests how well an AI agent can use a real computer to do tasks.

In practice, the agent has to look at the screen, understand what is happening, and click, type, or switch between apps to finish a job. The tasks are built to feel like normal computer use, such as working in desktop software, moving files, or carrying out steps across more than one app.

It matters because many agents can answer questions well but still struggle when they must act inside a computer interface. OSWorld helps compare those agents in a more realistic setting.

OSWorld is not the computer operating system itself. It is not a general measure of intelligence, and a good score does not mean an agent will work well on every real task. The term is still part of a fast-moving area, so people often use it as shorthand for the benchmark and the environment behind it.
