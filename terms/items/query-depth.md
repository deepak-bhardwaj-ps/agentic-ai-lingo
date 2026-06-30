---
title: Query depth
short_description: The number of hops, rounds, or steps a search or agent system takes to answer one query.
category: Knowledge and wiki systems
tags:
  - search
  - retrieval
  - rag
  - agents
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a fixed industry standard term when different systems use it to mean different things.
  - Confusing query depth with chunk depth, document depth, or model depth.
related_terms:
  - multi-hop retrieval
  - iterative retrieval
  - query decomposition
  - graph traversal
evidence:
  - source_title: Implementing a Multi-Step Agent with Langchain | Cohere
    source_url: https://docs.cohere.com/v1/docs/implementing-a-multi-step-agent-with-langchain
    source_type: official_docs
    relevance: Shows that multi-step agents answer a query by making more than one tool call in sequence, which matches the practical meaning of query depth in agent systems.
    key_point: A later step can use the result of an earlier tool call, so deeper queries require more than one round of retrieval or action.
  - source_title: X-Pack Graph explore API | Java REST Client [7.17] - Elastic
    source_url: https://www.elastic.co/guide/en/elasticsearch/client/java-rest/current/java-rest-high-x-pack-graph-explore.html
    source_type: official_docs
    relevance: Defines graph exploration in terms of hops, which is the clearest official usage of depth as the number of relationship steps taken from the original query.
    key_point: Each next hop explores another level of connections discovered from the previous level.
  - source_title: Generative Multi-hop Retrieval
    source_url: https://aclanthology.org/2022.emnlp-main.92.pdf
    source_type: research_paper
    relevance: Gives a research-backed view of query depth as the number of retrieval hops in multi-hop question answering.
    key_point: Multi-hop retrieval iterates through multiple hops, often appending prior results to the query, and the number of hops can vary by query.
---

Query depth is the number of steps a search system, graph query, or agent takes to answer one question.

In practice, a shallow query is answered in one round. A deeper query needs extra rounds, such as another search, another tool call, or another hop through related data.

The term matters because deeper queries can find better answers, but they usually take more time and cost more work.

This is not a single fixed industry standard term. Different systems use it to mean different things, most often the number of retrieval hops, graph hops, or tool-use rounds.
