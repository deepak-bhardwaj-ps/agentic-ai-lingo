---
slug: agentic-web
name: Agentic Web
title: Agentic Web
category: Protocols
short_description: A loose term for web services designed so software agents can find
  them, understand them, and use them with permission.
aliases:
- agentic web
status: emerging
tags:
- protocols
- agents
- web
meaning_type: emerging_unsettled
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it like an official web standard.
- Assuming any website is safe for an agent to use without permission or checks.
- Using it to mean chatbots on the web instead of machine-readable services and controls.
related_terms:
- Model Context Protocol
- agent
- agentic system
- API
- authorisation
- interoperability
evidence:
- source_title: AI Agent Protocol Community Group
  source_url: https://www.w3.org/community/agentprotocol/
  source_type: standards_doc
  relevance: Shows that the term is being used in current standards discussions about
    interoperable agent protocols on the web.
  key_point: W3C frames this as work on technical foundations for an emerging Agentic
    Web.
- source_title: Architecture overview - Model Context Protocol
  source_url: https://modelcontextprotocol.io/docs/learn/architecture
  source_type: official_docs
  relevance: Explains the protocol pattern behind agent-friendly services.
  key_point: MCP uses explicit servers, tools, resources, and transport-level authorisation
    rather than hidden browser automation.
- source_title: Understanding Authorization in MCP
  source_url: https://modelcontextprotocol.io/docs/tutorials/security/authorization
  source_type: official_docs
  relevance: Shows how access control is handled for restricted services.
  key_point: MCP expects explicit authorisation for sensitive resources and operations.
- source_title: Building effective agents
  source_url: https://www.anthropic.com/engineering/building-effective-agents
  source_type: engineering_blog
  relevance: Supports the idea that agent systems work best when tool surfaces are
    simple, explicit, and auditable.
  key_point: Anthropic recommends simple, composable patterns rather than complex
    frameworks.
- source_title: RFC 6749 The OAuth 2.0 Authorization Framework
  source_url: https://datatracker.ietf.org/doc/html/rfc6749
  source_type: standards_doc
  relevance: Provides the standard model for limited access to web services.
  key_point: OAuth is about granting limited access, which is the safety model this
    term depends on.
---

Agentic Web means a web built so software agents can find services, understand what they do, and use them with permission.

In practice, that means services should have clear descriptions, structured interfaces, identity checks, and rules about what an agent is allowed to do.

This matters because most websites are made for people clicking buttons, not for software acting safely on a person’s behalf.

It is not a formal web standard. It also does not mean an agent can safely use any website. A site still needs clear rules, permission, and safety checks.
