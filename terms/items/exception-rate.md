---
slug: exception-rate
name: Exception Rate
category: AgentOps
title: Exception Rate
aliases: []
short_description: Exception Rate is the proportion of workflows that need manual
  handling, escalation, or fallback.
termStatus: Operational metric/practice
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/evals
---

## Term status

Operational metric/practice.

## Meaning

Exception rate is the proportion of workflows that need manual handling, escalation, or fallback.

## Boundary

It is not a canonical KPI or discipline. Define the event boundary, numerator and denominator, threshold, owner and operational decision it informs.

## How it is used

Exception Rate is used when you need to know how often the agent system falls out of the happy path. It is a practical operational metric because it captures where automation is still leaking into manual handling.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
