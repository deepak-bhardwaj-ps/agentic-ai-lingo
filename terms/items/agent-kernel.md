---
slug: agent-kernel
name: Agent Kernel
category: Runtime
title: Agent Kernel
aliases: null
short_description: A kernel is the smallest runtime core that keeps one agent
termStatus: Emerging practitioner shorthand
researchBasis: Anthropic, OpenAI Agents SDK, LangGraph
sources:
- https://www.langchain.com/langgraph
---

## Term status

Emerging practitioner shorthand.

## Meaning

A kernel is the smallest runtime core that keeps one agent coherent across turns: state intake, policy application, decision, tool call, and update. The term is useful when you need to isolate the irreducible loop from orchestration, handoffs, and surrounding infrastructure.

## Boundary

It is not a standard term unless a specific product or protocol defines it. Use it only when you can name the concrete responsibilities, interfaces, and ownership of the loop you mean.

## How it is used

A kernel is used when you need to discuss the smallest reliable core of an agent: state, reasoning, tool use, and control flow. It is the place where behaviour becomes concrete enough to inspect, test, and constrain.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) distinguishes the [[Agent Loop|agent loop]] from surrounding workflow orchestration and keeps the runtime core small and explicit.

[OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) separates orchestration, [[Guardrails|guardrails]], state, tools, and observability from the app’s own logic.

[LangGraph](https://www.langchain.com/langgraph) frames reliable agents around explicit stateful graphs rather than an opaque loop, which is the same design pressure behind the kernel label.
