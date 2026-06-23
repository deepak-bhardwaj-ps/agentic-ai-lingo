---
slug: agentic-workflow
name: Agentic Workflow
category: Core
title: Agentic Workflow
aliases: []
short_description: Agentic Workflow is a workflow that includes planning, tool use,
  state, and recovery rather than a single model call.
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

Agentic Workflow is used when a task is decomposed into steps the system can sequence, inspect, and repair over time. It is the right term when you need to talk about the workflow mechanics, not just the model that happens to sit inside them.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
