---
title: Agent Payments Protocol
short_description: An open protocol for letting an AI agent make or prepare a payment with clear user approval, spending limits, and an audit trail.
category: Protocols
tags:
  - payments
  - agentic-commerce
  - protocol
status: draft
aliases:
  - AP2
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a general AI shopping system rather than a payments protocol.
  - Assuming it lets an agent spend money without user-set limits or proof of approval.
  - Confusing it with A2A, which is about agent-to-agent communication, not payments.
related_terms:
  - agentic commerce
  - mandate
  - payment mandate
  - verifiable credential
  - Universal Commerce Protocol
  - Agent2Agent protocol
evidence:
  - source_title: GitHub - google-agentic-commerce/AP2
    source_url: https://github.com/google-agentic-commerce/AP2
    source_type: official_docs
    relevance: Official repository for the protocol and its reference implementation.
    key_point: Describes AP2 as the Agent Payments Protocol and shows it is organised around specifications, SDKs, and samples for payment flows.
  - source_title: Developer’s Guide to AI Agent Protocols
    source_url: https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/
    source_type: engineering_blog
    relevance: Explains AP2 in the context of agentic commerce and how it adds authorisation to payment flows.
    key_point: Says AP2 adds typed mandates, guardrails, and an audit trail so an agent can only transact within approved limits.
  - source_title: Google donates Agent Payments Protocol to FIDO Alliance
    source_url: https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/
    source_type: engineering_blog
    relevance: Gives the most current stewardship status and shows the protocol is intended to stay open and platform-agnostic.
    key_point: States that AP2 was donated to the FIDO Alliance and is being positioned as an open standard for secure agentic payments.
  - source_title: FIDO Alliance to Develop Standards for Trusted AI Agent Interactions
    source_url: https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/
    source_type: standards_doc
    relevance: Confirms AP2 is now part of a broader standards effort for trusted agent interactions.
    key_point: Shows AP2 is being used as input to FIDO Alliance work on open, interoperable standards for agentic payments.
---
Agent Payments Protocol, often called AP2, is an open payments protocol for AI agents.

It is used when a person wants an agent to help with a purchase, but the payment still needs clear approval, spending limits, and a record of what happened. In AP2, the agent does not just pay freely. It works with signed authorisation records, often called mandates, so merchants and payment providers can check that the purchase was allowed.

The term matters because agent shopping can fail if nobody can prove what the user agreed to. AP2 is meant to make those purchases safer, clearer, and easier to audit.

It is not the same as a general shopping app, and it is not the same as a protocol for agents chatting with each other. It is specifically about payment authorisation and proof.
