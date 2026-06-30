---
title: Knowledge graph
short_description: A way of storing facts as linked things and relationships so software can understand connections between them.
category: Knowledge and wiki systems
tags:
  - graph
  - linked-data
  - semantic-web
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating it as the same thing as a graph database. A graph database is the storage tool; a knowledge graph is the connected model of facts.
  - Treating any diagram with boxes and arrows as a knowledge graph.
  - Assuming it always uses artificial intelligence. It can help AI, but it is not the same as AI.
related_terms:
  - graph database
  - RDF
  - linked data
  - semantic web
  - ontology
  - entity relationship
evidence:
  - source_title: RDF 1.2 Concepts and Abstract Data Model
    source_url: https://www.w3.org/TR/rdf12-concepts/
    source_type: standards_doc
    relevance: W3C is the main standards body behind RDF, which is one of the most common foundations for knowledge graphs.
    key_point: RDF describes information as triples, and an RDF graph is a set of those triples. That matches the core idea of a knowledge graph: facts connected by named relationships.
  - source_title: W3C Workshop on Web Standardization for Graph Data
    source_url: https://www.w3.org/Data/events/data-ws-2019/
    source_type: standards_doc
    relevance: This W3C workshop explains how knowledge graphs are used in enterprises, not just in research.
    key_point: It describes enterprise knowledge graphs as actively maintained models of entities, their types, their properties, and their relationships, and says RDF and Linked Data can form a foundation for them.
  - source_title: Enterprise Knowledge Graph overview
    source_url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview
    source_type: official_docs
    relevance: Google Cloud shows the term in a current product and explains what the system is meant to do in practice.
    key_point: It says enterprise knowledge graphs organise siloed information into organisational knowledge by consolidating, standardising, and reconciling data.
  - source_title: What is a knowledge graph?
    source_url: https://neo4j.com/blog/knowledge-graph/what-is-knowledge-graph/
    source_type: engineering_blog
    relevance: Neo4j is a major graph database vendor, and its explanation is useful for distinguishing the model from the storage technology.
    key_point: It describes knowledge graphs as organised representations of real-world entities and their relationships, which helps separate the concept from a simple database.
---

A knowledge graph is a way of organising facts so that things and the links between them are stored together.

In practice, it records entities such as a person, a place, or a product, then connects them with named relationships such as “works for”, “lives in”, or “bought”. This makes it easier for software to see how information fits together.

The term matters because linked facts are easier to search, combine, and reason over than scattered data in separate systems. That is why knowledge graphs are often used for search, recommendations, data integration, and enterprise knowledge systems.

It is not the same as a graph database. A graph database is the software used to store or query the data. A knowledge graph is the connected set of facts itself. It is also not just any picture with boxes and arrows.
