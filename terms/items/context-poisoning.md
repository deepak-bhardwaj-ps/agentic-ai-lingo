---
slug: context-poisoning
name: Context Poisoning
category: Context
title: Context Poisoning
aliases: []
short_description: Context Poisoning is used for untrusted content that enters an
  agent’s active prompt or retrieved evidence and attempts to steer its tool use.
termStatus: Security risk
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Security risk.

## Meaning

Context poisoning is untrusted or manipulated content entering an agent's active context and steering its subsequent model behaviour or tool use.

## Boundary

It is not solved by asking the model to ignore instructions. Apply provenance, isolation, parsing, tool policy and confirmation controls.

## How it is used

Context Poisoning is used for untrusted content that enters an agent’s active prompt or retrieved evidence and attempts to steer its tool use. Treat it as an input-integrity threat: label untrusted content, isolate instructions and gate consequential actions.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
