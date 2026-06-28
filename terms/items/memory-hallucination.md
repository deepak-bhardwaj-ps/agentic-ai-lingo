---
title: Memory Hallucination
short_description: A memory failure where an agent stores, recalls, or uses the wrong
  information.
category: Memory
tags: []
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

Memory hallucination is when an AI agent gets the wrong memory and then acts on it.

It can happen when the agent stores something false, pulls back the wrong detail, or uses an old fact that no longer fits. In practice, that means the agent may remember the wrong name, repeat an outdated instruction, or make a decision based on a memory that should have been removed.

This matters because memory is supposed to help an agent stay consistent over time. If the memory is wrong, the agent can stay confidently wrong for longer than if it had no memory at all.

It is not the same as a normal hallucination, where the model makes up an answer in the moment. It is also not a fixed technical standard. People use the term loosely, so it should be defined clearly in each project.
