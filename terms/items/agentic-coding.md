---
slug: agentic-coding
title: Agentic Coding
short_description: Coding where an AI system can plan steps, edit code, run tools or
  tests, and improve its work over several turns.
category: Core
tags:
- coding
- agents
- automation
- autonomy
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating any code suggestion from an AI as agentic coding.
- Confusing it with a normal coding assistant that only replies once.
- Assuming the AI works without human review, limits, or approval.
related_terms:
- AI agents
- agent loop
- coding agent
- tool use
- human-in-the-loop
evidence:
- source_title: Build a coding agent with GPT 5.1
  source_url: https://developers.openai.com/cookbook/examples/build_a_coding_agent_with_gpt-5.1
  source_type: official_docs
  relevance: Shows the current OpenAI view of a coding agent as something that edits files, runs shell commands, and iterates on a codebase.
  key_point: OpenAI describes a coding agent as a system that can scaffold code, apply patches, run shell commands, and refine its work through feedback.
- source_title: GitHub Copilot coding agent 101
  source_url: https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/
  source_type: engineering_blog
  relevance: Confirms that industry use of the term includes an asynchronous agent that explores a repository, writes code, runs tests, and opens a pull request.
  key_point: GitHub says its coding agent works like a teammate, runs in GitHub Actions, passes tests, and opens a PR for review.
- source_title: Overview - Claude Code Docs
  source_url: https://docs.anthropic.com/en/docs/claude-code/overview
  source_type: official_docs
  relevance: Shows that Anthropic uses similar language for a tool that reads codebases, edits files, runs commands, and works across multiple files.
  key_point: Anthropic describes Claude Code as an agentic coding tool that reads a codebase, edits files, runs commands, and integrates with development tools.
- source_title: Agents
  source_url: https://docs.langchain.com/oss/python/langchain/agents
  source_type: official_docs
  relevance: Gives a plain definition of agents as systems that call tools in a loop until the task is done, which is the core pattern behind agentic coding.
  key_point: LangChain defines an agent as a model that calls tools in a loop with a harness around that loop.
---

Agentic coding is coding where an AI system can do several steps on its own instead of only suggesting a single piece of code.

In practice, it may read files, make changes, run tests or commands, look at the results, and try again until the task is done. A person still usually sets the goal, chooses the limits, and checks the final code.

This matters because the AI is doing more than autocomplete. Once it can work through a task step by step, you need to think about safety, mistakes, permissions, and who is responsible for the result.

It is not just a chatbot that writes code on request. It is also not fully independent. If it cannot plan, act, check its work, and correct itself within clear limits, it is not really agentic coding.
