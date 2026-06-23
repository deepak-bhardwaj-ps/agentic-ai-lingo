---
slug: agent-kernel
name: Agent Kernel
category: Runtime
title: Agent Kernel
aliases: []
short_description: Agent Kernel is the core execution loop that turns observations
  into decisions and tool calls for one agent.
termStatus: Emerging practitioner shorthand
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Emerging practitioner shorthand.

## Meaning

An agent kernel is the minimal loop that keeps one agent coherent across turns: state intake, policy application, decision, tool call, and update. The term is useful when you need to isolate the irreducible runtime core from orchestration around it.

## Boundary

It is not a standard term unless a specific product or protocol defines it. State the concrete responsibilities, interfaces and ownership.

## How it is used

Agent Kernel is used when you need to discuss the smallest reliable core of an agent: state, reasoning, tool use, and control flow. It is the place where the agent’s behaviour becomes concrete enough to inspect, test, and constrain.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
