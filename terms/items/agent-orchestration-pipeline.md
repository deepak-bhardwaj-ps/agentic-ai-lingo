---
title: Agent orchestration pipeline
short_description: A step-by-step control flow that routes work between agents, tools, and checks.
category: Agentic patterns
tags:
  - orchestration
  - multi-agent
  - workflow
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating any chain of prompts as a full orchestration pipeline
  - Confusing orchestration with the model itself
  - Using the term as a vague synonym for automation
related_terms:
  - agent orchestration
  - multi-agent orchestration
  - orchestration loop
  - workflow orchestration
  - tool use
evidence:
  - source_title: Agents SDK
    source_url: https://developers.openai.com/api/docs/guides/agents
    source_type: official_docs
    relevance: Shows that OpenAI separates orchestration from the model call and treats it as part of the application layer.
    key_point: OpenAI says the application can own orchestration, tool execution, approvals, and state, which matches the idea of a pipeline around agents rather than the model itself.
  - source_title: Agent Builder
    source_url: https://developers.openai.com/api/docs/guides/agent-builder
    source_type: official_docs
    relevance: Shows a concrete product example of multi-step agent workflows built from connected steps.
    key_point: OpenAI describes Agent Builder as a visual canvas for multi-step agent workflows with nodes, inputs, outputs, and run previews.
  - source_title: Workflow for orchestration
    source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-for-orchestration.html
    source_type: standards_doc
    relevance: Gives a clear multi-agent orchestration pattern where a central orchestrator plans and delegates to workers.
    key_point: AWS describes an orchestrator agent that plans, decomposes, and delegates subtasks to specialised worker agents, which is the closest current meaning of this term.
---

An agent orchestration pipeline is a step-by-step control flow that decides which agent, tool, or check should happen next.

In practice, it is the software around the agents. It may split a task into smaller parts, send each part to a specialist agent, wait for results, combine them, and then choose the next step.

This matters because many agent jobs are too big for one prompt. A pipeline helps keep work ordered, makes hand-offs clearer, and gives the system a way to handle retries, approvals, and stopping rules.

It is not the model itself. It is not the same as a simple prompt chain. And it is not a formal standard term, so different teams may use it to mean a slightly different kind of workflow.
