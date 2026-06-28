---
slug: agent-estate
name: Agent Estate
category: AgentOps
title: Agent Estate
aliases:
- agent fleet
short_description: The full live set of AI agents an organisation runs, plus the people,
  rules, tools, permissions, and controls around them.
status: active
tags:
- agentops
- governance
- inventory
- lifecycle
- risk
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it as just a count of agents.
- Treating it as a static spreadsheet instead of a live operational view.
- Mixing it up with an agent portfolio, which is about funding and strategy rather
  than day-to-day control.
related_terms:
- Agent Inventory
- Agent Registry
- Agent Portfolio
- Agent Lifecycle Management
- Agent Ownership Model
- Agent Sprawl
- Control Plane
evidence:
- source_title: Manage agent registry in Microsoft 365 admin center
  source_url: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
  source_type: official_docs
  relevance: Shows that organisations need a central inventory for viewing and governing
    agents.
  key_point: Microsoft describes an agent registry as a central place to monitor,
    manage, and govern agents across the organisation.
- source_title: Governance and Lifecycle actions for agents available in Microsoft
    365 admin center
  source_url: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-actions?view=o365-worldwide
  source_type: official_docs
  relevance: Shows that agent management includes visibility, access, distribution,
    and retirement.
  key_point: Microsoft frames agent governance as lifecycle management, not just listing
    agents.
- source_title: Overview of Microsoft Agent 365
  source_url: https://learn.microsoft.com/en-us/microsoft-agent-365/overview
  source_type: official_docs
  relevance: Shows the shift towards a single operational view of all agents.
  key_point: Microsoft says admins can view all agents in one central registry with
    adoption, activity, and health signals.
- source_title: Introducing OpenAI Frontier
  source_url: https://openai.com/index/introducing-openai-frontier/
  source_type: official_docs
  relevance: Shows enterprise agent platforms are built around shared context, permissions,
    and boundaries.
  key_point: OpenAI describes a platform for building, deploying, and managing agents
    with clear permissions and boundaries.
- source_title: Agent Identity overview
  source_url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview
  source_type: official_docs
  relevance: Shows that agents need their own identity and access controls.
  key_point: Google says the agent itself can be the principal, with permissions granted
    directly to that identity.
---

An agent estate is the full live set of AI agents an organisation runs, plus the rules and controls around them.

In practice, that includes the agents themselves, their instructions, tools, permissions, identities, owners, data access, and retirement rules. It is not just a list. It is a working view of what exists and what each agent is allowed to do.

This matters because agents can act on behalf of people. They may read data, call systems, or change records. If an organisation does not keep track of them properly, it can lose control, create duplicates, or leave old agents active when they should have been removed.

An agent estate is not the same as an [[Agent Portfolio|agent portfolio]]. A portfolio is about which agents to fund, build, or keep. An estate is about controlling the agents that already exist.
