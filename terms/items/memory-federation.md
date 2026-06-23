---
slug: memory-federation
name: Memory Federation
category: Memory
title: Memory Federation
aliases: []
short_description: Memory Federation is used when several systems retain their own
  agent-related state but expose it through a common access pattern.
updated_at: '2026-06-22T20:54:07.871658+00:00'
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Memory Federation concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Memory Federation is used when several systems retain their own agent-related state but expose it through a common access pattern. The design must resolve identity, authority, conflict handling, freshness and deletion across stores.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
