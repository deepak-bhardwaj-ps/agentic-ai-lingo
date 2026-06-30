---
title: AgentDojo
short_description: Benchmark environment for testing whether AI agents can be hijacked by prompt injection while using tools.
category: Evals and benchmarks
tags: [agent-security, prompt-injection, benchmark, llm-agents]
status: draft
aliases: []
meaning_type: novel
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general AI benchmark instead of a security-focused environment for agent hijacking and prompt injection.
  - Assuming it only measures model quality, when it also measures whether the agent follows malicious instructions hidden in tool outputs or other untrusted data.
related_terms:
  - prompt injection
  - indirect prompt injection
  - agent hijacking
  - AI agent benchmark
  - agent security
evidence:
  - source_title: AgentDojo official documentation
    source_url: https://agentdojo.spylab.ai/
    source_type: official_docs
    relevance: The project site explains how the benchmark is used and what it is for.
    key_point: AgentDojo is presented as a dynamic environment for evaluating prompt injection attacks and defenses for LLM agents.
  - source_title: AgentDojo paper
    source_url: https://arxiv.org/abs/2406.13352
    source_type: research_paper
    relevance: The paper is the main technical definition of the term.
    key_point: AgentDojo is an evaluation framework for agents that use tools over untrusted data, and it is designed to study prompt injection attacks and defences.
  - source_title: NIST technical blog on agent hijacking evaluations
    source_url: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations
    source_type: engineering_blog
    relevance: Shows how a public-sector evaluation team used and extended AgentDojo in practice.
    key_point: AgentDojo is used as a framework for testing agent hijacking, and NIST extended it with new injection tasks for higher-risk scenarios.
---

AgentDojo is a benchmark environment for testing whether an AI agent can be tricked into doing the wrong thing by hidden instructions in the data it reads.

In practice, it is used to see if an agent can finish a normal task while ignoring malicious prompt injection. The agent may be reading emails, web pages, or other tool outputs that contain instructions written by an attacker.

The term matters because agent systems can fail in a different way from ordinary chatbots. They do not just need to answer questions well. They also need to avoid following bad instructions that arrive through tools, search results, or other untrusted content.

AgentDojo is not a general label for all AI testing. It is a specific security benchmark and environment. It is also not just about raw model intelligence. Its focus is on safety against prompt injection and agent hijacking.
