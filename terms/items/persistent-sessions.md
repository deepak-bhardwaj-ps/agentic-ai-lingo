---
title: Persistent sessions
short_description: A persistent session is an agent session whose state is saved so work can be resumed later instead of starting over.
category: Agentic patterns
tags:
- sessions
- state
- resumption
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse:
- Thinking it means the model remembers everything by itself.
- Treating it as the same as long-term memory.
- Assuming state always survives every crash or outage.
related_terms:
- sessions
- session state
- conversation history
- resumable agents
- checkpointing
evidence:
  - source_title: Session resume and persistence
    source_url: https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/session-persistence
    source_type: official_docs
    relevance: GitHub describes session persistence as saving conversation history, tool state, and planning context so work can be resumed after restarts or client changes.
    key_point: A persistent session keeps enough state to pause work and continue later from the same session ID.
  - source_title: Storage
    source_url: https://learn.microsoft.com/en-us/agent-framework/agents/conversations/storage
    source_type: official_docs
    relevance: Microsoft explains that storage controls where conversation history lives and how reliably sessions can be resumed, which is the core idea behind persistent sessions.
    key_point: Persisting session state is about resume reliability, not just keeping chat logs.
  - source_title: Manage hosted agent sessions
    source_url: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-hosted-sessions
    source_type: official_docs
    relevance: Microsoft Foundry separates sessions from conversations and shows that session state can persist across turns and idle periods in a sandbox.
    key_point: A session can preserve working state across interruptions while conversation history is a separate concern.
---

Persistent sessions are agent sessions that save their state so the work can be picked up later.

In practice, this means the agent can remember the current task, saved files, tool state, or conversation history after a pause, restart, or later visit. Instead of beginning again, it can continue from the same session or from stored session data.

This matters because real tasks do not always finish in one go. A person may stop an agent to check its work, a system may restart, or the task may span many turns. Persistent sessions make that safer and less wasteful.

This is not the same as general memory. Memory is about what the agent knows across tasks or users. A persistent session is about keeping one working session alive long enough to resume it. It also does not guarantee recovery from every crash unless the system was built for that.
