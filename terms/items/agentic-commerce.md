---
slug: agentic-commerce
title: Agentic Commerce
short_description: A new term for shopping and buying where an AI agent helps a person discover, choose, check out, or pay, but only within the person's rules.
category: Core
tags:
  - commerce
  - payments
  - agents
  - ai
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: high
maturity_level: emerging
common_misuse:
  - Treating it as a full shopping system instead of a shopping flow that uses AI agents.
  - Assuming the agent can spend money without user approval, limits, or records.
  - Confusing it with a normal chatbot that only recommends products.
related_terms:
  - AP2
  - Universal Commerce Protocol
  - AI agent
  - agentic AI
  - agentic payments
  - checkout
evidence:
  - source_title: Under the Hood: Universal Commerce Protocol (UCP)
    source_url: https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/
    source_type: engineering_blog
    relevance: This is a current Google explanation of the commerce layer built for the agentic commerce era, so it helps define the term in practice.
    key_point: Google describes UCP as an open-source standard for the next generation of agentic commerce, covering the shopping journey between consumer surfaces, businesses, and payment providers.
  - source_title: Developer's Guide to AI Agent Protocols
    source_url: https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/
    source_type: engineering_blog
    relevance: This source separates the parts of the stack, which helps avoid mixing up shopping, commerce, and payment authorisation.
    key_point: Google says UCP standardises commerce while AP2 handles payment authorisation, which shows agentic commerce is broader than payments alone.
  - source_title: Building the Trust Layer for Agentic Payments with AP2 and Verifiable Intent
    source_url: https://fidoalliance.org/building-the-trust-layer-for-agentic-payments-with-ap2-and-verifiable-intent/
    source_type: standards_doc
    relevance: This gives the clearest current standards framing for what must be controlled when an agent helps with a purchase.
    key_point: FIDO describes agentic payment flows as involving AI agents, merchants, wallets, and payment providers coordinating around user authorisation, with verifiable mandates that capture what the user approved.
  - source_title: GitHub - google-agentic-commerce/AP2
    source_url: https://github.com/google-agentic-commerce/AP2
    source_type: official_docs
    relevance: This is the official protocol repository, which confirms the payments side of agentic commerce is being built as an interoperable technical standard.
    key_point: The repository presents AP2 as the Agent Payments Protocol and provides samples and specs for agent-led payment flows.
---

Agentic commerce is shopping and buying where an AI agent helps a person discover, choose, check out, or pay, but only within the person's rules.

In practice, the agent might compare products, fill in details, start checkout, or ask for approval before a purchase. The person still decides the limits, such as what can be bought, how much can be spent, and when the agent must stop and ask.

The term matters because shopping is no longer just a person clicking buttons. Once software can act in the buying process, the system needs clear approval, records, and safety checks.

It is not the same as a normal chatbot that only gives advice. It is also not a fully free shopping bot that can spend money on its own. The term is still new, and companies use it in slightly different ways, but the core idea is the same: an AI agent helps with commerce under user control.
