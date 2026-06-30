---
title: MCP server
short_description: A program that exposes tools, data, or prompts to an MCP client through the Model Context Protocol.
category: Tools and products
tags:
  - model-context-protocol
  - ai-tools
  - protocol
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Using "MCP server" to mean any ordinary web server or API server
  - Treating the server as the AI model itself
  - Confusing an MCP server with an MCP client, which is the part that connects to it
related_terms:
  - Model Context Protocol
  - MCP client
  - MCP host
  - tool
  - resource
evidence:
  - source_title: Build an MCP server
    source_url: https://modelcontextprotocol.io/docs/develop/build-server
    source_type: official_docs
    relevance: Shows the current maintainer definition and the kinds of capabilities a server can expose.
    key_point: MCP servers can provide tools, resources, and prompts to MCP clients, and the docs show how to build one for use in Claude Desktop and other clients.
  - source_title: Introducing the Model Context Protocol
    source_url: https://www.anthropic.com/news/model-context-protocol
    source_type: engineering_blog
    relevance: Early protocol explanation from one of the creators, useful for understanding the server/client split.
    key_point: Developers expose data through MCP servers, while MCP clients connect to those servers in a two-way architecture.
  - source_title: Connect to local MCP servers
    source_url: https://modelcontextprotocol.io/docs/develop/connect-local-servers
    source_type: official_docs
    relevance: Clarifies that MCP servers are separate programs that give apps controlled access to tools and local resources.
    key_point: MCP servers are programs that run on your computer and provide specific capabilities through a standard protocol, with user approval for actions.
---

An MCP server is a program that gives an MCP app access to tools, data, or prompts through the Model Context Protocol.

In practice, the server sits on the other side of the connection from the app. It might let the app read files, query a database, call an API, or use a pre-made prompt. Some MCP servers run on your computer, and some run remotely.

The term matters because it gives AI apps a standard way to connect to useful services without building a one-off link for each app and each service.

An MCP server is not the AI model, and it is not the whole app. It is also not just any web server. It is a server that speaks MCP so an MCP client can discover and use its tools or data.
