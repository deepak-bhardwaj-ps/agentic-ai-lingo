---
slug: agent-identity
name: Agent Identity
category: Governance
title: Agent Identity
aliases:
short_description: Agent Identity is the principal identity under which an agent acts
termStatus: Governance/security concept
researchBasis: OWASP Top 10 for LLM Applications
sources:
- https://www.ietf.org/archive/id/draft-klrc-aiagent-auth-02.html
---

## Term status

Governance/security concept.

## Meaning

Agent identity is the durable principal under which an agent authenticates, receives authority, acts, and is audited. It links a deployed workload to an accountable owner and makes its permissions, policy decisions, and actions distinguishable from both the user who requested work and the platform that hosts it.

For enterprise systems, an agent identity should be first-class rather than a shared integration account or a label embedded in a prompt.

## Common misconceptions

The agent’s identity is not the user’s identity. An agent may act on a user’s behalf, but its own credential needs separately bounded permissions, provenance, expiry, and revocation. Otherwise a trace cannot answer whether a user, an agent, or a downstream service made a change.

Nor does identity by itself secure an agent. The design still needs authentication, least-privilege authorisation, delegated scopes, policy enforcement at tools and data, session handling, monitoring, and an emergency disable path.

## How it is used

Give a procurement agent a distinct workload identity and narrowly scoped grants to read approved supplier data, draft a purchase request, and submit it only after a human approval. Record the initiating user, the agent identity, the approval, each tool call, and the resulting transaction as separate facts.

Microsoft Entra Agent ID illustrates the pattern by representing an agent identity as a specialised service principal and supporting tenant-wide authentication controls. The IETF’s draft guidance on AI-agent authentication and authorisation highlights the emerging cross-platform concern, but it is not yet a final standard.

## Evidence

[Microsoft Entra’s agent-identity overview](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities) and [administration guidance](https://learn.microsoft.com/en-us/entra/agent-id/manage-agent-identities-admin) provide concrete product evidence. The [IETF AI-agent authentication and authorisation draft](https://www.ietf.org/archive/id/draft-klrc-aiagent-auth-02.html) and [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) provide broader security context.
