---
slug: action-plane
name: Action Plane
category: Governance
title: Action Plane
aliases:
short_description: Action Plane is the enforcement layer that actually blocks, approves,
termStatus: Governance/security concept
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Governance/security concept.

## Meaning

Action Plane is the runtime enforcement layer that sits between intent and execution. It is where an action gets blocked, approved, modified, logged, or escalated.

## Boundary

It is not just a label for governance. A real action plane has a concrete enforcement point, a defined principal, a scoped policy, durable logs, a revocation path, and a human override route.

## How it is used

Action Plane is used when a system needs to make action control visible and operational. If nothing actually intercepts execution, the term is decorative.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) is the relevant reference point. For coined labels, it supports the underlying concept, not the claim that the label itself is standard.
