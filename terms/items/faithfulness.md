---
title: Faithfulness
short_description: A measure of whether an answer stays supported by the context it was given.
category: Evals
tags:
- rag
- evaluation
- groundedness
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as factual correctness, even though faithfulness checks support from the provided context rather than truth in the wider world.
- Using it as a general honesty score for a person or model.
related_terms:
- groundedness
- hallucination
- factual correctness
- context precision
- response relevance
evidence:
- source_title: Faithfulness - Ragas
  source_url: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
  source_type: official_docs
  relevance: This is a current, explicit definition of the metric in a widely used RAG evaluation library.
  key_point: Faithfulness measures how factually consistent a response is with the retrieved context, and scores higher when all claims are supported by that context.
- source_title: Evaluation of Retrieval-Augmented Generation: A Survey
  source_url: https://arxiv.org/html/2405.07437v1
  source_type: research_paper
  relevance: This survey shows how faithfulness is used across RAG evaluation, which helps confirm the glossary term’s scope.
  key_point: In RAG evaluation, faithfulness checks whether the generated response reflects the information in the relevant documents and is often treated as the generation-side counterpart to groundedness or consistency.
- source_title: FaithEval: Can Your Language Model Stay Faithful to Context, Even If “The Moon is Made of Marshmallows”
  source_url: https://arxiv.org/html/2410.03727v1
  source_type: research_paper
  relevance: This paper clarifies that faithfulness is about staying aligned with the provided context, especially when the context is incomplete, contradictory, or false.
  key_point: Faithfulness is a contextual property: the model should not add unsupported claims, even if those claims sound plausible or match outside knowledge.
---
Faithfulness is how well an answer stays supported by the context it was given.

In practice, this means checking whether each claim in the answer can be backed up by the supplied documents or other context. If the answer adds facts that are not in that context, it is less faithful.

This term matters because a fluent answer can still be wrong. Faithfulness helps you spot answers that sound good but make up details, especially in retrieval-augmented generation systems where the model should stay close to the source material.

It is not the same as factual correctness. A response can be faithful to the given context even if the context itself is wrong. In this glossary, the term is also close to groundedness, but faithfulness usually focuses on whether the answer is supported by the provided context rather than whether it matches the outside world.
