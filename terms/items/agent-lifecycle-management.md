---
title: Agent Lifecycle Management
short_description: Managing an AI agent from approval and launch through updates,
  monitoring, suspension, and retirement.
category: AgentOps
tags:
- AgentOps
- governance
- lifecycle
- operations
status: active
aliases:
- Agent identity lifecycle management
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it like a single dashboard metric instead of an operating practice.
- Counting agents without clear rules for approval, ownership, and retirement.
- Mixing up lifecycle management with evaluation or monitoring alone.
related_terms:
- agent identity
- governance
- evaluation
- monitoring
- retirement
evidence:
- source_title: AI Risk Management Framework (AI RMF)
  source_url: https://www.nist.gov/itl/ai-risk-management-framework
  source_type: official_docs
  relevance: NIST describes AI risk management across design, development, deployment,
    evaluation, and use.
  key_point: Responsible AI work covers the whole life of a system, not just launch
    day.
- source_title: AI RMF Core and Manage function
  source_url: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
  source_type: official_docs
  relevance: NIST’s AI RMF Core and Manage function emphasise ongoing tracking and
    post-deployment monitoring.
  key_point: Risk management continues after launch and includes monitoring over the
    system’s life.
- source_title: Manage AI agents across your organisation
  source_url: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/integrate-manage-operate
  source_type: official_docs
  relevance: Microsoft describes managing AI agents from deployment to retirement
    as part of operations.
  key_point: Agent management includes ongoing operation and retirement, not just
    building and launching.
- source_title: Agent lifecycle and deployment processes
  source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03.html
  source_type: official_docs
  relevance: AWS says agent lifecycle management includes behavioural change, capability
    updates, and operational governance.
  key_point: Agents need ongoing control as their behaviour, tools, and environment
    change.
- source_title: What are agent identities?
  source_url: https://learn.microsoft.com/en-us/entra/agent-id/what-are-agent-identities
  source_type: official_docs
  relevance: Shows that agents can have identities that are created, managed, and
    governed.
  key_point: If agents have managed identities, they also need clear ownership and
    retirement rules.
---

Agent lifecycle management is the work of looking after an AI agent from the day it is approved until the day it is retired.

In practice, it means deciding who owns the agent, what it is allowed to do, how it is tested, how it is checked after launch, when it is changed, and when it should be paused or shut down.

This matters because an agent can change over time, pick up new tools, make mistakes, or become out of date. It needs ongoing control, not just one approval at the start.

It is not just a dashboard, a score, or a single test. It is also not the same as evaluation alone. Evaluation checks how well an agent works; lifecycle management covers the whole journey from start to finish.
