---
slug: delegation-recovery
title: Delegation Recovery
short_description: The steps for giving an agent back the right level of access, or
  safely replacing its access, after something goes wrong.
category: Governance
tags:
- governance
- security
- access-control
- agentic-ai
status: draft
aliases:
- delegation recovery
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a standard, clearly defined security term when it is still a loose
  label in agentic AI.
- Mixing it up with ordinary permission revocation or account recovery.
- Assuming recovery means restoring full access instead of restoring only the minimum
  safe access.
related_terms:
- delegation
- revocation
- access control
- audit log
- escalation
- least privilege
evidence:
- source_title: OWASP Top 10 for LLM Applications
  source_url: https://genai.owasp.org/llm-top-10/
  source_type: official_docs
  relevance: Shows that delegated actions, permissions, and oversight are part of
    real LLM risk management.
  key_point: LLM systems need controls around authority, scope, and misuse; the label
    "delegation recovery" is not itself a standard OWASP term.
- source_title: Review permissions granted to enterprise applications
  source_url: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/manage-application-permissions
  source_type: official_docs
  relevance: Shows how delegated access can be reviewed, revoked, and restored in
    a real system.
  key_point: Permissions granted to an application can be reviewed, revoked, and in
    some cases restored.
- source_title: View Activity logs of application permissions
  source_url: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/app-perms-audit-logs
  source_type: official_docs
  relevance: Shows the need for audit records when delegated access is granted or
    removed.
  key_point: Systems should keep audit logs for granting and revoking delegated permissions.
- source_title: Grant or revoke API permissions programmatically
  source_url: https://learn.microsoft.com/en-us/graph/permissions-grant-via-msgraph
  source_type: official_docs
  relevance: Shows that delegated permission grants can be managed and revoked in
    a controlled way.
  key_point: Delegated permissions let an app act on behalf of a user and can be granted
    or revoked.
- source_title: NFSv4 delegation recovery
  source_url: https://tools.wordtothewise.com/rfc5661
  source_type: standards_doc
  relevance: Provides an established technical use of the phrase "delegation recovery"
    outside AI.
  key_point: Delegation recovery is used for restoring delegated state after client
    restart, server restart, or network failure.
---

Delegation Recovery is the process of safely restoring, replacing, or taking back an agent’s [[Delegated Authority|delegated access]] after something changes or goes wrong.

In practice, it means checking what the agent was al[[Context Collapse|l]]owed to do, deciding whether that access is still safe, and then giving back o[[Context Collapse|n]]ly the right permissions. If the agent lost context, was restarted, or acted in a risky way, recovery may mean revoking its access, reducing its scope, or handing the task to a human or another system.

This matters because agents can keep acting after the original person has stopped watching. If the wrong access is left in place, the agent may do something it should not do. Good delegation recovery helps prevent mistakes, limits damage, and makes it possible to trace who was responsible for what.

It is not a single button or a standard security control with one fixed meaning. It is also not the same as “account recovery” for a person. In agent systems, it is about recovering the safe state of [[Delegated Authority|delegated authority]], not just resetting a login.
