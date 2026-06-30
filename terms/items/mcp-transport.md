---
title: MCP transport
short_description: MCP transport is the way an MCP client and server send messages to each other.
category: Protocols
tags:
  - model-context-protocol
  - transport
  - protocol
status: established
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse:
  - Treating the transport as the whole MCP protocol
  - Confusing a transport with a server or client
  - Assuming every MCP setup uses the same transport
related_terms:
  - Model Context Protocol
  - MCP client
  - MCP server
  - stdio
  - Streamable HTTP
evidence:
  - source_title: Transports
    source_url: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
    source_type: standards_doc
    relevance: Current official specification for how MCP messages move between clients and servers.
    key_point: The MCP spec says transport is the communication binding, and that the standard transports are stdio and Streamable HTTP.
  - source_title: Architecture overview
    source_url: https://modelcontextprotocol.io/docs/learn/architecture
    source_type: official_docs
    relevance: Explains where transport fits in the MCP architecture and how local and remote servers differ.
    key_point: MCP has a transport layer separate from the data layer, and STDIO is typically used for local servers while Streamable HTTP is typically used for remote servers.
  - source_title: Introducing the Model Context Protocol
    source_url: https://www.anthropic.com/news/model-context-protocol
    source_type: engineering_blog
    relevance: Early source from the organisation that introduced MCP, useful for the original design intent.
    key_point: MCP was introduced as a standard way to connect AI apps to external systems through a client-server model.
---

MCP transport is the way an MCP client and an MCP server send messages to each other.

In practice, the transport is the connection method underneath MCP. The official MCP spec currently defines stdio and Streamable HTTP as the standard transports, and it also allows custom transports.

This matters because the transport affects how the connection is started, how messages are framed, and whether the server is local or remote. A local MCP server often uses stdio. A remote MCP server often uses Streamable HTTP.

An MCP transport is not the whole MCP protocol. It does not define what the messages mean. It is also not the same thing as an MCP client or server. It is just the path the messages travel through.
