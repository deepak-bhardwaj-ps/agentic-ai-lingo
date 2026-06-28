---
slug: tool-authorization
title: Tool Authorization
short_description: Rules that decide whether an agent may use a tool or take an action.
category: Governance
tags:
- governance
- security
- agents
- authorization
status: active
aliases:
- tool access control
- tool permissions
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating the model’s choice to call a tool as proof that the user is allowed to
  do it.
- Hiding the rule inside prompts instead of enforcing it in a real policy check.
- Giving every tool to every agent and calling that “guardrails”.
related_terms:
- authorization
- least privilege
- permission-gates
- delegation-policy
- human-oversight
evidence:
- source_title: Authorization - Model Context Protocol
  source_url: https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
  source_type: official_docs
  relevance: Shows that agent systems need transport-level authorisation for restricted
    servers.
  key_point: MCP defines authorization flows so clients can request access on behalf
    of a resource owner and servers can validate tokens for the right audience.
- source_title: RAG Security Cheat Sheet - Tool Invocation and Agent Safety
  source_url: https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html
  source_type: official_docs
  relevance: Explains why tool calls need their own checks in agent systems.
  key_point: OWASP says tool-level authorisation must be enforced independently of
    the model’s decision to call a tool.
- source_title: Zero Trust Architecture
  source_url: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=930420
  source_type: standards_doc
  relevance: Provides the broader security idea behind limiting access per request.
  key_point: NIST describes zero trust as making accurate least-privilege access decisions
    for each request.
- source_title: Agent approvals & security
  source_url: https://developers.openai.com/codex/agent-approvals-security
  source_type: official_docs
  relevance: Shows a practical approval model for risky tool actions.
  key_point: Destructive app or MCP tool calls require approval when the tool advertises
    side effects.
---

Tool Authorization is the rule that decides whether an agent is allowed to use a tool or carry out a specific action.

In practice, it means the system checks the request before the action happens. The check should look at who the agent is acting for, what tool is being used, what the action will do, and whether the request fits the allowed scope. If the action is risky, a human may need to approve it.

This matters because an agent can choose the wrong tool, be tricked into using it badly, or be given more power than it should have. Good tool authorisation limits damage, makes responsibility clearer, and helps with auditing and stopping bad actions.

It is not the same as a prompt saying “be careful”. It is also not the same as the model deciding to call a tool. Real authorisation is enforced by the system, not just described in text.
