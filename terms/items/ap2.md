---
title: AP2
short_description: An open payments protocol that lets an AI agent help with a purchase only within the user's approved limits and payment rules.
category: Protocols and standards
tags:
  - payments
  - agentic-commerce
  - protocol
status: draft
aliases:
  - Agent Payments Protocol
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating AP2 as a whole shopping system instead of a payments protocol.
  - Assuming it lets an agent spend money without clear user approval or limits.
  - Confusing it with A2A, which is about agent-to-agent communication.
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
    relevance: Official repository and reference implementation for the protocol.
    key_point: Identifies AP2 as the Agent Payments Protocol and shows it is organised around specifications, SDKs, and samples for payment flows.
  - source_title: Developer's Guide to AI Agent Protocols
    source_url: https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/
    source_type: engineering_blog
    relevance: Explains what AP2 adds to agentic commerce.
    key_point: Describes AP2 as the layer that adds typed mandates, guardrails, and an audit trail so an agent can only transact within approved limits.
  - source_title: Google donates Agent Payments Protocol to FIDO Alliance
    source_url: https://fidoalliance.org/google-donates-agent-payments-protocol-to-fido-alliance/
    source_type: standards_doc
    relevance: Gives the current stewardship status of AP2.
    key_point: Says AP2 was donated to the FIDO Alliance and is being developed as part of an open, interoperable standards effort.
  - source_title: FIDO Alliance to Develop Standards for Trusted AI Agent Interactions
    source_url: https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/
    source_type: standards_doc
    relevance: Confirms AP2 is being folded into broader work on trusted agent interactions.
    key_point: Shows AP2 is part of a wider standards effort for secure delegation and trusted transactions involving AI agents.
---

AP2 is short for Agent Payments Protocol.

It is a way for an AI agent to help with a payment without being allowed to spend freely. The person still sets the rules, such as what can be bought, how much can be spent, and what counts as approval.

In practice, AP2 is about proving that a purchase was allowed. That makes it easier for merchants, wallets, and payment providers to check what the user agreed to and to keep a record of it.

This term matters because an agent can only be trusted with money if its actions are limited and explainable. AP2 is meant to make agent-led payments safer and easier to audit.

AP2 is not a shopping app, and it is not the same as A2A. A2A is for agents talking to other agents. AP2 is for payment authorisation.
