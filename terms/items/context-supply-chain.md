---
slug: context-supply-chain
title: Context Supply Chain
short_description: The chain of people, systems, and steps that decide what information
  reaches an AI agent at the moment it answers.
category: Context
tags:
- context
- retrieval
- agents
- lineage
- governance
status: emerging
aliases:
- context pipeline
- retrieval and prompt supply chain
- context lineage
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal industry standard
- Using it to mean only retrieval, when it also includes preparation, permissions,
  freshness, and delivery
- Assuming it is the same as the model’s training data
related_terms:
- Retrieval-Augmented Generation
- context window
- prompt engineering
- data lineage
- provenance
evidence:
- source_title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
  source_url: https://arxiv.org/abs/2005.11401
  source_type: research_paper
  relevance: Primary research showing that a model can use retrieved external information
    at generation time.
  key_point: RAG combines retrieval with generation, which supports the idea that
    runtime context can come from upstream sources rather than only the model’s training
    data.
- source_title: Context windows
  source_url: https://docs.anthropic.com/en/docs/build-with-claude/context-windows
  source_type: official_docs
  relevance: Defines the model’s working memory and distinguishes it from training
    data.
  key_point: The context window is the text a model can use while answering, so the
    path by which that text arrives matters.
- source_title: Prompt caching
  source_url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
  source_type: official_docs
  relevance: Shows that repeated context can be stored and reused, making delivery
    and reuse of context an operational concern.
  key_point: Caching is about how prompt content is carried forward efficiently, which
    is part of managing context flow.
- source_title: Prompt Caching in the API
  source_url: https://openai.com/index/api-prompt-caching/
  source_type: official_docs
  relevance: Confirms that prompt reuse, cost, and latency are practical concerns
    in real agent systems.
  key_point: Reusing prompt content affects performance and cost, so the path from
    source material to model input has operational value.
---

## Meaning

Context supply chain means the path information takes before an AI agent uses it to answer.

It includes where the information came from, how it was chosen, how it was cleaned or shortened, who is allowed to see it, and how it is sent into the model.

## In practice

If an agent answers a question from company documents, the context supply chain is everything between the original document and the final prompt the model reads.

That can include search, ranking, filtering, summarising, permission checks, freshness checks, prompt assembly, and caching.

## Why it matters

If this chain is weak, the agent can use the wrong facts, miss newer facts, or see information it should not have seen.

It also matters for debugging. When an answer is wrong, you need to know whether the problem came from the source, the retrieval step, the prompt, or the delivery step.

## What it is not

It is not a formal product category.

It is not the same as the model’s training data.

It is not just retrieval. It also includes the steps that shape, protect, and deliver the information the model gets at runtime.
