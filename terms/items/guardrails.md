---
slug: guardrails
name: Guardrails
category: Governance
title: Guardrails
aliases: []
short_description: Rules and checks that limit what an AI agent can do, say, or use.
status: established
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse:
- Treating a prompt as if it were a real security boundary.
- Using the word for vague safety features that are not actually enforced.
related_terms:
- policy
- approvals
- sandboxing
- allow-list
- rate limit
- prompt injection
evidence:
- source_title: OWASP Gen AI Security Project - LLM01:2025 Prompt Injection
  source_url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  source_type: standards_doc
  relevance: Shows why input controls are needed for LLM systems.
  key_point: Prompt injection can change an LLM's behaviour in unwanted ways, so systems
    need controls beyond the prompt itself.
- source_title: Claude Code Hooks Guide
  source_url: https://docs.anthropic.com/en/docs/claude-code/hooks-guide
  source_type: official_docs
  relevance: Shows guardrails as deterministic controls around agent actions.
  key_point: Hooks provide deterministic control so certain actions always happen
    instead of relying on the model to choose them.
- source_title: OpenAI Agents SDK - Guardrails
  source_url: https://platform.openai.com/docs/api-reference/roles/project/list?lang=javascript
  source_type: official_docs
  relevance: Shows guardrails as a named part of agent tooling.
  key_point: OpenAI includes guardrails as a core part of its agents documentation,
    alongside sandboxes and orchestration.
---

Guardrails are rules and checks that keep an AI agent inside set limits.

In practice, guardrails decide what the agent is allowed to read, write, say, or do. They can block unsafe requests, require approval before an action, check that outputs follow a format, limit how often something can happen, or stop the agent from touching certain tools or data.

They matter because a model can make mistakes, follow bad instructions, or try to do the wrong thing. Guardrails help keep those mistakes from turning into real harm.

Guardrails are not the same as a prompt. A prompt is just instructions for the model. Real guardrails are enforced outside the model, so they still work even if the model is confused or tricked.
