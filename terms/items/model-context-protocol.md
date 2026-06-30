---
title: Model Context Protocol
short_description: An open standard, usually called MCP, that lets AI apps connect to tools, data, and workflows in a shared way.
category: Protocols
tags:
  - ai
  - protocol
  - tools
  - integration
status: established
aliases:
  - MCP
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: established
common_misuse:
  - Treating Model Context Protocol as a model, app, or agent instead of a protocol
  - Assuming MCP itself gives access to data without the user or host approving it
  - Using the full name as if it were different from MCP
related_terms:
  - MCP client
  - MCP server
  - tools
  - resources
  - prompts
evidence:
  - source_title: Model Context Protocol
    source_url: https://modelcontextprotocol.io/docs/getting-started/intro
    source_type: official_docs
    relevance: Official introduction from the protocol maintainers, useful for the plain-language definition and scope.
    key_point: MCP is an open-source standard for connecting AI applications to external systems such as local files, databases, tools, and workflows.
  - source_title: Specification - Model Context Protocol
    source_url: https://modelcontextprotocol.io/specification/2025-11-25
    source_type: standards_doc
    relevance: The current protocol specification is the most authoritative source for what MCP formally is and how it works.
    key_point: MCP is an open protocol with defined client-server behaviour, security considerations, and built-in concepts such as tools and resources.
  - source_title: Introducing the Model Context Protocol
    source_url: https://www.anthropic.com/news/model-context-protocol
    source_type: engineering_blog
    relevance: Early maintainer explanation that shows the intended use of MCP as a connection standard, not a model or app.
    key_point: MCP is an open standard for secure, two-way connections between data sources and AI-powered tools.
---
Model Context Protocol is the full name for MCP.

It is a standard way for an AI app to connect to outside tools and data. In practice, that can mean reading files, checking a database, or asking a helper service to do a job for the app.

This matters because it gives different AI apps and services one shared way to work together instead of each team building its own custom link.

It is not the AI model itself. It is not the chatbot. It is also not a guarantee that a connected system is safe. People still have to choose which MCP servers to trust and what they are allowed to access.
