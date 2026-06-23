---
slug: memory-drift
name: Memory Drift
category: Memory
title: Memory Drift
aliases: null
short_description: Memory Drift is gradual change in stored state or retrieval behaviour
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

Memory Drift is used when stored state changes slowly enough that behaviour shifts without an obvious breakage event. It is the term for a memory layer that has started to answer differently than it used to.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
