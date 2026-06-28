---
slug: delegation-contract
title: Delegation Contract
short_description: A delegation contract is a clear record of what authority an agent
  has, who gave it, and where the limits are.
category: Governance
tags:
- governance
- agentic-ai
- authorization
- oversight
status: draft
aliases:
- delegated authority contract
- delegation scope
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treated as if it is a formal standard term when it is mostly a useful label for
  a governance idea.
- Used to mean any policy, even when no specific authority, limit, or revocation is
  defined.
related_terms:
- delegation of authority
- authorization
- human oversight
- audit trail
- revocation
evidence:
- source_title: OWASP GenAI Security Project - LLM06 Excessive Agency
  source_url: https://genai.owasp.org/llmrisk/llm06-sensitive-information-disclosure/
  source_type: standards_doc
  relevance: High
  key_point: Excessive agency is about an AI being able to perform harmful actions
    beyond what was intended or allowed, which is why authority limits matter.
- source_title: NIST AI RMF Playbook - Manage
  source_url: https://airc.nist.gov/airmf-resources/playbook/manage/
  source_type: official_docs
  relevance: High
  key_point: NIST asks organisations to define roles, responsibilities, and delegation
    of authorities for people involved in AI systems.
- source_title: NIST AI RMF Playbook - Measure
  source_url: https://airc.nist.gov/airmf-resources/playbook/measure/
  source_type: official_docs
  relevance: Medium
  key_point: NIST recommends documenting human oversight, including the degree of
    oversight and downstream actions.
- source_title: OpenAI - Practices for Governing Agentic AI Systems
  source_url: https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf
  source_type: research_paper
  relevance: Medium
  key_point: Agentic systems need clear baseline responsibilities and safety practices
    across the people and services involved.
---

A delegation contract is a clear record of what an agent is allowed to do, who gave it that power, and where the limits are.

In practice, it says things like: this agent may book travel, but only up to a set budget; it may send draft emails, but not send final approvals; and if the person who granted the power changes their mind, the permission can be removed.

This matters because agents can act quickly and at scale. If the rules are vague, an agent can do something that was never meant to be allowed. A good delegation contract makes responsibility clearer, helps with audit trails, and makes it easier to stop or review actions later.

It is not just a policy document with a fancy name. It is also not a formal universal standard term. In many cases, it is a useful way to describe the idea of [[Delegated Authority|delegated authority]], with clear limits, checks, and revocation.
