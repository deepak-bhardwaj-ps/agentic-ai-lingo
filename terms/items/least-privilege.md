---
slug: least-privilege
title: Least Privilege
short_description: Giving an agent only the access it needs for the task at hand.
category: Governance
tags:
- security
- governance
- access-control
- agent-safety
status: established
aliases:
- least privilege
- principle of least privilege
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
- Assuming prompt instructions alone can enforce access limits
- Giving an agent broad credentials "just in case"
- Treating it as a model behaviour issue instead of a system design control
related_terms:
- zero trust
- role-based access control
- scoped credentials
- short-lived tokens
- permission boundaries
evidence:
- source_title: OWASP LLM01:2025 Prompt Injection
  source_url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
  source_type: official_docs
  relevance: Shows least privilege as a recommended mitigation for agent and tool
    abuse.
  key_point: OWASP advises restricting the model's access privileges to the minimum
    necessary for its intended operations.
- source_title: NIST SP 800-207, Zero Trust Architecture
  source_url: https://csrc.nist.gov/pubs/sp/800/207/final
  source_type: official_docs
  relevance: Gives the core security principle behind least-privilege access decisions.
  key_point: Zero trust is built around accurate, least-privilege per-request access
    decisions.
- source_title: CISA Zero Trust Maturity Model
  source_url: https://www.cisa.gov/zero-trust-maturity-model
  source_type: official_docs
  relevance: Confirms least privilege as a practical control in modern security programmes.
  key_point: CISA describes zero trust as aiming to minimise uncertainty through precise,
    least-privilege access decisions.
---

Least privilege means giving an agent only the access it needs to do the job, and nothing more.

In practice, that means the agent should use the smallest set of permissions, data, tools, and credentials needed for the current task. If it only needs to read one folder, it should not be able to write to everything else. If it only needs to send one request, it should not also be able to delete records or change settings.

This matters because agents can make mistakes, get tricked, or be misused. If their access is limited, the damage they can cause is also limited.

It is not something you fix by writing a better prompt. It is a security control that has to be built into accounts, tokens, permissions, and tool access.
