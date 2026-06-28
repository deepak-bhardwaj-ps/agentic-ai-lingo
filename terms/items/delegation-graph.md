---
slug: delegation-graph
name: Delegation Graph
category: Governance
title: Delegation Graph
aliases:
- delegated authority graph
- delegation chain
short_description: A delegation graph shows who gave an agent permission to act, what
  it may do, and how that permission passes along a chain.
status: active
meaning_type: emerging_unsettled
novelty_level: high
maturity_level: experimental
common_misuse:
- Using the term for any tool call history, even when no authority was actually delegated.
- Assuming a single access token or log entry is enough to show who is responsible.
related_terms:
- delegation
- authorization
- access control
- audit trail
- provenance
- human oversight
evidence:
- source_title: The OAuth 2.0 Authorization Framework (RFC 6749)
  source_url: https://datatracker.ietf.org/doc/html/rfc6749
  source_type: standards_doc
  relevance: Shows the standard meaning of delegated authorization in software systems.
  key_point: OAuth lets a third-party app get limited access on behalf of a resource
    owner.
- source_title: OAuth 2.0 Token Exchange (RFC 8693)
  source_url: https://www.rfc-editor.org/info/rfc8693/
  source_type: standards_doc
  relevance: Shows how delegation can pass through a chain of actors.
  key_point: The standard covers token exchange for delegation and impersonation scenarios.
- source_title: Authorization Propagation in Multi-Agent AI Systems
  source_url: https://arxiv.org/html/2605.05440v1
  source_type: research_paper
  relevance: Explains why delegation in agentic systems must be tracked as a flow,
    not a single permission check.
  key_point: Authorization must hold at every point in a directed graph of delegations
    and accesses.
- source_title: OWASP Top 10 for LLM Applications 2025
  source_url: https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
  source_type: official_docs
  relevance: Places delegation and privilege control inside current AI security guidance.
  key_point: Agent and privilege abuse are recognised risks in LLM and agentic systems.
---

A delegation graph is a map of who is allowed to act for whom, and what that permission covers.

In practice, it shows the path of authority from a person or system to an AI agent, and sometimes from one agent to another. It can record what the agent may do, where that permission came from, when it ends, and how it can be taken back.

This matters because [[Agentic AI|agentic systems]] can take actions, cal[[Context Collapse|l]] tools, and pass work to other agents. If you do not track delegation clearly, it becomes hard to know who approved an action, who is responsible, and whether the agent stayed within its limits.

It is not just a log of events. It is not the same as general monitoring. And it is not a standard term with one fixed definition yet, so different teams may use it in slightly different ways.
