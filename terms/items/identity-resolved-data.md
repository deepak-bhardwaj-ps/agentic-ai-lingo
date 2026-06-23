---
slug: identity-resolved-data
name: Identity-Resolved Data
category: Context
title: Identity-Resolved Data
aliases: []
short_description: Identity-Resolved Data is used when teams need to reason about
  the information presented to a model at decision time.
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

Identity-Resolved Data is used when teams need to reason about the information presented to a model at decision time. It should result in explicit source selection, provenance, freshness, permissions and token-budget behaviour.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
