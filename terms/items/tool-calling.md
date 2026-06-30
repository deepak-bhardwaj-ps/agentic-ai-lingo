---
title: Tool calling
short_description: A way for a model to ask an app to run a tool and return the result.
category: Protocols and standards
tags:
- ai
- protocol
- tools
- agents
status: active
aliases:
- function calling
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse:
- Thinking the model runs the tool itself
- Confusing tool calling with a full agent system
- Assuming every team means exactly the same thing by the phrase
related_terms:
- function calling
- tools
- tool use
- MCP
- agentic workflow
evidence:
  - source_title: Function calling
    source_url: https://developers.openai.com/api/docs/guides/function-calling
    source_type: official_docs
    relevance: Gives a current, explicit version of the same pattern and shows the app executes the function, not the model.
    key_point: A model can request a named function with arguments, and the application runs it and returns the result.
  - source_title: Tool use with Claude
    source_url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
    source_type: official_docs
    relevance: Confirms that major model providers describe the same idea as tool use or tool calling, with the client or platform doing the execution.
    key_point: Claude returns a structured tool call, and either the application or Anthropic executes it depending on the tool type.
  - source_title: Tools
    source_url: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
    source_type: standards_doc
    relevance: Shows the broader protocol view, where tools are exposed by servers and invoked by language models through a standard interface.
    key_point: MCP lets servers expose tools that language models can invoke to interact with external systems.
---

Tool calling is when a model asks an app to run a tool and send back the result.

In practice, the model picks a tool, sends the inputs it needs, and waits for the app or platform to do the real work. The tool might look up data, call an API, calculate something, or make a change in another system.

The term matters because it lets AI apps do more than write text. Tool calling is how a model can check live information, trigger actions, or work through a task step by step.

It is not the same as the whole agent. It is only the part where the model requests a tool. It is also not always a strict technical term, because many people use it the same way they use function calling, while others use tool use for the broader pattern.
