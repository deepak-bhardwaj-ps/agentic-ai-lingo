---
title: MCP connector
short_description: Anthropic’s MCP connector is a Claude API feature for connecting to remote MCP servers without building a separate MCP client.
category: Tools and products
tags:
- anthropic
- claude
- mcp
- tools
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the MCP standard itself rather than Anthropic’s connector feature
- Assuming it works with every MCP transport, including local STDIO servers
- Confusing it with a generic integration or plugin
related_terms:
- Model Context Protocol
- remote MCP server
- MCP client
- tool use
- Claude API
evidence:
- source_title: MCP connector
  source_url: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
  source_type: official_docs
  relevance: This is the primary product documentation for the term and shows that MCP connector is Anthropic’s feature for connecting the Messages API to remote MCP servers.
  key_point: Claude’s MCP connector lets you connect to remote MCP servers directly from the Messages API without a separate MCP client.
- source_title: Remote MCP servers
  source_url: https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers
  source_type: official_docs
  relevance: This page shows how Anthropic uses the connector feature in practice and confirms that the servers are third-party remote services connected through the MCP connector API.
  key_point: Remote MCP servers are connected through the Anthropic MCP connector API and are not owned or operated by Anthropic.
- source_title: What is the Model Context Protocol (MCP)?
  source_url: https://modelcontextprotocol.io/docs/getting-started/intro
  source_type: official_docs
  relevance: This defines MCP itself, which matters because the glossary term is a connector feature built on top of MCP, not MCP as a whole.
  key_point: MCP is an open standard for connecting AI applications to external systems, tools, data sources, and workflows.
---

MCP connector is Anthropic’s feature for linking Claude’s Messages API to remote MCP servers.

In practice, it lets Claude use tools exposed by a remote MCP server without you building a separate MCP client yourself. That makes it easier to connect Claude to external systems such as issue trackers, databases, or other services that expose MCP tools.

This matters because it is a practical bridge between Claude and outside systems. It reduces the amount of glue code needed when you want Claude to read data or take actions through a remote service.

It is not the same thing as the MCP standard. It is also not a general name for every kind of plugin, connector, or integration. In Anthropic’s docs, it is specifically for remote MCP servers, not local STDIO servers.
