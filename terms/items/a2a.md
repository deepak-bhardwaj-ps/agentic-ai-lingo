---
slug: a2a
name: A2A
category: Protocols
title: A2A
aliases:
- Agent2Agent
short_description: A2A is an open standard that lets one AI agent find, talk to, and
  hand work to another AI agent.
status: established
meaning_type: novel
novelty_level: high
maturity_level: established
common_misuse:
- Treating A2A as a full agent framework instead of a communication protocol.
- Assuming it replaces the agent's own reasoning, tools, or safety rules.
related_terms:
- MCP
- agent card
- multi-agent system
evidence:
- source_title: A2A Protocol
  source_url: https://a2a-protocol.org/latest/
  source_type: official_docs
  relevance: Official overview of the protocol.
  key_point: A2A is an open standard for communication and collaboration between AI
    agents, with a separate section explaining what it is not.
- source_title: Agent2Agent (A2A) Protocol Specification
  source_url: https://a2a-protocol.org/latest/specification/
  source_type: standards_doc
  relevance: Technical specification for how the protocol works.
  key_point: The spec says A2A supports discovery, task exchange, progress updates,
    and results, while keeping each agent's internal state private.
- source_title: Announcing the Agent2Agent Protocol (A2A)
  source_url: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
  source_type: engineering_blog
  relevance: Explains the design goals and intended use.
  key_point: Google describes A2A as a way for agents to communicate securely and
    coordinate work, alongside other protocols such as MCP.
---

A2A is a standard that helps one AI agent find another AI agent, talk to it, and pass work to it.

In practice, A2A gives agents a common way to share what they can do, send a task, show progress, and return the result. This matters when different agents are built by different teams or companies and still need to work together.

It matters because one agent is usually not good at everything. A2A makes it easier for specialised agents to cooperate instead of forcing one system to do every job on its own.

A2A is not the agent itself, and it is not the code that makes an agent smart. It does not decide how the agent thinks, which tools it uses, or what safety rules it follows. It only defines how agents communicate.
