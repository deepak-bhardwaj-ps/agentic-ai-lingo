---
slug: blast-radius
title: Blast Radius
short_description: How much damage a mistake, bug, or security problem could cause
  before it is stopped.
category: Governance
tags: []
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating it as the same thing as risk, when it is really about how far damage
  can spread.
- Using it only for security, when it also applies to outages, bad deployments,
  and human mistakes.
related_terms:
- fault isolation
- bulkhead architecture
- cell-based architecture
- attack surface
- execution isolation
evidence:
- source_title: Design principles
  source_url: https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html
  source_type: official_docs
  relevance: Shows how the term is used in reliability engineering to describe limiting the impact of changes and failures.
  key_point: AWS says smaller, incremental changes reduce blast radius and make failures easier to reverse.
- source_title: How do you use fault isolation to protect your workload?
  source_url: https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.question.REL_10.en.html
  source_type: official_docs
  relevance: Defines the practical idea behind the term as containment of failures inside boundaries.
  key_point: AWS explains that fault-isolated boundaries limit a failure to a small number of components while other components stay unaffected.
- source_title: Implement security by design
  source_url: https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design
  source_type: official_docs
  relevance: Shows that the term is also used in security architecture, not just reliability.
  key_point: Google Cloud says teams should identify the boundaries of the potential impact, explicitly calling that the blast radius.
- source_title: Tips for an effective security architecture
  source_url: https://learn.microsoft.com/en-us/security/zero-trust/security-adoption-discipline-architecture-tips
  source_type: official_docs
  relevance: Confirms the term's use in modern security design and human-error containment.
  key_point: Microsoft says modern security architecture should reduce the blast radius of human error, such as one phishing click.
---

Blast radius is how far damage can spread when something goes wrong.

In practice, it means asking: if one part fails, what else could be affected? The answer might be one user, one database, one app, or many connected systems.

Teams use this idea to keep problems small. A low blast radius means a mistake is easier to contain and fix. A high blast radius means one problem can spread widely.

It matters because systems with a smaller blast radius are safer to change, easier to recover, and less likely to cause a big outage or security incident.

Blast radius is not the same as risk. It does not mean how likely something is to fail. It means how much harm the failure could cause if it happens.
