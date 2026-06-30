---
title: Agentic harness
short_description: Software around a model that runs the agent loop, tools, state, and checks.
category: Evals
tags:
  - agents
  - orchestration
  - evaluation
  - runtime
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the model itself
  - Using it to mean a benchmark or test suite
  - Assuming it has one fixed industry-wide definition
related_terms:
  - Agent harness
  - Evaluation harness
  - Agent runtime
  - Agent orchestrator
  - Agent evaluation
evidence:
  - source_title: Sandbox Agents
    source_url: https://developers.openai.com/api/docs/guides/agents/sandboxes
    source_type: official_docs
    relevance: Shows the current OpenAI framing of the harness as the control layer around an agent, which is the closest authoritative match for this term.
    key_point: OpenAI says the harness is the control plane around the model and owns the agent loop, tool routing, handoffs, approvals, tracing, recovery, and run state.
  - source_title: Demystifying evals for AI agents
    source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    source_type: engineering_blog
    relevance: Distinguishes an agent harness from the model and shows why the surrounding system matters when evaluating agent behaviour.
    key_point: Anthropic says an agent harness enables a model to act as an agent by processing inputs, orchestrating tool calls, and returning results, and that agent evaluation covers both the harness and the model together.
  - source_title: Agents
    source_url: https://docs.langchain.com/oss/javascript/langchain/agents
    source_type: official_docs
    relevance: Provides a plain-language definition used by a major agent framework and confirms that a harness is the software around the model loop.
    key_point: LangChain says an agent is a model calling tools in a loop and that the harness is everything around that loop, including the model, prompt, tools, and middleware.
---
An agentic harness is the software around an AI model that lets it act like an agent.

In practice, it runs the loop that sends work to the model, lets the model call tools, keeps track of what has happened, and decides when to continue, stop, ask for approval, or hand work to another step.

This matters because an agent is usually more than one model reply. The harness is what keeps the work organised so the system can do longer jobs without losing context or drifting off task.

This is not the model itself. It is also not a fixed standard term. Many teams would call the same thing an agent harness, runtime, scaffold, or orchestration layer.
