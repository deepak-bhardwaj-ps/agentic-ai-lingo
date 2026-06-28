---
slug: execution-state
name: Execution State
title: Execution State
category: Runtime
short_description: The mutable record an agent runtime uses to continue a run after
  each step.
aliases:
- run state
- agent state
status: active
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse:
- Treating it as the same thing as long-term memory
- Storing the full chat log instead of only the facts needed to resume work
- Leaving out checkpoints, budgets, or tool results that the orchestrator needs
related_terms:
- agent-runtime
- agent-memory
- context-engineering
- checkpoint
- orchestration
evidence:
- source_title: MemGPT
  source_url: https://arxiv.org/abs/2310.08560
  source_type: research_paper
  relevance: Shows the need for separating working context from longer-lived state
    in long-running agents.
  key_point: MemGPT manages memory across context limits so the agent can keep working
    without holding everything in the prompt.
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Describes agent applications as owning orchestration, tool execution,
    approvals, and state.
  key_point: State is part of the application runtime that helps the agent complete
    multi-step work.
- source_title: Effective harnesses for long-running agents
  source_url: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  source_type: engineering_blog
  relevance: Explains how long-running agent systems need context management such
    as compaction.
  key_point: Agent runtimes need a way to carry forward only the useful parts of a
    run.
---

Execution state is the working record an agent system keeps so it can continue a task after each step.

In practice, it usually stores things like the current plan, what the agent has already tried, tool results, checkpoints, and any limits the system must respect. When the agent takes another step, the runtime reads this record and updates it.

This matters because a long task can involve many model calls, tools, and pauses. Without execution state, the agent would forget where it was and could not safely resume work.

It is not the same as long-term memory. Execution state is for the current run. It should stay small and focused on what is needed to continue the task, not every message ever seen.
