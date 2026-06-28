---
title: Delegation Scope
short_description: Delegation scope is the exact boundary of what an agent or system
  is allowed to do on behalf of someone else.
category: Governance
tags:
- governance
- security
- access-control
- delegation
status: active
aliases:
- scoped delegation
- delegation boundary
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating delegation as safe without clear limits, expiry, logging, or a way to revoke
  it.
- Confusing scope with permission in general, instead of the exact boundary of what
  is allowed.
related_terms:
- delegated authority
- least privilege
- revocation
- audit trail
- human oversight
evidence:
- source_title: OWASP Top 10 for LLM Applications
  source_url: https://genai.owasp.org/llm-top-10/
  source_type: standards_doc
  relevance: Gives the current security context for agent actions and excessive authority.
  key_point: LLM and agent systems need limits on what they can do, because too much
    agency creates security risk.
- source_title: OWASP Top 10 for LLM and GenAI
  source_url: https://genai.owasp.org/initiative/owasp-top-10-for-llm-and-genai/
  source_type: standards_doc
  relevance: Shows that agentic AI is now being discussed through governance and risk
    controls.
  key_point: The OWASP project treats agentic AI as an area where action limits and
    oversight matter.
- source_title: AI RMF Playbook - Govern
  source_url: https://airc.nist.gov/airmf-resources/playbook/govern/
  source_type: official_docs
  relevance: Supports the idea that AI authority and oversight should be defined and
    documented.
  key_point: Good AI governance includes defining scope, intended use, and connected
    risk controls.
- source_title: Claude Code Security
  source_url: https://docs.anthropic.com/en/docs/claude-code/security
  source_type: official_docs
  relevance: Example of a real agent tool using permission and scope controls.
  key_point: Agent tools can be restricted by configured permissions rather than given
    open-ended access.
- source_title: Delegation in access control systems
  source_url: https://csrc.nist.gov/files/pubs/conference/2000/10/19/proceedings-of-the-23rd-nissc-2000/final/docs/papers/021.pdf
  source_type: research_paper
  relevance: Academic grounding for delegation as a bounded security concept.
  key_point: Delegation is about passing specific authority to another active entity,
    not handing over everything.
---

Delegation scope is the exact boundary of what an agent or system is allowed to do on behalf of someone else.

In practice, it says three things: what actions are allowed, what data can be used or changed, and how long the permission lasts. A good delegation scope also shows who gave the permission, who can use it, and how it can be taken back.

This matters because an agent should not get more power than it needs. Tight scope reduces mistakes, limits damage if something goes wrong, and makes checking the agent’s actions much easier.

It is not the same as full trust. It is not a control just because a tool says it has one. If the scope is unclear, too broad, never expires, or cannot be audited, it is not a proper delegation boundary.
