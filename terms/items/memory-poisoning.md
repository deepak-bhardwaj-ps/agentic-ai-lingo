---
title: Memory poisoning
short_description: Memory poisoning is when someone puts bad or misleading information into an AI agent's long-term memory so it changes later behaviour.
category: Governance and security
tags:
- agentic-ai
- security
- memory
- context-poisoning
status: emerging
aliases:
- Persistent memory poisoning
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as prompt injection in one chat
- Using it for any wrong answer, even when no stored memory was changed
- Assuming the model can safely filter poisoned memory by itself
related_terms:
- Context poisoning
- Prompt injection
- Indirect prompt injection
- RAG poisoning
- Data poisoning
evidence:
- source_title: OWASP Agent Memory Guard
  source_url: https://owasp.org/www-project-agent-memory-guard/
  source_type: official_docs
  relevance: OWASP treats memory poisoning as a real security problem for agents with persistent memory.
  key_point: Persistent agent memory can be corrupted, and that corruption can affect behaviour across sessions.
- source_title: Memory Poisoning Attack and Defense on Memory Based LLM-Agents
  source_url: https://arxiv.org/abs/2601.05504
  source_type: research_paper
  relevance: Gives a direct research definition for memory poisoning in LLM agents.
  key_point: Adversaries can inject malicious instructions into long-term memory and influence future responses.
- source_title: OWASP Top 10 for Agentic Applications for 2026
  source_url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
  source_type: standards_doc
  relevance: Places memory poisoning inside a current security taxonomy for agentic systems.
  key_point: OWASP treats memory and context poisoning as a major risk for systems that plan and act over time.
---

Memory poisoning is when bad or misleading information gets into an AI agent's long-term memory and changes what it does later.

In practice, this means the agent stores something it should not trust, then reads it back in a later session or task. The bad memory can come from a document, web page, chat message, tool output, or another place the agent treats as memory.

This matters because long-term memory is meant to help the agent remember useful facts. If an attacker poisons that memory, the agent may make bad choices, reveal information, or do the wrong thing much later, when the original bad input is no longer visible.

It is not the same as one-off prompt injection in a single chat. It is also not the same as training-data poisoning, which changes the data used to train a model. Memory poisoning targets stored memory used after the model has already been built.
