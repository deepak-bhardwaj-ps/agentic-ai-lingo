---
slug: agentops
name: AgentOps
category: AgentOps
title: AgentOps
aliases: []
short_description: AgentOps is the operational practice of deploying, observing,
  evaluating, and governing agentic applications.
termStatus: Emerging operational label
researchBasis: OpenAI, Evals design guide, NIST AI RMF
sources:
- https://platform.openai.com/docs/guides/evals
- https://www.nist.gov/itl/ai-risk-management-framework
---

## Term status

Emerging operational label.

## Meaning

AgentOps is the operational practice of deploying, observing, evaluating, and governing agentic applications. It borrows heavily from MLOps, DevOps, SRE, and application security.

## Boundary

It is not an established standard or a separate technology layer. Ask which concrete capabilities are meant: tracing, evaluation, release control, incident response, or access governance.

## How it is used

It is used when the conversation is about keeping agents running safely in production: tracing, evaluation, release control, incident response, and access governance. It is a discipline term, not a product feature.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the operational evaluation framing that AgentOps usually bundles.

[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) gives the broader governance and risk-management context for running AI systems in production.

The label is useful as shorthand only if it is unpacked into concrete operational capabilities and owners.
