---
slug: least-privilege
name: Least Privilege
category: Governance
title: Least Privilege
aliases: []
short_description: Least Privilege is used in agent governance to make an action attributable
  and bounded.
termStatus: Established security principle
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Established security principle.

## Meaning

Least privilege grants an agent only the identities, data scopes and actions required for its current task, preferably with short-lived credentials.

## Boundary

It is not a model instruction. It must be implemented by the identity, token, tool and data-access layers.

## How it is used

Least Privilege is used in agent governance to make an action attributable and bounded. In practice, teams tie it to a principal, a permitted decision, an enforcement service, durable evidence and an escalation path.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
