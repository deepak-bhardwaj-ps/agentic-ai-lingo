---
slug: verification-loop
name: Verification Loop
category: Runtime
title: Verification Loop
aliases: []
short_description: Verification Loop is the cycle of checking results, feeding back
  evidence, and deciding whether to continue.
termStatus: Architecture pattern
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/evals
---

## Term status

Architecture pattern.

## Meaning

A verification loop generates or executes a check on an agent's proposed result, then feeds the evidence into a retry, repair or escalation decision.

## Boundary

It is not self-verification by assertion. Prefer executable tests, independent data sources or separated [[Verifier|verifier]] roles for high-stakes claims.

## How it is used

Verification Loop is used when the system keeps checking outputs, feeding back evidence, and deciding whether to continue. In production it needs explicit stop conditions, iteration limits, and spend control.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
