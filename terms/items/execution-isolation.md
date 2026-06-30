---
title: Execution isolation
short_description: Keeping an agent's work inside a limited environment so it cannot freely touch the rest of the system.
category: Agentic patterns
tags:
- agents
- sandbox
- security
- runtime
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal industry standard name
- Confusing it with the model itself instead of the environment around it
- Assuming a sandbox alone is enough without limits on files, network, and permissions
related_terms:
- sandbox
- execution boundary
- guardrails
- approvals
- tool authorization
- containment
evidence:
- source_title: Sandbox Agents
  source_url: https://developers.openai.com/api/docs/guides/agents/sandboxes
  source_type: official_docs
  relevance: Shows the current agent pattern of placing work inside an isolated execution environment with files, commands, and controlled access.
  key_point: OpenAI describes a sandbox as an isolated Unix-like execution environment with controlled access to external systems.
- source_title: Sandbox
  source_url: https://developers.openai.com/codex/concepts/sandboxing
  source_type: official_docs
  relevance: Uses the same containment idea for Codex and makes the boundary explicit.
  key_point: OpenAI says the sandbox is the boundary that lets Codex act autonomously without unrestricted access to the machine.
- source_title: How we contain Claude across products
  source_url: https://www.anthropic.com/engineering/how-we-contain-claude
  source_type: engineering_blog
  relevance: Explains why real agent systems need containment around actions, not just model prompts.
  key_point: Anthropic frames containment as limiting an agent's blast radius and supervising actions through human review and other controls.
---

Execution isolation means keeping an AI agent's work inside a limited, controlled place.

In practice, that place is usually a sandbox or similar runtime boundary. The agent can run commands, edit files, or use tools only within the rules of that environment. It may not be able to reach the rest of the computer, the wider network, or sensitive data unless those things are explicitly allowed.

This matters because agents can make mistakes or follow bad instructions. If their actions are isolated, a mistake is less likely to damage the host machine, leak data, or send a harmful command to a real system.

It is not the AI model itself. It is also not the same as a prompt or a vague safety rule. Execution isolation is about where the action happens and what that place is allowed to touch.

This term is not used in one fixed way across the industry. Some teams use it to mean sandboxing, while others use it more broadly to include permission checks and approval steps around execution.
