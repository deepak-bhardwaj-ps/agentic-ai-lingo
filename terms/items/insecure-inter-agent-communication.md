---
title: Insecure inter-agent communication
short_description: A security weakness where agents send messages to each other without enough checks on identity, secrecy, or message integrity.
category: Governance
tags:
- ai
- security
- protocol
- multi-agent
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as general insecure network traffic.
- Assuming encryption alone is enough, without checking who sent the message or whether it was changed.
- Confusing it with agent failure or bad reasoning instead of a trust and transport problem.
related_terms:
- A2A
- ACP
- multi-agent system
- authentication
- message integrity
- trust boundary
evidence:
  - source_title: AI Agent Security - OWASP Cheat Sheet Series
    source_url: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
    source_type: official_docs
    relevance: OWASP security guidance for agent systems, including direct advice on inter-agent communication.
    key_point: The cheat sheet says teams should implement trust boundaries between agents and validate and sanitise inter-agent communications.
  - source_title: AIVSS Scoring System For OWASP Agentic AI Core Security Risks v0.8
    source_url: https://aivss.owasp.org/assets/publications/AIVSS%20Scoring%20System%20For%20OWASP%20Agentic%20AI%20Core%20Security%20Risks%20v0.8.pdf
    source_type: standards_doc
    relevance: Defines the attack class in terms of how adversaries abuse agent-to-agent message flow.
    key_point: The document describes inter-agent communication exploitation as intercepting, manipulating, or injecting messages, especially when authentication, encryption, or integrity checks are weak or missing.
  - source_title: Addressing the OWASP Top 10 Risks in Agentic AI with Microsoft Copilot Studio
    source_url: https://www.microsoft.com/en-us/security/blog/2026/03/30/addressing-the-owasp-top-10-risks-in-agentic-ai-with-microsoft-copilot-studio/
    source_type: engineering_blog
    relevance: Shows how a major vendor explains the same risk in practical terms for agentic systems.
    key_point: Microsoft summarises the risk as spoofing, intercepting, or manipulating agent-to-agent messages when authentication or integrity checks are weak.
---
Insecure inter-agent communication is when one AI agent sends messages to another without enough protection.

In practice, this means an attacker could pretend to be a trusted agent, change a message while it is moving, or send a fake instruction into the agent chain. The problem is not just the network link itself. It is the lack of checks on who sent the message, whether it was altered, and whether the receiver should trust it.

The term matters because multi-agent systems often pass tasks, approvals, and results between agents. If those messages are weakly protected, one compromised agent or one fake message can mislead the whole system.

It is not the same as a general software bug, and it is not just about encryption. A system can encrypt messages and still be unsafe if it does not verify identity, integrity, and allowed behaviour at the agent level.
