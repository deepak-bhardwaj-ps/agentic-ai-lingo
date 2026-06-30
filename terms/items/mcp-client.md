---
title: MCP client
short_description: A software component in an MCP host that connects to an MCP server and asks it for context or tools.
category: Tools and products
tags:
  - model-context-protocol
  - ai-tools
status: review
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating the client as the whole app, when it is usually just one part of the app.
  - Confusing the client with the MCP server, which is the thing being connected to.
  - Using the term to mean any app that uses AI tools, even if it does not speak MCP.
related_terms:
  - Model Context Protocol
  - MCP host
  - MCP server
  - tool
evidence:
  - source_title: Understanding MCP clients
    source_url: https://modelcontextprotocol.io/docs/learn/client-concepts
    source_type: official_docs
    relevance: The clearest current definition of the term from the protocol maintainers.
    key_point: MCP clients are components created by host applications to communicate with specific MCP servers, with each client handling one direct server connection.
  - source_title: Architecture overview
    source_url: https://modelcontextprotocol.io/docs/learn/architecture
    source_type: official_docs
    relevance: Confirms where the client sits in the MCP architecture and how it differs from host and server roles.
    key_point: The architecture defines an MCP client as a component that maintains a connection to an MCP server and gets context for the host to use.
  - source_title: Introducing the Model Context Protocol
    source_url: https://www.anthropic.com/news/model-context-protocol
    source_type: engineering_blog
    relevance: Early but still influential explanation from one of the protocol's creators.
    key_point: Describes MCP clients as the AI applications that connect to MCP servers in the protocol's two-way architecture.
---

An MCP client is the part of an app that connects to an MCP server and asks it for context, tools, or other information.

In practice, the client sits inside a bigger app called the host. The host manages what the user sees, while the client handles the conversation with one MCP server. If the app connects to several servers, it usually has several clients.

The term matters because MCP is meant to make tool connections more standard. A client can reuse the same protocol to talk to different servers instead of needing a separate custom link for each one.

An MCP client is not the server itself. It is also not the whole app unless the app only does that one job. The term is specific to the Model Context Protocol, so it should not be used for any ordinary software client that just happens to call an API.
