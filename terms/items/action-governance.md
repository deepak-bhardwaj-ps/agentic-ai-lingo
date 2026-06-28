---
slug: action-governance
title: Action Governance
short_description: The rules, checks, and approvals that decide whether an AI agent
  is allowed to take a specific action.
category: Governance
tags:
- agentic-ai
- governance
- safety
- approvals
status: active
aliases:
- Action control
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse: Treating it as a vague policy idea instead of a concrete set of checks,
  approvals, logs, and stop conditions for each action.
related_terms:
- approvals
- guardrails
- orchestration
- audit trail
- authorisation
evidence:
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Shows that agent systems include orchestration, tool execution, approvals,
    and state.
  key_point: OpenAI describes agents as applications that plan, call tools, and keep
    state, and says the SDK is used when the application owns orchestration, tool
    execution, approvals, and state.
- source_title: Guardrails and human review
  source_url: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
  source_type: official_docs
  relevance: Shows that risky actions can be paused for human approval.
  key_point: OpenAI says approvals are the human-in-the-loop path for tool calls and
    that a run can pause until a person approves or rejects a sensitive action.
- source_title: Safety in building agents
  source_url: https://developers.openai.com/api/docs/guides/agent-builder-safety
  source_type: official_docs
  relevance: Shows that tool use should be checked and reviewed before action is allowed.
  key_point: OpenAI recommends tool approvals so users can review and confirm operations,
    and guardrails to filter unsafe input.
- source_title: How we contain Claude across products
  source_url: https://www.anthropic.com/engineering/how-we-contain-claude
  source_type: engineering_blog
  relevance: Shows that tool calls can be filtered through policy checks before they
    take effect.
  key_point: Anthropic describes tool calls passing through proxies that enforce network
    and file policy and inspect return values before they enter the model context.
- source_title: OWASP MCP Top 10
  source_url: https://owasp.org/www-project-mcp-top-10/
  source_type: standards_doc
  relevance: Shows the security need for clear boundaries, permissions, and auditing
    around agent-connected tools.
  key_point: OWASP highlights risks such as privilege escalation, tool poisoning,
    and weak audit and telemetry in agent-connected systems.
---

Action governance is the set of rules that decides whether an AI agent is allowed to do a specific action.

It is the part that sits between “the agent wants to do something” and “the thing actually happens”. That can mean sending a message, changing a file, making a booking, calling a tool, or using money.

In practice, action governance checks things like who requested the action, what the action is, whether it is safe, whether it matches policy, and whether a person must approve it first.

It matters because an agent can do more than answer questions. It can take real actions. Without control, it can make mistakes quickly, expose private data, or do something costly before anyone notices.

Action governance is not just a policy document. It is the working system of permissions, approvals, logs, and stop conditions around each action.

It is also not the same as general company governance. This term is about the moment-by-moment control of what an AI agent may do next.
