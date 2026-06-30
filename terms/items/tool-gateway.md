---
title: Tool Gateway
short_description: A tool gateway is a middle layer that checks and controls agent
  tool calls before they reach real systems.
category: Core
tags:
- agentic-ai
- tools
- governance
- security
status: draft
aliases:
- MCP gateway
- tool proxy
- tool access gateway
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it like a protocol instead of a system design pattern
- Assuming it replaces proper authorisation in the target system
- Using it only for routing, without policy checks or logging
related_terms:
- API gateway
- MCP
- authorisation
- policy enforcement
- audit logging
evidence:
- source_title: OWASP Top 10 for Large Language Model Applications
  source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
  source_type: standards_doc
  relevance: OWASP’s LLM security guidance supports the need to control tool access,
    validate inputs, and limit damage from unsafe tool use.
  key_point: Agent tool use needs controls such as validation, approval, and logging
    to reduce security risk.
- source_title: Model Context Protocol - Authorization
  source_url: https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization
  source_type: official_docs
  relevance: MCP defines transport-level authorisation for restricted servers, which
    supports the idea of a controlled access layer for tools.
  key_point: Access to MCP servers can be restricted and authorised at the protocol
    transport level.
- source_title: Request validation for REST APIs in API Gateway
  source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html
  source_type: official_docs
  relevance: API gateways commonly validate requests before they reach backend systems,
    which is the same basic pattern used by tool gateways.
  key_point: A gateway can validate request parameters and schemas before forwarding
    traffic.
- source_title: MCP Schema Validation Policy
  source_url: https://docs.mulesoft.com/gateway/latest/policies-included/mcp-schema-validation
  source_type: official_docs
  relevance: Shows a real gateway product applying schema checks to MCP tool calls,
    which is direct evidence that this pattern is being implemented in practice.
  key_point: Gateways can validate MCP requests and tool schemas before the upstream
    server sees them.
---
A tool gateway is a middle layer that sits between an agent and the tools it can use.

It checks a tool call before letting it through. That can include who is allowed to call it, whether the request matches the expected shape, whether the call should be logged, and whether it should be slowed down or blocked.

In practice, this helps keep an agent from reaching every tool directly. The gateway can act like a guard at the door, so only allowed requests go to the real system.

This matters because tools can change data, send messages, or start actions in other systems. If an agent makes a bad request, the gateway can reduce the harm.

A tool gateway is not a language model. It is not the tool itself. It is also not a full replacement for permissions inside the target system, because the target system still needs its own security checks.

The term is still somewhat new and not fully standard. Different teams may use different names for the same idea, such as a tool proxy or [[MCP]] gateway.
