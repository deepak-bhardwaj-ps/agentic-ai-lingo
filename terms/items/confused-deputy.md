---
slug: confused-deputy
name: Confused Deputy
title: Confused Deputy
category: Governance
short_description: A confused deputy is a trusted system tricked into using its own
  permissions for the wrong person.
tags:
- security
- governance
- access-control
status: established
aliases:
- delegated authority misuse
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Calling it an AI hallucination instead of an access-control failure
- Thinking the fix is better wording rather than stronger permission checks
related_terms:
- prompt injection
- excessive agency
- access control
evidence:
- source_title: The Confused Deputy
  source_url: https://www.cs.umd.edu/~jkatz/security/downloads/capabilities.html
  source_type: research_paper
  relevance: Original explanation of the term and the authority-mixing failure it
    describes.
  key_point: A program can be tricked into using authority from the wrong source,
    which is why it becomes a confused deputy.
- source_title: The confused deputy problem - AWS Identity and Access Management
  source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html
  source_type: official_docs
  relevance: Clear modern security explanation and mitigation patterns used in real
    systems.
  key_point: An entity without permission can coerce a more-privileged entity to perform
    an action on its behalf.
- source_title: LLM06:2025 Excessive Agency
  source_url: https://genai.owasp.org/llmrisk/llm06-sensitive-information-disclosure/
  source_type: standards_doc
  relevance: Shows how the term is applied in agentic AI security discussions.
  key_point: Agent systems can be given actions and tools that make authority leakage
    and misuse a practical risk.
---

A confused deputy is a trusted system that gets tricked into using its own permissions for the wrong person.

In practice, this happens when a program, service, or agent is allowed to do something useful, but an untrusted request makes it do that thing on the attacker’s behalf. The trusted part is not “broken” in the usual sense. It is using the right permission in the wrong context.

This matters because the damage can look like a normal authorised action. If the system cannot tell who really asked for the action, it may write, send, delete, or read something it should not.

It is not the same as a hallucination. A hallucination is a wrong answer. A confused deputy is a security problem about authority and trust.
