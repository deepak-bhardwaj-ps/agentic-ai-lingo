---
slug: agent-coalition
name: Agent Coalition
category: Protocols
title: Agent Coalition
aliases: null
short_description: Agent Coalition is a set of separately owned agents that cooperate
termStatus: Emerging interoperability/architecture label
researchBasis: Model Context Protocol specification
sources:
- https://openai.github.io/openai-agents-python/tracing/
---

## Term status

Emerging interoperability/architecture label.

## Meaning

Agent coalition is an emerging, non-standard label for independently owned agents that agree to pursue a bounded outcome without becoming one centrally managed application. The architectural point is the agreement surface: identity, authority, data-sharing rules, allowed calls, commercial or operational responsibility, and exit conditions.

Most product teams would describe the same arrangement as federated collaboration, delegated workflow, or cross-system orchestration. The coalition metaphor is useful only when independence and differing incentives genuinely matter.

## Common misconceptions

A coalition is not a team of subagents inside one runtime. A supervisor that delegates to workers it owns has no independent parties to govern; an OpenAI Agents SDK hand-off, for example, transfers control under one application’s runtime rules.

Nor is it an interoperability protocol. A real cross-organisation arrangement needs discoverability, authentication, scoped authority, consent, audit records, revocation, liability boundaries, and compatible message contracts. The label supplies none of them.

## How it is used

Consider a travel agent that asks an airline, hotel, and corporate-policy agent to construct an itinerary. Calling that a coalition is defensible only if each service retains control over its policy, inventory, and data; the orchestrator cannot silently broaden permissions or treat a recommendation as a binding booking.

For enterprise architecture, document the collaboration as explicit contracts rather than an aspirational “agent network”: principals, delegations, data classifications, compensating actions, service levels, dispute handling, and end-to-end traces.

## Evidence

No canonical source defines “agent coalition”. The practical mechanics appear in [OpenAI Agents SDK hand-offs](https://openai.github.io/openai-agents-python/handoffs/) and [handoff tracing](https://openai.github.io/openai-agents-python/tracing/); the [Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-06-18) is relevant background for integration, not proof that the label is established.
