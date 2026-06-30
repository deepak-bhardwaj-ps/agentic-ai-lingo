---
slug: episodic-memory
title: Episodic Memory
short_description: Memory for specific events, times, and experiences; in AI, a design
  label for storing and recalling past episodes or interactions.
category: Memory
tags:
  - memory
  - cognition
  - agents
status: established
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating it as the same as semantic memory, which stores facts and concepts rather than specific events.
  - Assuming an AI system has human-like memory just because it stores past interactions.
related_terms:
  - semantic memory
  - working memory
  - long-term memory
  - agent memory
evidence:
  - source_title: Memory | UCSF Memory and Aging Center
    source_url: https://memory.ucsf.edu/brain-health/memory
    source_type: official_docs
    relevance: Clear human-memory reference from a reputable medical centre.
    key_point: Defines episodic memory as memory for recent or past events and experiences, and contrasts it with semantic memory for facts.
  - source_title: Cognitive Architectures for Language Agents
    source_url: https://arxiv.org/abs/2309.02427
    source_type: research_paper
    relevance: Strong AI-agent framing from a widely cited architecture paper.
    key_point: Uses episodic memory for experiences from earlier decision cycles and separates it from semantic memory in language-agent design.
  - source_title: Memory overview
    source_url: https://docs.langchain.com/oss/python/concepts/memory
    source_type: official_docs
    relevance: Current engineering guidance on how the term is used in agent systems.
    key_point: Says episodic memory in AI agents means recalling past events or actions, often to help the agent remember how to complete a task.
---

Episodic memory is memory for specific events, times, and experiences.

In people, it helps you remember things like what you did yesterday, where you parked the car, or a conversation with a friend.

In AI agents, the term is used by analogy. It usually means a stored record of a past interaction, action, or task that can be looked up later and used again.

This matters because agents have limited context. If they only use the current chat, they can lose earlier details. Episodic memory lets them bring back useful past events instead of starting from zero.

It is not the same as general knowledge. General knowledge stores facts, while episodic memory stores particular experiences.

It also does not mean an AI has human memory. In AI, it is a design label for storing and reusing past episodes, not proof of human understanding.
