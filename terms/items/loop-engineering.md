---
slug: loop-engineering
name: Loop Engineering
category: Runtime
title: Loop Engineering
aliases:
short_description: Loop Engineering is the practice of designing repeated plan-act-observe
termStatus: Architecture/implementation term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture/implementation term.

## Meaning

Loop engineering is the design of the repetitive plan-act-observe cycle that lets an agent make progress over multiple steps.

## Boundary

It is not a standard architecture. The useful design question is the decision rule, state boundary, failure handling and termination condition.

## How it is used

Loop Engineering is used when the repeated plan-act-observe cycle itself has to be designed and controlled. It becomes a production concern once stop conditions, iteration limits, and spend limits matter.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
