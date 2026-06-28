---
title: Policy Interceptor
short_description: A Policy Interceptor is a place in a system where a requested action
  is checked against policy before it is allowed to continue.
category: Governance
tags:
- governance
- security
- authorization
- policy-enforcement
- agent-controls
status: draft
aliases:
- policy gate
- policy enforcement point
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
- Treating the label as if it names a standard architecture pattern rather than a
  custom name for an authorisation check.
- Leaving the policy decision vague so no one knows who can approve, deny, or reverse
  the action.
- Putting the check in the wrong place, after the risky action has already started.
related_terms:
- policy enforcement point
- policy decision point
- authorisation
- least privilege
- human approval
- tool authorization
evidence:
- source_title: NIST Glossary - Policy Enforcement Point
  source_url: https://csrc.nist.gov/glossary/term/policy_enforcement_point
  source_type: standards_doc
  relevance: Defines the standard security concept this term is based on.
  key_point: A policy enforcement point is the place that enforces an authorisation
    decision.
- source_title: OpenID Foundation - Authorization API 1.0
  source_url: https://openid.net/specs/authorization-api-1_0.html
  source_type: standards_doc
  relevance: Shows the standard split between policy decision points and policy enforcement
    points.
  key_point: The API lets decision points and enforcement points exchange requests
    and decisions.
- source_title: OWASP Top 10 for LLM Applications 2025
  source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
  source_type: standards_doc
  relevance: Grounds the idea in current agent safety guidance.
  key_point: High-risk actions should be constrained with human approval and strong
    controls.
- source_title: OWASP Top 10 for LLM Applications
  source_url: https://genai.owasp.org/llm-top-10/
  source_type: industry_article
  relevance: Background reference for agent safety and excessive autonomy risks.
  key_point: LLM systems need controls that limit unsafe or over-privileged actions.
---

A Policy Interceptor is the place in a system where a requested action is checked before it is allowed to happen.

In practice, it sits between the request and the action. It asks, “Is this allowed?” and then either lets the action continue, blocks it, or sends it to a human for approval.

This matters because agents and automated tools can act quickly. If the check happens at the wrong point, a system may do something unsafe before anyone can stop it.

It is not a magic safety feature just because it has a name. It is only useful if the system clearly says who makes the decision, what rule is used, where the check happens, and how the decision can be changed or audited later.

It is also not the same as the action itself. The interceptor does not do the work. It only decides whether the work should go ahead.
