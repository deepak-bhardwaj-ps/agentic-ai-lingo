---
slug: orchestration-loop
name: Orchestration Loop
category: Runtime
title: Orchestration Loop
aliases:
short_description: Orchestration Loop is the control cycle that schedules work, checks
termStatus: Architecture/implementation term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture/implementation term.

## Meaning

An orchestration loop sequences model calls, tool use, state updates, and checks so a task can proceed over time.

## Boundary

It is not a standard architecture. The useful design question is the decision rule, state boundary, failure handling and termination condition.

## How it is used

Orchestration Loop is used when the control layer has to keep scheduling work, checking results, and choosing the next step. In production it needs explicit stop conditions, iteration limits, and spend control.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
