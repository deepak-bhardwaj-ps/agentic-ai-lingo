---
slug: tool-gateway
name: Tool Gateway
category: Protocols
title: Tool Gateway
aliases: null
short_description: Tool Gateway is a control point that brokers access to tools and
termStatus: Architecture pattern
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Architecture pattern.

## Meaning

A tool gateway is an intermediary service through which agents access tools or APIs, commonly centralising authentication, policy checks, logging, rate limits and schema validation.

## Boundary

It is not a protocol and does not remove application-level authorisation requirements.

## How it is used

Tool Gateway is used when tool access needs to be mediated rather than handed directly to the agent. It is the right term when policy, logging, throttling, and approval need to sit between request and side effect.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
