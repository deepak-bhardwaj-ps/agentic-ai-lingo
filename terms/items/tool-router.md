---
slug: tool-router
title: Tool Router
short_description: A tool router decides which tool an agent should use for a request.
category: Runtime
tags:
- agentic-ai
- runtime
- tools
- routing
status: active
aliases:
- tool routing
- router
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating the router as security or permission control
- Assuming it can safely validate every tool input by itself
related_terms:
- tool-authorization
- policy-plane
- skill-routing
- dynamic-skill-routing
evidence:
- source_title: Building Effective Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Shows that effective agents use simple control patterns, including deciding
    when to call tools.
  key_point: Anthropic describes agents as systems that use tool selection as part
    of the control loop, rather than one giant prompt doing everything.
- source_title: Function calling
  source_url: https://developers.openai.com/api/docs/guides/function-calling
  source_type: official_docs
  relevance: Explains the standard tool-calling pattern that a router often sits in
    front of.
  key_point: OpenAI documents tool calling as a way for models to request external
    actions through application code, which needs logic to choose and run the right
    tool.
- source_title: Build a multi-source knowledge base with routing
  source_url: https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base
  source_type: official_docs
  relevance: Describes the routing pattern used to send requests to the most suitable
    specialised agent or tool set.
  key_point: LangChain presents routing as a classification step that directs input
    to the right specialist path.
---

A tool router is the part of an agent system that decides which tool should handle a request.

In practice, it looks at the user’s request, the current context, and any rules or limits, then chooses one tool or a small set of tools that are allowed to run. For example, a router might send a billing question to a payments tool and a coding task to a code-search tool.

This matters because agents often have many tools, and not every tool should be available for every request. A router helps keep the system more accurate, faster, and easier to control.

A tool router is not the same as authorisation. It helps choose a tool, but the tool itself must still check who is allowed to use it, what data it can touch, and whether the input is safe.
