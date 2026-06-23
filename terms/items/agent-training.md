---
slug: agent-training
name: Agent Training
category: Protocols
title: Agent Training
aliases:
short_description: Agent training is the onboarding or calibration of agents to
termStatus: Emerging interoperability/architecture label
researchBasis: Anthropic, OpenAI Agents SDK, MCP
sources:
- https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization
---

## Term status

Emerging interoperability/architecture label.

## Meaning

Agent training is the preparation or calibration of an agent so it can operate correctly inside a wider ecosystem.

## Boundary

It is not a protocol unless it defines a public wire format, lifecycle, compatibility, and security model. Do not imply interoperability from the label alone.

## How it is used

It is used when an agent needs instruction, calibration, or behavioural adaptation before it can join a wider system. It should not be confused with model training unless the underlying weights or policy are actually being updated.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) emphasises that useful agent behaviour comes from simple, composable patterns and good tool design, which is the real substrate for “training” an agent.

[OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) separates orchestration and state from the model itself, which is what makes calibration distinct from model training.

[[[MCP]] authorization](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) captures the integration side: onboarding an agent safely requires explicit permissions, not just configuration.
