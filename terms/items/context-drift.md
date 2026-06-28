---
slug: context-drift
title: Context Drift
category: Context
short_description: A gradual change in the information an AI system uses, which can
  quietly change its answers or actions.
tags:
- context
- retrieval
- agents
- prompts
status: emerging
aliases:
- context drift
meaning_type: emerging_unsettled
novelty_level: low
maturity_level: emerging
common_misuse:
- Using it to mean any model mistake, even when the real problem is a bad prompt,
  missing data, or a model limit.
- Treating it as a formal technical standard instead of a loose practitioner term.
related_terms:
- context window
- retrieval-augmented generation
- prompt engineering
- memory
- long-context
evidence:
- source_title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
  source_url: https://arxiv.org/abs/2005.11401
  source_type: research_paper
  relevance: Establishes the idea of combining retrieved evidence with model generation,
    which is the core setting where context quality and freshness matter.
  key_point: When the evidence supplied to the model changes, the model’s behaviour
    can change too.
- source_title: Prompt engineering
  source_url: https://developers.openai.com/api/docs/guides/prompt-engineering
  source_type: official_docs
  relevance: Shows that model output depends on the instructions and context you provide.
  key_point: Clear and effective context is part of getting reliable results from
    a model.
- source_title: Prompt guidance
  source_url: https://developers.openai.com/api/docs/guides/prompt-guidance
  source_type: official_docs
  relevance: Describes monitoring context usage, compacting conversations, and keeping
    prompts stable when resuming work.
  key_point: Changes in the active context can change behaviour, so systems should
    manage context deliberately.
---

Context drift is when the information an AI system is using slowly changes, and that change starts to affect what it says or does.

In practice, this usually means the model is seeing a different mix of messages, retrieved documents, memories, or instructions than it saw before. The change may be small at first, but over time it can make the system less consistent, less accurate, or less predictable.

This matters because AI tools do not think from scratch each time. They depend on the context they are given. If that context becomes stale, incomplete, reordered, compressed badly, or replaced with the wrong evidence, the system may make different decisions without any obvious error message.

Context drift is not the same as a model “learning” on its own. It is also not a formal technical category with one strict definition. People often use it as shorthand for a context problem: the inputs changed, so the output changed.
