---
slug: memory-compaction
name: Memory Compaction
category: Memory
title: Memory Compaction
short_description: Memory compaction is shortening stored context so an agent can
  keep working without carrying every detail.
aliases: null
status: active
tags:
- memory
- context-management
- agents
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it like permanent storage instead of a lossy summary.
- Assuming the compacted version keeps every detail exactly as written.
- Using it as a substitute for proper archival records.
related_terms:
- context window
- summarisation
- long-term memory
- retrieval
- checkpointing
evidence:
- source_title: MemGPT
  source_url: https://arxiv.org/abs/2310.08560
  source_type: research_paper
  relevance: Foundational research on managing limited LLM context by moving information
    between active context and external memory.
  key_point: The paper treats context as bounded and uses memory management to preserve
    useful information while trimming what no longer fits.
- source_title: Compaction
  source_url: https://developers.openai.com/api/docs/guides/compaction
  source_type: official_docs
  relevance: Current product documentation showing compaction as a practical context-management
    feature in agent workflows.
  key_point: Compaction reduces context size while preserving the state needed for
    later turns.
- source_title: Memory overview
  source_url: https://docs.langchain.com/oss/python/concepts/memory
  source_type: official_docs
  relevance: Current framework guidance that distinguishes short-term context from
    longer-lived stored memory.
  key_point: Memory systems are used to keep useful information across turns and sessions,
    which is the practical setting where compaction sits.
---

Memory compaction is the process of shrinking stored context so an agent can keep working when there is too much information to keep in full.

In practice, it means older messages, tool results, or notes are turned into a shorter version that keeps the important points and drops some detail. The agent can then continue with less data in its active context.

This matters because AI systems have a limit on how much they can hold at once. Without compaction, a long task can run out of space or become slow and expensive.

Memory compaction is not the same as saving everything forever. It is a shorter working version, not a full archive. If something is important, it still needs to be kept in source records or long-term storage.
