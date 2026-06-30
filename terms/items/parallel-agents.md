---
title: Parallel agents
short_description: Multiple agents that work at the same time on separate parts of a task, then have their results combined.
category: Tools and products
tags:
  - multi-agent
  - orchestration
  - concurrency
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Assuming the agents can share state automatically while they run
  - Using parallel agents for steps that depend on each other
  - Treating any multi-agent system as parallel when it is actually taking turns
related_terms:
  - subagents
  - multi-agent workflow
  - agent orchestration
  - concurrent execution
evidence:
  - source_title: Subagents
    source_url: https://developers.openai.com/codex/subagents
    source_type: official_docs
    relevance: OpenAI’s Codex docs describe spawning specialised agents in parallel and collecting the results, which closely matches the practical meaning of this term.
    key_point: Codex can run subagent workflows by spawning specialised agents in parallel and then collecting their results in one response.
  - source_title: Parallel template workflow agent
    source_url: https://adk.dev/agents/workflow-agents/parallel-agents/
    source_type: official_docs
    relevance: Google’s ADK docs give a concrete workflow definition for parallel agents, including independent branches, concurrent execution, and deterministic merging of results.
    key_point: The ParallelAgent executes sub-agents concurrently when the tasks are independent and their outputs are collected afterwards.
  - source_title: Prompting best practices
    source_url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
    source_type: official_docs
    relevance: Anthropic’s guidance explains when subagents should be used in parallel and when they should not, which helps separate the term from ordinary sequential delegation.
    key_point: Use subagents when tasks can run in parallel, require isolated context, or involve independent workstreams that do not need shared state.
  - source_title: Introducing Codex
    source_url: https://openai.com/index/introducing-codex/
    source_type: official_docs
    relevance: OpenAI’s Codex launch page shows the product-level use of parallel agents: multiple tasks run independently in separate sandboxes.
    key_point: Codex can work on many tasks in parallel, with each task running in its own isolated cloud sandbox.
---

Parallel agents are multiple AI agents that work at the same time on different parts of one bigger task.

In practice, each agent is given a separate piece of work. They run in parallel, which means they are active at the same time instead of taking turns. When they finish, a system or person combines their results.

This matters because independent work can finish faster this way. It is useful for things like checking several code issues at once, gathering information from different sources, or reviewing different parts of a plan.

Parallel agents are not the same as one agent doing several steps in order. They also do not mean the agents automatically share memory or understand each other unless that is built in.
