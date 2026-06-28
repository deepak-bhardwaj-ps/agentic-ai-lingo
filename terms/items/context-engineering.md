---
slug: context-engineering
name: Context Engineering
category: Context
title: Context Engineering
aliases: []
short_description: The deliberate work of choosing, shaping, and updating the information
  an AI model sees before it answers.
status: emerging
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a new name for prompt engineering only
- Using it to describe any AI feature without explaining the context being managed
- Assuming it is a fixed standard term with one agreed definition
related_terms:
- prompt engineering
- context window
- retrieval-augmented generation
- memory
- tool use
evidence:
- source_title: Effective context engineering for AI agents
  source_url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  source_type: engineering_blog
  relevance: Directly defines context engineering as curating and maintaining the
    right set of tokens and explains how it differs from prompt engineering.
  key_point: Context engineering is about selecting and maintaining the best information
    for a model call, not just writing better prompts.
- source_title: Context engineering in agents
  source_url: https://docs.langchain.com/oss/python/langchain/context-engineering
  source_type: official_docs
  relevance: Shows the term used in agent-building practice and ties it to reliability,
    tools, memory, and state.
  key_point: The main job is getting the right information and tools into the right
    format so the model can do the task.
- source_title: A Survey of Context Engineering for Large Language Models
  source_url: https://arxiv.org/abs/2507.13334
  source_type: research_paper
  relevance: Gives a research view that treats the topic as a broader discipline covering
    retrieval, processing, management, and system design.
  key_point: Context engineering goes beyond prompt design and includes retrieval,
    processing, management, memory systems, tool reasoning, and multi-agent systems.
---

Context engineering is the careful work of choosing and shaping the information an AI model sees before it answers.

In practice, it means deciding what instructions, facts, chat history, memory, tools, and summaries should be included, and what should be left out. The goal is to give the model the most useful context without wasting space or confusing it.

It matters because AI models only use the information that fits in their context window. If the wrong details are included, or important details are missing, the model can give a worse answer.

It is not just prompt engineering with a new name. Prompt engineering is mainly about writing good instructions. Context engineering is broader: it also includes what information is retrieved, stored, compressed, and passed into the model at the right time.
