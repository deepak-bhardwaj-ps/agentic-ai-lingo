---
title: Human-on-the-loop
short_description: A setup where a person watches an AI system, can step in if needed, and can stop or change its actions.
category: Agentic patterns
tags:
  - agents
  - oversight
  - safety
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the same thing as human-in-the-loop.
  - Assuming the person approves every action in real time.
  - Using it as a vague claim that a human is “somewhere in the process” without real control.
related_terms:
  - human-in-the-loop
  - human-in-command
  - human oversight
  - autonomous system
evidence:
  - source_title: "Ethics guidelines for trustworthy AI"
    source_url: "https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai"
    source_type: standards_doc
    relevance: "This is a widely cited European Commission source that names human-on-the-loop as one way to provide human oversight for AI systems."
    key_point: "Human-on-the-loop is part of human oversight, alongside human-in-the-loop and human-in-command."
  - source_title: "Requirements of Trustworthy AI"
    source_url: "https://ec.europa.eu/futurium/en/ai-alliance-consultation/guidelines/1.html"
    source_type: standards_doc
    relevance: "This explains the practical difference between the oversight modes and is useful for defining the term narrowly."
    key_point: "In human-on-the-loop, a human checks the system and can abort intended actions, rather than approving every decision."
  - source_title: "Artificial Intelligence Risk Management Framework: Generative AI Profile"
    source_url: "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf"
    source_type: standards_doc
    relevance: "This recent NIST profile shows that different AI systems need different levels of human oversight, which supports the term as an oversight pattern rather than a fixed job title."
    key_point: "Generative AI may need different human oversight arrangements, including review, tracking, documentation, and management oversight."
---

Human-on-the-loop is a way of using AI where a person watches what the system is doing and can step in if something looks wrong.

In practice, the AI does the work most of the time. The human does not approve every step. Instead, they monitor the system, check its output, and can stop or change actions when needed.

This matters because AI can be useful without being fully unattended. A human-on-the-loop setup gives the system more freedom than human-in-the-loop, but still keeps a person responsible for oversight and intervention.

It is not the same as human-in-the-loop, where a person is involved in each decision cycle. It is also not fully autonomous, because the human still has a real oversight role.
