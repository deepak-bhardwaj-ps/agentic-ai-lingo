---
slug: delegation-failure
title: Delegation Failure
short_description: A delegation failure happens when an agent is given authority it
  should not have, cannot prove who allowed it to act, or keeps acting outside its
  limits.
category: Governance
tags:
- agentic-ai
- governance
- security
- delegation
status: draft
aliases:
- delegated authority failure
- broken delegation chain
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a single fixed security control instead of a governance problem.
- Using it for any agent mistake, even when authority and limits were clear.
- Confusing it with prompt injection, which is a different cause of failure.
related_terms:
- least privilege
- human-in-the-loop
- agent governance
- authorization
- audit trail
evidence:
- source_title: OWASP Top 10 for Agentic Applications 2026
  source_url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
  source_type: standards_doc
  relevance: OWASP frames agentic AI risk around how systems plan, act, and delegate
    across tools and workflows.
  key_point: Agentic systems need clear controls around authority, identity, and safe
    action boundaries.
- source_title: A practical guide to building agents
  source_url: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
  source_type: official_docs
  relevance: OpenAI explains that agent actions should stay within clearly defined
    guardrails and approval steps.
  key_point: Important actions should not be left to unconstrained agent behaviour.
- source_title: Authenticated Delegation and Authorized AI Agents
  source_url: https://arxiv.org/html/2501.09674v1
  source_type: research_paper
  relevance: This paper discusses secure, auditable delegation of authority to AI
    agents.
  key_point: Delegation should be authenticated, authorised, scoped, and auditable.
---

Delegation failure is when an agent is given power to act, but that power is unclear, too broad, not checked properly, or not easy to trace back to the person or system that allowed it.

In practice, this means the agent may do something it should not do, such as access the wrong data, use the wrong tool, or keep acting after its permission should have ended. The problem is not just the action itself. It is the broken chain of authority behind the action.

This matters because [[Agentic AI|agentic systems]] can take real-world actions. If the limits are vague, the audit trail is missing, or revocation does not work, the system becomes hard to trust and hard to control.

It is not the same as a bad answer from a chatbot. It is also not the same as prompt injection, although prompt injection can cause a delegation failure if it tricks an agent into using its authority badly.
