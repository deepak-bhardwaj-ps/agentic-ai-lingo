---
title: Agent goal hijacking
short_description: An attack where an AI agent is pushed to follow an attacker’s goal instead of the user’s goal.
category: Governance and security
tags:
  - ai-agents
  - security
  - prompt-injection
  - governance
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Confusing it with ordinary bugs in an agent’s logic
  - Treating it as only direct prompt injection, when the attack can also come through tools, web pages, documents, or memory
  - Assuming the agent is “hacked” in the normal software sense rather than subtly steered
related_terms:
  - prompt injection
  - indirect prompt injection
  - tool abuse
  - memory poisoning
  - privilege escalation
  - agent security
evidence:
  - source_title: AI Agent Security Cheat Sheet
    source_url: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
    source_type: official_docs
    relevance: OWASP gives a direct agent-security risk entry for goal hijacking, so this is the clearest current industry definition.
    key_point: Goal hijacking means manipulating an agent’s objectives so it serves attacker purposes while appearing to act normally.
  - source_title: The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis
    source_url: https://ar5iv.labs.arxiv.org/html/2602.10453
    source_type: research_paper
    relevance: This paper explains how untrusted inputs can hijack agent behaviour and ties the term to real agent workflows and trust boundaries.
    key_point: Prompt injection in agents can hijack behaviour because the system mixes trusted instructions and untrusted data in one context.
  - source_title: Towards Action Hijacking of Large Language Model-based Agent
    source_url: https://arxiv.org/html/2412.10807v1
    source_type: research_paper
    relevance: This paper shows how attackers can steer agent reasoning, planning, and actions, which is the practical mechanism behind goal hijacking.
    key_point: Indirect prompt injection can control an agent’s reasoning and planning through malicious instructions hidden in external content.
---

Agent goal hijacking is when someone tricks an AI agent into chasing the wrong goal.

In practice, the agent still looks busy and helpful, but its actions are being steered towards what the attacker wants instead of what the user asked for. The trick can come through a message, a web page, a document, a tool result, or stored memory.

This matters because agents can take actions, not just write text. If the wrong goal wins, the agent may leak information, use tools in unsafe ways, or carry out tasks it was never meant to do.

It is not just a normal software bug. It is also not the same as a simple bad answer. The key idea is that the agent’s purpose has been shifted, often without obvious signs.

The term is still emerging, and different security groups use it a little differently. In most current usage, it is a close synonym of goal hijacking in agent security.
