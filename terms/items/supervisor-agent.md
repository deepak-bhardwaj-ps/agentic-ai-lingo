---
slug: supervisor-agent
name: Supervisor Agent
category: Runtime
title: Supervisor Agent
short_description: A supervisor agent is the main agent that assigns tasks to other
  agents, checks their work, and decides what happens next.
aliases: []
status: Common framework pattern
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse: []
related_terms: []
evidence: []
---

## Meaning

A supervisor agent is the main agent in a team of agents. It gives out tasks, checks the replies, and decides whether to keep going, try again, or stop.

## Description

In practice, this means one agent acts like a team lead and other agents act like specialists. The supervisor may ask one agent to research, another to compare options, and another to draft an answer, then it puts the pieces together.

This matters because some jobs are too big for one agent to do well on its own. Splitting the work can make the result better and easier to follow.

A supervisor agent is not the same as a safety rule or a permission system. It should not be the thing that decides on its own whether a risky action is allowed. Important approvals and policy checks should be handled by separate, deterministic systems.

It is also not just any chatbot that forwards a message. The term is used when there is a clear top-level agent coordinating other agents.
