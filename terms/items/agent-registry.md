---
title: Agent Registry
short_description: A central catalogue of AI agents that helps people and systems find,
  organise, and govern them.
category: Protocols
tags:
- ai-agents
- governance
- registry
- discovery
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it as a security approval system.
- Treating it as a full control plane or runtime.
- Using it as a static list that does not get updated.
related_terms:
- Agent Inventory
- Agent Estate
- Agent Control Plane
- Agent Lifecycle Management
- Governance
evidence:
- source_title: Agent Registry overview | Google Cloud Documentation
  source_url: https://docs.cloud.google.com/agent-registry/overview
  source_type: official_docs
  relevance: Defines the term directly in a current cloud product and shows the core registry pattern.
  key_point: Google describes Agent Registry as a centralised catalogue for storing, discovering, and governing AI agents, MCP servers, and tools.
- source_title: Manage agent registry in Microsoft 365 admin center
  source_url: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide
  source_type: official_docs
  relevance: Shows the registry used as an organisation-wide admin surface, not just a lookup list.
  key_point: Microsoft presents Agent Registry as a central place to manage, govern, pin, and audit agents across an organisation.
- source_title: AWS Agent Registry: Discover and manage agents, tools, and resources
  source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html
  source_type: official_docs
  relevance: Confirms the same pattern in another major platform and clarifies what kinds of things can be registered.
  key_point: AWS describes an agent registry as a searchable catalogue for agents, tools, skills, and custom resources with approval workflows and access control.
- source_title: AI Risk Management Framework 1.0
  source_url: https://www.nist.gov/itl/ai-risk-management-framework
  source_type: standards_doc
  relevance: Explains why inventories and records matter for AI governance even when the exact product term differs.
  key_point: NIST says organisations need mechanisms to inventory AI systems so they can manage risk, responsibility, and lifecycle changes.
---

An agent registry is a central list of AI agents and related things such as tools or endpoints.

It usually stores details like the agent’s name, purpose, owner, version, and how it can be found or used. In some systems, it also includes approval status and access rules.

In practice, it works like a shared address book for software agents. It helps people and systems discover what agents exist, keep the records up to date, and manage them in one place.

This matters because organisations can end up with many agents quickly. A registry makes it easier to find them, avoid duplication, and keep track of which ones are still meant to be used.

An agent registry is not the same as a security approval process, and it is not the agent itself. Being listed does not mean the agent is safe, correct, or allowed to act.
