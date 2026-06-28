---
slug: agent-inventory
title: Agent Inventory
short_description: A live record of the AI agents an organisation uses, who owns them,
  and where they run.
category: AgentOps
tags:
- agentops
- governance
- inventory
- lifecycle
- ai-agents
status: active
aliases:
- AI agent inventory
- agent registry
- agent register
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse:
- A simple list of bots with no owner, version, scope, or status.
- Treating it like a scorecard instead of a control record.
- Mixing approved agents with untracked experiments.
related_terms:
- agent registry
- model inventory
- asset inventory
- governance
- lifecycle management
evidence:
- source_title: NIST AI Risk Management Framework 1.0
  source_url: https://www.nist.gov/itl/ai-risk-management-framework
  source_type: standards_doc
  relevance: Sets the governance expectation that organisations understand and manage
    the AI systems they use.
  key_point: AI risk management depends on knowing what systems exist, what they do,
    and who is responsible for them.
- source_title: NIST AI RMF Playbook
  source_url: https://airc.nist.gov/airmf-resources/playbook/
  source_type: standards_doc
  relevance: Gives practical governance guidance for keeping AI system records current.
  key_point: Organisations should assign responsibility for documenting and maintaining
    AI system inventory details.
- source_title: OpenAI Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Shows that agents are applications, not just models, so they need tracking
    as separate operational assets.
  key_point: Agents can plan work, call tools, and keep state to finish a task.
- source_title: Agent Registry overview
  source_url: https://docs.cloud.google.com/agent-registry/overview
  source_type: official_docs
  relevance: Demonstrates the product pattern of a central catalog for AI agents and
    related tools.
  key_point: A unified catalog helps organisations store, discover, and govern AI
    agents across the business.
- source_title: Model inventory management - Build a Secure Enterprise Machine Learning
    Platform on AWS
  source_url: https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/model-inventory-management.html
  source_type: official_docs
  relevance: Provides a close governance parallel for versioning, ownership, lineage,
    and auditability.
  key_point: Production AI assets should be registered, versioned, and traceable so
    they can be audited and managed safely.
---

## Meaning

An agent inventory is a live record of the AI agents an organisation uses.

It usually lists the agent’s name, purpose, owner, version, where it runs, what tools it can use, and whether it is live, paused, or retired.

In practice, it works like a control list. It helps teams answer simple questions fast: What agents do we have? Who is responsible for each one? Which ones are approved? Which ones should be turned off?

It matters because agents can be copied, changed, and deployed quietly. If no one keeps track, an organisation can lose sight of what an agent is doing, which systems depend on it, and what risk it creates.

It is not just a list of bot names. It is not a scorecard, and it is not a general company dashboard. A useful inventory must stay current, show ownership clearly, and record changes over time.
