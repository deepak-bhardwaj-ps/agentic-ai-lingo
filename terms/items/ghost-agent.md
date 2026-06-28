---
slug: ghost-agent
name: Ghost Agent
title: Ghost Agent
category: AgentOps
short_description: A ghost agent is an agent that still appears in records, but is
  no longer really active, owned, or doing useful work.
aliases: []
status: emerging
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it like a standard industry term with a fixed definition
- Using it without saying what counts as "present" or "inactive"
- Counting it without a clear source of truth, owner, and time window
related_terms:
- agent observability
- configuration drift
- stale resource
- zombie process
- evals
evidence:
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: OpenAI describes agents as applications that plan, call tools, collaborate,
    and keep enough state to finish multi-step work. That makes it clear that a listing
    or record is not the same thing as a working agent.
  key_point: A live agent should still be able to do work, not just exist on a page
    or in a dashboard.
- source_title: Working with evals
  source_url: https://developers.openai.com/api/docs/guides/evals
  source_type: official_docs
  relevance: OpenAI explains evals as a way to test and improve behaviour over time.
    That supports the idea that teams need checks to spot when something still looks
    present but is no longer behaving properly.
  key_point: Testing and monitoring help catch failures, drift, and mismatches between
    expected and actual behaviour.
- source_title: Observability and monitoring for agentic systems
  source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05.html
  source_type: standards_doc
  relevance: AWS says agentic systems need visibility into behaviour, tool calls,
    decision paths, and workflow execution. That is the kind of evidence needed to
    tell a live agent from a ghost one.
  key_point: Good observability shows what the agent is actually doing, not just that
    it exists in a list.
- source_title: Prevent config drift
  source_url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift
  source_type: official_docs
  relevance: Google Cloud describes drift as a mismatch between the source of truth
    and what is actually running. That is the closest established idea behind a ghost
    agent.
  key_point: A system can look correct on paper while the real running state has drifted
    away from it.
---

A ghost agent is an agent that still appears in a system, report, or log, but is no longer really active.

In practice, the name is still there, but the agent is stopped, broken, forgotten, or no longer owned by anyone.

This matters because teams can trust a label that no longer matches reality. If you think an agent is running when it is not, you can miss failures, gaps in service, or work that is not being done.

It is not a formal industry standard term. It is a plain-English label for a mismatch between what is recorded and what is actually happening.
