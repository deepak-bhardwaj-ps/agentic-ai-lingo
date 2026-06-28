---
slug: delegation-policy
title: Delegation Policy
short_description: Rules that define what an agent is allowed to do on someone else’s
  behalf.
category: Governance
tags:
- governance
- security
- agents
- authority
status: active
aliases:
- delegated authority policy
- agent delegation policy
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating a name as a real control without defining who can act, on what, for how
  long, and with what review.
- Confusing delegation with full ownership or unlimited access.
related_terms:
- authorization
- accountability
- access control
- human oversight
evidence:
- source_title: OWASP Top 10 for LLM Applications
  source_url: https://genai.owasp.org/llm-top-10/
  source_type: industry_article
  relevance: Shows why agent authority, oversight, and control boundaries matter in
    LLM and agent systems.
  key_point: The OWASP guidance highlights the need to control what an AI system can
    do and to keep human oversight for risky actions.
- source_title: Overview of Microsoft Graph permissions
  source_url: https://learn.microsoft.com/en-us/graph/permissions-overview
  source_type: official_docs
  relevance: Gives a clear example of delegated access in real software systems.
  key_point: Delegated permissions let an app act on behalf of a signed-in user, but
    only within that user’s allowed access.
- source_title: NIST AI RMF Playbook - Govern
  source_url: https://airc.nist.gov/airmf-resources/playbook/govern/
  source_type: official_docs
  relevance: Supports the need to define responsibilities and governance for AI systems.
  key_point: AI governance should define roles, responsibilities, and oversight so
    authority is clear and accountable.
---

Delegation Policy is a set of rules that says what an agent is allowed to do for someone else.

In practice, it answers simple questions: who gave the permission, what actions are allowed, where the permission applies, how long it lasts, and when a human must step in.

This matters because an agent can do the wrong thing very quickly if its power is unclear. A good delegation policy limits the damage, makes responsibility clear, and gives people a way to check or stop the agent.

It is not the same as giving an agent free access. It is also not just a fancy name for a safety rule. A real delegation policy needs clear limits, a record of the decision, and a way to take the permission back.
