---
slug: agent-marketplace
name: Agent Marketplace
category: Protocols
title: Agent Marketplace
aliases:
short_description: A marketplace is a catalogue for discovering, selecting, and
termStatus: Product/operating-model label
researchBasis: OWASP Top 10 for LLM Applications, PROV-AGENT, Anthropic
sources:
- https://www.anthropic.com/engineering/building-effective-agents
---

## Term status

Product/operating-model label.

## Meaning

A marketplace is a catalogue and distribution mechanism for agents or skills, usually with discovery, installation, versioning, and governance features.

## Boundary

It is not a security boundary. Treat third-party agents as software supply-chain dependencies with review, provenance, and permission controls.

## How it is used

It is used when agents are exposed as discoverable offerings rather than internal utilities. The hard questions are catalogue quality, trust, pricing, and how a buyer knows the agent will actually do what is claimed.

## Evidence

[OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) is the strongest security-side reference for treating third-party agent capabilities as a supply-chain and permission problem.

[PROV-AGENT](https://arxiv.org/abs/2508.02866) reinforces the need for provenance when agents, prompts, and downstream actions are distributed across heterogeneous environments.

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) supports the operational distinction between internal agent patterns and packaging those capabilities into something reusable and discoverable.
