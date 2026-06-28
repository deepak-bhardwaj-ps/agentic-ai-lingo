---
slug: safety-monitor
name: Safety Monitor
category: Runtime
title: Safety Monitor
short_description: A safety monitor is a check that watches an agent's actions and
  stops or flags unsafe behaviour.
aliases: []
status: active
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse: []
related_terms: []
evidence: []
---

A safety monitor is a check that watches an agent's actions and looks for unsafe behaviour.

In practice, it may flag a risky plan, stop a tool call, alert a person, or log an incident for review. It can sit beside other controls such as rules, permission limits, content filters, and human approval.

The term matters because agents can act on their own, use tools, and cause real-world harm if they go off track. A safety monitor helps catch problems early instead of finding them after damage has already happened.

It is not the same as being safe. A system can call itself a safety monitor and still miss bad actions, be easy to bypass, or do nothing useful. It is also not the whole safety plan. Real safety needs clear rules, testing, access limits, and a response process.
