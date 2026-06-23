---
slug: agent-loop
name: Agent Loop
category: Runtime
title: Agent Loop
aliases: []
short_description: Agent Loop is used when a model-driven process repeatedly plans,
  acts and incorporates observations.
termStatus: Architecture term
researchBasis: Yao et al., ReAct (ICLR 2023)
sources:
- https://arxiv.org/abs/2210.03629
---

## Term status

Architecture term.

## Meaning

An agent loop repeatedly provides state to a model, interprets its decision, executes an allowed action, appends the observation and stops on a success, budget or policy condition.

## Boundary

It is not necessarily [[ReAct]] and must have explicit loop, cost and failure limits.

## How it is used

Agent Loop is used when a model-driven process repeatedly plans, acts and incorporates observations. In production it needs a maximum iteration count, spend limit, loop-detection signal and explicit stop outcomes.

## Evidence

[Yao et al., [[ReAct]] (ICLR 2023)](https://arxiv.org/abs/2210.03629) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
