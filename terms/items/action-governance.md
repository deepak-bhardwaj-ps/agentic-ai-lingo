---
slug: action-governance
name: Action Governance
category: Governance
title: Action Governance
aliases:
short_description: Action Governance is the control layer that decides whether an
termStatus: Governance/security concept
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Governance/security concept.

## Meaning

Action Governance is the decision and enforcement layer that determines whether a specific agent action is allowed, denied, delayed, or escalated.

## Boundary

It is not governance in the abstract. The principal, policy, enforcement point, audit trail, revocation path, and escalation route all need to be explicit and operational.

## How it is used

Action Governance is used when a system needs a concrete gate for a concrete action. In practice, the useful version names the actor, the action, the policy that applies, the evidence produced, and the fallback when the decision is contested.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) is the relevant reference point. For coined labels, it supports the underlying concept, not the claim that the label itself is standard.
