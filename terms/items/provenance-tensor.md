---
slug: provenance-tensor
title: Provenance Tensor
short_description: A proposed way to describe where agent context came from, how trustworthy
  it is, and how it should be handled.
category: Context
tags: []
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: high
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

Provenance Tensor is a proposed way to describe where an agent's context came from, how reliable it is, and how it should be treated.

In practice, it means keeping the source of each piece of context attached to the context itself. That source might be a document, a memory, a tool result, a retrieval step, or a human note. The idea is to track more than just the words. It also tracks where they came from, whether they are fresh, and whether the system is allowed to use them.

This matters because [[Agentic AI|agentic systems]] often mix many inputs. Some are trusted. Some are stale. Some are only allowed for certain users. If the system cannot tell those apart, it can use the wrong context or explain itself badly.

It is not a standard term with one agreed meaning. It is not a formal product category, and it is [[Context Collapse|n]]ot the same thing as a citation list. It is closer to a structured way of carrying provenance through an agent pipeline.
