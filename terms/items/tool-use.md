---
title: Tool use
short_description: A model asking outside software to do something for it, such as look up data, call an API, or run a check.
category: Protocols and standards
tags:
  - agentic-ai
  - tools
  - function-calling
  - mcp
status: draft
aliases:
  - tool calling
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating tool use as the same thing as reasoning, when it is really the step where the model asks another system to act.
  - Using it to mean any chat response that mentions a tool, even if no external action is actually taken.
  - Assuming all companies mean exactly the same thing by the term, when some use it for function calls, some for built-in tools, and some for protocol features like MCP.
related_terms:
  - function calling
  - Model Context Protocol
  - agent orchestration
  - external tool
  - actions
  - computer use
evidence:
  - source_title: Tool use with Claude
    source_url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
    source_type: official_docs
    relevance: Defines tool use as Claude calling functions you define or Anthropic provides, which is a clear current example of the term in practice.
    key_point: The model decides when to call a tool and returns a structured call that the app or Anthropic executes.
  - source_title: Tools
    source_url: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
    source_type: standards_doc
    relevance: Shows the protocol-level meaning of tools in an open standard, where servers expose callable tools to models.
    key_point: MCP tools let models interact with external systems such as databases, APIs, and computations through a standard schema.
  - source_title: New tools for building agents
    source_url: https://openai.com/index/new-tools-for-building-agents/
    source_type: engineering_blog
    relevance: Shows how OpenAI frames tools as part of agent building, including built-in tools such as web search, file search, and computer use.
    key_point: Tools are the actions an agent can take outside the model, often through the Responses API and Agents SDK.
---

Tool use is when a model asks another system to do a job for it.

In practice, the model does not just write text. It may ask for a database lookup, an API call, a file search, a calculation, or another action that software can carry out. The system then sends the result back to the model, so it can continue with better information.

This matters because many useful AI systems need more than chat. They need to fetch facts, check work, or trigger actions in the real world. Tool use is one of the main ways agents do that.

Tool use is not the same as thinking, and it is not a guarantee that the answer is right. It is also not one single universal standard. Different platforms use the term for slightly different setups, such as function calling, built-in tools, or protocol-based tools like MCP.
