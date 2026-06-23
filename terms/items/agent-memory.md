---
slug: agent-memory
name: Agent Memory
category: Memory
title: Agent Memory
aliases: []
short_description: Agent Memory is externally managed state for carrying facts, preferences,
  and past work across turns.
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

Agent Memory is used when an agent must carry facts, preferences, or past work between turns. Teams still need to define record type, write trigger, provenance, retrieval rule, retention period, and correction route.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
