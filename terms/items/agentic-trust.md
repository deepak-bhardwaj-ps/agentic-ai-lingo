---
title: Agentic Trust
short_description: The amount of freedom a person or organisation gives an AI agent
  to act on its own before its actions must be checked or approved.
category: Core
tags:
- agentic-ai
- trust
- governance
- approvals
- permissions
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a general feeling of confidence instead of a decision about action limits
- Using it to mean the same thing as full autonomy
- Assuming trust is enough without permissions, logging, or human review
related_terms:
- autonomy boundaries
- human oversight
- permission gates
- action governance
- delegated authority
evidence:
- source_title: Secure autonomous agentic AI systems
  source_url: https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems
  source_type: official_docs
  relevance: Shows that agent systems need permissions, boundaries, and human approval for risky actions, which is the practical basis for deciding how much trust to place in an agent.
  key_point: Microsoft says agents should operate within defined intent, permissions, and boundaries, and that high-risk actions require deterministic human approval.
- source_title: Human oversight protection and agent containment
  source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07.html
  source_type: standards_doc
  relevance: Explains that human oversight only works when people can review and stop agent actions, which helps define trust as a control problem rather than a feeling.
  key_point: AWS says human oversight must be effective and that agents should be detected and contained if they drift outside their intended behaviour.
- source_title: A practical guide to building agents
  source_url: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
  source_type: official_docs
  relevance: Supports the idea that agent builders must choose where to place tool use, approvals, and guardrails, which directly affects how much autonomy an agent gets.
  key_point: OpenAI frames agent design around tool design, guardrails, and the level of control needed for the task.
- source_title: OWASP Top 10 for Large Language Model Applications
  source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
  source_type: standards_doc
  relevance: Grounds the term in known security risks around excessive agency, permissions, and weak oversight in agent-connected systems.
  key_point: OWASP treats excessive autonomy and excessive permissions as security risks that must be managed with clear controls.
---

Agentic trust is the amount of freedom you give an AI agent to act on its own before a person checks or approves what it does.

In practice, it means deciding whether the agent can finish a task by itself or must ask first. A low-risk job, like sorting messages, may allow more freedom. A high-risk job, like moving money, changing code, or editing shared settings, needs tighter limits and human approval.

This matters because an agent does more than answer questions. It can take actions. So agentic trust is not just a feeling. It is a safety decision about permissions, monitoring, and stopping the agent if something goes wrong.

It is not the same as liking the system. It is not a general score that says an AI is good or bad. It is not a promise that the agent will always make the right choice. It is the practical limit on how much the agent is trusted to act without a person stepping in.
