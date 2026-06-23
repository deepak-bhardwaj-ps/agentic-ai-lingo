---
slug: agentic-multi-agent-architecture
name: Agentic Multi-Agent Architecture
category: Protocols
title: Agentic Multi-Agent Architecture
aliases: []
short_description: Agentic Multi-Agent Architecture is a design where multiple specialised
  agents coordinate on one task or system.
termStatus: Architecture description
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture description.

## Meaning

A multi-agent architecture assigns specialised roles or tasks to multiple model-driven workers and coordinates their messages, shared state and termination.

## Boundary

More agents do not automatically improve quality. The additional interfaces, cost and error propagation require a measurable reason to decompose work.

## How it is used

Agentic Multi-Agent Architecture is used when work is deliberately decomposed across multiple agents with distinct responsibilities. It should only be used if the architecture explains why decomposition beats a single agent or workflow.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
