---
slug: context-debt
title: Context Debt
short_description: The build-up of stale, duplicated, missing, or poorly delivered
  context that makes an AI agent less accurate and more expensive to run.
category: Context
tags:
- context
- retrieval
- prompting
- agents
status: Emerging practitioner shorthand
aliases:
- context debt
- prompt debt
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal technical standard rather than a loose shorthand.
- Using it to mean any bad prompt, even when the real issue is retrieval, memory,
  or token limits.
related_terms:
- retrieval-augmented generation
- context window
- prompt caching
- compaction
- token budget
evidence:
- source_title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
  source_url: https://arxiv.org/abs/2005.11401
  source_type: research_paper
  relevance: Establishes the core idea of supplying external retrieved information
    to a model at generation time.
  key_point: RAG shows that model quality depends on what context is retrieved and
    provided, which is the basis for discussing context quality and freshness.
- source_title: Prompt caching
  source_url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
  source_type: official_docs
  relevance: Shows that repeated prompt prefixes can be cached to reduce cost and
    latency.
  key_point: Repeated or unchanged context has a direct cost, so poor context handling
    can waste tokens and time.
- source_title: Manage costs effectively - Claude Code Docs
  source_url: https://docs.anthropic.com/en/docs/claude-code/costs
  source_type: official_docs
  relevance: Describes how stale context wastes tokens in ongoing sessions.
  key_point: Old context carries a real cost and can keep harming later messages if
    it is not cleared or compacted.
---

Context debt is the build-up of stale, duplicated, missing, or badly organised information that an AI agent has to carry when it works.

In practice, it means the agent may be given old summaries, repeated notes, irrelevant documents, or too much text to think clearly. That can make answers slower, more expensive, and less accurate.

The term matters because AI systems do better when the right information is current, short, and easy to use. If the context is messy, the model has more noise to sort through and less room for what actually matters.

Context debt is not a formal technical standard. It is also not the same thing as a bug in the model itself. It usually points to a problem in how information is gathered, updated, filtered, compacted, or passed into the agent.
