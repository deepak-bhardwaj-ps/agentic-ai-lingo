---
slug: memory-architecture
name: Memory Architecture
category: Memory
title: Memory Architecture
aliases:
short_description: Memory Architecture is the design of storage, retrieval, and correction
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Memory Architecture concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Memory Architecture is used when a system has more than one kind of memory and needs a deliberate storage and retrieval design. The question is how facts move, how stale records are retired, and how corrections are applied.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
