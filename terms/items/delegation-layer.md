---
title: Delegation Layer
short_description: A delegation layer is the part of a system that defines who can
  act for whom, what they may do, and how that permission is checked.
category: Governance
tags:
- governance
- security
- agentic-ai
- delegation
status: active
aliases:
- delegated authority layer
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating any named permission step as a real delegation layer
- Confusing delegation with full ownership or trust
- Leaving out expiry, limits, revocation, or audit records
related_terms:
- authorization
- delegated access
- least privilege
- audit log
- agent permissions
evidence:
- source_title: The OAuth 2.0 Authorization Framework
  source_url: https://datatracker.ietf.org/doc/html/rfc6749
  source_type: standards_doc
  relevance: Defines delegated access in widely used internet security standards.
  key_point: OAuth 2.0 lets a third-party application obtain limited access on behalf
    of a resource owner.
- source_title: Govern
  source_url: https://airc.nist.gov/airmf-resources/playbook/govern/
  source_type: official_docs
  relevance: Shows that AI governance needs clear policies, roles, and accountability.
  key_point: NIST says AI risk governance should have documented policies, processes,
    and responsibilities across the organisation.
- source_title: LLM06:2025 Excessive Agency
  source_url: https://genai.owasp.org/llmrisk/llm06-sensitive-information-disclosure/
  source_type: industry_article
  relevance: Explains the risk of systems being allowed to take damaging actions with
    too much authority.
  key_point: OWASP warns that granting an LLM-based system too much agency can lead
    to harmful actions.
---

A delegation layer is the part of a system that says who is allowed to act for someone else, what they are allowed to do, and how that permission is checked.

In practice, it records the person or service giving the permission, the tasks allowed, how long the permission lasts, and how it can be removed. It should also leave a record so people can see what happened later.

This matters because [[Agentic AI|agentic systems]] can make real changes, send messages, or access data. If delegation is unclear, the system may do too much, do the wrong thing, or keep acting after permission should have ended.

It is not just a label for any control step. A real delegation layer needs clear limits, a way to enforce those limits, a way to revoke access, a[[Context Collapse|n]]d a trace of what was allowed.
