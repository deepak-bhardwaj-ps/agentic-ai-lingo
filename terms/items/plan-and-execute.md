---
title: Plan-and-execute
short_description: A way of splitting an agent task into a plan first, then doing the steps one by one.
category: Agentic patterns
tags:
- agents
- planning
- orchestration
status: active
aliases:
- plan-then-execute
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal standard with one fixed implementation
- Confusing it with ReAct, which plans and acts in a tighter loop
- Assuming a plan is never revised after execution starts
related_terms:
- Planning
- Execution
- ReAct
- Agent orchestration
- Task decomposition
evidence:
  - source_title: Plan-and-Execute Agents
    source_url: https://blog.langchain.dev/plan-and-execute-agents/
    source_type: engineering_blog
    relevance: This is the clearest current description of the pattern in popular agent tooling, showing the split between making a plan and then carrying it out step by step.
    key_point: Plan-and-execute agents first create a plan, then iteratively execute the planned steps.
  - source_title: Workflows and agents
    source_url: https://docs.langchain.com/oss/python/langgraph/workflows-agents
    source_type: official_docs
    relevance: Helps distinguish plan-and-execute from broader agent workflows by showing that workflows are ordered and predefined, while agents are more dynamic.
    key_point: The pattern is a structured control flow, not just a single model reply.
  - source_title: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models
    source_url: https://arxiv.org/abs/2305.04091
    source_type: research_paper
    relevance: Provides an earlier research basis for the idea of first making a plan and then carrying it out, which supports the term’s meaning beyond one product.
    key_point: Decomposing a task into subtasks before solving it can reduce missing-step errors.
  - source_title: Orchestration is the concept of handling multiple steps, tool use, handoffs between different agents, guardrails, and context
    source_url: https://developers.openai.com/tracks/building-agents
    source_type: official_docs
    relevance: Shows where plan-and-execute fits in modern agent systems: as a control pattern inside orchestration, not as the model itself.
    key_point: Agent systems often need multiple steps where each step feeds the next.
---

Plan-and-execute is an agent pattern where the system makes a plan first and then carries out the plan step by step.

In practice, one part of the system decides the steps, and another part does them. The plan may be fixed at the start, or it may be adjusted after some steps are completed if the situation changes.

This matters because some tasks are too large or messy to solve well in one shot. Breaking the work into steps can make the agent more reliable, easier to debug, and easier to stop or review.

It is not the same as a normal chatbot reply. It is also not exactly the same as ReAct, where thinking and acting happen in a tighter loop. The term is not fully standard, so different tools may use it in slightly different ways, but they usually mean the same basic idea of planning before execution.
