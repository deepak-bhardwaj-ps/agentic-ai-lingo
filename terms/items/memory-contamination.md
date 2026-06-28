---
title: Memory Contamination
short_description: Memory contamination is when a system stores, retrieves, or reuses
  bad memory so later decisions are based on false or irrelevant information.
category: Memory
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

Memory contamination is when an AI agent keeps the wrong memory and later uses it as if it were true.

In practice, this can happen when the agent stores a false fact, keeps an old fact after it has changed, or retrieves the wrong item from its memory store. It can also happen when someone deliberately inserts a bad memory entry so the agent behaves badly later.

This matters because memory is supposed to help the agent stay consistent over time. If the memory is contaminated, the agent may repeat mistakes, follow outdated instructions, or make decisions based on information that was never correct.

It is not the same as a model being trained on bad data. It is also not every case of a wrong answer. The term is about stored or retrieved state inside the agent, and the fix is usually better memory controls: clear sources, stricter write rules, safer retrieval, and ways to correct or delete bad entries.
