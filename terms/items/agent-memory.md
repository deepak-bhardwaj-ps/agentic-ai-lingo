---
slug: agent-memory
title: Agent Memory
short_description: Information kept outside the model so an agent can remember useful facts, preferences, and past steps across turns or sessions.
category: Memory
tags:
- agentic-ai
- memory
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the model itself learning forever
- Treating it as a full transcript of every chat
- Assuming all memory is accurate, private, or permanent
related_terms:
- context window
- working memory
- long-term memory
- retrieval
- memory governance
evidence:
- source_title: Memory FAQ
  source_url: https://help.openai.com/articles/8590148-memory-faq
  source_type: official_docs
  relevance: Shows a current product definition of memory as stored information used to personalise later chats.
  key_point: Memory can remember useful context across chats, files, and connected apps so users do not need to repeat themselves.
- source_title: Adding memory to Semantic Kernel Agents
  source_url: https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-memory
  source_type: official_docs
  relevance: Describes agent memory as a separate capability that can persist user preferences and context across threads.
  key_point: Agent memory is an external layer that stores and recalls selected information for later use.
- source_title: Glossary
  source_url: https://docs.anthropic.com/en/docs/resources/glossary
  source_type: official_docs
  relevance: Gives the baseline distinction between a model's context window and the model's training data.
  key_point: The context window is the model's working memory, which is separate from longer-lived stored memory.
---

Agent memory is stored information that helps an AI agent remember useful things across chats or tasks.

In practice, a system keeps selected facts, preferences, instructions, or past steps in a separate place, then brings back the useful parts when the agent needs them. This can help the agent avoid asking the same questions again and stay more consistent over time.

This matters because a model can only use a limited amount of text at once. Agent memory helps it work across many turns or even later sessions without relying only on the current chat.

It is not the model secretly learning forever. It is also not a full copy of every message. Good agent memory is selective, can be corrected or removed, and still needs rules for privacy, accuracy, and who can change it.
