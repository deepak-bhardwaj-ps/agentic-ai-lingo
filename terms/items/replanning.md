---
title: Replanning
short_description: Updating a plan after new information shows the old one is no longer the best path.
category: Agentic patterns
tags:
- agentic-ai
- planning
- agent-loop
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as planning from the start
- Using it to mean any small correction, even when the overall plan stays the same
- Confusing it with reflection, which is about reviewing and judging a step rather than changing the plan itself
related_terms:
- Planning
- Reflection
- Plan-and-execute
- ReAct
- Error recovery
evidence:
  - source_title: Plan-and-Execute Agents
    source_url: https://blog.langchain.dev/plan-and-execute-agents/
    source_type: engineering_blog
    relevance: Shows a common agent pattern where a system makes a plan, executes it, and may call the agent again with a re-planning prompt after execution.
    key_point: After a plan has been tried, the system can generate a follow-up plan if the first one did not work.
  - source_title: Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks
    source_url: https://arxiv.org/html/2503.09572v3
    source_type: research_paper
    relevance: Defines replanning as part of a planner-executor setup for long tasks, which is close to how the term is used in agent systems.
    key_point: A plan guides execution, but execution can feed back into later planning when the task changes or the first plan is insufficient.
  - source_title: Agent planning and execution
    source_url: https://docs.warp.dev/agent-platform/capabilities/planning/
    source_type: official_docs
    relevance: Shows a current product example where a running agent can adjust its plan when the user updates it or the situation changes.
    key_point: Plans are not always fixed; they can be revised during execution.
  - source_title: Plan-execute-reflect agents
    source_url: https://docs.opensearch.org/latest/ml-commons-plugin/agents-tools/agents/plan-execute-reflect/
    source_type: official_docs
    relevance: Gives a modern control-flow example where the planner creates and updates a plan, which helps ground replanning as an explicit step in an agent loop.
    key_point: The planner can create and update a plan as the agent works through a task.
---

Replanning is when an AI agent changes an existing plan after it gets new information, hits a problem, or sees that the original plan is no longer good enough.

In practice, the agent tries a plan, checks what happened, and then chooses a different next set of steps. The new plan may be small, like changing one action, or larger, like taking a different route to the same goal.

This matters because real tasks change while they are happening. Tools can fail, data can be incomplete, or the user can update the request. Replanning helps the agent recover instead of blindly continuing down the wrong path.

Replanning is not the same as planning from scratch. It is also not the same as reflection, which is about looking back and judging what happened, even though reflection can lead to replanning. The term is used in a fairly consistent way in agent work, but it is not a strict formal standard.
