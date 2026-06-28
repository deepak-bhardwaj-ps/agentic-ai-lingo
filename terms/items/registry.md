---
slug: registry
name: Registry
category: Protocols
title: Registry
aliases: []
short_description: A registry is a catalogue that helps people or software find named
  things such as servers, tools, or packages.
updated_at: '''2026-06-28T00:00:00+00:00'''
termStatus: Established systems term
researchBasis: Official MCP Registry documentation and MCP introduction docs
sources: []
status: active
tags: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse: []
related_terms: []
evidence: []
---

A registry is a list that helps software or people find named things in one place.

In practice, a registry stores details such as a name, where to find the item, and how to use it. In agent systems, that might be an [[MCP]] server, a too[[Context Collapse|l]], a package, or another service. The registry usually does not contain the thing itself. It contains the information needed to discover it.

This matters because large systems are hard to manage with scattered links a[[Context Collapse|n]]d memory alone. A registry gives one place to look when you want to find something, publish it, or check its basic details.

A registry is not the same as trust, safety, or compatibility. Just because something is listed does not mean it is safe to use, works with every client, or is the right choice for a task. It is a discovery aid, not a guarantee.
