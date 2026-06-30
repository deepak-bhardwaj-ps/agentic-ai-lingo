---
slug: alignment-verification
name: Alignment Verification
category: Governance
title: Alignment Verification
aliases: []
short_description: Checking whether an AI agent keeps to the rules, purpose, and limits it was given.
status: active
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a formal, widely agreed technical standard term. It is still an emerging phrase.
  - Using it as a synonym for accuracy. A system can be factually right and still break its instructions or limits.
  - Confusing it with alignment training. Verification checks behaviour; it does not create alignment by itself.
related_terms:
  - AI alignment
  - agentic misalignment
  - evaluation
  - monitoring
  - test, evaluation, verification, and validation
evidence:
  - source_title: How we monitor internal coding agents for misalignment
    source_url: https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/
    source_type: engineering_blog
    relevance: Shows current deployment practice for checking whether agent behaviour matches intent and policy, which is the closest real-world use of this term.
    key_point: OpenAI describes monitoring as looking for actions and reasoning that conflict with user intent or with security and compliance policies.
  - source_title: Artificial Intelligence Risk Management Framework (AI RMF 1.0)
    source_url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
    source_type: standards_doc
    relevance: Grounds the idea in the broader AI governance practice of testing, evaluation, verification, and validation.
    key_point: NIST treats verification as part of TEVV, meaning checks that an AI system behaves as intended throughout its lifecycle.
  - source_title: Challenges to the monitoring of deployed AI systems
    source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-4.pdf
    source_type: standards_doc
    relevance: Explains why post-deployment checks matter for systems that can change behaviour in real use.
    key_point: NIST says post-deployment monitoring is needed to verify that an AI system is operating reliably and as expected in real-world scenarios.
---

Alignment verification means checking whether an AI agent still follows the rules, purpose, and limits it was given.

In practice, this means asking questions like: Did the agent do what it was meant to do? Did it stay within its allowed scope? Did it avoid actions the team said were not allowed? Can we show that with tests, logs, or human review?

This matters because an agent can look useful and still do the wrong thing. It may follow a request too far, ignore safety rules, or take actions the team did not approve. Verification is the check that tries to catch that.

It is not the same as general accuracy. A system can give correct facts and still break its instructions, safety rules, or job.

It is also not a single magic control. It is usually a repeatable set of tests, reviews, and monitoring steps.

The term is not yet widely standardised, so people may mean slightly different things by it. In most cases, it means checking that an AI agent behaves as intended.
