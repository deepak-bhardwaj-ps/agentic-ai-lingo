---
slug: agent-loop
title: Agent Loop
short_description: A repeated cycle where an AI system makes a step, checks the result, and decides what to do next.
category: Runtime
tags:
- agents
- orchestration
- runtime
- tools
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse:
- Treating any repeated model call as a full agent system
- Thinking the loop is the model itself
- Assuming the loop is safe or correct without limits and checks
related_terms:
- agent runtime
- orchestration loop
- tool calling
- human-in-the-loop
- state
evidence:
- source_title: Running agents
  source_url: https://developers.openai.com/api/docs/guides/agents/running-agents
  source_type: official_docs
  relevance: Gives a current, direct definition of the agent loop as the turn-by-turn control cycle for an agent run.
  key_point: OpenAI describes the loop as calling the model, checking the output, running tools or handoffs if needed, and stopping when there is a final answer.
- source_title: Agent SDK overview
  source_url: https://code.claude.com/docs/en/agent-sdk/overview
  source_type: official_docs
  relevance: Shows that an agent loop is the built-in control flow behind a working agent, not just a single prompt.
  key_point: Anthropic says the SDK gives builders the same tools, agent loop, and context management used by Claude Code.
- source_title: Agents
  source_url: https://docs.langchain.com/oss/python/langchain/agents
  source_type: official_docs
  relevance: Uses very plain language for the same idea and helps confirm the term is about repeated tool use until the task is complete.
  key_point: LangChain defines an agent as a model calling tools in a loop until the task is done, with a harness around that loop.
---

An agent loop is a repeating cycle where an AI system takes a step, checks the result, and decides what to do next.

In practice, the system may ask a model what to do, use a tool, read the result, and then repeat the process until the task is finished. What happens in one step becomes the input for the next step.

This matters because many useful jobs cannot be done well in one reply. Looking things up, comparing choices, fixing mistakes, and checking work often need several rounds.

It is not just a normal chat reply. It is also not the same as the whole app around the agent. The loop is only the repeat-and-check part, so it still needs clear stop rules, limits, and error handling.
