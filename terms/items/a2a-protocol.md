---
title: A2A protocol
short_description: A2A protocol is the Agent2Agent standard for letting one AI agent find, talk to, and hand work to another.
category: Protocols and standards
tags:
- ai
- protocol
- interoperability
status: established
aliases:
- Agent2Agent protocol
meaning_type: novel
novelty_level: high
maturity_level: established
common_misuse:
- Treating A2A as a full agent framework instead of a communication protocol.
- Assuming it replaces an agent's own reasoning, tools, or safety rules.
related_terms:
- A2A
- agent card
- multi-agent system
- MCP
evidence:
- source_title: A2A Protocol
  source_url: https://a2a-protocol.org/latest/
  source_type: official_docs
  relevance: Official overview of the protocol and its current naming.
  key_point: The official site defines A2A as the Agent2Agent protocol and says it is an open standard for communication and collaboration between AI agents.
- source_title: Agent2Agent (A2A) Protocol Specification
  source_url: https://a2a-protocol.org/latest/specification/
  source_type: standards_doc
  relevance: Technical specification for what the protocol actually does.
  key_point: The spec says A2A is for communication and interoperability between independent AI agent systems and supports discovery, task exchange, progress updates, and results.
- source_title: Announcing the Agent2Agent Protocol (A2A)
  source_url: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
  source_type: engineering_blog
  relevance: Early design explanation from one of the main backers.
  key_point: Google describes A2A as a protocol for agents from different vendors and frameworks to communicate and coordinate work.
---

A2A protocol is the standard for letting one AI agent find another agent, talk to it, and hand work to it.

In practice, A2A gives agents a shared way to advertise what they can do, send a task, show progress, and return a result. It is meant for cases where agents come from different teams, products, or companies.

It matters because one agent usually cannot do everything well. A2A makes it easier for specialised agents to work together without custom integration for every pair.

It is not the agent itself, and it is not the code that makes an agent smart. It does not decide how the agent thinks, which tools it uses, or what safety rules it follows. It only defines how agents communicate.
