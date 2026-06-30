---
title: Function calling
short_description: A way for a model to ask an app to run a named function with arguments and then use the result.
category: Protocols and standards
tags:
- ai
- protocol
- tools
- agents
status: active
aliases:
- Tool calling
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse:
- Thinking the model runs the function itself
- Confusing function calling with a full agent system
- Assuming the model can call any code without the app defining the function first
related_terms:
- tools
- tool calling
- structured outputs
- MCP
- agentic workflow
evidence:
  - source_title: Function calling
    source_url: https://developers.openai.com/api/docs/guides/function-calling
    source_type: official_docs
    relevance: OpenAI gives a clear current definition and shows the basic request-response loop for function calls.
    key_point: Function calling lets a model request a named tool or function with arguments, while the application executes the function and returns the result.
  - source_title: Tool use with Claude
    source_url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
    source_type: official_docs
    relevance: Confirms that another major model provider uses the same pattern and that the application, not the model, executes the tool.
    key_point: Claude can return a structured tool call, and the client or Anthropic then executes the tool depending on the tool type.
  - source_title: Function calling with the Gemini API
    source_url: https://ai.google.dev/gemini-api/docs/function-calling
    source_type: official_docs
    relevance: Shows the same pattern in Google’s current API docs and makes the execution boundary explicit.
    key_point: The model receives function declarations, but your application executes the function and sends the result back.
---

Function calling is a way for an AI model to ask an app to run a named function with specific inputs.

In practice, the model does not do the work itself. It picks a function, sends the arguments, and waits for the app to run that function and return the result. The app then uses that result to continue the conversation or finish the task.

The term matters because it lets a model connect to real data and real actions, such as checking a booking, looking up weather, or saving a record. It is one of the main ways modern AI apps do more than generate text.

Function calling is not the same as the whole agent. It is only the part where the model asks for a function to be run. It is also not magic code execution, because the app must define the function first and decide what it is allowed to do.
