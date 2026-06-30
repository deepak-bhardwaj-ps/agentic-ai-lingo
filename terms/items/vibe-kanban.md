---
title: vibe-kanban
short_description: A tool for planning, running, and reviewing AI coding agents with a kanban-style board.
category: Tools and products
tags:
  - ai-agents
  - kanban
  - coding-workflow
  - product
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the same thing as Kanban itself, when it is a specific product built around a kanban-style workflow.
  - Assuming it replaces the coding agent, when it mainly helps organise, run, and review agent work.
  - Thinking it is a general project management board, when its focus is AI coding agents and code review.
related_terms:
  - kanban-board
  - coding-agent
  - issue-tracker
  - git-worktree
  - code-review
evidence:
  - source_title: BloopAI/vibe-kanban README
    source_url: https://github.com/BloopAI/vibe-kanban
    source_type: official_docs
    relevance: The project repository is the primary source for what the tool is and how its makers describe it.
    key_point: Describes Vibe Kanban as a way to plan work with kanban issues, run coding agents in workspaces, review diffs, preview apps, and create pull requests.
  - source_title: Vibe Kanban website
    source_url: https://vibekanban.com/
    source_type: official_docs
    relevance: The product website explains the current workflow and intended use.
    key_point: Frames the tool as a way to orchestrate parallel coding agents, break work into issues and sub-issues, and move through plan, prompt, and review stages.
  - source_title: GitHub All-Stars #11: vibe-kanban – a Kanban board for AI agents
    source_url: https://virtuslab.com/blog/ai/vibe-kanban
    source_type: engineering_blog
    relevance: Independent explanation of how the tool works in practice and why people use it.
    key_point: Confirms the product is a kanban board for AI agents, with parallel work, isolated git worktrees, and a review step before merging.
  - source_title: What is Kanban in Project Management?
    source_url: https://www.atlassian.com/agile/kanban
    source_type: official_docs
    relevance: Useful for distinguishing the general kanban idea from this specific product.
    key_point: Shows kanban is a workflow method using visual boards and cards, which helps clarify that Vibe Kanban is a product built around that method rather than kanban itself.
---

Vibe Kanban is a tool for organising AI coding agents with a kanban-style board.

In practice, you use it to plan work as issues, send tasks to coding agents, and then review the changes they make before merging them. It is built for situations where several agent tasks can run at the same time, so you can keep track of what is waiting, what is being worked on, and what is ready to check.

This matters because AI coding agents can do useful work, but they still need a human to split work into parts, watch progress, and check the result. Vibe Kanban tries to make that process easier and less messy.

It is not the same as the kanban method in general, and it is not just a plain task board for any kind of project. It is a specific product focused on AI coding work and code review.
