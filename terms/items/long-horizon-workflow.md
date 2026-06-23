---
slug: long-horizon-workflow
name: Long-Horizon Workflow
category: Runtime
title: Long-Horizon Workflow
aliases: []
short_description: Long-Horizon Workflow is used in runtime design to name the component
  that coordinates decisions and side effects.
termStatus: Descriptive capability term
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/evals
---

## Term status

Descriptive capability term.

## Meaning

Long-Horizon Workflow describes work that requires an agent to preserve state and make progress across many dependent steps, often with retries or interruption.

## Boundary

It is not a benchmark category or proof of autonomy. Define the task horizon, checkpointing, budget, recovery and success criteria.

## How it is used

Long-Horizon Workflow is used in runtime design to name the component that coordinates decisions and side effects. A useful specification gives its input event, durable state, action contract, retry policy, timeout and terminal states.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
