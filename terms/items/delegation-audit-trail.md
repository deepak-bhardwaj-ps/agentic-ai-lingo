---
slug: delegation-audit-trail
title: Delegation Audit Trail
short_description: A record showing who gave an agent permission to act, what it was
  allowed to do, and when that permission changed.
category: Governance
tags:
- governance
- security
- audit
- delegation
status: active
aliases:
- Delegated Access Audit Trail
- Delegation Log
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating any log as a full delegation audit trail
- Confusing permission logs with proof that the permission was valid
- Leaving out who approved the delegation, what scope was allowed, and when it expired
related_terms:
- audit trail
- audit log
- delegation
- service account
- non-repudiation
evidence:
- source_title: audit trail - NIST CSRC Glossary
  source_url: https://csrc.nist.gov/glossary/term/audit_trail
  source_type: standards_doc
  relevance: Core definition of an audit trail as a record of who accessed a system
    and what they did.
  key_point: An audit trail is a record showing who accessed an IT system and what
    operations they performed.
- source_title: Cloud Audit Logs overview - Google Cloud Documentation
  source_url: https://docs.cloud.google.com/logging/docs/audit
  source_type: official_docs
  relevance: Shows how audit logs answer who did what, where, and when in practice.
  key_point: Audit logs record administrative activities and access, helping trace
    actions over time.
- source_title: Example logs for service accounts - Google Cloud Documentation
  source_url: https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts
  source_type: official_docs
  relevance: Demonstrates that delegation and service-account use can be logged for
    tracing actions back to an actor.
  key_point: Service account audit logs can show management and use of delegated identities.
- source_title: OWASP Top 10 for LLM Applications
  source_url: https://genai.owasp.org/llm-top-10/
  source_type: standards_doc
  relevance: Background for agentic systems where tool use and delegated actions create
    security and accountability risks.
  key_point: Agent systems need controls that reduce loss of traceability and accountability.
---

An audit trail for delegation is a record of who gave an agent permission to act, what the agent was allowed to do, and when that permission changed or ended.

In practice, it should show the person or system that granted the permission, the exact scope of the permission, any limits or expiry date, and the actions taken under that permission.

This matters because it helps people work out who was responsible if an agent makes a mistake, does something unexpected, or gets abused.

It is not just any log file. A useful delegation audit trail must connect the original approver, the delegated power, and the later actions that used it. If it does not show those links, it does not really prove much.
