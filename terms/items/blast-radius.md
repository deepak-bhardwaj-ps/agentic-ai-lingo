---
slug: blast-radius
title: Blast Radius
short_description: How much damage a mistake, bug, or security problem could cause
  before it is stopped.
category: Governance
tags: []
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse: []
related_terms: []
evidence: []
---

Blast radius is how much damage a mistake, bug, or security problem could cause before it is stopped.

In practice, it means asking: if one part fails, what else could be affected? That could be one user, one database, one app, or many connected systems.

The term matters because good systems try to keep problems small. If the blast radius is low, a failure is easier to contain and fix. If it is high, one mistake can spread widely.

Blast radius is not the same as the problem itself. It is not a fix, and it is not just a scary-sounding word for “risk”. It is a way to describe how far damage could spread, so teams can design better boundaries and safer controls.
