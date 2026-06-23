---
slug: verifier
name: Verifier
category: Runtime
title: Verifier
aliases: []
short_description: Verifier is used in runtime design to name the component that coordinates
  decisions and side effects.
termStatus: Architecture component
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/evals
---

## Term status

Architecture component.

## Meaning

A verifier is a component that checks whether an output or action satisfies defined criteria, for example a type checker, test suite, policy engine or independent model judge.

## Boundary

A model verifier has correlated failure modes with the generator. Match verification strength to impact and use deterministic checks where possible.

## How it is used

Verifier is used in runtime design to name the component that coordinates decisions and side effects. A useful specification gives its input event, durable state, action contract, retry policy, timeout and terminal states.

## Evidence

[OpenAI, Evals design guide](https://platform.openai.com/docs/guides/evals) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
