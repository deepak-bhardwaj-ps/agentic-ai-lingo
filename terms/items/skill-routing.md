---
slug: skill-routing
name: Skill Routing
category: Runtime
title: Skill Routing
aliases: null
short_description: Skill Routing is selecting the right capability from a tool or
termStatus: Architecture/implementation term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture/implementation term.

## Meaning

Skill routing chooses the right capability for a task and delivers it through the execution path that can use it.

## Boundary

It is not a standard architecture. The useful design question is the decision rule, state boundary, failure handling and termination condition.

## How it is used

Skill Routing is used when the system chooses a capability at run time from a set of tools or skills. The routing policy should expose candidate selection, permission filtering, fallback and how a bad selection is observed.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
