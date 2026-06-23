---
slug: agentic-workflow
name: Agentic Workflow
category: Core
title: Agentic Workflow
aliases: []
short_description: Agentic Workflow is used to discuss an agent-system design concern.
termStatus: Architecture description
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture description.

## Meaning

A workflow is a pre-defined control flow that invokes model steps, tools or agents. It may include branching and retries, but the orchestration logic is largely explicit.

## Boundary

Do not equate a workflow with an autonomous agent. Anthropic distinguishes workflows (predefined paths) from agents (model-directed process and tool use).

## How it is used

Agentic Workflow is used to discuss an agent-system design concern. Its practical value is in turning the label into an explicit interface, state model, policy or testable outcome.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
