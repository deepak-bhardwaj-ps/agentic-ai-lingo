---
slug: agent-loop
name: Agent Loop
category: Runtime
title: Agent Loop
aliases:
short_description: A loop repeats planning, acting, and observation updates until
termStatus: Architecture term
researchBasis: Yao et al., ReAct, Anthropic
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture term.

## Meaning

A loop repeatedly feeds state to a model, interprets the decision, executes an allowed action, appends the observation, and stops on a success, budget, or policy condition.

## Boundary

It is not necessarily [[ReAct]] and it is not safe by default. It needs explicit loop, cost, and failure limits, otherwise it becomes an uncontrolled retry mechanism.

## How it is used

It is used when a system must repeatedly plan, act, and incorporate observations. In production it needs explicit stop conditions, spend limits, and a way to detect looping.

## Evidence

[Yao et al., ReAct](https://arxiv.org/abs/2210.03629) gives the canonical reasoning-and-acting loop that many agent implementations build on.

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) describes agents as tool-using systems that operate in a loop with checkpoints, stop conditions, and human feedback when needed.
