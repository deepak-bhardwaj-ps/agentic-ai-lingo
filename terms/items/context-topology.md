---
title: Context Topology
short_description: A way of describing where an AI system gets its context, how that
  context is chosen, and how it moves between stores, tools, and model calls
category: Context
tags:
- agentic-ai
- context
- retrieval
- terminology
status: emerging
aliases:
- context map
- context flow
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal standard term when it is mostly practitioner shorthand
- Using it to mean only retrieval, when it also includes selection, movement, freshness,
  and control
related_terms:
- Retrieval-Augmented Generation
- context engineering
- prompt caching
- retrieval
- memory
evidence:
- source_title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
  source_url: https://arxiv.org/abs/2005.11401
  source_type: research_paper
  relevance: Foundational paper for systems that bring outside information into generation
    time.
  key_point: RAG combines a model with retrieved passages, showing that useful context
    can come from external sources at runtime.
- source_title: Effective context engineering for AI agents
  source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  source_type: engineering_blog
  relevance: Current engineering explanation of how teams curate the tokens an agent
    uses during inference.
  key_point: Context engineering is about selecting and maintaining the right information,
    not just writing one prompt.
- source_title: Context windows
  source_url: https://docs.anthropic.com/en/docs/build-with-claude/context-windows
  source_type: official_docs
  relevance: Defines the model's working memory and explains why context size and
    quality matter.
  key_point: A model can only use the text in its context window, so what enters that
    window is a design choice.
- source_title: Prompt caching
  source_url: https://developers.openai.com/api/docs/guides/prompt-caching
  source_type: official_docs
  relevance: Shows that repeated prompt prefixes can be reused across calls.
  key_point: Cached prompt prefixes make context reuse and movement an operational
    concern, not just a prompt-writing detail.
---

Context topology is the shape of where an AI system’s context lives and how it moves.

In practice, it means tracking what comes from the user, what comes from memory or search, what comes from tools, and what finally reaches the model for one answer.

It matters because an AI system is only as good as the information it can actually see. If the wrong facts are sent, the facts are old, or the context is too large, the answer can become wrong, slow, or unsafe.

It is not a fixed product category or an official standard. People use it as shorthand for the design of context flow in an AI system.

It is also not just retrieval. It includes where information is stored, who can use it, how fresh it is, how much can fit in the model’s [[Working Memory|working memory]], and what gets reused between calls.
