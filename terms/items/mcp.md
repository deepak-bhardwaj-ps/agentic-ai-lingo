---
slug: mcp
name: MCP
category: Protocols
title: MCP
aliases: null
short_description: MCP is the Model Context Protocol for connecting models to tools,
termStatus: Established protocol
researchBasis: Model Context Protocol specification
sources:
- https://modelcontextprotocol.io/specification/2025-06-18
---

## Term status

Established protocol.

## Meaning

Model Context Protocol is a client-server protocol through which an AI application can discover and call tools, read resources and use prompt templates supplied by an MCP server.

## Boundary

MCP is not an agent protocol: it connects an AI host to a capability provider. It does not grant trust, authorisation or safe execution by itself.

## How it is used

MCP is used when a model needs a standard way to discover tools, resources, and prompts from an external server. It matters because the protocol constrains the integration surface, but it does not by itself solve orchestration, policy, or trust.

## Evidence

[Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-06-18) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
