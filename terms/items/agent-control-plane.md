---
slug: agent-control-plane
name: Agent Control Plane
category: Runtime
title: Agent Control Plane
aliases:
short_description: Agent Control Plane is the service layer that coordinates fleet-level
termStatus: Architecture pattern
researchBasis: 'NIST AI RMF: Generative AI Profile'
sources:
- https://learn.microsoft.com/en-us/agents/adoption-maturity-model/maturity-model-security-governance
---

## Term status

Architecture pattern.

## Meaning

An agent control plane manages the conditions under which an agent fleet may exist and operate: registration, identity, policy, configuration, release, telemetry, incident response, and retirement. It borrows the infrastructure meaning of control plane—global decisions and desired state—rather than describing an agent’s local reasoning loop.

The pattern has moved beyond theory: Microsoft Foundry now uses “Control Plane” for its fleet-management product. The broader label remains an architecture pattern, not a portable standard component.

## Common misconceptions

The control plane should not sit in the execution path for every model token. That turns governance into a latency and availability bottleneck. It publishes policy, credentials, configuration, and controls; the runtime or data plane executes individual tasks and must still fail safely when central services are unavailable.

It also is not an “agent brain”. Prompt logic, planning, tool selection, and short-lived task state belong with the runtime. A control plane may constrain those behaviours, but it should not disguise centrally managed prompts as enterprise governance.

## How it is used

A practical implementation provides an [[Agent Registry|agent registry]], workload identities, scoped tool grants, versioned policy, approved model and connector catalogues, deployment promotion, traces, evaluation records, and emergency revocation. Kubernetes supplies the relevant systems analogy: its control plane manages cluster state while worker nodes run workloads.

Define authority boundaries early. The platform team might revoke an agent’s tool credential and quarantine a release; the business owner approves its purpose and data use; the runtime enforces a per-request decision. NIST’s GenAI profile supports the need for lifecycle risk management, but does not prescribe this particular topology.

## Evidence

[Kubernetes’ architecture](https://kubernetes.io/docs/concepts/architecture/) defines the original control-plane metaphor. [Microsoft Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview) demonstrates current agent-fleet usage, while [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) and [Microsoft’s governance guidance](https://learn.microsoft.com/en-us/agents/adoption-maturity-model/maturity-model-security-governance) support the associated risk and lifecycle concerns.
