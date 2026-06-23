---
slug: least-privilege
name: Least Privilege
category: Governance
title: Least Privilege
aliases: null
short_description: Least Privilege is the principle of giving an agent only the access
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

Least Privilege is used when the agent should have only the access needed for the task. In practice, anything more is risk, not convenience.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
