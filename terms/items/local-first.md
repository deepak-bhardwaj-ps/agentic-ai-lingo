---
title: Local-first
short_description: Software that keeps a person's data on their own device first, then syncs it to other devices or shared copies when needed.
category: Knowledge and wiki systems
tags:
  - storage
  - sync
  - collaboration
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the same as offline-first, when local-first also cares about syncing and ownership across devices.
  - Assuming it means “no cloud at all”, when many local-first apps still sync through servers.
  - Using it to mean any app with a cache or a fast local screen.
related_terms:
  - offline-first
  - synchronisation
  - conflict-free replicated data type
  - data ownership
evidence:
  - source_title: 'Local-first software: You own your data, in spite of the cloud'
    source_url: https://www.inkandswitch.com/essay/local-first/
    source_type: engineering_blog
    relevance: This is the original modern statement of the term and sets the core meaning used in the field.
    key_point: Local-first software keeps data in local storage on each device, works offline, and still supports collaboration and user control.
  - source_title: 'Local-first software: you own your data, in spite of the cloud'
    source_url: https://martin.kleppmann.com/papers/local-first.pdf
    source_type: research_paper
    relevance: This paper explains the technical meaning behind the term and why local data plus sync is central to it.
    key_point: The paper defines local-first apps as keeping data local on each device while synchronising changes across devices, often with techniques such as CRDTs.
  - source_title: Local-First Software
    source_url: https://docs.powersync.com/resources/local-first-software
    source_type: official_docs
    relevance: This current vendor documentation shows how the term is used in real products today, especially in app design and sync architecture.
    key_point: Local-first is described as prioritising local storage and local operation first, with server sync as a later concern rather than the main place where work happens.
---

Local-first is software that keeps your data on your own device first and then syncs it with other devices or shared services when needed.

In practice, that means the app should still work when the internet is slow or missing. You can keep working locally, and the changes are copied across later so your other devices stay up to date.

The term matters because it puts the user’s device, not a remote server, at the centre of the app. That usually makes the app faster, more private, and less likely to lock your work into one company’s system.

Local-first is not the same as offline-first. Offline-first means an app can work without a connection. Local-first adds a stronger idea: your device holds the main copy of your data, and syncing is built around that.

It is also not the same as “no cloud”. Many local-first apps still use servers for sync, backup, or sharing. The difference is that the server is not the place where your work must live first.
