---
slug: permission-gates
title: Permission Gates
name: Permission Gates
category: Governance
short_description: A permission gate is a check that decides whether an action is
  allowed before an agent or system can do it.
aliases:
- permission gate
- approval gate
status: active
tags:
- governance
- security
- access-control
- permissions
- agentic-ai
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating a label or prompt as if it were a real security control
- Letting the model decide on its own when to ignore the gate
- Failing to record who approved the action and what exactly was allowed
related_terms:
- authorization
- access control
- role-based access control
- human approval
- guardrails
evidence:
- source_title: LLM06:2025 Excessive Agency
  source_url: https://genai.owasp.org/llmrisk/llm06-sensitive-information-disclosure/
  source_type: official_docs
  relevance: Shows that excessive permissions and excessive autonomy are core risks
    when AI systems can act on the world.
  key_point: OWASP says excessive agency is caused by excessive functionality, permissions,
    or autonomy, so high-impact actions need hard limits and controls.
- source_title: Manage permissions in the OpenAI platform
  source_url: https://developers.openai.com/api/docs/guides/rbac
  source_type: official_docs
  relevance: Gives a current example of permissions being set with roles, scopes,
    and enforceable controls.
  key_point: OpenAI’s RBAC guidance shows permissions should be assigned deliberately
    and enforced consistently across systems.
- source_title: NIST Risk Management Framework
  source_url: https://csrc.nist.gov/projects/risk-management
  source_type: standards_doc
  relevance: Shows that authorisation is a formal decision made after controls are
    assessed, not a casual label.
  key_point: NIST describes authorisation as a risk-based decision to allow a system
    to operate, which matches the idea of a gate before action.
---

A permission gate is a check that decides whether a requested action is allowed before it happens.

In practice, it sits between the request and the action. If the action is safe and the right person or system has approval, the gate opens. If not, the action stops.

This matters because agents can do real things, like send messages, change records, move files, or call tools. Without a gate, a mistake or a bad instruction can cause damage quickly.

A permission gate is not the same as a warning, a polite instruction, or a line in a prompt. It only counts if there is a real enforcement point, a clear policy, and a record of who approved what.

It is also not enough for the model to “promise” to behave. The check has to happen outside the model so the action is blocked when permission is missing.
