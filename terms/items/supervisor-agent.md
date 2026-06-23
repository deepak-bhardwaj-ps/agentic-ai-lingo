---
slug: supervisor-agent
name: Supervisor Agent
category: Runtime
title: Supervisor Agent
aliases: null
short_description: Supervisor Agent is the top-level agent that delegates, checks,
termStatus: Common framework pattern
researchBasis: Anthropic, Building effective agents
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Common framework pattern.

## Meaning

A supervisor agent routes work to specialised workers, synthesises results and decides whether to continue, retry or stop.

## Boundary

It is not an authoritative control plane. High-risk authorisation and policy checks should be deterministic services, not another model prompt.

## How it is used

Supervisor Agent is used when one agent is responsible for routing work to specialised workers and deciding whether to continue or stop. It is the right term when orchestration is still model-led, but the system needs a clear top of chain.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
