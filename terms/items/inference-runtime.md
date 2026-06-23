---
slug: inference-runtime
name: Inference Runtime
category: Runtime
title: Inference Runtime
aliases: []
short_description: Inference Runtime is used in runtime design to name the component
  that coordinates decisions and side effects.
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

Inference Runtime is used in runtime design to name the component that coordinates decisions and side effects. A useful specification gives its input event, durable state, action contract, retry policy, timeout and terminal states.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
