---
slug: react
title: ReAct
short_description: ReAct is a way for an AI system to think, take an action, then
  use what it learned to keep going.
category: Runtime
tags: []
status: established
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse: []
related_terms: []
evidence: []
---

ReAct is a pattern for an AI system to think, do something, see the result, and then think again.

In practice, the system writes down a short reasoning step, chooses an action such as a tool call, reads the result, and uses that result to decide the next step. This is useful when one answer is not enough and the system needs to work through a task step by step.

The term matters because it shows one common way to build agents that use tools. It can make the system easier to follow than a single hidden guess, and it can help with tasks that need outside information.

It is not the same as React, the JavaScript library. It is also not a promise that the AI will always be right, or that every action is safe. It is only a way of organising the loop between thinking and acting.
