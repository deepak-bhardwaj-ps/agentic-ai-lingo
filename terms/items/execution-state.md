---
slug: execution-state
name: Execution State
category: Runtime
title: Execution State
aliases: null
short_description: 'Execution State is used for the mutable record that lets an orchestrator
  continue a run: plan, observations, tool results, checkpoints and budgets.'
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Execution State concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Execution State is used for the mutable record that lets an orchestrator continue a run: plan, observations, tool results, checkpoints and budgets. Its schema determines resumability and should not contain unbounded conversation history.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
