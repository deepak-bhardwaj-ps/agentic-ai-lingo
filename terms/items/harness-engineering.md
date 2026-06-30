---
title: Harness Engineering
short_description: The work of building the control layer around an AI agent so it can
  act safely and reliably.
category: AgentOps
tags:
- agent-harness
- sandbox
- approvals
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as just prompt writing.
- Treating it as a formal standard with one agreed definition.
related_terms:
- agent harness
- sandbox
- approvals
- guardrails
- tool routing
evidence:
- source_title: Sandbox – Codex
  source_url: https://developers.openai.com/codex/concepts/sandboxing
  source_type: official_docs
  relevance: Shows the current OpenAI Codex view that sandboxing and approvals are separate controls in an agent system.
  key_point: OpenAI says the sandbox sets technical boundaries, while approvals decide when the agent must stop and ask before crossing them.
- source_title: Sandbox Agents
  source_url: https://developers.openai.com/api/docs/guides/agents/sandboxes
  source_type: official_docs
  relevance: Defines the harness as the control plane around the model, which matches the term's core meaning here.
  key_point: OpenAI describes the harness as owning the agent loop, model calls, tool routing, approvals, tracing, recovery, and run state.
- source_title: Build an Agent Improvement Loop with Traces, Evals, and Codex
  source_url: https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop
  source_type: engineering_blog
  relevance: Shows how practitioners use the word in real agent workflows, not as a theoretical abstraction.
  key_point: The notebook says the harness is the full contract around the model, including instructions, tools, routing, output requirements, and validation checks.
- source_title: Prompting best practices
  source_url: https://docs.anthropic.com/claude/prompt-library
  source_type: official_docs
  relevance: Supports the broader idea that agent systems use scaffolding and framework-level controls around the model.
  key_point: Anthropic discusses agentic systems and scaffolding as part of building reliable tool-using behaviour, which aligns with harness engineering.
---

Harness engineering is the work of building the control layer around an AI agent so it can act safely and reliably.

In practice, it means deciding what the agent can see, what tools it can use, when it must ask a human, how its actions are checked, and how failures are handled. It also includes the workspace or sandbox the agent runs in.

This matters because a good model is not enough on its own. An agent can still fail if it cannot reach the right files, if it is given too much power, or if nobody checks its work. Harness engineering helps make those failures less likely and easier to catch.

It is not just prompt writing. It is also not a fully settled technical standard. People usually use the term to describe the support system around a tool-using agent, especially in coding and workflow automation.
