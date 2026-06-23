---
slug: guardrails
name: Guardrails
category: Governance
title: Guardrails
aliases: null
short_description: Guardrails are the rules and constraints that limit what an agent
termStatus: Established industry label
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Established industry label.

## Meaning

Guardrails are controls that constrain or detect unsafe inputs, outputs and actions: schemas, allow-lists, policy checks, approvals, rate limits and sandboxing.

## Boundary

Guardrails are not a security boundary when implemented only in a prompt. Enforce high-impact controls outside the model.

## How it is used

Guardrails is used when the system needs hard constraints on what the agent may do. In practice, the guardrail has to be testable and enforceable.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
