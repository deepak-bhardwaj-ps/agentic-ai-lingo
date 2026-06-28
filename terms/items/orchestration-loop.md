---
slug: orchestration-loop
name: Orchestration Loop
category: Runtime
title: Orchestration Loop
aliases:
- agent loop
short_description: A control cycle that decides what an AI system should do next,
  checks the result, and either stops or tries again.
status: active
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating any repeated model call as a full orchestration system
- Assuming the loop is the same as the model itself
- Leaving out stop conditions, budgets, and failure handling
related_terms:
- agent loop
- workflow
- state machine
- tool use
- planner
evidence:
- source_title: Building Effective Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: High-level reference for agent workflows and control patterns.
  key_point: Anthropic describes effective agents as simple, composable control patterns
    that coordinate model calls, tools, and checks rather than relying on one giant
    prompt.
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Shows how a runtime can own orchestration, tool execution, approvals,
    and state.
  key_point: OpenAI separates the application-owned orchestration layer from the model
    call itself.
- source_title: LangGraph Overview
  source_url: https://docs.langchain.com/oss/python/langgraph/overview
  source_type: official_docs
  relevance: Explains orchestration as durable execution, state, and human-in-the-loop
    control.
  key_point: LangGraph treats orchestration as a stateful control layer for long-running
    agent work.
---

An orchestration loop is the control cycle that decides what an AI system should do next, checks what happened, and then either stops or chooses another step.

In practice, it is the bit of software around the model that sends a prompt, watches for a tool call or result, updates the task state, and repeats this until the job is done or the system gives up.

This matters because many useful AI tasks are not one-step tasks. The system may need to search, calculate, ask a tool for help, read the result, and then decide the next move. The loop keeps that process organised.

It is not the AI model itself. It is also not a magical “autonomous agent”. It is just control logic, so it needs clear stop rules, limits on retries, and a way to handle errors. Without those, it can waste time, money, or get stuck repeating the same steps.
