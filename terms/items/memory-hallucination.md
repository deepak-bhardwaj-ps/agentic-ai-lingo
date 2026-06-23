---
slug: memory-hallucination
name: Memory Hallucination
category: Memory
title: Memory Hallucination
aliases:
short_description: Memory Hallucination is false, irrelevant, malicious, or misretrieved
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Memory Hallucination concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Memory Hallucination is used when stored agent state is false, irrelevant, malicious or incorrectly retrieved and then affects a later decision. Teams investigate source provenance, write controls, retrieval ranking and correction or deletion paths.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
