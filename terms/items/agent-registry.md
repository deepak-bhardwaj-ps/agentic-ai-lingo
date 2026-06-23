---
slug: agent-registry
name: Agent Registry
category: Protocols
title: Agent Registry
aliases: []
short_description: Agent Registry is a catalogue of agent identities, capabilities,
  endpoints, versions, and owners.
termStatus: Architecture component
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://genai.owasp.org/llm-top-10/
---

## Term status

Architecture component.

## Meaning

An agent [[Registry|registry]] is a catalogue of agent identities and metadata such as owner, capabilities, endpoints, versions and lifecycle status.

## Boundary

It is not discovery interoperability by itself, nor a marketplace. Registration should not grant execution authority.

## How it is used

Agent Registry is used when systems need a durable directory of agents rather than an ad hoc list or marketplace. It matters when identity, lifecycle status, and ownership have to be queried reliably.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
