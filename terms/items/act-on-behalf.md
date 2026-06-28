---
title: Act-on-Behalf
short_description: Acting on behalf means an agent is allowed to do one specific task
  for someone else, with clear limits.
category: Governance
tags:
- governance
- security
- delegation
- agents
status: draft
aliases:
- on-behalf-of
- delegated action
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
- Treating delegation as a full handover of control
- Forgetting to limit what the agent can do
- Assuming the agent is responsible instead of the person who granted the access
related_terms:
- delegated authority
- authorization
- token exchange
- on-behalf-of flow
evidence:
- source_title: OWASP Top 10 for Large Language Model Applications
  source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
  source_type: official_docs
  relevance: Shows that letting an AI system act with too much freedom is a real safety
    risk.
  key_point: Excessive agency is dangerous when permissions are too broad or limits
    are too weak.
- source_title: RFC 6749 - The OAuth 2.0 Authorization Framework
  source_url: https://datatracker.ietf.org/doc/html/rfc6749
  source_type: standards_doc
  relevance: Gives the basic web model for limited access granted to a third party.
  key_point: OAuth lets a third-party app get limited access to a user’s resources
    instead of full control.
- source_title: RFC 8693 - OAuth 2.0 Token Exchange
  source_url: https://datatracker.ietf.org/doc/rfc8693/
  source_type: standards_doc
  relevance: Defines a standard way to exchange tokens when one party is acting for
    another.
  key_point: Token exchange supports delegation and keeps track of both the subject
    and the actor.
- source_title: Microsoft identity platform and OAuth 2.0 On-Behalf-Of flow
  source_url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow
  source_type: official_docs
  relevance: Shows a real-world version of on-behalf-of access in a service-to-service
    call.
  key_point: A middle service can use a user’s token to get a new token for a downstream
    service, but only with the right scope.
- source_title: Authenticated Delegation and Authorized AI Agents
  source_url: https://arxiv.org/abs/2501.09674
  source_type: research_paper
  relevance: Explains what safe delegated authority for AI agents should look like.
  key_point: Human users should be able to delegate to agents while keeping scope,
    accountability, and audit trails clear.
---

Act-on-behalf means an agent is allowed to do one specific task for another person or system.

In practice, the agent should only get the access it needs for that one job. The permission should be narrow, time-limited, and easy to check later.

This matters because it stops an agent from using an account, tool, or document as if it owned them. It also makes it easier to see what was allowed, what was done, and who is responsible if something goes wrong.

It is not the same as handing over an account. It is not a blank cheque. It is not a way to hide responsibility. If the limits are not clear, then the agent is not safely acting on behalf of anyone.
