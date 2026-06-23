---
slug: act-on-behalf
name: Act-on-Behalf
category: Governance
title: Act-on-Behalf
aliases:
short_description: Act-on-Behalf is acting under delegated authority for a specific
termStatus: Governance/security concept
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Governance/security concept.

## Meaning

Act-on-Behalf describes delegated action: an agent performs work under another principal’s authority, with the scope and responsibility still attached to that principal.

## Boundary

It is not a control by itself. The accountable principal, permitted scope, enforcement point, audit record, revocation path, and human escalation route all need to be explicit.

## How it is used

Act-on-Behalf is used when an agent is operating for someone else rather than on its own behalf. In a real system, the delegation should be traceable to a named principal, bounded by scope, and removable without ambiguity.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) is the relevant reference point. For coined labels, it supports the underlying concept, not the claim that the label itself is standard.
