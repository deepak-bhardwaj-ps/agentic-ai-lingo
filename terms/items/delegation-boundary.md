---
slug: delegation-boundary
name: Delegation Boundary
title: Delegation Boundary
short_description: The point where one person or system is allowed to act for another,
  with clear limits.
category: Governance
tags:
- governance
- security
- agentic-ai
- delegation
- permissions
status: draft
aliases:
- authority boundary
- permission boundary
meaning_type: novel
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating a name as proof that the boundary is actually enforced.
- Confusing delegation with full ownership.
- Leaving out limits, expiry, audit logs, or the person who can stop the action.
related_terms:
- least privilege
- human oversight
- roles and responsibilities
- permission scope
- audit trail
evidence:
- source_title: OWASP Top 10 for Large Language Model Applications
  source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
  source_type: standards_doc
  relevance: High-level security guidance for AI systems that act on external input
    and can trigger downstream actions.
  key_point: LLM and agent risks depend on what they can be trusted to do, which makes
    boundaries, controls, and oversight central.
- source_title: Artificial Intelligence Risk Management Framework (AI RMF 1.0)
  source_url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
  source_type: standards_doc
  relevance: Defines how organisations should assign roles, responsibilities, and
    oversight for AI systems.
  key_point: NIST says policies should define and differentiate roles and responsibilities
    for human-AI configurations and oversight.
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Shows that production agents rely on application-owned orchestration,
    tool execution, approvals, and state.
  key_point: Agent systems need explicit control over orchestration, tools, approvals,
    and state rather than letting the model do everything by itself.
- source_title: New tools for building agents
  source_url: https://openai.com/index/new-tools-for-building-agents/
  source_type: official_docs
  relevance: Explains that agents are systems that act on behalf of users and need
    built-in tooling and tracing.
  key_point: Agentic systems are designed to complete tasks for users, which makes
    it important to separate what the model can suggest from what it is allowed to
    do.
---

## Term status

Governance and security concept.

## Meaning

A delegation boundary is the line where one person or system is allowed to act for another, but only within clear limits.

In practice, it says:
who is acting,
what they are allowed to do,
how far that permission goes,
how long it lasts,
and who can take it back.

## Why it matters

When an agent can send messages, change files, call tools, or start workflows, it can cause real effects. A delegation boundary keeps that power controlled and visible.

Without one, an agent may do things it should not do, or nobody may be able to prove who approved the action.

## What it is not

It is not just a label.

It is not the same as ownership.

It is not safe just because a system says it has a boundary.

If there is no clear permission, no enforcement, no log, and no way to stop the action, then there is no real boundary.

## In practice

A good delegation boundary usually includes:
the original person or system,
the allowed task,
the exact limits,
when the permission ends,
what gets recorded,
and how the permission is revoked.

Example: a student can ask an agent to draft an email, but not send it unless a teacher approves it.
