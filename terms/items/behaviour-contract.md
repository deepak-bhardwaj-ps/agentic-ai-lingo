---
slug: behaviour-contract
name: Behaviour Contract
category: Governance
title: Behaviour Contract
aliases:
- Behavior Contract
short_description: A behaviour contract is a clear written description of what an
  agent is allowed to do, what it must do, and when a person must step in.
tags:
- governance
- agent-safety
- policy
- accountability
status: draft
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating a nice-sounding document as if it actually controls the agent
- Confusing a behaviour contract with a prompt or system message
- Leaving out who is responsible, what is allowed, and how the rules are checked
related_terms:
- autonomy-boundary
- policy
- guardrail
- audit-log
- human-escalation
- acceptance-criteria
evidence:
- source_title: OWASP LLM Top 10
  source_url: https://genai.owasp.org/llm-top-10/
  source_type: official_docs
  relevance: This is the closest security reference for defining boundaries, controls,
    and oversight for AI systems.
  key_point: OWASP treats AI risk as something that needs explicit controls, not just
    good intentions or prompts.
- source_title: NIST AI Risk Management Framework
  source_url: https://www.nist.gov/itl/ai-risk-management-framework
  source_type: standards_doc
  relevance: Supports the idea that AI behaviour should be governed through documented
    risk controls, accountability, and monitoring.
  key_point: NIST says AI risks should be managed with governance, mapped responsibilities,
    and ongoing oversight.
- source_title: AI RMF Playbook
  source_url: https://airc.nist.gov/docs/AI_RMF_Playbook.pdf
  source_type: standards_doc
  relevance: Shows how governance needs to be turned into practical controls, evidence,
    and review.
  key_point: NIST connects governance to documentation, auditability, and human review
    of AI decisions.
- source_title: Anthropic - Writing effective tools for agents
  source_url: https://www.anthropic.com/engineering/writing-tools-for-agents
  source_type: engineering_blog
  relevance: Shows that agent behaviour depends on tools, instructions, and constraints,
    not just one prompt.
  key_point: Effective agents need clear tool design and constraints so they behave
    reliably in real tasks.
---

A behaviour contract is a clear written rulebook for an AI agent or helper. It says what the agent may do, what it must do, and when it must ask a person for help.

In practice, it describes the agent’s job in plain words. It can include limits, required checks, safety rules, and what counts as success. A good behaviour contract is more than a prompt. It should also be backed by code, tests, policies, and records that show whether the agent followed the rules.

It matters because AI agents can take actions, not just give answers. If the rules are unclear, the agent may do the wrong thing, go too far, or act without enough human oversight. A behaviour contract helps people set boundaries and check whether the agent stayed inside them.

It is not a magic shield. A document by itself does not control an agent. It is also not just a fancy name for a prompt. If a behaviour contract cannot be checked or enforced, it is only a promise on paper.
