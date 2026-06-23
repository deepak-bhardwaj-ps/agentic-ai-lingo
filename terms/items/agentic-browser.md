---
slug: agentic-browser
name: Agentic Browser
category: Core
title: Agentic Browser
aliases:
short_description: An agentic browser is a browser-driven agent that can navigate
termStatus: Emerging product category
researchBasis: OWASP Top 10 for LLM Applications, Anthropic
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Emerging product category.

## Meaning

An agentic browser describes a browser product or integration that lets an AI system navigate, read, and act on web content on a user's behalf.

## Boundary

It is not a web standard or a security model. The important properties are browsing isolation, identity delegation, confirmation, and treatment of untrusted page content.

## How it is used

It is used when the browser itself is the working surface for the agent, typically through clicks, form fills, page reading, and navigation. The useful question is not whether it is “agentic” in the abstract, but what it can reliably do inside the browser without human micromanagement.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) is the security reference point: browser-mediated agents inherit prompt injection, tool abuse, and untrusted content problems.

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) reinforces the production lesson: keep the tool surface simple, explicit, and auditable.
