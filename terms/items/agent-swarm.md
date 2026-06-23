---
slug: agent-swarm
name: Agent Swarm
category: Runtime
title: Agent Swarm
aliases:
short_description: A swarm is a loosely coordinated pool of agents working on
termStatus: Informal architecture label
researchBasis: Anthropic, multi-agent coordination research
sources:
- https://arxiv.org/abs/2510.10047
---

## Term status

Informal architecture label.

## Meaning

A swarm usually means a set of agents operating concurrently on related tasks, sometimes with shared state or aggregation.

## Boundary

It is not a defined architecture. Parallelism increases coordination, duplication, and privilege risks; use it only when tasks are genuinely separable.

## How it is used

It is used when several agents can work in parallel and exchange results without a strict hierarchy. It is useful for exploration and breadth, but it needs coordination rules or it turns into noisy duplication.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) treats parallelization as one pattern among several, not as a default design.

[SWARM+](https://arxiv.org/abs/2603.19431) shows that decentralised multi-agent coordination needs explicit consensus and failure handling to scale.

[SwarmSys](https://arxiv.org/abs/2510.10047) shows the same point from a reasoning perspective: swarm-like coordination only works when the interaction protocol is designed, not improvised.
