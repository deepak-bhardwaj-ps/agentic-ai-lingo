---
title: Identity and privilege abuse
short_description: An attack where an AI agent gets more identity, access, or permission than it should have.
category: Governance
tags:
  - agentic-ai
  - security
  - identity
  - access-control
  - least-privilege
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a normal login problem instead of a failure in how agent permissions are granted and used
  - Using it to mean any identity issue, even when the agent did not gain extra access or misuse a privileged identity
  - Confusing it with goal hijacking, which changes what the agent is trying to do rather than what it is allowed to access
related_terms:
  - least privilege
  - authorization
  - privilege escalation
  - agent identity
  - tool abuse
  - access control
evidence:
  - source_title: OWASP Top 10 for Agentic Applications for 2026
    source_url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
    source_type: standards_doc
    relevance: OWASP formally names Identity & Privilege Abuse as one of the main risks for agentic systems, so this is the clearest current industry anchor for the term.
    key_point: Agentic systems can be harmed when an attacker abuses identity or privilege so the agent can act with more authority than intended.
  - source_title: AI Agent Security Cheat Sheet
    source_url: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
    source_type: standards_doc
    relevance: This cheat sheet explains the nearby security failure mode in plain operational terms and shows how privilege problems appear in agent workflows.
    key_point: Low-trust sessions must not reach privileged tools, credentials, or admin actions, even if the model confidently asks for them.
  - source_title: Security considerations for data in generative AI
    source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-considerations-gen-ai/security.html
    source_type: official_docs
    relevance: AWS describes why agentic systems need granular identity and access management to stop unauthorised actions, privilege escalation, and lateral movement.
    key_point: Each agent or sub-agent should have only the permissions needed for its task, with strong traceability and auditability.
  - source_title: Meet your new AI coding teammate: Gemini CLI GitHub Actions
    source_url: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-github-actions/
    source_type: engineering_blog
    relevance: Google gives a concrete example of agent security using a custom identity and least privilege, which helps show how identity abuse is prevented in practice.
    key_point: Agents should be given only the precise permissions they need, with controls that limit what commands and actions they can perform.
---
Identity and privilege abuse is when an AI agent uses the wrong identity, or gets more permission than it should have, so it can do things it was never meant to do.

In practice, this can happen when an agent is given a service account, token, or tool permission that is too broad, reused across too many tasks, or not checked carefully enough. It can also happen when a lower-trust agent finds a way to reach higher-trust tools, data, or admin actions.

This matters because agents can act quickly and at scale. If their identity or permissions are abused, they may read private data, change systems, send messages, or make purchases without proper approval.

It is not the same as goal hijacking. Goal hijacking changes what the agent is trying to achieve. Identity and privilege abuse changes what the agent is allowed to access or do. The term is still emerging, but the core idea is clear: keep agent identities separate, narrow, and easy to audit.
