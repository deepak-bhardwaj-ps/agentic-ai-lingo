---
slug: confused-deputy
name: Confused Deputy
category: Governance
title: Confused Deputy
aliases: []
short_description: Confused Deputy is used in agent governance to make an action attributable
  and bounded.
termStatus: Established security term
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Established security term.

## Meaning

A confused deputy occurs when a more-privileged component is tricked into using its authority on behalf of a less-privileged requester. Tool-using agents can become deputies when untrusted content influences authorised actions.

## Boundary

This is a security design failure, not a hallucination. Preserve caller identity and authorisation context through every delegated call.

## How it is used

Confused Deputy is used in agent governance to make an action attributable and bounded. In practice, teams tie it to a principal, a permitted decision, an enforcement service, durable evidence and an escalation path.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
