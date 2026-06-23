---
slug: execution-graph
name: Execution Graph
category: Runtime
title: Execution Graph
aliases: []
short_description: Execution Graph is the graph of steps, dependencies, and side effects
  that defines how work proceeds.
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

Execution Graph is used when the system is easier to reason about as connected steps than as a single loop. It helps make explicit what must happen first, what can branch, and where retries or human approvals sit.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
