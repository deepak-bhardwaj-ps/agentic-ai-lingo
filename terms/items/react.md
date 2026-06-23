---
slug: react
name: ReAct
category: Runtime
title: ReAct
aliases:
short_description: ReAct is the reasoning-plus-action pattern that interleaves thought,
termStatus: Established research pattern
researchBasis: Yao et al., ReAct (ICLR 2023)
sources:
- https://arxiv.org/abs/2210.03629
---

## Term status

Established research pattern.

## Meaning

ReAct is the prompting pattern from Yao et al. that interleaves reasoning traces with actions and observations. It is one implementation pattern for tool-using agents.

## Boundary

It is not React the JavaScript library, and it is not a guarantee that hidden reasoning is faithful or that tool calls are safe.

## How it is used

ReAct is used when the system needs to alternate between reasoning and acting rather than answer in one shot. It is the canonical pattern for showing how a tool-using agent can loop through thought, action, and observation.

## Evidence

[Yao et al., ReAct (ICLR 2023)](https://arxiv.org/abs/2210.03629) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
