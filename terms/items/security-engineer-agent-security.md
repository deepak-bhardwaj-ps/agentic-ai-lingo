---
title: Security engineer, agent security
short_description: A security engineer who designs and ships protections for AI agents that can plan and act.
category: Roles
tags:
  - ai-agents
  - security
  - roles
  - agentic-ai
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a generic security engineer role with a new label
  - Assuming it is the same as a SOC analyst or incident responder role
  - Confusing the role with a product called "agent security"
related_terms:
  - security engineer
  - agentic security
  - AI security engineer
  - least privilege
  - sandboxing
  - identity and privilege abuse
evidence:
  - source_title: Security Engineer, Agent Security
    source_url: https://openai.com/careers/security-engineer-agent-security-san-francisco/
    source_type: official_docs
    relevance: This is the clearest current example of the exact job title, and it describes the work the role does.
    key_point: The role designs security policies, frameworks, and controls for agentic AI systems, including identity, network, and runtime defences.
  - source_title: Security Engineer, Enterprise Security AI
    source_url: https://www.google.com/about/careers/applications/jobs/results/124193923898712774-security-engineer-enterprise-security-ai
    source_type: official_docs
    relevance: Google shows the same kind of specialist role in another major company, which confirms this is a real hiring pattern rather than a one-off title.
    key_point: The work includes threat models, guardrails, and remediation for AI agents, plus sharing agent-security expertise across teams.
  - source_title: Agentic Security Initiative
    source_url: https://genai.owasp.org/initiatives/agentic-security-initiative/
    source_type: standards_doc
    relevance: OWASP explains the security problems that this role exists to solve, which helps anchor the job in a real technical domain.
    key_point: Securing autonomous agents and multi-step AI workflows needs dedicated controls, not just ordinary app security habits.
  - source_title: Four security principles for agentic AI systems
    source_url: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/
    source_type: engineering_blog
    relevance: AWS sets out the controls a security engineer working on agents is expected to apply in practice.
    key_point: Agent security should be enforced with external, deterministic controls such as least privilege, approval gates, and runtime policy enforcement.
---

Security engineer, agent security means a security engineer who works on protecting AI agents.

In practice, this person designs and builds controls that limit what an AI agent can see, do, and change. That can include access rules, sandboxing, logging, approval steps for risky actions, and checks that stop an agent from using the wrong identity or too much permission.

The role matters because AI agents can take actions, not just produce text. If they are tricked or over-privileged, they can expose data, change systems, or carry out unsafe actions quickly.

This is not the same as a general security engineer role, although it uses many of the same skills. It is also not just a SOC job watching alerts, and it is not a product name. The term is still fairly new, but the work it describes is becoming a real specialism inside security teams.
