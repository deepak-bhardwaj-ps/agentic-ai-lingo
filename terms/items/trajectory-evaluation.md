---
slug: trajectory-evaluation
name: Trajectory Evaluation
category: AgentOps
title: Trajectory Evaluation
aliases:
short_description: Trajectory Evaluation is evaluation of the path an agent took,
termStatus: Evaluation technique
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/evals
---

## Term status

Evaluation technique.

## Meaning

Trajectory evaluation scores the sequence of intermediate decisions, tool calls and observations an agent took, as well as its final outcome.

## Boundary

It should not replace outcome evaluation. A valid but unusual path may be acceptable, while a superficially plausible trace may hide unsafe actions.

## How it is used

Trajectory Evaluation is used when the intermediate decisions, tool calls, and observations matter as much as the final output. It is useful for spotting unsafe or inefficient paths that outcome-only tests would miss.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
