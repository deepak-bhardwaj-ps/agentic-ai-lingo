---
title: ACP
short_description: ACP is the Agent Client Protocol, a standard for communication between code editors and coding agents.
category: Protocols
tags:
- ai
- protocol
- coding
- editor
status: emerging
aliases:
- Agent Client Protocol
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Thinking ACP is the agent itself rather than the protocol it uses
- Treating ACP as a general AI platform instead of an editor-to-agent communication standard
- Confusing ACP with MCP, which links AI apps to tools and data rather than editors to coding agents
related_terms:
- MCP
- A2A
- code editor
- coding agent
- JSON-RPC
evidence:
- source_title: Introduction - Agent Client Protocol
  source_url: https://agentclientprotocol.com/get-started/introduction
  source_type: official_docs
  relevance: Official definition from the ACP project homepage.
  key_point: ACP standardises communication between code editors/IDEs and coding agents, and is designed for both local and remote use.
- source_title: Overview - Agent Client Protocol
  source_url: https://agentclientprotocol.com/protocol/v1/overview
  source_type: standards_doc
  relevance: Shows how ACP actually works at the protocol level.
  key_point: ACP uses JSON-RPC-style methods and notifications so clients and agents can exchange prompts, progress updates, permissions, and results.
- source_title: Copilot CLI ACP server
  source_url: https://docs.github.com/en/copilot/reference/copilot-cli-reference/acp-server
  source_type: official_docs
  relevance: Confirms ACP is being used by a major tool vendor and frames the client/agent split clearly.
  key_point: GitHub describes ACP as the protocol that standardises communication between code editors and agents such as Copilot CLI.
---

ACP is the Agent Client Protocol. It is a standard way for a code editor to talk to a coding agent.

In practice, ACP lets an editor and an agent exchange messages about tasks, progress, permissions, and results. It is meant for coding tools, not for general chat between any two AI systems.

It matters because a shared protocol makes it easier for different editors and agents to work together without custom one-off integrations for each pair.

ACP is not the agent itself. It is not the AI model, and it is not the editor. It is the communication rule between them. It is also different from MCP, which connects AI apps to tools and data rather than editors to coding agents.
