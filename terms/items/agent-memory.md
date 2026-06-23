---
slug: agent-memory
name: Agent Memory
category: Memory
title: Agent Memory
aliases: []
short_description: Agent Memory is used in designs for information an agent retains
  beyond the immediate prompt.
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Agent memory is externally managed state that helps an agent retain task context, facts, preferences or past experiences across model calls or sessions.

## Boundary

It is not persistent model learning. Memory writes and retrieval must be scoped, attributable, correctable and access-controlled.

## How it is used

Agent Memory is used in designs for information an agent retains beyond the immediate prompt. Teams specify record type, write trigger, source provenance, retrieval rule, retention period and correction route.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
