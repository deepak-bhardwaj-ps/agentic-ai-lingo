---
title: Workflow Runtime
short_description: The software layer that runs a workflow step by step and keeps
  it going across failures or pauses.
category: Runtime
tags: []
status: active
aliases: []
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

A workflow runtime is the software that carries out a workflow one step at a time.

In practice, it decides what happens next, keeps track of what has already happened, and helps the work continue if something fails or has to pause. It may retry steps, wait for approval, save state, and stop when the job is finished.

This matters because many real jobs are longer than a single model response or API call. If a task has several steps, the runtime is what keeps those steps in order and makes the process reliable.

It is not the workflow plan itself. The plan is the set of steps; the runtime is the part that runs them.

It is also not a precise standard term. Different teams may use it to mean a workflow engine, an orchestration layer, or the durable execution system underneath an agent.
