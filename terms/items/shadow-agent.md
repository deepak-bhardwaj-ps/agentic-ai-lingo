---
title: Shadow Agent
short_description: An agent that runs without the normal visibility, approval, or
  oversight from the team that owns it.
category: AgentOps
tags:
- agentops
- governance
- visibility
status: draft
aliases:
- shadow AI agent
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it like a formal industry standard term.
- Confusing it with a shadow deployment, where a system is tested without affecting
  users.
related_terms:
- shadow AI
- shadow deployment
- governance
- observability
evidence:
- source_title: Building Governed AI Agents - A Practical Guide to Agentic Scaffolding
  source_url: https://developers.openai.com/cookbook/examples/partners/agentic_governance_guide/agentic_governance_cookbook
  source_type: engineering_blog
  relevance: Shows that AI agents need governance, visibility, and discovery to avoid
    unsanctioned use.
  key_point: OpenAI recommends centralised governance and early visibility to prevent
    shadow AI from spreading.
- source_title: Deployment - AWS Prescriptive Guidance
  source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ml-operations-planning/deployment.html
  source_type: official_docs
  relevance: Defines shadow deployment, which is a related but different idea.
  key_point: A shadow model can run alongside production without influencing decisions.
- source_title: Governance scope - AWS Prescriptive Guidance
  source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/what-needs-to-be-governed.html
  source_type: official_docs
  relevance: Supports the need for visibility, registries, access management, and
    audit for agentic systems.
  key_point: Agentic AI should be governed through central registries, access control,
    and audit requirements.
---

A shadow agent is an agent that is running without the normal visibility, approval, or oversight from the team that owns it.

In practice, this means the agent may be doing useful work, but nobody has properly recorded it, reviewed it, or checked whether it is allowed to do what it is doing.

The term matters because hidden automation can create security, safety, and compliance problems. If a team does not know an agent exists, it cannot judge the data it can reach, the tools it can use, or the decisions it affects.

It is not a formal technical standard. It is also not the same as a shadow deployment, where a system is tested alongside a live one without changing the user-facing result.
