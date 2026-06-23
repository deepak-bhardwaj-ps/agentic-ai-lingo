---
slug: agent-evals
name: Agent Evals
category: AgentOps
title: Agent Evals
aliases: []
short_description: Agent Evals is used in operating reviews to make a production concern
  observable and owned.
termStatus: Established practice, informal label
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/evals
---

## Term status

Established practice, informal label.

## Meaning

Agent evaluation measures task outcomes and intermediate trajectories under controlled scenarios. Useful suites include tool-call correctness, policy compliance, recovery behaviour, cost and latency.

## Boundary

A model benchmark or a single success rate is not sufficient for an agent. Evaluate the real action surface and adversarial failure modes.

## How it is used

Agent Evals is used in operating reviews to make a production concern observable and owned. Define the underlying event, measurement method, threshold, operational response and accountable team rather than using it as a broad maturity label.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
