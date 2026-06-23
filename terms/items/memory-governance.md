---
slug: memory-governance
name: Memory Governance
category: Memory
addedDate: May 8, 2025
title: Memory Governance
aliases: []
short_description: Memory Governance is policy for who can read, write, retain, or
  delete agent memory.
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Memory Governance concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Memory Governance is used when teams need rules for who may read, write, retain, or delete [[Agent Memory|agent memory]]. It is the control layer that keeps memory from becoming a liability.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
