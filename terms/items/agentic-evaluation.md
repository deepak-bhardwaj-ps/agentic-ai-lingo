---
slug: agentic-evaluation
name: Agentic Evaluation
category: AgentOps
title: Agentic Evaluation
aliases: null
short_description: Agentic evaluation is evaluation for multi-step, stateful,
termStatus: Established practice, informal label
researchBasis: OpenAI, trace grading, Anthropic
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Established practice, informal label.

## Meaning

Agentic evaluation is evaluation designed for multi-step, stateful, tool-using systems rather than isolated text outputs.

## Boundary

It is a descriptive phrase, not a distinct scientific method. Define the task environment, oracle, trajectory checks, and release threshold.

## How it is used

It is used when the system’s behaviour depends on a trajectory of actions rather than a single answer. It is the right term when you need to assess the path, not just the destination.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) covers the basic scaffolding for evaluating agent behaviour rather than isolated outputs.

[Trace grading](https://platform.openai.com/docs/guides/trace-grading) is the clearest platform reference for scoring multi-step behaviour from traces.

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) reinforces why trajectories, checkpoints, and recovery matter more than one-shot answers in these systems.
