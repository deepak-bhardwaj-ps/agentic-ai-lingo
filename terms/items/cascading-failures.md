---
title: Cascading failures
short_description: A failure that spreads from one part of a system to another, making the outage bigger over time.
category: Governance and security
tags:
- resilience
- reliability
- distributed-systems
- outages
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating it as the same thing as a correlated failure.
- Using it for any outage, even when the failure does not spread.
related_terms:
- correlated failures
- overload
- circuit breaker
- graceful degradation
- fault tolerance
evidence:
- source_title: Cascading Failures: Reducing System Outage
  source_url: https://sre.google/sre-book/addressing-cascading-failures/
  source_type: standards_doc
  relevance: Google SRE is one of the most widely cited operational guides for large systems, and this chapter gives the core definition used in reliability engineering.
  key_point: A cascading failure is a failure that grows over time because one failed part makes other parts more likely to fail.
- source_title: Minimizing Correlated Failures in Distributed Systems
  source_url: https://aws.amazon.com/builders-library/minimizing-correlated-failures-in-distributed-systems/
  source_type: engineering_blog
  relevance: AWS explicitly distinguishes cascading failure from correlated failure, which helps avoid mixing up two similar reliability terms.
  key_point: AWS describes cascading failure as one component failing, increasing load on the next component, which then fails, and so on.
- source_title: Patterns for scalable and resilient apps
  source_url: https://docs.cloud.google.com/architecture/scalable-and-resilient-apps
  source_type: official_docs
  relevance: Google Cloud gives practical mitigation examples and shows that the term is used in real system design, not just in theory.
  key_point: Google Cloud warns that the failure of one service can cause other services to fail, and recommends circuit breakers, backoff, and graceful degradation to reduce that risk.
---

Cascading failures is when one part of a system fails and that failure spreads to other parts, making the problem bigger.

In practice, this often happens in software systems when a service becomes slow or stops working, so other services retry, wait, or pile up work. That extra pressure can then break the next part of the system too.

This matters because a small problem can turn into a much larger outage if the system is not designed to contain it. Engineers try to stop this with things like circuit breakers, backoff, and graceful degradation.

It is not the same as a correlated failure. A correlated failure means several things fail because they share the same cause. A cascading failure starts with one failure and then spreads from there.
