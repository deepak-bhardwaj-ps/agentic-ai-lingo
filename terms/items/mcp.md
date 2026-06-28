---
title: MCP
short_description: MCP is the Model Context Protocol, a standard way for AI apps to
  connect to tools and data.
category: Protocols
tags:
- ai
- protocol
- tools
- integration
status: established
aliases:
- Model Context Protocol
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: established
common_misuse:
- Thinking MCP is an AI model rather than a connection standard
- Thinking MCP itself makes a system safe or trustworthy
- Treating MCP as an agent that can plan or act on its own
related_terms:
- client-server architecture
- tools
- resources
- prompts
- authorization
evidence:
- source_title: What is the Model Context Protocol (MCP)?
  source_url: https://modelcontextprotocol.io/docs/getting-started/intro
  source_type: official_docs
  relevance: Introductory definition from the official MCP site.
  key_point: MCP is an open standard for connecting AI applications to external systems
    such as data sources, tools, and workflows.
- source_title: Architecture - Model Context Protocol
  source_url: https://modelcontextprotocol.io/specification/2025-06-18/architecture
  source_type: standards_doc
  relevance: Shows how MCP is structured and what problem it solves.
  key_point: MCP uses a client-host-server architecture built around context exchange
    and coordination between clients and servers.
- source_title: Tools - Model Context Protocol
  source_url: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
  source_type: standards_doc
  relevance: Defines one of MCP’s main features.
  key_point: MCP servers can expose tools that language models can invoke to interact
    with external systems.
- source_title: Introducing the Model Context Protocol
  source_url: https://www.anthropic.com/news/model-context-protocol
  source_type: engineering_blog
  relevance: Early explanation from the organisation that introduced MCP.
  key_point: MCP is an open standard for secure, two-way connections between data
    sources and AI tools.
---

MCP is a standard way for an AI app to connect to tools and data.

In practice, it lets one app ask another computer service for things like files, database records, search results, or helper actions. The AI app does not need a custom link for every service if both sides speak MCP.

It matters because it gives developers one shared way to plug AI apps into other systems. That makes connections easier to build, reuse, and maintain.

MCP is not the AI model itself. It is not an agent that thinks or decides things on its own. It is also not a promise of safety or trust. People still need to decide which servers to connect, what they can access, and what permissions they have.
