---
slug: agent-memory
title: Agent Memory
short_description: Information kept outside the model so an agent can remember useful
  facts, preferences, and past steps across turns or sessions.
category: Memory
tags: []
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

Agent memory is information kept outside the model so an agent can remember useful things later.

In practice, it is a separate place where the system saves selected facts, preferences, instructions, or past steps. When the agent needs them again, the system looks up the useful parts and gives them back to the model.

This matters because a model can only read a limited amount of text at once. Memory helps an agent stay consistent across turns and sessions, and reduces the chance that it forgets important details.

Agent memory is not the model secretly learning forever. It is also not a full copy of every message. Good memory is selective, has a purpose, and can be updated or removed when it is wrong.
