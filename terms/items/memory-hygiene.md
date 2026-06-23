---
slug: memory-hygiene
name: Memory Hygiene
category: Memory
title: Memory Hygiene
aliases: null
short_description: Memory Hygiene is routine cleanup that keeps memory accurate, current,
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Memory Hygiene concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Memory Hygiene is used when the memory store needs routine cleanup: stale entries removed, duplicates merged, and bad records corrected. It is operational maintenance, not architecture.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
