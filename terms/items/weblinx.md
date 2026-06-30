---
title: WebLINX
short_description: A benchmark and dataset for conversational web navigation, where an agent uses a browser to follow multi-turn instructions on real websites.
category: Evals
tags: [benchmark, dataset, web-navigation, agents, evaluation]
status: active
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating WebLINX as a browser product or chatbot instead of a benchmark and dataset.
  - Using it to claim general web-agent ability on all websites.
  - Confusing the original WebLINX release with the later BrowserGym packaging of WebLINX.
related_terms:
  - BrowserGym
  - WebArena
  - MiniWoB
  - Mind2Web
evidence:
  - source_title: WebLINX: Real-World Website Navigation with Multi-Turn Dialogue
    source_url: https://arxiv.org/abs/2402.05930
    source_type: research_paper
    relevance: Primary paper that defines the term and describes the benchmark.
    key_point: The paper introduces WebLINX as a large-scale benchmark for conversational web navigation with 100K interactions from 2,300 expert demonstrations across more than 150 real websites.
  - source_title: McGill-NLP/weblinx
    source_url: https://github.com/mcgill-nlp/weblinx
    source_type: engineering_blog
    relevance: Official repository that confirms how the project is framed and how it is used today.
    key_point: The repo describes WebLINX as a benchmark for building web navigation agents with conversational capabilities and notes that it is now available through BrowserGym.
  - source_title: BrowserGym, a Gym environment for web task automation
    source_url: https://github.com/servicenow/browsergym
    source_type: engineering_blog
    relevance: Official BrowserGym repository showing the current packaging of the benchmark.
    key_point: BrowserGym lists WebLINX as a built-in static benchmark, which helps distinguish the benchmark itself from the platform that now hosts it.
---
WebLINX is a benchmark and dataset for testing how well an AI agent can navigate websites in a browser while following instructions across multiple turns of a conversation.

In practice, this means the agent has to read what the user wants, look at the page, choose actions like clicking or typing, and keep going as the task changes. The focus is on web browsing behaviour, not on writing essays or answering general trivia.

The term matters because web tasks are messy and real websites change often. A benchmark like WebLINX helps researchers compare agents on the same tasks and see where they still struggle, especially on websites they have not seen before.

WebLINX is not a web browser product, and it is not proof that an agent can safely do any web task in the real world. It is also not the same thing as every other web benchmark. The original WebLINX release is a dataset and benchmark, while BrowserGym is the platform that now packages it for use.
