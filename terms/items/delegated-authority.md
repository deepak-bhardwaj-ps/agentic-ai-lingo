---
title: Delegated Authority
short_description: Delegated authority is permission given by one person or system
  to another to act within a set limit.
category: Governance
tags:
- governance
- security
- access-control
status: active
aliases:
- delegated access
- delegated administration
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating any hand-off as safe without limits, expiry, logging, or a clear owner.
related_terms:
- authority
- delegation
- access control
- least privilege
- revocation
evidence:
- source_title: OWASP Top 10 for LLM Applications - Excessive Agency
  source_url: https://genai.owasp.org/llm-risk/llm06-excessive-agency/
  source_type: standards_doc
  relevance: Shows why uncontrolled agent action is a security risk.
  key_point: Systems that can act on behalf of a user need tight limits, because too
    much agency can cause harmful actions.
- source_title: Microsoft identity platform - delegated access scenario
  source_url: https://learn.microsoft.com/en-us/entra/identity-platform/delegated-access-primer
  source_type: official_docs
  relevance: Clear example of acting on behalf of a signed-in user.
  key_point: Delegated access means an app works with a user's resources only within
    the user's and app's authorised permissions.
- source_title: AWS Organizations - delegated administrator
  source_url: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_delegated_admin.html
  source_type: official_docs
  relevance: Shows delegated authority in account and service administration.
  key_point: A delegated administrator gets limited management power for a specific
    service, not full control of everything.
- source_title: A Role-Based Delegation Model and Some Extensions
  source_url: https://csrc.nist.gov/files/pubs/conference/2000/10/19/proceedings-of-the-23rd-nissc-2000/final/docs/papers/021.pdf
  source_type: research_paper
  relevance: Academic grounding for delegation as a security and access-control idea.
  key_point: Delegation is an established control concept where one active entity
    gives another authority to carry out some functions.
---

Delegated authority means one person or system is allowed to act for another, but only within clear limits.

In practice, it should answer four questions: who is allowed to act, what they can do, how long they can do it for, and how the permission can be taken back.

This matters because it lets work get done without giving away full control. For example, a manager might allow a team member to approve a small expense, or a program might be allowed to perform one job for a user.

It is not the same as total trust. It is also not safe just because it has a fancy name. If the limits are vague, the permission lasts too long, or no one can check the actions later, the delegation is weak and risky.
