---
slug: agent-swarm
name: Agent Swarm
category: Runtime
title: Agent Swarm
aliases: []
short_description: Agent Swarm is a loosely coordinated pool of agents working on
  related tasks in parallel.
termStatus: Informal architecture label
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Informal architecture label.

## Meaning

Agent swarm usually means a set of agents operating concurrently on related tasks, sometimes with shared state or aggregation.

## Boundary

It is not a defined architecture. Parallelism increases coordination, duplication and privilege risks; use it only when tasks are genuinely separable.

## How it is used

Agent Swarm is used when several agents can work in parallel and exchange results without a strict hierarchy. It is useful for exploration and breadth, but it needs coordination rules or it turns into noisy duplication.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
