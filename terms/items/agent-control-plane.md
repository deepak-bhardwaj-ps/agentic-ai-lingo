---
slug: agent-control-plane
name: Agent Control Plane
category: Runtime
title: Agent Control Plane
aliases: []
short_description: Agent Control Plane is the service layer that coordinates fleet-level
  policy, configuration, identity, and lifecycle.
termStatus: Architecture pattern
researchBasis: 'NIST AI RMF: Generative AI Profile'
sources:
- https://doi.org/10.6028/NIST.AI.600-1
---

## Term status

Architecture pattern.

## Meaning

An agent control plane is a proposed central service layer for fleet-level configuration, identity, policy, deployment, observability and lifecycle management.

## Boundary

It borrows the control-plane/data-plane metaphor; it is not a standard component and should not be confused with the agent's own decision loop.

## How it is used

Agent Control Plane is used when the conversation is about shared policy and orchestration across many agents rather than one agent’s internal loop. The useful question is what state it owns, what it can change, and which actions it can authorise.

## Evidence

[NIST AI RMF: Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
