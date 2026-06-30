---
title: Session capture
short_description: Recording the full set of actions from one agent session so it can be reviewed later.
category: Knowledge and wiki systems
tags:
  - agent-observability
  - tracing
  - replay
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the same thing as a plain chat transcript.
  - Assuming capture means the session can be replayed exactly the same way every time.
  - Using it as a generic name for any log or screenshot.
related_terms:
  - Trace
  - Session replay
  - Observability
  - Audit log
  - Checkpoint
evidence:
  - source_title: Sessions
    source_url: https://langfuse.com/docs/observability/features/sessions
    source_type: official_docs
    relevance: Shows the common agent-observability meaning of a session as grouped traces from one interaction.
    key_point: Langfuse describes sessions as a way to group observations across traces and view a simple replay of the full interaction.
  - source_title: agent-strace
    source_url: https://pypi.org/project/agent-strace/0.32.0/
    source_type: engineering_blog
    relevance: Shows a tool built specifically around full-session capture for agent work, including prompts, tool calls, and replay.
    key_point: The project says it captures the full session and can replay every tool call, prompt, and response.
  - source_title: Use time-travel
    source_url: https://docs.langchain.com/oss/python/langgraph/use-time-travel
    source_type: official_docs
    relevance: Shows the difference between recording a run and replaying it, which helps define what capture is and is not.
    key_point: LangGraph explains that replay re-executes nodes from a checkpoint, and the result may change because calls run again.
  - source_title: Claude Code Tracing with Langfuse
    source_url: https://langfuse.com/integrations/developer-tools/claude-code
    source_type: official_docs
    relevance: Shows that session-level capture commonly includes prompts, tool use, timing, and grouped interactions in real agent tooling.
    key_point: The guide says tracing Claude Code can capture user inputs, assistant responses, tool invocations, and session information.
---

Session capture means recording everything that happens during one agent session so it can be looked at later.

In practice, that can include the user’s prompts, the assistant’s replies, tool calls, file edits, errors, and timing. Some tools also group those records into one session view or let you replay part of the run.

The term matters because agent work often happens in many small steps. If you only keep the final answer, you miss how the result was produced and where things went wrong.

It is not just a chat transcript. It is also not a promise that the session will replay in exactly the same way every time, because tools, data, and models can change.
