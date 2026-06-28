---
slug: trust-plane
name: Trust Plane
category: Governance
title: Trust Plane
aliases: []
short_description: A trust plane is a proposed layer for deciding what an AI agent
  is allowed to do, proving why it was allowed, and keeping a record of it.
tags:
- governance
- security
- agentic-ai
status: emerging
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating the term as if it has one fixed, agreed meaning
- Using it as a fancy word for ordinary access control or logging
- Calling any AI safety feature a trust plane even when it does not enforce permissions
related_terms:
- control plane
- governance
- permissions
- audit log
- zero trust
evidence:
- source_title: OWASP Top 10 for Large Language Model Applications
  source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
  source_type: standards_doc
  relevance: OWASP is the main public security reference here and shows that AI agent
    security is usually discussed as governance, permissions, and attack surfaces
    rather than as a fixed "trust plane" standard.
  key_point: The OWASP GenAI Security Project covers security and governance risks
    for agentic AI systems, but it does not define "trust plane" as an official standard
    term.
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: OpenAI's agent docs show that real agent systems need orchestration,
    tool execution, approvals, and state management.
  key_point: Agent builders must control approvals and tool use, which is the kind
    of job people usually mean when they talk about a trust plane.
- source_title: Agent approvals & security
  source_url: https://developers.openai.com/codex/agent-approvals-security
  source_type: official_docs
  relevance: This shows a concrete example of enforcement and review around risky
    agent actions.
  key_point: Some actions need approval, risky actions can be denied, and failures
    are designed to fail closed.
- source_title: Permissions
  source_url: https://developers.openai.com/codex/permissions
  source_type: official_docs
  relevance: This is direct evidence that enforcement boundaries, network limits,
    and approval policies are separate controls in a real agent system.
  key_point: Permission profiles define the boundaries for sandboxed command execution,
    while other controls handle approvals and other surfaces.
- source_title: How we contain Claude across products
  source_url: https://www.anthropic.com/engineering/how-we-contain-claude
  source_type: engineering_blog
  relevance: Anthropic explains the practical layers used to contain an agent.
  key_point: Security comes from overlapping boundaries such as sandboxes, filesystem
    limits, egress controls, tool permissions, and oversight, not from a single magic
    layer.
---

## Meaning

A trust plane is a proposed layer that decides what an AI agent is allowed to do and keeps evidence of why those actions were allowed.

In practice, it sits above the tools the agent can use. It checks identity, permissions, limits, approvals, and logs before the agent acts.

This matters because an AI agent can do real-world things, like read files, send messages, or call APIs. If those actions are not controlled, the agent can cause damage by accident or by being tricked.

A trust plane is not the same as a chatbot prompt, and it is not just a log file. It only counts if it can actually stop, allow, limit, or record actions.

The term is useful, but it is not yet widely standardised. Different teams may use it to mean slightly different things.
