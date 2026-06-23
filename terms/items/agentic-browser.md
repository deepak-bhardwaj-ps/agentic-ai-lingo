---
slug: agentic-browser
name: Agentic Browser
category: Core
title: Agentic Browser
aliases: []
short_description: Agentic Browser is a browser-driven agent that can navigate pages,
  inspect content, and take actions on the web.
termStatus: Emerging product category
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Emerging product category.

## Meaning

Agentic browser describes a browser product or integration that lets an AI system navigate, read and act on web content on a user's behalf.

## Boundary

It is not a web standard or a security model. The important properties are browsing isolation, identity delegation, confirmation and treatment of untrusted page content.

## How it is used

Agentic Browser is used when the browser itself is the working surface for the agent, typically through clicks, form fills, page reading, and navigation. The useful question is not whether it is “agentic” in the abstract, but what it can reliably do inside the browser without human micromanagement.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
