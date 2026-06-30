---
title: Sequential orchestration
short_description: A pattern where agent steps run one after another, and each step uses the output of the step before it.
category: Agentic patterns
tags:
- agents
- orchestration
- multi-agent
status: active
aliases:
- linear orchestration
- pipeline
- prompt chaining
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as any orchestration when it specifically means a fixed one-after-another order
- Assuming the steps can run in parallel
- Using it as a synonym for any prompt chain, even when there is no real control flow
related_terms:
- Agent orchestration
- Concurrent orchestration
- Handoff orchestration
- Agentic workflow
- Pipeline
evidence:
  - source_title: AI Agent Orchestration Patterns
    source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
    source_type: official_docs
    relevance: This is one of the clearest current definitions of the sequential pattern and shows how the term is used in agent design guidance.
    key_point: Microsoft defines sequential orchestration as chaining agents in a predefined, linear order, where each agent processes the previous agent's output.
  - source_title: Sequential orchestration
    source_url: https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-orchestration/sequential
    source_type: official_docs
    relevance: Gives a direct product-level explanation of how the pattern works in practice and confirms the pipeline framing.
    key_point: Sequential orchestration means agents are organised in a pipeline and each agent passes its output to the next one in turn.
  - source_title: Workflow orchestrations in Agent Framework
    source_url: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/
    source_type: official_docs
    relevance: Places sequential orchestration alongside the other main multi-agent patterns, which helps keep the scope narrow.
    key_point: Microsoft lists sequential orchestration as the pattern where agents execute one after another in a defined order.
  - source_title: Workflow orchestration agents
    source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html
    source_type: official_docs
    relevance: Supports the broader orchestration idea in agent systems: multistep work is coordinated through intermediate results, not a single model call.
    key_point: AWS describes workflow orchestration agents as coordinating multistep tasks and adapting based on intermediate results, which fits the sequential pattern when the steps are ordered.
---

Sequential orchestration is a pattern where agent steps run one after another in a fixed order.

In practice, the first agent or step does some work, then its result goes to the next step, and so on until the task is finished. Each step depends on what came before it.

This matters because some jobs are easiest when they are broken into simple stages. A later step can check, refine, or transform the earlier result instead of trying to solve everything at once.

It is not the same as concurrent orchestration, where steps run at the same time. It is also not the same as handoff orchestration, where control moves to a different agent because the task needs a different specialist.
