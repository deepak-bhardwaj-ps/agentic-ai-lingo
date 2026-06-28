---
slug: context-constructor
title: Context Constructor
short_description: A context constructor is the part of an AI system that chooses
  and assembles the information sent to the model for one request.
category: Context
tags:
- context
- agents
- retrieval
- orchestration
status: active
aliases:
- context assembly
- context builder
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal industry standard term
- Confusing it with retrieval alone
- Assuming it only means copying text into a prompt
related_terms:
- context engineering
- retrieval-augmented generation
- prompt engineering
- model context protocol
evidence:
- source_title: Prompt engineering | OpenAI API
  source_url: https://developers.openai.com/api/docs/guides/prompt-engineering
  source_type: official_docs
  relevance: Explains that adding relevant context to a model request is often necessary
    and links this to retrieval-augmented generation.
  key_point: Context can be gathered from outside the model and included in the request,
    so the system must decide what to add.
- source_title: Effective context engineering for AI agents
  source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  source_type: engineering_blog
  relevance: Describes context engineering as selecting and maintaining the right
    tokens during inference.
  key_point: The hard part is curating the best information for the limited context
    window.
- source_title: What is the Model Context Protocol (MCP)?
  source_url: https://docs.anthropic.com/en/docs/agents-and-tools/mcp
  source_type: official_docs
  relevance: Shows how AI apps connect to external systems that can supply data, tools,
    and workflows for the context layer.
  key_point: A context constructor may need to pull from files, databases, tools,
    and workflows, not just prompts.
- source_title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
  source_url: https://arxiv.org/abs/2005.11401
  source_type: research_paper
  relevance: The core RAG paper that underpins the idea of fetching external information
    before generation.
  key_point: Retrieving outside information before generating text is a recognised
    pattern, even if the label "context constructor" is not standard.
---

A context constructor is the part of an AI system that chooses and assembles the information sent to the model for one request.

In practice, it decides what to include from the user’s message, saved state, retrieved documents, tool results, rules, and other notes. It also decides what to leave out when the context window is getting full.

The term matters because a model only works with the information it is given. If the wrong facts are included, or important ones are missing, the answer can be weak, late, or wrong.

It is not a formal product category, and it is not the same as retrieval alone. Retrieval finds information; a context constructor turns that information into the final package the model sees.
