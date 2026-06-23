---
slug: agent-control-plane
name: Agent Control Plane
category: Runtime
title: Agent Control Plane
aliases: []
short_description: Agent Control Plane is used in runtime design to name the component
  that coordinates decisions and side effects.
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

Agent Control Plane is used in runtime design to name the component that coordinates decisions and side effects. A useful specification gives its input event, durable state, action contract, retry policy, timeout and terminal states.

## Evidence

[NIST AI RMF: Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
