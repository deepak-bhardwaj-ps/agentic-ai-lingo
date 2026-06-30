---
title: Defensive security agent
short_description: An AI agent that helps defenders find, triage, and respond to security issues.
category: Industry verticals
tags: [cybersecurity, security-operations, agents]
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a fully autonomous replacement for a security team
  - Using it as a vague label for any AI feature in a security product
  - Confusing it with offensive security agents that try to break systems
related_terms:
  - cybersecurity agent
  - security operations agent
  - offensive security agent
  - guardrails
  - agentic security
evidence:
  - source_title: How Google Does It: Building AI agents for cybersecurity and defense
    source_url: https://cloud.google.com/transform/how-google-does-it-building-ai-agents-cybersecurity-defense
    source_type: engineering_blog
    relevance: Google uses the language of AI agents for cybersecurity and defence, which is a close current match for the term.
    key_point: Defensive security agents help defenders identify issues, reason through them, and take actions with tools.
  - source_title: Microsoft Security Copilot agents overview
    source_url: https://learn.microsoft.com/en-us/copilot/security/agents-overview
    source_type: official_docs
    relevance: Microsoft documents security agents that automate repetitive security and IT work across threat detection, triage, and response.
    key_point: Security agents are built to reduce manual workload for defenders, not to replace security judgement.
  - source_title: Technical Blog: Strengthening AI Agent Hijacking Evaluations
    source_url: https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations
    source_type: standards_doc
    relevance: NIST frames agentic systems as software that can automate tasks on behalf of users, which explains why defender-facing agents still need controls.
    key_point: Security agents can act autonomously enough to need careful limits, approvals, and monitoring.
  - source_title: Building AI defenses at scale: Before the threats emerge
    source_url: https://aws.amazon.com/blogs/security/building-ai-defenses-at-scale-before-the-threats-emerge/
    source_type: engineering_blog
    relevance: AWS describes security agents as autonomous systems used to tackle security work at scale, which supports the defender-focused meaning.
    key_point: Defensive agents are used to discover, validate, and report security problems across many tasks.
---

A defensive security agent is an AI agent that helps protect systems by doing security work for defenders.

In practice, it can sort alerts, review suspicious messages, look for weaknesses, gather evidence, and suggest or carry out safe response steps. Some versions only assist a human analyst. Others can take limited actions on their own, but they still need clear rules and checks.

The term matters because security teams often face too many alerts and too much repetitive work for people to handle quickly by hand. A defensive security agent can help them react faster and spend more time on hard decisions.

It is not the same as an offensive security agent, which tries to attack or break systems. It is also not a guarantee of safety. If the agent has too much access or weak checks, it can make mistakes or be misused.
