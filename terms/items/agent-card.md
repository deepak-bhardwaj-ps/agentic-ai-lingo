---
title: Agent Card
short_description: A JSON document that tells other systems what an A2A agent is, what it can do, and how to contact it.
category: Protocols
tags:
- protocol
- interoperability
- ai-agents
status: active
aliases:
- agent card
meaning_type: novel
novelty_level: medium
maturity_level: established
common_misuse:
- Treating it as a general profile for any AI agent, rather than the discovery document defined by A2A.
- Assuming it describes the agent's whole behaviour or safety policy.
related_terms:
- A2A protocol
- agent registry
- service endpoint
- agent discovery
- authentication
evidence:
- source_title: Agent2Agent (A2A) Protocol Specification
  source_url: https://a2a-protocol.org/latest/specification/
  source_type: standards_doc
  relevance: The core specification defines what an Agent Card is in the protocol.
  key_point: The spec says an Agent Card is a JSON metadata document published by an A2A Server that describes identity, capabilities, skills, service endpoint, and authentication requirements.
- source_title: Agent Discovery - A2A Protocol
  source_url: https://a2a-protocol.org/latest/topics/agent-discovery/
  source_type: official_docs
  relevance: Explains how the card is used in practice for discovery.
  key_point: The docs describe the Agent Card as a digital business card that helps clients find an agent and understand how to interact with it securely.
- source_title: Developer's Guide to AI Agent Protocols
  source_url: https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/
  source_type: engineering_blog
  relevance: Gives a plain-language explanation from a main protocol backer.
  key_point: Google explains that each A2A agent publishes an Agent Card at a well-known URL so other systems can discover its name, capabilities, and endpoint.
---
An Agent Card is a JSON file that describes an A2A agent so other systems can find it and know how to talk to it.

In practice, it works like a small digital business card for an agent. It usually tells you the agent's name, what it can do, where its service lives, and what kind of login or permission it needs.

It matters because agents need a standard way to discover one another. Without that, every team would have to invent its own way to publish agent details and connect to them.

An Agent Card is not the agent itself. It does not make the agent intelligent, decide what it should do, or replace its safety rules. It is just the description other systems read before they connect.
