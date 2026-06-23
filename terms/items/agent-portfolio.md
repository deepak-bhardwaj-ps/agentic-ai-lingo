---
slug: agent-portfolio
name: Agent Portfolio
category: AgentOps
title: Agent Portfolio
aliases: []
short_description: A portfolio is the set of agents an organisation manages as a
  mix of value, risk, and investment.
termStatus: Operational metric/practice
researchBasis: OpenAI, NIST AI RMF, Anthropic
sources:
- https://platform.openai.com/docs/guides/evals
- https://www.nist.gov/itl/ai-risk-management-framework
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Operational metric/practice.

## Meaning

A portfolio is the set of agents an organisation manages as a mix of assets, risks, and investments.

## Boundary

It is not a canonical KPI or formal discipline. Define the event boundary, owner, and decision it informs before turning it into a dashboard.

## How it is used

It is used when the question is mix, value, and risk across many agents rather than one deployment. It helps compare which agents should grow, stabilise, or be retired.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) supports comparing systems through measurement, which is what portfolio management depends on.

[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) gives the broader governance frame for balancing risk across many systems.

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) reinforces the practical point that simple, composable systems tend to beat excessive architectural sprawl.
