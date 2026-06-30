---
title: Server-side compaction
short_description: A server-managed way to shorten conversation state so an agent can keep going when its context gets too large.
category: Agentic patterns
tags:
  - context-management
  - agents
  - memory
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it like permanent memory instead of a lossy shortening step.
  - Assuming it keeps every detail exactly as written.
  - Confusing it with client-side summarisation or manual prompt trimming.
related_terms:
  - memory-compaction
  - context window
  - conversation state
  - summarisation
evidence:
  - source_title: Compaction
    source_url: https://developers.openai.com/api/docs/guides/compaction
    source_type: official_docs
    relevance: OpenAI's current API guide describes server-side compaction as a built-in way to reduce context size during long-running conversations.
    key_point: When the rendered token count crosses a threshold, the server runs compaction so the conversation can continue without a separate manual compaction call.
  - source_title: Compact a response
    source_url: https://developers.openai.com/api/reference/resources/responses/methods/compact/
    source_type: official_docs
    relevance: Confirms that compaction is an API-level operation for long conversations, not just an application-side summarisation pattern.
    key_point: The endpoint returns a compacted response object for continuing a conversation with reduced context.
  - source_title: Context windows
    source_url: https://docs.anthropic.com/en/docs/build-with-claude/context-windows
    source_type: official_docs
    relevance: Anthropic also uses the term for server-side context summarisation when conversations approach the window limit, which shows the term maps to a real provider feature.
    key_point: Compaction automatically summarises earlier parts of the conversation on the server so the conversation can continue past the limit.
---

Server-side compaction is when the system shortens a conversation for you on the server so the agent can keep working as the context gets too large.

In practice, the service keeps the important parts of the conversation and removes some of the older detail. The next turn can then use the shorter version instead of the full history.

It matters because long agent runs can run out of room, get slower, or become more expensive if every message is kept in full. Compaction helps the run continue without you having to manually cut the conversation down.

It is not the same as permanent memory. It is also not the same as a full archive of everything that happened. It is a shortened working version, and some detail is lost.
