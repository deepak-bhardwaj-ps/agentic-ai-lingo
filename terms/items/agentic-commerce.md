---
slug: agentic-commerce
name: Agentic Commerce
category: Core
title: Agentic Commerce
aliases:
short_description: Agentic commerce is commerce in which an agent can compare
termStatus: Emerging industry label
researchBasis: OWASP Top 10 for LLM Applications, Anthropic, OpenAI Agents SDK
sources:
- https://developers.openai.com/api/docs/guides/agents
---

## Term status

Emerging industry label.

## Meaning

Agentic commerce describes shopping, comparison, ordering, and payment flows initiated or completed by an agent for a user or business.

## Boundary

It is not a payments protocol. It requires explicit authority, merchant and user identity, transaction limits, confirmation, receipts, and dispute handling.

## How it is used

It is used when buying, booking, reordering, or negotiating is delegated to a system that can act on the user’s behalf. The hard part is not the shopping flow; it is the authority to spend, the verification of intent, and the audit trail for what was actually agreed.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) frames the security side: delegated actions need explicit controls and auditability.

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) emphasises tool use, checkpoints, and human feedback when autonomy crosses into action.

[OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) reinforces the same operational split between orchestration, state, tools, and [[Guardrails|guardrails]].
