---
title: Sandbox execution
short_description: Running agent work inside a restricted environment so it can read files, run commands, and make changes without full access to the host system.
category: Tools and products
tags:
- agents
- sandbox
- execution
- isolation
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a new kind of model
- Assuming it means any kind of Docker container
- Thinking the sandbox alone makes an agent safe
related_terms:
- sandbox
- execution environment
- control plane
- harness
- agent runtime
- execution isolation
evidence:
  - source_title: Sandbox Agents
    source_url: https://developers.openai.com/api/docs/guides/agents/sandboxes
    source_type: official_docs
    relevance: OpenAI uses the phrase "sandbox execution plane", which is the closest current official phrasing for this term in agent systems.
    key_point: OpenAI separates the harness from compute, and says compute is where model-directed work reads and writes files, runs commands, and manages state.
  - source_title: Sandbox - Codex
    source_url: https://developers.openai.com/codex/concepts/sandboxing
    source_type: official_docs
    relevance: Shows the same idea in a product setting and makes the boundary easy to explain to non-specialists.
    key_point: OpenAI says the sandbox is the boundary that lets Codex act autonomously without unrestricted access to the machine.
  - source_title: Docker Sandboxes
    source_url: https://docs.docker.com/ai/sandboxes/
    source_type: official_docs
    relevance: Gives a concrete implementation example of sandbox execution for coding agents.
    key_point: Docker says its sandboxes run AI coding agents in isolated microVMs with separate filesystem and network access.
  - source_title: Making Claude Code more secure and autonomous with sandboxing
    source_url: https://www.anthropic.com/engineering/claude-code-sandboxing
    source_type: engineering_blog
    relevance: Shows how another major AI team describes sandboxed code execution with filesystem and network controls.
    key_point: Anthropic says Claude Code sandboxing isolates code execution and can automatically allow safe operations while blocking malicious ones.
---

Sandbox execution means running an AI agent's work in a limited environment instead of on the main computer directly.

In practice, the agent can read and write files, run commands, install packages, or use tools only inside that restricted space. The sandbox is set up so the agent can do useful work, but cannot freely touch the rest of the machine.

This matters because agents can make mistakes. A sandbox reduces the chance that a bad command, broken script, or unsafe download will damage the host system or reach sensitive data.

It is not the model itself. It is also not just "any Docker container". In this glossary, the term means the execution boundary around the agent's work, not the whole agent system and not a guarantee of safety by itself.
