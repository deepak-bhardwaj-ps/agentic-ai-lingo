---
slug: agent-mesh
name: Agent Mesh
category: Protocols
title: Agent Mesh
aliases:
short_description: A mesh is a decentralised agent network with real discovery,
termStatus: Emerging interoperability/architecture label
researchBasis: A2A protocol, MCP, Anthropic
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Emerging interoperability/architecture label.

## Meaning

A mesh is a decentralised network of agents that can discover and route work to one another.
The label only earns its keep when discovery, addressing, and routing are explicit enough to survive implementation.

## Boundary

It is not a protocol unless it defines a public wire format, lifecycle, compatibility, and security model. Do not imply interoperability from the label alone.

## How it is used

It is used when coordination is decentralised and agents need discovery, addressing, and routing rules to work together without one central coordinator. The phrase only earns its keep if the mesh has real topology and not just a metaphor in a slide deck.

## Evidence

[Agent2Agent protocol specification](https://[[A2A|a2a]]-protocol.org/dev/specification/) shows what real agent-to-agent interoperability has to spell out: discovery, message exchange, and participation rules.

[Model Context Protocol authorization](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) shows the adjacent problem on the tool side: wiring agents to systems safely needs explicit auth, not just connectivity.

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) reinforces that most production systems still depend on simple composable patterns rather than vague network metaphors.
