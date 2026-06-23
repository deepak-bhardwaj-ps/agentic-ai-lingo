---
slug: agent-runtime
name: Agent Runtime
category: Runtime
title: Agent Runtime
aliases: []
short_description: Agent Runtime is the execution environment that hosts an agent’s
  loop, tools, memory, and side effects.
termStatus: Architecture term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture term.

## Meaning

An agent runtime is the software that executes an [[Agent Loop|agent loop]]: it manages model calls, state, tool invocation, retries, events and termination.

## Boundary

It is not the model-serving runtime. An implementation may combine both, but their scaling and security responsibilities differ.

## How it is used

Agent Runtime is used when the discussion is about the whole running environment rather than a single model call. It is the term for the machinery that keeps the agent alive across turns, tool calls, and retries.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
