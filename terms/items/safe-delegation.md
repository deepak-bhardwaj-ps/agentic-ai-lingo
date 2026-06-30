---
title: Safe delegation
short_description: Delegating a task to an AI agent with clear limits, checks, and a way to stop or review what it does.
category: Agentic patterns
tags:
- agentic-ai
- delegation
- governance
- security
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating delegation as safe just because an agent can do the task.
- Leaving out scope, time limits, approval steps, or logs.
- Confusing safe delegation with full autonomy or full trust.
related_terms:
- delegation boundary
- delegation scope
- delegated authority
- human oversight
- revocation
evidence:
- source_title: Grant agents access to Microsoft 365 resources
  source_url: https://learn.microsoft.com/en-us/entra/agent-id/grant-agent-access-microsoft-365
  source_type: official_docs
  relevance: Shows a current product pattern for letting agents act on behalf of users without overextending their access.
  key_point: Microsoft recommends delegated permissions for agents that act on behalf of a signed-in user, and says to use the smallest set of permissions needed.
- source_title: Overview of permissions and consent in the Microsoft identity platform
  source_url: https://learn.microsoft.com/en-us/entra/identity-platform/permissions-consent-overview
  source_type: official_docs
  relevance: Explains the difference between delegated access and app-only access, which is the core safety choice behind safe delegation.
  key_point: Delegated permissions let an application act on a user's behalf, but only within what that user can already access.
- source_title: Practices for Governing Agentic AI Systems
  source_url: https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf
  source_type: research_paper
  relevance: Gives a current governance framing for agentic systems that act for people and need clear responsibility.
  key_point: Agentic systems need explicit controls, oversight, and accountability so actions taken on behalf of users stay bounded.
- source_title: Authenticated Delegation and Authorized AI Agents
  source_url: https://arxiv.org/html/2501.09674v1
  source_type: research_paper
  relevance: Directly addresses delegated authority for AI agents and why permission scope must be restricted and auditable.
  key_point: The paper proposes authenticated, authorised, and auditable delegation so users can securely restrict what agents may do.
---

Safe delegation means letting an AI agent act for someone else only when the task is clearly limited, checked, and easy to stop or review.

In practice, that means the agent should know exactly what it may do, what it may not do, how long the permission lasts, and when a human must approve the next step.

This matters because an agent can send messages, change files, make bookings, or trigger other systems. If delegation is not safe, the agent may do too much, use the wrong data, or keep acting after it should have stopped.

Safe delegation is not the same as full autonomy. It is also not safe just because the task sounds harmless. A task is only safely delegated when the limits, review steps, and revocation path are clear.

The term is useful, but it is not a single formal standard. People use it to describe the safety of giving an agent limited authority, not a promise that the agent cannot fail.
