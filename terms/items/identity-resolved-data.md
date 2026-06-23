---
slug: identity-resolved-data
name: Identity-Resolved Data
category: Context
title: Identity-Resolved Data
aliases: null
short_description: Identity-Resolved Data is data tied to a specific principal, role,
termStatus: Governance/security concept
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Governance/security concept.

## Meaning

Identity-Resolved Data concerns constraining, attributing or reviewing an agent's ability to act on behalf of a principal.

## Boundary

The name is not a control. Define the principal, delegated scope, enforcement point, audit record, revocation and escalation path.

## How it is used

Identity-Resolved Data is used when an agent’s access or action depends on whose identity is in play. It matters for delegation, auditability, and deciding whether a piece of context belongs to a user, a service, or an intermediate agent.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
