---
slug: agent-registry
name: Agent Registry
category: Protocols
title: Agent Registry
aliases: []
short_description: A registry is a catalogue of agent identities, capabilities,
  endpoints, versions, owners, and lifecycle status.
termStatus: Architecture component
researchBasis: OWASP Top 10 for LLM Applications, PROV-AGENT, provenance research
sources:
- https://genai.owasp.org/llm-top-10/
- https://arxiv.org/abs/2508.02866
- https://arxiv.org/abs/1703.03835
---

## Term status

Architecture component.

## Meaning

A registry is a catalogue of agent identities and metadata such as owner, capabilities, endpoints, versions, and lifecycle status.

## Boundary

It is not discovery interoperability by itself, nor a marketplace. Registration should not grant execution authority.

## How it is used

It is used when systems need a durable directory of agents rather than an ad hoc list or marketplace. It matters when identity, lifecycle status, and ownership have to be queried reliably.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) supports the governance framing: third-party or untrusted capabilities need review and provenance, not blind registration.

[PROV-AGENT](https://arxiv.org/abs/2508.02866) shows why registry metadata needs to connect to downstream interactions and traceability.

[Provenance Threat Modeling](https://arxiv.org/abs/1703.03835) is an older but still relevant reference for why metadata and provenance matter for ownership attribution and debugging.
