---
slug: skill-libraries
name: Skill Libraries
category: Protocols
title: Skill Libraries
aliases:
short_description: Skill Libraries are reusable packages of instructions, tools, examples,
termStatus: Implementation pattern
researchBasis: Hashimoto, Harness engineering
sources:
- https://mitchellh.com/writing/my-ai-adoption-journey
---

## Term status

Implementation pattern.

## Meaning

Skill libraries are reusable packages of instructions, tools, examples and sometimes code that give agents repeatable capabilities.

## Boundary

They are not model capabilities or a protocol. Version, test and permission-scope them as executable dependencies.

## How it is used

Skill Libraries is used when agent capabilities are packaged for reuse and versioned like dependencies rather than copied into prompts. It is most useful when skills need testing, permission scoping, and controlled rollout.

## Evidence

[Hashimoto, [[Harness Engineering|Harness engineering]]](https://mitchellh.com/writing/my-ai-adoption-journey) provides the relevant primary source or established reference. For coined labels, it is background for the underlying concept—not evidence that the label itself is standard.
