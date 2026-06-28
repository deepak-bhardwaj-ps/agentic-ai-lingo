---
title: Intent Mesh
short_description: A loose term for routing a user's intent across multiple agents,
  tools, or services before action is taken.
category: Protocols
tags: []
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

An intent mesh is a loose name for a system that moves a user's intent across several agents, tools, or services before anything is carried out.

In practice, it means one part of the system receives a request, decides where it should go, and passes it on to the right agent or tool. That may include checking what is available, choosing who should handle the next step, and keeping track of where the request is in the process.

The term matters because real agent systems often need more than one model or tool to finish a task. A clear routing layer can reduce confusion about who owns the next action and help larger systems stay organised.

It is not a widely agreed technical standard. By itself, the phrase does not guarantee a public interface, security rules, versioning, or compatibility between different systems. It is also not the same thing as [[MCP|Model Context Protocol]], which is a defined standard for connecting AI applications to tools and data.
