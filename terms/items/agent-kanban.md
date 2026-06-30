---
title: Agent kanban
short_description: A Kanban-style task board for planning, running, and reviewing work done by AI coding agents.
category: Tools and products
tags:
- kanban
- agentic-ai
- coding-agents
- task-management
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a standard Kanban board for people, when the focus is agent tasks and agent execution.
- Assuming every product with a task board and an agent is an agent kanban system.
- Using it to imply true autonomy, when humans still set work, review output, and approve changes.
related_terms:
- kanban board
- agent orchestration
- coding agent
- task management
- human-in-the-loop
- workflow runtime
evidence:
  - source_title: GitHub - BloopAI/vibe-kanban
    source_url: https://github.com/BloopAI/vibe-kanban
    source_type: engineering_blog
    relevance: The project describes itself as a Kanban board for coding agents, with planning, execution workspaces, diff review, and PR creation.
    key_point: Shows the term in current product use as a board for coordinating AI coding work.
  - source_title: GitHub - saltbo/agent-kanban
    source_url: https://github.com/saltbo/agent-kanban
    source_type: engineering_blog
    relevance: The repository explicitly calls itself an agent-first task board and mission control for an AI workforce.
    key_point: Confirms that “agent kanban” is being used to mean a task board designed around agents, not just people.
  - source_title: What is a kanban board?
    source_url: https://www.atlassian.com/agile/kanban/boards
    source_type: official_docs
    relevance: Defines the base Kanban idea: visualise work, track cards through columns, and limit work in progress.
    key_point: Establishes the workflow-board meaning that the agent version adapts.
  - source_title: What is Kanban?
    source_url: https://www.atlassian.com/agile/kanban
    source_type: official_docs
    relevance: Explains Kanban as a visual workflow method focused on flow and work-in-progress limits.
    key_point: Supports the idea that the “kanban” part is about visible flow control, not autonomy by itself.
---

Agent kanban is a task board for AI agents, usually coding agents, that shows work as cards moving through stages such as to do, in progress, review, and done.

In practice, it helps a person split work into tasks, send those tasks to an agent, watch progress, and review the results before anything is accepted.

The term matters because it gives a simple way to organise several agent jobs at once. It makes the work easier to see, easier to check, and easier to stop if something goes wrong.

It is not a formal standard. It does not mean the agents are fully independent, and it does not mean the board itself does the work. Humans still choose the tasks and approve the output.
