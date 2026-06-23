---
slug: memory-debt
name: Memory Debt
category: Memory
title: Memory Debt
aliases: []
short_description: Memory Debt is used for accumulated shortcuts in storage, retrieval
  and summarisation that make an agent’s state unreliable or expensive to change.
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Memory Debt concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Memory Debt is used for accumulated shortcuts in storage, retrieval and summarisation that make an agent’s state unreliable or expensive to change. It should be tracked through concrete defects such as stale records, missing provenance or uncontrolled growth.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
