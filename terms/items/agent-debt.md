---
slug: agent-debt
name: Agent Debt
category: AgentOps
title: Agent Debt
aliases: []
short_description: Agent Debt is the accumulated operational risk created by shortcuts,
  weak controls, and unresolved failure modes in an agent system.
termStatus: Operational metric/practice
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/evals
---

## Term status

Operational metric/practice.

## Meaning

Agent debt is the accumulated operational risk created by shortcuts, weak controls, and unresolved failure modes.

## Boundary

It is not a canonical KPI or discipline. Define the event boundary, numerator and denominator, threshold, owner and operational decision it informs.

## How it is used

Agent Debt is used when an agent system is carrying unresolved operational shortcuts that will cost more later: weak tests, poor ownership, brittle prompts, or missing recovery paths. The term is useful if it points to a specific backlog item or remediation plan.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
