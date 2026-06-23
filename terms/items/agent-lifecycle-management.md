---
slug: agent-lifecycle-management
name: Agent Lifecycle Management
category: AgentOps
title: Agent Lifecycle Management
aliases:
short_description: A lifecycle management practice governs the introduction,
termStatus: Operational metric/practice
researchBasis: OpenAI, NIST AI RMF, Microsoft Entra Agent ID
sources:
- https://learn.microsoft.com/en-us/entra/agent-id/agent-identities
---

## Term status

Operational metric/practice.

## Meaning

A lifecycle management practice covers introduction, operation, update, suspension, and retirement of agents.

## Boundary

It is not a canonical KPI or formal discipline. Define the event boundary, owner, and operational decision it informs before you count anything.

## How it is used

It is used when the full life of an agent matters: approval, rollout, monitoring, update, suspension, and retirement. It turns “we built an agent” into an operational asset with a clear exit path.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) frames evaluation as part of operating a system, not a one-off test.

[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) is the broader governance reference for tracking and managing AI risks across the lifecycle.

[Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) reinforces the need to register, manage, and retire agent identities rather than leaving them to drift.
