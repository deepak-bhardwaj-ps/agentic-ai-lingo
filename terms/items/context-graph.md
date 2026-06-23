---
slug: context-graph
name: Context Graph
category: Context
title: Context Graph
aliases:
short_description: Context Graph is a graph representation of the entities and relationships
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT
sources:
- https://arxiv.org/abs/2310.08560
---

## Term status

Implementation pattern.

## Meaning

Context Graph means representing the relevant entities and relationships as a graph so an agent can query or traverse them.

## Boundary

A graph representation does not itself provide truth, provenance, permissions or reasoning. Define the schema and update authority.

## How it is used

Context Graph is used when the model benefits from traversable relationships rather than flat retrieved chunks. It is especially useful when context needs to be queried, joined, or explored over time.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
