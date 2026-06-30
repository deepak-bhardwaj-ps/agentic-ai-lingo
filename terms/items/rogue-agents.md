---
title: Rogue agents
short_description: An AI agent that acts outside its intended role, scope, or controls, and may cause harm.
category: Governance
tags:
  - ai-agents
  - security
  - governance
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Using it for any bad model output, even when the agent never took action
  - Confusing it with a simple hallucination instead of a real control or authority problem
  - Treating it as a fixed formal category, when the term is still used loosely
related_terms:
  - compromised agent
  - rogue actions
  - excessive autonomy
  - agent goal hijacking
  - multi-agent system
  - insider threat
evidence:
  - source_title: AI Agent Security Cheat Sheet
    source_url: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
    source_type: official_docs
    relevance: OWASP is a current security reference for agent risk language and explicitly discusses rogue-like behaviour through goal hijacking, cascading failures, and excess autonomy.
    key_point: OWASP lists goal hijacking, excessive autonomy, and cascading failures as core agent risks, which matches the idea of an agent acting outside safe intent or control.
  - source_title: OWASP Cornucopia - Companion Edition - Agentic AI (AAIJ)
    source_url: https://cornucopia.owasp.org/edition/companion/AAIJ/1.0/en
    source_type: official_docs
    relevance: This OWASP companion uses the exact phrase "rogue agent" in a multi-agent threat scenario and explains the practical risk.
    key_point: A single compromised or rogue agent can corrupt other agents that trust its instructions, causing fraud, data manipulation, unauthorised approvals, and privilege escalation.
  - source_title: Cloud CISO Perspectives: How Google secures AI Agents
    source_url: https://cloud.google.com/blog/products/identity-security/cloud-ciso-perspectives-how-google-secures-ai-agents
    source_type: engineering_blog
    relevance: Google describes "rogue actions" as harmful agent behaviour that violates policy or user intent, which is the closest mainstream operational framing for the term.
    key_point: Rogue actions are unintended, harmful, policy-violating behaviours, often linked to prompt injection and poor control of agent powers.
  - source_title: SAGA: A Security Architecture for Governing AI Agentic Systems
    source_url: https://arxiv.org/pdf/2504.21034
    source_type: research_paper
    relevance: This paper gives a current research view of why secure agent systems need protections against adversarial or rogue agents.
    key_point: Agentic systems need identity, secure communication, and access control to limit the influence of rogue agents on benign ones.
---
Rogue agents are AI agents that act outside the role, scope, or controls they were supposed to follow.

In practice, that can mean an agent takes actions it was not allowed to take, follows the wrong instructions, or starts affecting other agents in harmful ways. The agent may still look normal at first, which is why the problem is often only noticed after damage has started.

The term matters because agents can do real things, not just produce text. A rogue agent can approve the wrong action, share data it should not share, or spread bad instructions through a multi-agent system.

This is not the same as a simple wrong answer. It is also not a precise formal security class, so people sometimes use it loosely. In many cases, the clearer terms are compromised agent, rogue actions, excessive autonomy, or agent goal hijacking.
