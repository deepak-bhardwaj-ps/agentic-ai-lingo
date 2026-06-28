---
slug: context-collapse
name: Context Collapse
category: Context
title: Context Collapse
aliases: 'null'
short_description: A failure mode where an agent gets too much, too little, or the
  wrong context to do the task well.
status: emerging
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

## Meaning

Context collapse is when an agent stops doing well because the context it gets is overloaded, confused, stale, or badly chosen.

## In practice

This can happen when the prompt is too long, when the wrong documents are retrieved, when old instructions are mixed with new ones, or when important facts are hidden among lots of noise.

## Why it matters

An agent can only use the context it is given. If that context is messy, the answer can be wrong even when the model is capable enough.

## What it is not

It is not a formal product category. It does not just mean "more tokens". The real problem is often poor selection, poor ordering, or poor freshness of the information.
