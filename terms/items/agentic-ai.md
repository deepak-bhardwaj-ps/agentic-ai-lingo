---
slug: agentic-ai
name: Agentic AI
category: Core
title: Agentic AI
aliases: null
short_description: Agentic AI is an umbrella term for AI systems that can take
termStatus: Umbrella term
researchBasis: Anthropic, OpenAI Agents SDK, NIST AI RMF
sources:
- https://www.nist.gov/itl/ai-risk-management-framework
---

## Term status

Umbrella term.

## Meaning

Agentic AI describes systems that use a model in an action-and-feedback loop rather than only returning a single response. It is useful as a broad category, not a technical standard, and it should be narrowed as soon as the design question gets concrete.

## Boundary

It is frequently used as branding. A product is not meaningfully agentic merely because it calls an LLM or has a multi-step backend workflow.

## How it is used

Use it when the point is the shift from passive generation to action-taking systems that can plan, call tools, and influence an environment. It is a broad term, so in serious work it should be followed by the exact task, authority boundary, and failure mode.

## Evidence

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) is the clearest product-side reference for the shift from passive generation to tool-using systems.

[OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) shows the same pattern in platform terms: orchestration, tools, state, and evaluation are first-class concerns.

[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) is the governance backdrop for making that broad category operational rather than rhetorical.
