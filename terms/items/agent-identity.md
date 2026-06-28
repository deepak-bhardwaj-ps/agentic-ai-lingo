---
slug: agent-identity
title: Agent Identity
name: Agent Identity
category: Governance
short_description: The separate identity an AI agent uses so systems can recognise
  it, control what it can do, and trace its actions
aliases:
- AI agent identity
- agent workload identity
status: active
tags:
- governance
- security
- identity
- ai-agents
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating the user’s identity as the agent’s identity
- Using one shared service account for every agent
- Thinking identity alone is enough to make an agent safe
related_terms:
- authentication
- authorisation
- service account
- workload identity
- delegated access
evidence:
- source_title: What are agent identities?
  source_url: https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities
  source_type: official_docs
  relevance: Defines agent identities as separate identity accounts for AI agents.
  key_point: Agent identities are meant to be distinct from human identities so agents
    can authenticate and be controlled on their own.
- source_title: Overview of agent identities in Microsoft Entra
  source_url: https://learn.microsoft.com/en-us/entra/agent-id/agent-identities
  source_type: official_docs
  relevance: Explains how agent identity is used as the main account for an AI agent.
  key_point: Agent identity is the primary account an AI agent uses to authenticate
    and access resources.
- source_title: AI Agent Authentication and Authorization
  source_url: https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/
  source_type: standards_doc
  relevance: Shows that agent identity is being handled by extending existing identity
    and access standards.
  key_point: The draft treats agent identity as part of a wider security model rather
    than a brand-new protocol.
- source_title: OWASP Top 10 for Agentic Applications for 2026
  source_url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
  source_type: industry_article
  relevance: Explains why weak identity and excessive privilege are major risks in
    agentic systems.
  key_point: If agent identity is handled badly, an agent can get too much power or
    do actions that are hard to trace.
---

Agent identity is the special identity an AI agent uses when it acts.

In practice, it is like a name badge and access card for the agent. It helps a system know which agent is making a request, what that agent is allowed to do, and which actions came from it.

This matters because agents can read data, use tools, and make changes. If they all share the same identity, it becomes hard to control them, limit them, or find out what happened when something goes wrong.

Agent identity is not the same as a person’s login. It is also not a full safety system on its own. A safe setup still needs permission checks, logging, approval steps, and a way to stop the agent.
