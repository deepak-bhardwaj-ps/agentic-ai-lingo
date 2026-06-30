---
slug: composite-principal
title: Composite Principal
short_description: A composite principal is one acting identity made from more than
  one identity or delegated role.
category: Governance
tags: []
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse: []
related_terms: []
evidence: []
---

A composite principal is one acting identity made from more than one identity, role, or delegated permission.

In practice, it means a system is not just asking “who are you?” It is also asking “who gave you the right to act, and under what limits?” That matters when an agent, service, or person acts on behalf of someone else, or when several identities together create one effective authority.

This term matters because modern systems often split identity and power across steps. One account may start the action, another may approve it, and a third may actually carry it out. If you cannot trace that chain clearly, you cannot tell who is responsible when something goes wrong.

It is not a magic security feature. A composite principal does not become safe just because it has a fancy name. It is also not the same as authentication. Authentication tells you who or what is present. A composite principal is about how authority is combined, delegated, and recorded.
