---
slug: agent-memory
name: Agent Memory
category: Memory
title: Agent Memory
aliases: []
short_description: A memory layer stores governed state so an agent can reuse
  facts, preferences, and prior work across turns.
termStatus: Implementation pattern
researchBasis: Packer et al., MemGPT, provenance-focused memory research
sources:
- https://arxiv.org/abs/2310.08560
- https://arxiv.org/abs/2605.25869
- https://arxiv.org/abs/2603.02473
---

## Term status

Implementation pattern.

## Meaning

A memory layer is externally managed state that helps an agent retain task context, facts, preferences, or past experiences across model calls or sessions.

## Boundary

It is not persistent model learning. Memory writes and retrieval must be scoped, attributable, correctable, and access-controlled.

## How it is used

It is used when an agent must carry facts, preferences, or past work between turns. Teams still need to define record type, write trigger, provenance, retrieval rule, retention period, and correction route.

## Evidence

[Packer et al., MemGPT](https://arxiv.org/abs/2310.08560) is the baseline reference for separating an agent’s working context from longer-lived memory.

[Mitigating Provenance-Role Collapse in Long-Term Agents via Typed Memory Representation](https://arxiv.org/abs/2605.25869) shows why memory has to preserve source and claim structure, not just raw text.

[Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory](https://arxiv.org/abs/2603.02473) highlights that retrieval quality can dominate write-time sophistication in real systems.
