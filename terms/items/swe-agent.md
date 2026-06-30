---
title: SWE-agent
short_description: An AI agent project that helps a language model work through software engineering tasks in code repositories.
category: Evals and benchmarks
tags:
- coding-agents
- software-engineering
- ai-agents
- benchmarks
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating SWE-agent as the same thing as SWE-bench
- Assuming it is a general-purpose chatbot instead of a coding agent built for software tasks
- Using the name for any AI that edits code, even when it is not this specific project
related_terms:
- coding agent
- software engineering agent
- SWE-bench
- agent-computer interface
- tool use
evidence:
  - source_title: SWE-agent paper, "Agent-Computer Interfaces Enable Automated Software Engineering"
    source_url: https://arxiv.org/abs/2405.15793
    source_type: research_paper
    relevance: This is the main research paper for the project and gives the clearest definition of what SWE-agent is meant to do.
    key_point: SWE-agent is a system that lets language model agents use computers to solve software engineering tasks, including browsing repositories, editing files, and running tests.
  - source_title: SWE-agent GitHub repository
    source_url: https://github.com/SWE-agent/SWE-agent
    source_type: official_docs
    relevance: The official repository shows the project’s current positioning and confirms that it is an active coding-agent system, not just a paper idea.
    key_point: SWE-agent is described as a tool that takes a GitHub issue and tries to automatically fix it using a language model.
  - source_title: SWE-agent documentation background page
    source_url: https://github.com/princeton-nlp/SWE-agent/blob/main/docs/background/index.md
    source_type: official_docs
    relevance: This documentation page explains how the project frames its own behaviour and why it uses a special interface for software tasks.
    key_point: SWE-agent turns language models into software engineering agents that can fix issues in GitHub repositories through an agent-computer interface.
  - source_title: SWE-bench repository
    source_url: https://github.com/swe-bench/SWE-bench
    source_type: official_docs
    relevance: SWE-agent is closely tied to SWE-bench, and this source helps separate the agent from the benchmark it is evaluated on.
    key_point: SWE-bench is the benchmark; SWE-agent is one of the systems evaluated on real GitHub issues.
---

SWE-agent is an AI coding agent project that helps a language model work on software engineering tasks in a code repository.

In practice, it can read files, edit code, and run tests so it can try to fix a GitHub issue or complete a coding task step by step.

This matters because normal chatbots only answer questions. SWE-agent is built to do the messy work of navigating a real project and making changes inside it.

It is not the same as SWE-bench, which is the benchmark used to test these systems. It is also not a general chatbot, and it is not a guarantee that the code it writes is correct.
