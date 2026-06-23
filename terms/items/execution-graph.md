---
slug: execution-graph
name: Execution Graph
category: Runtime
title: Execution Graph
aliases: []
short_description: Execution Graph is used in runtime design to name the component
  that coordinates decisions and side effects.
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Execution Graph means representing the relevant entities and relationships as a graph so an agent can query or traverse them.

## Boundary

A graph representation does not itself provide truth, provenance, permissions or reasoning. Define the schema and update authority.

## How it is used

Execution Graph is used in runtime design to name the component that coordinates decisions and side effects. A useful specification gives its input event, durable state, action contract, retry policy, timeout and terminal states.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
