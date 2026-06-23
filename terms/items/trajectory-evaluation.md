---
slug: trajectory-evaluation
name: Trajectory Evaluation
category: AgentOps
title: Trajectory Evaluation
aliases: []
short_description: Trajectory Evaluation is used in operating reviews to make a production
  concern observable and owned.
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

Trajectory Evaluation is used in operating reviews to make a production concern observable and owned. Define the underlying event, measurement method, threshold, operational response and accountable team rather than using it as a broad maturity label.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
