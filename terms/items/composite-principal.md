---
slug: composite-principal
title: Composite Principal
short_description: A composite principal is one acting identity built from more than one principal or a chain of delegated authority.
category: Governance
tags:
  - agentic-ai
  - identity
  - access-control
  - delegation
  - iam
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the same thing as authentication.
  - Assuming it always means one user with many roles.
  - Using it to mean any combined permissions, even when there is no clear delegation chain.
related_terms:
  - principal
  - delegation chain
  - impersonation
  - service account
  - authorization propagation
evidence:
  - source_title: class CompositePrincipal · AWS CDK
    source_url: https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.CompositePrincipal.html
    source_type: official_docs
    relevance: Shows the term has a concrete meaning in AWS IAM tooling, where multiple IAM principals can be combined into one composite principal.
    key_point: AWS CDK says a CompositePrincipal is made from multiple IAM principals, and it cannot have conditions.
  - source_title: Create short-lived credentials for multiple service accounts
    source_url: https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated
    source_type: official_docs
    relevance: Shows the delegation-chain pattern that motivates the broader governance use of composite principal language.
    key_point: Google Cloud describes delegated requests through one or more service accounts, and says the final credential represents only the final service account, not the intermediates.
  - source_title: Agent Identity overview
    source_url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview
    source_type: official_docs
    relevance: Shows how modern agent systems track when an agent acts for itself versus on behalf of a user, which is the practical setting where composite-principal language appears.
    key_point: Google says agents can act on behalf of users through OAuth delegation, and audit logs must show whether the agent acted as itself or for an end user.
  - source_title: A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents
    source_url: https://arxiv.org/html/2606.12320v1
    source_type: research_paper
    relevance: Shows the term is emerging as a formal governance idea for multi-agent systems, not just an IAM convenience term.
    key_point: The paper defines a composite principal model for reasoning over delegation chains and bounding authority in agentic systems.
---

A composite principal is one acting identity made from more than one principal, or from a chain of delegated authority.

In practice, it means the system is not only asking who is acting. It is also tracking how that actor got its power, and which earlier identities or permissions are part of the chain.

This matters because modern systems often let one identity act for another. An agent may act for a user, a service account may act for another service account, or several principals may be grouped together for one policy decision. If the chain is not clear, it becomes hard to know who is responsible and what they were really allowed to do.

This term is not fully standardised across all systems. In AWS CDK it has a specific IAM meaning. In broader agent and governance writing, it is used more as a way to describe delegated authority that has been combined into one acting identity.

It is not the same as authentication. Authentication says who or what logged in. A composite principal is about how authority is combined, delegated, and traced.
