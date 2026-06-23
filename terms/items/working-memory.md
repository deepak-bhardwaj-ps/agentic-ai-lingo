---
slug: working-memory
name: Working Memory
category: Memory
title: Working Memory
aliases: []
short_description: Working Memory is used in designs for information an agent retains
  beyond the immediate prompt.
termStatus: Established cognitive term; applied metaphor
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Established cognitive term; applied metaphor.

## Meaning

Working memory in agent systems usually means the bounded, task-local state currently supplied to the model: recent observations, scratch state and active plan.

## Boundary

It is not the model's neural memory, and the metaphor should not hide token limits, eviction policy or confidentiality controls.

## How it is used

Working Memory is used in designs for information an agent retains beyond the immediate prompt. Teams specify record type, write trigger, source provenance, retrieval rule, retention period and correction route.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
