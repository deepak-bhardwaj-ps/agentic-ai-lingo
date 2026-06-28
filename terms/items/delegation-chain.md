---
slug: delegation-chain
title: Delegation Chain
short_description: A delegation chain is the line of people or systems that pass authority
  from one to another.
category: Governance
tags:
- governance
- security
- delegation
- agents
status: active
aliases:
- delegated chain
- authority chain
- chain of delegation
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a real control when no scope, approval, or record exists
- Assuming authority automatically passes through every hand-off
- Forgetting to track who is still responsible at each step
related_terms:
- act-on-behalf
- delegated authority
- authorization
- token exchange
- audit trail
evidence:
- source_title: RFC 6749 - The OAuth 2.0 Authorization Framework
  source_url: https://datatracker.ietf.org/doc/html/rfc6749
  source_type: standards_doc
  relevance: Shows the standard web model for limited access granted to a third party
    on behalf of someone else.
  key_point: OAuth lets a third-party app get limited access instead of taking full
    control.
- source_title: RFC 8693 - OAuth 2.0 Token Exchange
  source_url: https://datatracker.ietf.org/doc/html/rfc8693
  source_type: standards_doc
  relevance: Shows how one token can be exchanged for another while keeping track
    of who the original subject and acting party are.
  key_point: Token exchange is used when one service acts for another and the chain
    of actors needs to stay clear.
- source_title: Microsoft identity platform and OAuth 2.0 On-Behalf-Of flow
  source_url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow
  source_type: official_docs
  relevance: Gives a real-world example of service-to-service delegation with a middle
    service acting for a user.
  key_point: A service can use a user’s token to ask for a new token for a downstream
    service, but only within the right scope.
- source_title: OWASP Top 10 for Agentic Applications 2026
  source_url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
  source_type: official_docs
  relevance: Shows that agentic systems need clear boundaries, permissions, and controls
    because they can take real actions.
  key_point: Excessive agency is a security risk when an agent can trigger high-impact
    actions without enough control.
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Shows that agent systems involve orchestration, tool execution, approvals,
    and state, which makes hand-off tracking important.
  key_point: When software owns orchestration and approvals, the system must keep
    track of who asked for what and what was allowed.
---

A delegation chain is the line of people or systems that pass authority from one to another.

In practice, it shows who started the request, who was allowed to act, what they were allowed to do, and where the authority ended. Each hand-off should be clear, limited, and recorded.

This matters because agents can take real actions, not just give answers. If the chain is unclear, it becomes hard to tell who approved the action, who is responsible, and whether the action was allowed.

It is not the same as trust by itself. It is not a full handover of control. It is not safe just because something is called a delegation chain. Without clear limits, checks, and records, it is only a label.
