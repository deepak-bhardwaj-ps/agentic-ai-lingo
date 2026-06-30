---
title: Tool routing
short_description: The step that chooses which tool an agent should use for a request.
category: Agentic patterns
tags:
- agentic-ai
- tools
- routing
- orchestration
status: glossary
aliases:
- skill routing
- tool router
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it as the same thing as authorisation or safety checks
- Thinking it means the tool itself rather than the decision about which tool to use
- Assuming it is a formal standard instead of a design pattern that different teams name differently
related_terms:
- tool calling
- function calling
- tool gateway
- agent orchestration
- task assignment
evidence:
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Anthropic describes routing as one of the simple control patterns used in practical agent systems.
  key_point: The article treats routing as a way to send a request to the next best step or specialist rather than handling everything in one prompt.
- source_title: Sandbox Agents
  source_url: https://developers.openai.com/api/docs/guides/agents/sandboxes
  source_type: official_docs
  relevance: OpenAI separates tool routing from the rest of the runtime, which shows that choosing a tool is a distinct control step.
  key_point: The harness owns tool routing, handoffs, approvals, tracing, recovery, and run state, so routing is part of the agent control plane.
- source_title: Router
  source_url: https://docs.langchain.com/oss/python/langchain/multi-agent/router
  source_type: official_docs
  relevance: LangChain gives a clear implementation of routing as a dedicated step that classifies input and dispatches to an agent.
  key_point: A router is described as a preprocessing step that chooses where the request should go, rather than doing the whole task itself.
- source_title: Function calling
  source_url: https://developers.openai.com/api/docs/guides/function-calling
  source_type: official_docs
  relevance: Shows the underlying tool-use mechanism that routing often sits in front of.
  key_point: The model can request tool use, but application logic still decides which tool is available and how it is run.
---

Tool routing is the step that decides which tool an agent should use for a request.

In practice, the system looks at the user’s request, the current context, and any rules it has, then sends the work to one tool or a small set of tools. For example, a billing question might go to a payments tool, while a code task might go to a search or editing tool.

This matters because agents often have many tools, and not every tool should be used for every job. Good routing can make the system faster, more accurate, and easier to control.

Tool routing is not the same as authorisation. It helps choose a tool, but it does not decide who is allowed to use it or whether the action is safe.

It is also not the tool itself. The tool does the work. Routing only decides where the request should go. In practice, people sometimes use tool routing, skill routing, and tool router to mean almost the same thing.
