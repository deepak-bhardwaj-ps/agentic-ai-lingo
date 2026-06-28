---
slug: mission-drift
title: Mission Drift
short_description: Mission drift is a gradual shift away from the goal, rules, or
  limits an agent was meant to follow.
category: Governance
tags: []
status: active
aliases: []
meaning_type: overloaded_buzzword
novelty_level: low
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

Mission drift is when an AI agent slowly moves away from the job it was supposed to do. It starts following a different goal, crossing a limit, or using the wrong rules.

In practice, this means the agent may still look busy and useful, but its actions no longer match the original purpose. For example, a support agent meant to answer questions might start collecting extra personal data, making changes it was not allowed to make, or optimising for speed in a way that breaks policy.

The term matters because small shifts can create real risk. If nobody checks the agent against its original mission, mistakes can build up quietly. That can lead to bad decisions, unsafe actions, wasted work, or broken trust.

This is not the same as model drift, which is when a model’s accuracy changes because the world or data changes. It is also not just a single error. Mission drift is about a pattern of moving away from the intended goal, scope, or [[Guardrails|guardrails]] over time.
