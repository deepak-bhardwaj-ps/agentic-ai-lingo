---
slug: agent-runtime
name: Agent Runtime
category: Runtime
title: Agent Runtime
aliases:
short_description: A runtime is the execution environment that hosts an agent’s
termStatus: Architecture term
researchBasis: Anthropic, OpenAI Agents SDK, LangGraph
sources:
- https://www.langchain.com/langgraph
---

## Term status

Architecture term.

## Meaning

A runtime is the software that executes an [[Agent Loop|agent loop]]: it manages model calls, state, tool invocation, retries, events, and termination.

## Boundary

It is not the model-serving runtime. An implementation may combine both, but their scaling and security responsibilities differ.

## How it is used

It is used when the discussion is about the whole running environment rather than a single model call. It is the machinery that keeps the agent alive across turns, tool calls, and retries.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) separates agent orchestration from the model call and describes the runtime machinery around state, tools, and termination.

[OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) makes the same split explicit through orchestration, state, tools, guardrails, and observability.

[LangGraph](https://www.langchain.com/langgraph) reinforces the architectural shape: a stateful execution substrate, not just a model endpoint.
