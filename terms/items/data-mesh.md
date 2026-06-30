---
slug: data-mesh
title: Data Mesh
short_description: An approach to organising data where the teams closest to the
  data own it as a product, with shared rules and platform support.
category: Data architecture
tags:
  - data architecture
  - data governance
  - data products
status: established
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as a single tool or database instead of a way of organising teams, rules, and data products.
  - Assuming it means chaos or no central control; the model still needs shared standards and governance.
related_terms:
  - data product
  - data governance
  - domain-driven design
  - self-service platform
evidence:
  - source_title: Data Mesh Principles and Logical Architecture
    source_url: https://martinfowler.com/articles/data-mesh-principles.html
    source_type: engineering_blog
    relevance: Foundational explanation of the term and its four core principles.
    key_point: Describes data mesh as built on domain-oriented ownership, data as a product, self-serve data infrastructure, and federated computational governance.
  - source_title: Data mesh - Data Analytics Lens
    source_url: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/data-mesh.html
    source_type: standards_doc
    relevance: Shows how a major cloud provider frames data mesh for real systems.
    key_point: Defines it as a pattern that gives domain experts control over data products within a decentralised governance framework.
  - source_title: Architecture and functions in a data mesh
    source_url: https://docs.cloud.google.com/architecture/data-mesh
    source_type: official_docs
    relevance: Current Google Cloud documentation that clarifies practical meaning.
    key_point: Calls data mesh an architectural and organisational framework where teams that understand the data create data products under organisation-wide governance standards.
---

Data mesh is a way of organising data so that the teams closest to the data own it and manage it like a product.

In practice, this means a sales team, finance team, or logistics team is responsible for the data it creates and uses, instead of sending everything to one central data team. Shared rules and a shared platform help those teams publish data that other people can find, trust, and use.

It matters because large organisations often slow down when one central team has to do all the data work. Data mesh tries to remove that bottleneck and make data easier to share across the business.

It is not a single database, a dashboard tool, or a replacement for good data governance. It is also not the same thing as a service mesh. It is a design approach for teams, rules, and data systems.
