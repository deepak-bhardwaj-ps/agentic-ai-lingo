---
slug: context-rot
title: Context Rot
short_description: A term for when an AI system becomes less reliable as its context gets longer, noisier, or more out of date.
category: Context
tags:
  - llm
  - context-window
  - agent
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse: Treating it as a formal technical term, or using it to mean any AI mistake instead of a drop in quality caused by too much, too messy, or too stale context.
related_terms:
  - context engineering
  - context window
  - retrieval augmented generation
  - prompt engineering
evidence:
  - source_title: Effective context engineering for AI agents
    source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    source_type: engineering_blog
    relevance: Gives a current, plain-language explanation of why managing context matters for agents.
    key_point: Anthropic says context is the set of tokens available to the model and notes that as context grows, models can lose focus and recall becomes less reliable.
  - source_title: Context Rot: How Increasing Input Tokens Impacts LLM Performance
    source_url: https://www.trychroma.com/research/context-rot
    source_type: research_paper
    relevance: The source that popularised the term and measured the effect directly.
    key_point: Chroma reports that performance consistently degrades as input length increases across models and tasks, which supports the idea behind context rot.
  - source_title: Context Length Alone Hurts LLM Performance Despite Perfect Retrieval
    source_url: https://arxiv.org/pdf/2510.05381
    source_type: research_paper
    relevance: Shows the problem is not only missing information, but also the length of the input itself.
    key_point: The paper finds that long-context models can still perform worse even when relevant information is present and retrieval is controlled.
---

Context rot is when an AI system becomes less reliable because the information it is given is too long, too messy, or too out of date.

In practice, the model may miss the important part, focus on the wrong detail, or keep using old information after newer information has arrived. The problem is not just having more text. It is also about whether the right facts are still easy to find and whether the context still matches the current task.

The term matters because AI systems can get worse quietly as more messages, documents, or tool results are added. A reply can sound confident and still be wrong if the useful facts are buried under noise or stale notes.

Context rot is not a formal standard with one fixed definition. It is a practical label for a real problem that shows up in long chats, weak summaries, poor retrieval, and badly managed context.
