---
slug: agent-marketplace
name: Agent Marketplace
category: Protocols
title: Agent Marketplace
aliases: []
short_description: Agent Marketplace is a directory or market where agents advertise
  capabilities and can be selected or bought.
termStatus: Product/operating-model label
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Product/operating-model label.

## Meaning

An agent marketplace is a catalogue and distribution mechanism for agents or skills, often with discovery, installation and governance features.

## Boundary

It is not a security boundary. Treat third-party agents as software supply-chain dependencies with review, provenance and permission controls.

## How it is used

Agent Marketplace is used when agents are exposed as discoverable offerings rather than internal utilities. The important questions are catalogue quality, trust, pricing, and how a buyer knows the agent will actually do what is claimed.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
