---
slug: agent-mesh
title: Agent Mesh
category: Protocols
short_description: A loose term for a network of AI agents that can find each other
  and hand work around without one central controller.
tags:
- agents
- interoperability
- protocols
- multi-agent-systems
status: Emerging
aliases:
- Mesh of agents
- Agent mesh network
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Used for any group of agents, even when there is no discovery, routing, or shared
  rules.
- Used as a marketing label for systems that are still controlled by one central coordinator.
- Used as if it guarantees interoperability between different vendors or frameworks.
related_terms:
- A2A Protocol
- Model Context Protocol
- multi-agent system
- agent orchestration
- agent discovery
evidence:
- source_title: A2A Protocol - Agent2Agent (A2A) Protocol Resources
  source_url: https://www.a2aprotocol.org/
  source_type: official_docs
  relevance: Describes core features that a true agent-to-agent setup needs.
  key_point: A2A frames discovery, task management, and structured exchange as explicit
    parts of agent collaboration.
- source_title: Getting Started with A2A Protocol
  source_url: https://www.a2aprotocol.org/en/tutorials/getting-started
  source_type: official_docs
  relevance: Shows how one agent finds another in the protocol.
  key_point: Discovery starts by fetching an Agent Card from a known location, so
    finding agents is designed in rather than assumed.
- source_title: Authorization - Model Context Protocol
  source_url: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
  source_type: official_docs
  relevance: Shows that safe connectivity also needs explicit transport rules and
    access control.
  key_point: MCP defines authorisation at the transport level, so connection alone
    is not enough for safe interoperability.
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Warns against treating complex multi-agent designs as automatically better.
  key_point: Many effective agent systems use simple, composable patterns rather than
    vague network metaphors.
---

## Meaning

An agent mesh is a name for a group of AI agents that can find each other and pass work between themselves, usually without one central controller.

In practice, each agent may advertise what it can do, be reachable at a known place, and hand a task to another agent. For the idea to mean something useful, there also need to be clear rules for finding agents, sending tasks, and deciding who is trusted. If those rules are missing, it is just a group of bots.

The term matters because it describes a looser way to organise work. One agent can focus on one job, and another can take a different job. That can make a system easier to grow, but also harder to test, understand, and secure.

It is not the same as any multi-agent system. It is not just several agents working together. It is also not a promise that different companies’ tools will work together. If there is no clear way to discover agents, reach them, and exchange work safely, the word mesh is mostly a label.
