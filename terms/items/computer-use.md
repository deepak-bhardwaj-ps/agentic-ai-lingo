---
slug: computer-use
name: Computer Use
category: Core
title: Computer Use
aliases: []
short_description: Computer Use is model-driven interaction with a desktop through
  cursor, keyboard, and screen control.
termStatus: Established product capability
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Established product capability.

## Meaning

Computer use means an agent observes and operates a graphical desktop or browser through mouse, keyboard and screen actions, rather than an application API.

## Boundary

It is an interaction modality, not a general autonomy level. UI automation has brittle selectors, weak transaction semantics and a larger prompt-injection surface.

## How it is used

Computer Use is used when the agent must operate at the operating-system level instead of through a clean API or browser abstraction. It usually carries a heavier safety and reliability burden because the interface is visible but not structured.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
