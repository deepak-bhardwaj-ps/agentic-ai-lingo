---
slug: agentic-rendering
name: Agentic Rendering
category: Runtime
title: Agentic Rendering
short_description: A loose term for a screen or interface that changes because an
  agent has made a choice, used a tool, or updated its state.
aliases: []
status: emerging
tags:
- agentic-ai
- runtime
- user-interface
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
- Using it to mean any changing screen, even when no agent is involved.
- Treating it like a formal standard term.
- Using it as a vague label for normal app logic.
related_terms:
- agent loop
- orchestration
- stateful UI
- runtime
evidence:
- source_title: Agents SDK | OpenAI API
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Shows that agents are built around state, tools, and orchestration, which
    is the technical basis people point to when they talk about agent-driven interface
    changes.
  key_point: OpenAI describes agents as applications that plan, call tools, collaborate
    across specialists, and keep enough state to complete multi-step work.
- source_title: Building Effective AI Agents - Anthropic
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Supports the idea that agents work in loops with feedback and tools,
    rather than as one-off prompts.
  key_point: Anthropic describes agents as LLMs using tools in a loop with feedback
    from the environment.
- source_title: Managing State – Apps SDK | OpenAI Developers
  source_url: https://developers.openai.com/apps-sdk/build/state-management
  source_type: official_docs
  relevance: Shows that UI behaviour in agent-connected apps can depend on explicit
    state management.
  key_point: OpenAI documents state handling for custom UI components rendered inside
    ChatGPT.
---

Agentic rendering is a loose term for a screen that changes because an agent has made a choice, used a tool, or updated its state.

In practice, that means the user does not just see fixed information. The interface may update after a search, a tool call, a new plan step, or a change in what the agent knows.

The term matters because it describes a tighter link between the agent and the screen. What the user sees depends on what the agent has done, not just on a simple page refresh.

It is not a formal standard name. It is also not the same as any ordinary dynamic website. If people use the term, they should say exactly what changes on the screen and what [[Execution State|agent state]] controls it.
