---
slug: decision-plane
title: Decision Plane
short_description: A decision plane is the part of a system where permission, approval,
  logging, and escalation rules are decided and recorded.
category: Governance
tags:
- governance
- security
- agentic-ai
- architecture
status: draft
aliases:
- decision layer
- governance plane
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a standard technical component when it is often just a design label
  for where decisions are made and recorded.
- Confusing it with the execution layer that actually carries out actions.
related_terms:
- control plane
- policy engine
- audit log
- human approval
- least privilege
evidence:
- source_title: OWASP Top 10 for LLM Applications
  source_url: https://genai.owasp.org/llm-top-10/
  source_type: standards_doc
  relevance: OWASP highlights excessive agency and the need to limit what an AI system
    is allowed to do, which matches the governance idea behind a decision plane.
  key_point: Agentic systems need clear limits on what they can do and how much authority
    they have.
- source_title: Secure autonomous agentic AI systems
  source_url: https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems
  source_type: official_docs
  relevance: Microsoft describes agents operating within defined intent, permissions,
    and boundaries, with high-risk actions requiring human approval and behaviour
    remaining auditable.
  key_point: Good agent security depends on defined boundaries, approval, and auditability.
- source_title: IAP for agents overview
  source_url: https://docs.cloud.google.com/iap/docs/agent-overview
  source_type: official_docs
  relevance: Google describes agent access being governed by IAM allow and deny policies
    enforced at runtime, which is the practical pattern a decision plane usually refers
    to.
  key_point: Access decisions can be enforced centrally with allow and deny policies
    at the point of use.
---

A decision plane is the part of a system where important decisions about an AI agent are made and recorded.

In practice, this is where the system decides what the agent is allowed to do, when a human must approve something, what gets logged, and when the agent must stop or ask for help.

It matters because [[Agentic AI|agentic systems]] can act on their own. If the ru[[Context Collapse|l]]es are vague, the agent can do the wrong thing too easily. A clear decisio[[Context Collapse|n]] plane helps keep the agent within safe limits.

It is not the same as the part that does the work. The decision plane decides. The execution layer carries out the action. It is also not a fixed industry standard term, so people may use it differently.
