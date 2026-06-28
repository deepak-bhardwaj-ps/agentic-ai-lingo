---
slug: identity-plane
title: Identity Plane
short_description: A layer that decides which person, app, or service is allowed to
  act, and what they are allowed to do.
category: Governance
tags:
- governance
- security
- identity
- access-control
status: glossary
aliases:
- identity plane
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal industry standard when it is usually a design label.
- Confusing it with the data plane or control plane.
- Using it as a vague synonym for login or authentication only.
related_terms:
- identity and access management
- authentication
- authorisation
- control plane
- data plane
- workload identity
evidence:
- source_title: Identity architecture design - Azure
  source_url: https://learn.microsoft.com/en-us/azure/architecture/identity/identity-start-here
  source_type: official_docs
  relevance: Shows that identity systems control access to apps and data, and distinguish
    authentication from authorisation.
  key_point: Identity is the basis for deciding who or what can access resources.
- source_title: Identity, the first pillar of a Zero Trust security architecture
  source_url: https://learn.microsoft.com/en-us/security/zero-trust/deploy/identity
  source_type: official_docs
  relevance: Explains identity as the main control point for access in modern security
    design.
  key_point: Identities for people, services, and devices must be verified before
    access is granted.
- source_title: SPIFFE
  source_url: https://spiffe.io/
  source_type: engineering_blog
  relevance: Uses the term "identity control plane" for workloads, showing how the
    idea is used in modern distributed systems.
  key_point: Workloads can be given strong, cryptographic identities through a dedicated
    identity layer.
- source_title: SPIFFE Federation
  source_url: https://spiffe.io/docs/latest/spiffe-specs/spiffe_federation/
  source_type: standards_doc
  relevance: Defines a workload identity framework and explains that trust domains
    act as identity namespaces.
  key_point: Identity can be managed as a distinct layer with clear boundaries between
    systems.
---

An identity plane is the part of a system that figures out who or what is acting, and what that actor is allowed to do.

In practice, it sits beside the rest of the system and keeps track of identities for people, apps, devices, or services. It helps answer questions like: Is this really the right user? Is this service trusted? What actions are allowed? It may also record approvals, audit logs, and revocations.

This matters because modern systems cannot rely on just a password or a single login screen. They need a clear way to control access across many services, devices, and automated agents.

It is not the same as the data plane, which moves data, or the [[Control Plane Architecture|control plane]], which manages the system. It is also not just “login”. Login is only one small part of identity.
