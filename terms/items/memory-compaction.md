---
slug: memory-compaction
name: Memory Compaction
category: Memory
title: Memory Compaction
aliases: []
short_description: Memory Compaction is used in designs for information an agent retains
  beyond the immediate prompt.
termStatus: Implementation technique
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation technique.

## Meaning

Memory compaction summarises or restructures old state to fit a bounded context window while attempting to preserve information needed for later work.

## Boundary

It is lossy transformation, not archival. Retain links to source records and evaluate whether compaction changes decisions.

## How it is used

Memory Compaction is used in designs for information an agent retains beyond the immediate prompt. Teams specify record type, write trigger, source provenance, retrieval rule, retention period and correction route.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
