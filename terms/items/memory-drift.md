---
slug: memory-drift
name: Memory Drift
category: Memory
title: Memory Drift
aliases: []
short_description: Memory Drift is used in designs for information an agent retains
  beyond the immediate prompt.
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Memory Drift concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Memory Drift is used in designs for information an agent retains beyond the immediate prompt. Teams specify record type, write trigger, source provenance, retrieval rule, retention period and correction route.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
