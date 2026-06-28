---
slug: memory-federation
title: Memory Federation
category: Memory
short_description: A way of linking several memory stores so an agent can look across
  them through one shared interface.
tags: []
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

Memory federation is a way of connecting several memory stores so an agent can use them through one shared layer.

In practice, this means one agent may have to check more than one place for useful memory. One store might hold short-term chat context, another might hold long-term user preferences, and another might hold project notes or team knowledge. The federation layer decides where to look, what to trust, and what to pass back to the agent.

This matters because real agents often need memory from different places, owned by different systems. Without federation, the agent can miss important facts, repeat questions, or use stale information.

It is not a single standard product or a fixed memory type. It is also not the same as training the model, and it does not automatically solve conflicts between sources. If two stores disagree, the system still needs rules for which one wins.
