---
slug: star-topology
name: Star Topology
category: Runtime
title: Star Topology
aliases: []
short_description: Star Topology is used to explain the communication shape among
  coordinator and worker agents.
termStatus: Architecture/implementation term
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Architecture/implementation term.

## Meaning

Star Topology describes a runtime mechanism for sequencing model calls, selecting capabilities, holding state or checking a result.

## Boundary

It is not a standard architecture. The useful design question is the decision rule, state boundary, failure handling and termination condition.

## How it is used

Star Topology is used to explain the communication shape among coordinator and worker agents. The diagram should be accompanied by message ownership, state-sharing, error propagation and termination rules.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
