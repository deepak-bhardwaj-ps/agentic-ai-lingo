---
title: Identity-Resolved Data
short_description: Data that has been matched to a real person, service, or role instead
  of staying anonymous or mixed up with other records.
category: Context
tags:
- agentic-ai
- identity
- security
- governance
status: draft
aliases:
- identity resolved data
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it as a formal security control instead of a description of how data is
  linked to an identity.
- Assuming one identity match is always correct, even when records can be wrong or
  incomplete.
- Using the phrase to mean any personalised data, when it really means data tied to
  a specific identity or delegation path.
related_terms:
- identity resolution
- principal
- delegation
- access control
- audit trail
- OAuth 2.0 token exchange
evidence:
- source_title: OWASP Top 10 for Large Language Model Applications
  source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
  source_type: official_docs
  relevance: Shows the security context for agentic systems and why identity, access,
    and agency boundaries matter.
  key_point: OWASP treats excessive agency and access control as core risks in LLM
    and agentic systems.
- source_title: OAuth 2.0 Token Exchange
  source_url: https://datatracker.ietf.org/doc/html/rfc8693
  source_type: standards_doc
  relevance: Defines a standard way to pass or exchange tokens when one service acts
    on behalf of another identity.
  key_point: The specification supports impersonation and delegation, which is the
    technical pattern behind identity-aware access.
- source_title: Microsoft identity platform and OAuth2.0 On-Behalf-Of flow
  source_url: https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow
  source_type: official_docs
  relevance: Gives a clear practical example of a service using one identity to call
    another service on behalf of a user.
  key_point: The flow passes a user's identity and permissions through a request chain
    using delegated scopes.
---

## Meaning

Identity-resolved data is data that has been matched to a specific person, service, or role, so the system knows whose identity it belongs to.

In practice, this means the data is not just a pile of records. It has been linked to a known identity, such as a user account, a service account, or a user who allowed one system to act for them.

This matters because systems often need to know who is allowed to see, change, or act on the data. If the identity is wrong, the system can show the wrong information, make the wrong decision, or give access to the wrong person.

It is not the same as a security control by itself. It is also not the same as perfect identity matching. The data may still be incomplete, merged incorrectly, or tied to the wrong person if the matching process is poor.

The term is most useful when talking about access, delegation, and audit trails in [[Agentic AI|agentic systems]], where one component may act for another but still needs the original identity to stay clear.
