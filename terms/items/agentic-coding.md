---
slug: agentic-coding
name: Agentic Coding
category: Core
title: Agentic Coding
aliases:
short_description: Agentic coding is coding in which an AI system can propose,
termStatus: Emerging practitioner term
researchBasis: Harness engineering, Anthropic, OpenAI Agents SDK
sources:
- https://developers.openai.com/api/docs/guides/agents
---

## Term status

Emerging practitioner term.

## Meaning

Agentic coding is software development in which an AI system plans and executes changes through repository tools, terminals, tests, and review loops; it may work across many files and turns.

## Boundary

It is not autocomplete, and it is not autonomous delivery. The engineering boundary is the permitted repository, command, credential, and merge authority.

## How it is used

It is used when the coding workflow includes tool use, multi-step revision, and explicit recovery rather than a single code completion. It matters because the control problem is different from autocomplete: you are designing the loop, the review boundary, and the rollback path.

## Evidence

[[[Harness Engineering|Harness engineering]]](https://mitchellh.com/writing/my-ai-adoption-journey) is the practical reference point for coding workflows that depend on explicit loops, verification, and recovery.

[Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) supports the broader point that the useful unit is the tool-using loop, not a single completion.

[OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) makes the same control split explicit with orchestration, tools, state, and evaluation.
