---
slug: tool-gateway
name: Tool Gateway
category: Protocols
title: Tool Gateway
aliases: []
short_description: Tool Gateway is used in discussions of coordination or discoverability
  between independently built agents and services.
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

Tool Gateway is used in discussions of coordination or discoverability between independently built agents and services. Before adopting the label, identify the concrete message format, discovery method, identity exchange, compatibility commitment and failure semantics.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
