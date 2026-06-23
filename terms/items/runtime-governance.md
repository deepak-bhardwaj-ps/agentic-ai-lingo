---
slug: runtime-governance
name: Runtime Governance
category: Runtime
title: Runtime Governance
aliases: []
short_description: Runtime Governance is the set of controls that constrains what
  a runtime can do and how it is supervised.
termStatus: Architecture/implementation term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture/implementation term.

## Meaning

Runtime governance is the set of controls that constrains what a runtime can do and how it is supervised.

## Boundary

It is not a standard architecture. The useful design question is the decision rule, state boundary, failure handling and termination condition.

## How it is used

Runtime Governance is used when runtime behaviour needs policy, approval, monitoring, or audit rather than just execution. It is the term for the controls that make autonomy reviewable and revocable.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
