---
slug: agentic-workflow
name: Agentic Workflow
category: Core
title: Agentic Workflow
aliases: null
short_description: Agentic workflow names a workflow that includes planning,
termStatus: Architecture description
researchBasis: Anthropic, OpenAI Agents SDK
sources:
- https://developers.openai.com/api/docs/guides/agents
---

## Term status

Architecture description.

## Meaning

A workflow is a pre-defined control flow that invokes model steps, tools, or agents. It may include branching and retries, but the orchestration logic is largely explicit. In agentic systems, the useful distinction is that the control flow is still visible.

## Boundary

Do not equate a workflow with an autonomous agent. Anthropic distinguishes workflows, which follow predefined paths, from agents, which let the model direct more of the process and tool use.

## How it is used

Use it when a task is decomposed into steps the system can sequence, inspect, and repair over time. It is the right term when you need to talk about the workflow mechanics, not just the model that happens to sit inside them.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) is the clearest reference for the workflow-versus-agent distinction.

[OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) reinforces that explicit orchestration and [[Guardrails|guardrails]] matter once you are sequencing work across steps.
