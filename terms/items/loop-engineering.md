---
slug: loop-engineering
name: Loop Engineering
category: Runtime
title: Loop Engineering
aliases: []
short_description: Loop Engineering is used when a model-driven process repeatedly
  plans, acts and incorporates observations.
termStatus: Architecture/implementation term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture/implementation term.

## Meaning

Loop Engineering describes a runtime mechanism for sequencing model calls, selecting capabilities, holding state or checking a result.

## Boundary

It is not a standard architecture. The useful design question is the decision rule, state boundary, failure handling and termination condition.

## How it is used

Loop Engineering is used when a model-driven process repeatedly plans, acts and incorporates observations. In production it needs a maximum iteration count, spend limit, loop-detection signal and explicit stop outcomes.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
