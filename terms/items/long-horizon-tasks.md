---
slug: long-horizon-tasks
name: Long-Horizon Tasks
category: Runtime
title: Long-Horizon Tasks
aliases:
short_description: Long-Horizon Tasks are tasks that unfold over many steps and require
termStatus: Descriptive capability term
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/evals
---

## Term status

Descriptive capability term.

## Meaning

Long-Horizon Tasks describes work that requires an agent to preserve state and make progress across many dependent steps, often with retries or interruption.

## Boundary

It is not a benchmark category or proof of autonomy. Define the task horizon, checkpointing, budget, recovery and success criteria.

## How it is used

Long-Horizon Tasks is used when a task cannot be completed in one model pass and needs durable memory, checkpoints, and error recovery. It is useful for separating “hard because it is long” from “hard because it is complex.”

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
