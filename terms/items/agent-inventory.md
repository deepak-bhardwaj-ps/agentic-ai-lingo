---
slug: agent-inventory
name: Agent Inventory
category: AgentOps
title: Agent Inventory
aliases: null
short_description: A maintained agent inventory lists the agents, versions,
termStatus: Operational metric/practice
researchBasis: OpenAI, NIST AI RMF
sources:
- https://www.nist.gov/itl/ai-risk-management-framework
---

## Term status

Operational metric/practice.

## Meaning

A maintained agent inventory records the agents, versions, capabilities, owners, and deployment scope currently in operation.

## Boundary

It is not a universal KPI or a formal discipline. Treat it as a control object: define what counts as an agent, when a record enters or leaves the inventory, and which operational decision the inventory supports.

## How it is used

It is used when an organisation needs a reliable count of what agents exist, where they run, and who owns them. It is the baseline for lifecycle control, risk review, exception handling, and decommissioning.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) is the clearest product-side reference for tracking what exists, what changed, and what is being measured.

[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) supports the governance framing: inventorying systems, documenting scope, and assigning ownership are prerequisites for managing AI risk in production.
