---
slug: agent-loop
title: Agent Loop
short_description: A repeating cycle where an AI system does something, checks the
  result, and decides the next step.
category: Runtime
tags: []
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse: []
related_terms: []
evidence: []
---

An agent loop is a repeating cycle where an AI system does a step, checks what happened, and then decides what to do next.

In practice, the system may plan, use a tool, read the result, adjust its next move, and repeat this until it reaches a stopping point. The result of one step becomes the input for the next step.

This matters because many jobs cannot be finished well in one reply. Looking things up, comparing choices, fixing mistakes, and checking work often need several rounds.

It is not the same as a normal chat response. It is also not automatically safe or correct. A good agent loop still needs limits, such as when to stop, how much it may do, and what happens if it keeps making the same mistake.
