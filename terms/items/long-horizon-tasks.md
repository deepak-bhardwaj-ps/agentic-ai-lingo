---
slug: long-horizon-tasks
title: Long-Horizon Tasks
short_description: Tasks that take many dependent steps to finish and need the work
  to stay on track over time.
category: Runtime
tags:
- agentic-ai
- tasks
- planning
- memory
status: active
aliases:
- Long horizon tasks
- Long-horizon work
meaning_type: emerging_unsettled
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it as proof that an agent is autonomous.
- Using it to mean any task that is merely slow.
- Leaving the task scope, checkpoints, or finish line undefined.
related_terms:
- checkpoints
- state
- memory
- planning
- multi-step tasks
evidence:
- source_title: Working with evals
  source_url: https://platform.openai.com/docs/guides/evals
  source_type: official_docs
  relevance: Shows that agent work should be evaluated with clear task structure,
    success criteria, and recovery from failures.
  key_point: Evals are for measuring behaviour on defined tasks, which supports the
    idea that long tasks need explicit checkpoints and success rules.
- source_title: Enabling Claude Code to work more autonomously
  source_url: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
  source_type: engineering_blog
  relevance: Describes checkpoints, subagents, hooks, and background tasks for longer,
    more complex work.
  key_point: Long-running tasks benefit from saved state and the ability to rewind
    to a previous point.
- source_title: How we built our multi-agent research system
  source_url: https://www.anthropic.com/engineering/multi-agent-research-system
  source_type: engineering_blog
  relevance: Explains that long conversations need memory, compression, and careful
    handoffs.
  key_point: When work spans many turns, systems must keep useful context outside
    the active chat window.
---

Long-horizon tasks are jobs that take many steps to finish and must stay on track as the work goes on.

In practice, this means the system has to remember what it has already done, keep moving towards the goal, and recover if something goes wrong. It may need checkpoints, notes, or saved progress so it can continue later without starting over.

The term matters because some tasks are hard not because each step is difficult, but because there are so many steps and each one depends on the last one. A long task can fail if the system forgets earlier decisions or loses its place.

This is not the same as being fully autonomous. It is also not just another word for a benchmark, a complex task, or a slow task. To use the term well, you should say how long the task is, what counts as progress, where checkpoints happen, and how success is measured.
