---
title: Fan-out
short_description: A step where one job is split into several smaller tasks that can run in parallel.
category: Agentic patterns
tags:
- agentic-ai
- orchestration
- multi-agent
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating it as the same thing as fan-in, which is the combining step
- Using it to mean any kind of delegation, even when the tasks are not split for parallel work
related_terms:
- fan-in
- concurrent orchestration
- parallel agents
- coordinator pattern
- scatter-gather
evidence:
- source_title: Parallel Agents with the OpenAI Agents SDK
  source_url: https://developers.openai.com/cookbook/examples/agents_sdk/parallel_agents
  source_type: official_docs
  relevance: Shows the term in current agent tooling and makes clear that fan-out means splitting work across multiple specialised agents.
  key_point: OpenAI describes fan-out as sending different parts of a job to multiple agents so they can work in parallel before their outputs are collected.
- source_title: Choose a design pattern for your agentic AI system
  source_url: https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
  source_type: official_docs
  relevance: Gives a current vendor definition of the parallel agent pattern, which is the broader design family fan-out belongs to.
  key_point: Google Cloud says the parallel pattern splits work across specialised agents at the same time and then combines the outputs.
- source_title: Building Effective AI Agents: Architecture Patterns and Implementation Frameworks
  source_url: https://resources.anthropic.com/hubfs/Building%20Effective%20AI%20Agents-%20Architecture%20Patterns%20and%20Implementation%20Frameworks.pdf
  source_type: engineering_blog
  relevance: Confirms fan-out/fan-in as a recognised agent architecture pattern rather than a one-off product term.
  key_point: Anthropic describes a pattern where work is spread across independent tasks first and then aggregated afterwards.
---

Fan-out is the step where one job is split into several smaller tasks so they can run at the same time.

In an agent workflow, a controller or coordinator often uses fan-out when one request needs several separate checks, searches, or analyses. Each subtask handles one part of the job, and the results can be joined later.

It matters because parallel work can be faster and can cover more ground than doing everything in one long line. It is useful when the subtasks do not depend on each other.

Fan-out is not fan-in. Fan-in is the step where the separate results are brought back together.

It is also not the same as general delegation. Fan-out specifically means splitting work for parallel processing, not just handing work to someone else.
