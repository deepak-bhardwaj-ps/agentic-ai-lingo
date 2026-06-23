---
slug: tool-router
name: Tool Router
category: Runtime
title: Tool Router
aliases: []
short_description: Tool Router is used in runtime design to name the component that
  coordinates decisions and side effects.
termStatus: Implementation pattern
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Implementation pattern.

## Meaning

A tool router selects or exposes the subset of callable tools for a request based on task, context or policy.

## Boundary

It is not authorisation by itself. The selected tool must independently enforce identity, scope and input validation.

## How it is used

Tool Router is used in runtime design to name the component that coordinates decisions and side effects. A useful specification gives its input event, durable state, action contract, retry policy, timeout and terminal states.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
