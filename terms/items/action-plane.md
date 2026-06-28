---
slug: action-plane
name: Action Plane
category: Governance
title: Action Plane
aliases: null
short_description: A design label for the part of an agent system that checks, allows,
  blocks, changes, or logs an action before it reaches the real world.
status: active
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a standard industry term when it is mostly a design label
- Using it to mean the whole agent system instead of the part that controls execution
- Confusing it with the control plane, which sets rules, rather than the place where
  actions are enforced
related_terms:
- control plane
- policy engine
- approval flow
- sandbox
- audit log
- human-in-the-loop
evidence:
- source_title: Sandbox – Codex
  source_url: https://developers.openai.com/codex/concepts/sandboxing
  source_type: official_docs
  relevance: Shows that technical limits and approval rules are separate, which matches
    the idea of an action-enforcement layer.
  key_point: OpenAI says the sandbox defines what Codex can do technically, while
    the approval policy decides when it must stop and ask.
- source_title: Agent approvals & security
  source_url: https://developers.openai.com/codex/agent-approvals-security
  source_type: official_docs
  relevance: Confirms the split between sandbox limits and approval policy in a real
    agent system.
  key_point: OpenAI describes the sandbox as the technical boundary and the approval
    policy as the rule for when the agent must stop and ask before acting.
- source_title: Tool use with Claude
  source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
  source_type: official_docs
  relevance: Shows that the model proposes an action but the application or server
    actually carries it out.
  key_point: Claude returns a structured tool call, and the application executes client
    tools or Anthropic executes server tools.
- source_title: How tool use works
  source_url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
  source_type: official_docs
  relevance: Explains that the model only requests an operation and the application
    or platform performs it.
  key_point: Anthropic says tool use is a contract where the model emits a request
    and the application runs the operation.
- source_title: APTS Manipulation Resistance
  source_url: https://owasp.org/APTS/standard/6_Manipulation_Resistance/
  source_type: standards_doc
  relevance: Supports the idea that safety controls and audit records should sit outside
    the agent runtime.
  key_point: OWASP treats the agent runtime as potentially untrusted and says safety
    controls and audit records must not be reachable or modifiable from within it.
- source_title: APTS Compliance Matrix
  source_url: https://owasp.org/APTS/standard/appendix/Compliance_Matrix.html
  source_type: standards_doc
  relevance: Reinforces that runtime containment and audit controls are part of the
    security model, not optional extras.
  key_point: The matrix links manipulation resistance to requirements that name the
    agent runtime as untrusted and require external enforcement.
---

## Meaning

An action plane is a design name for the part of an agent system that checks an action before it happens and decides what to do with it.

In practice, it sits between the agent’s plan and the real world. If an agent wants to send an email, run a command, or call an API, this is where the request can be allowed, blocked, changed, logged, or sent to a person for approval.

It matters because agents can make mistakes. A good action plane helps stop unsafe, unwanted, or accidental actions from reaching users, systems, or data.

It is not the same as the [[Control Plane Architecture|control plane]]. The [[Control Plane Architecture|control plane]] sets the rules. The action pla[[Context Collapse|n]]e applies them when an action is about to happen.

It is also not the whole agent system. If nothing intercepts the action, then there is no real action plane, just a label.
