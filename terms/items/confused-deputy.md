---
slug: confused-deputy
name: Confused Deputy
category: Governance
title: Confused Deputy
aliases: null
short_description: Confused Deputy is an agent tricked into using delegated authority
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

Confused Deputy is used when an agent is tricked into using authority it was granted for something else. In practice, the fix is tighter scoping and stronger checks on the caller.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
