---
slug: memory-systems
name: Memory Systems
category: Memory
title: Memory Systems
aliases:
short_description: Memory Systems is the full stack that stores, retrieves, updates,
updated_at: '2026-06-22T20:54:07.902480+00:00'
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Memory Systems concerns how agent state is stored, selected, updated or retired across model calls and sessions.

## Boundary

It is not model training or a standard memory type. Specify retention, retrieval, provenance, access control and correction behaviour.

## How it is used

Memory Systems is used when the discussion is about the complete stack of [[Agent Memory|agent memory]] rather than one store or one feature. It includes persistence, retrieval, summarisation, correction, and expiry.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
