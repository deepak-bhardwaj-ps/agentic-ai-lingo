---
slug: inference-runtime
name: Inference Runtime
category: Runtime
title: Inference Runtime
aliases:
short_description: Inference Runtime is the serving layer that executes model calls
termStatus: Established systems term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Established systems term.

## Meaning

An inference runtime serves model inference: batching, scheduling, token generation, caching and hardware utilisation.

## Boundary

It is not an [[Agent Runtime|agent runtime]]. It does not normally own workflow state, tool execution or user authorisation.

## How it is used

Inference Runtime is used when the concern is model execution infrastructure rather than the agent’s policy or workflow logic. It covers the mechanics of latency, batching, routing, and availability around inference.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
