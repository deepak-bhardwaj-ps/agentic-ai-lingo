---
slug: evidence-based-execution
title: Evidence-Based Execution
short_description: A rule that an agent may act only when the required proof, permission,
  or record has been checked.
category: Governance
tags:
- governance
- security
- agentic-ai
- access-control
- audit
status: draft
aliases:
- evidence based execution
- evidence-backed execution
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a standard industry term when it is mostly a coined governance phrase.
- Confusing it with simple logging, when it also includes permission checks and clear
  stopping rules.
- Assuming the agent can decide on evidence by itself instead of using an external
  control.
related_terms:
- least privilege
- policy enforcement
- audit trail
- revocation
- human escalation
- zero trust
evidence:
- source_title: OWASP Top 10 for Large Language Model Applications
  source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
  source_type: official_docs
  relevance: Shows the security context in which agents must be controlled, not trusted
    to act freely.
  key_point: LLM systems need security controls for risky behaviour, including how
    actions are authorised and constrained.
- source_title: Open Policy Agent Documentation
  source_url: https://openpolicyagent.org/docs
  source_type: official_docs
  relevance: Supports the idea of checking policy before action.
  key_point: Policy can be evaluated separately from application code and used to
    enforce decisions across systems.
- source_title: Security best practices in IAM
  source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
  source_type: official_docs
  relevance: Supports the least-privilege part of the concept.
  key_point: Access should be limited to only the permissions needed for the task.
- source_title: Access control
  source_url: https://www.cyber.gc.ca/en/guidance/cyber-security-privacy-risk-management/itsp10033/access-control
  source_type: official_docs
  relevance: Supports revocation and changing permissions when conditions change.
  key_point: Access authorisations should be revoked when the security attributes
    of people or objects change.
- source_title: AI Agent Security Cheat Sheet
  source_url: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
  source_type: official_docs
  relevance: Shows why agent actions need tool controls and permission boundaries.
  key_point: Agents can abuse tools or gain too much privilege unless strong controls
    are enforced.
---

Evidence-Based Execution means an agent only carries out an action after the needed proof, permission, or record has been checked.

In practice, this means the agent should not just “feel confident” and act. A separate control should decide whether the action is allowed. That control might check a policy, a user approval, a task record, a risk rule, or an audit requirement.

This matters because agents can make fast decisions, but fast is not the same as safe. If an action is risky, expensive, or hard to undo, the system needs clear evidence before it proceeds.

It is not just a logging rule. It is not the same as “the agent said it was okay.” It is also not a single universal standard term. In many systems, it is better understood as a governance idea built from existing security ideas like least privilege, policy enforcement, audit trails, and revocation.
