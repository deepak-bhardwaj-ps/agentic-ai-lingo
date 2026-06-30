---
title: SOC agent
short_description: An AI agent built to help a security operations centre sort alerts, investigate threats, and carry out some security tasks.
category: Industry verticals
tags:
- cybersecurity
- ai-agents
- security-operations
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as any security chatbot or dashboard
- Assuming it can act safely without human review or permission limits
- Using it to mean all security software
related_terms:
- cybersecurity agent
- security operations
- alert triage
- threat hunting
- SOAR
evidence:
  - source_title: Microsoft Security Copilot agents overview
    source_url: https://learn.microsoft.com/en-us/copilot/security/agents-overview
    source_type: official_docs
    relevance: Microsoft describes security agents as tools that automate repetitive security work and support security and IT operations, which is the clearest product-level definition close to SOC agent.
    key_point: Security agents help teams handle high-volume tasks such as triage and response work.
  - source_title: Microsoft Security Copilot agent development overview
    source_url: https://learn.microsoft.com/en-us/copilot/security/developer/custom-agent-overview
    source_type: official_docs
    relevance: This page explains that agents can act on behalf of a security domain such as Security Operations and execute or orchestrate security tasks.
    key_point: A SOC agent is a domain-specific agent for security operations, not a generic chatbot.
  - source_title: The agentic SOC - Rethinking SecOps for the next decade
    source_url: https://www.microsoft.com/en-us/security/blog/2026/04/09/the-agentic-soc-rethinking-secops-for-the-next-decade/
    source_type: engineering_blog
    relevance: Microsoft uses the term in the context of an operating model for SOC work, showing that the idea is tied to security-operations workflows rather than one fixed product.
    key_point: SOC agents are meant to add context, coordination, and faster response in security operations.
  - source_title: CAISI Issues Request for Information About Securing AI Agent Systems
    source_url: https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems
    source_type: official_docs
    relevance: NIST defines AI agent systems as systems that can plan and take autonomous actions affecting real-world systems, which explains why SOC agents need tight controls.
    key_point: If a SOC agent can take actions, permissions and oversight matter.
  - source_title: A Unified Framework for Human-AI Collaboration in Security Operations Centers
    source_url: https://arxiv.org/html/2505.23397v2
    source_type: research_paper
    relevance: This research shows SOC automation is usually discussed as human-AI collaboration with different levels of autonomy, which supports a cautious, non-overclaimed definition.
    key_point: SOC agents are part of a spectrum from assistive triage to more autonomous support, not a single fixed capability.
---

SOC agent means an AI agent built for security operations work.

In practice, a SOC agent can help sort security alerts, pull together evidence, spot patterns in suspicious activity, and suggest or carry out small response steps. SOC stands for security operations centre, the team that watches for attacks and handles security incidents.

This term matters because SOC teams deal with a lot of noisy data and time-sensitive decisions. A good SOC agent can reduce repetitive work and help analysts respond faster.

It is not the same as every security tool, and it is not just a chatbot with a security label. The term is still emerging, so people use it in slightly different ways. In most cases, it means an agent made for security operations, with human review and permission limits still in place for important actions.
