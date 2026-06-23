---
slug: ai-agents
name: AI Agents
category: Core
title: AI Agents
aliases:
short_description: AI agents is the umbrella label for software systems that can
updated_at: '2026-06-22T20:54:06.685468+00:00'
termStatus: Umbrella term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Umbrella term.

## Meaning

AI agent is an overloaded label for a model-based system that selects actions towards a goal, commonly by invoking tools and using observations. The autonomy and planning depth vary widely, so the label only becomes useful once you name the actual runtime shape.

## Boundary

A chatbot, workflow, and autonomous agent are not interchangeable. State the action surface, stopping condition, and human approval points.

## How it is used

Use it when the discussion is about a system that can plan, call tools, track state, and recover from failure rather than only answer a prompt. In practice it is the broadest umbrella in the glossary, so it should be narrowed quickly to the real runtime, governance, or workflow question.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) is the clearest reference for the modern tool-using, stateful agent pattern.

The label is umbrella terminology, not a technical standard. Its value is to name the family of systems before you narrow to the actual runtime or governance problem.
