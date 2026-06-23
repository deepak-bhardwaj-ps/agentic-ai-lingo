---
slug: agentic-multi-agent-architecture
name: Agentic Multi-Agent Architecture
category: Protocols
title: Agentic Multi-Agent Architecture
aliases:
short_description: Agentic multi-agent architecture is a design where multiple
termStatus: Architecture description
researchBasis: Anthropic, OpenAI Agents SDK, LangGraph
sources:
- https://www.langchain.com/langgraph
---

## Term status

Architecture description.

## Meaning

A multi-agent architecture assigns specialised roles or tasks to multiple model-driven workers and coordinates their messages, shared state, and termination.

## Boundary

More agents do not automatically improve quality. The additional interfaces, cost, and error propagation require a measurable reason to decompose work.

## How it is used

It is used when work is deliberately decomposed across multiple agents with distinct responsibilities. It should only be used if the architecture explains why decomposition beats a single agent or workflow.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) treats multiple agents as one pattern among several, with clear trade-offs around coordination and reliability.

[OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) shows how orchestration, tools, and [[Guardrails|guardrails]] have to be explicit once you move beyond a single loop.

[LangGraph](https://www.langchain.com/langgraph) reinforces the architectural reason for decomposition: stateful coordination is the thing you have to design, not a side effect you get for free.
