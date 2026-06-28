---
slug: data-fabric
title: Data Fabric
short_description: A data fabric is a layer that helps people find, connect, govern,
  and use data across many systems.
category: Context
tags:
- data-architecture
- data-management
- metadata
- governance
status: established
aliases:
- data fabric
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse:
- Treating it as one product instead of an architecture pattern
- Confusing it with data mesh
- Assuming it removes the need for data cleaning or governance
related_terms:
- data mesh
- metadata
- data governance
- data integration
- data lakehouse
evidence:
- source_title: What Is a Data Fabric?
  source_url: https://www.ibm.com/think/topics/data-fabric
  source_type: official_docs
  relevance: Current vendor definition and practical description of data fabric.
  key_point: IBM describes data fabric as a modern data architecture that uses metadata,
    automation, governance, and access services to connect distributed data.
- source_title: What is data fabric? Architecture, benefits, and uses
  source_url: https://www.sap.com/resources/what-is-data-fabric
  source_type: official_docs
  relevance: Current vendor explanation of how the term is used in practice.
  key_point: SAP describes data fabric as a unified data layer that connects, governs,
    and delivers data across systems using shared metadata and automation.
- source_title: Data Mesh Principles and Logical Architecture
  source_url: https://martinfowler.com/articles/data-mesh-principles.html
  source_type: engineering_blog
  relevance: Useful contrast for separating data fabric from data mesh.
  key_point: Martin Fowler’s data mesh article shows that data mesh is a different
    architectural idea focused on decentralised ownership and federated governance.
---

Data fabric is a way of joining up data spread across many systems so people can find it, trust it, and use it more easily.

In practice, it is a layer of tools and rules that connects different databases, data platforms, and apps. It often uses metadata, which is data about data, to help track where information came from, who can use it, and how it should be handled.

It matters because many organisations keep data in separate places. A data fabric tries to make that data feel more connected, so teams do not have to build a new connection and policy system every time they need data from somewhere else.

It is not the same as [[Data Mesh|data mesh]]. [[Data Mesh|Data mesh]] is more about giving different teams responsibility for their own data. Data fabric is more about providing a shared layer that helps connect a[[Context Collapse|n]]d govern data across systems.

It is also not magic. It does not automatically fix bad data, and it does not remove the need for clear ownership, cleaning, or rules.
