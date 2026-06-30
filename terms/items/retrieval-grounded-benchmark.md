---
title: Retrieval-grounded benchmark
short_description: A benchmark that checks whether answers are supported by retrieved evidence.
category: Evals and benchmarks
tags:
  - benchmark
  - evals
  - retrieval
  - grounding
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a single official benchmark instead of a broad label for a family of tests.
  - Using it as if it only means retrieval quality, when it also checks whether the final answer stays supported by the retrieved evidence.
  - Confusing it with web search or plain question answering without evidence checks.
related_terms:
  - groundedness
  - faithfulness
  - retrieval-augmented generation
  - retrieval evaluation
  - evidence-grounded QA
evidence:
  - source_title: Demystifying evals for AI agents
    source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    source_type: engineering_blog
    relevance: Anthropic describes groundedness checks as part of research-agent evaluation, which closely matches the idea behind retrieval-grounded benchmarks.
    key_point: Groundedness checks verify that claims are supported by retrieved sources, while coverage and source-quality checks test whether the right evidence was found and used.
  - source_title: Retrieval
    source_url: https://developers.openai.com/api/docs/guides/retrieval
    source_type: official_docs
    relevance: OpenAI shows retrieval systems are meant to produce grounded responses from search results, which is the behaviour these benchmarks measure.
    key_point: Retrieved results can be supplied back to a model so it can generate a grounded response rather than answer from memory alone.
  - source_title: Faithfulness - Ragas
    source_url: https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/
    source_type: official_docs
    relevance: Ragas gives a current, explicit grounding-style metric for RAG, showing how the field measures support from retrieved context.
    key_point: Faithfulness measures whether a response is factually consistent with the retrieved context and whether its claims are supported by that context.
  - source_title: MIRAGE: A Benchmark for Medical Information Retrieval-Augmented Generation Evaluation
    source_url: https://arxiv.org/html/2402.13178v1
    source_type: research_paper
    relevance: This is a concrete retrieval-augmented benchmark that evaluates how well systems answer using retrieved medical evidence, which is a strong example of the term in practice.
    key_point: The benchmark tests retrieval-augmented generation on medical QA, combining evidence retrieval with answer generation and evaluation.
---

A retrieval-grounded benchmark is a test that checks whether a model’s answer is supported by the evidence it was given or retrieved.

In practice, the model is asked a question, some documents or search results are retrieved, and then the answer is judged on whether it stays close to that evidence. Good scores usually mean the system found the right material and did not add unsupported claims.

This matters because a model can sound confident and still make things up. These benchmarks help teams see whether a system is using evidence properly, especially in retrieval-augmented generation and research assistants.

It is not the same as a plain retrieval benchmark, which only checks whether the right documents were found. It is also not just general factual accuracy, because the answer may be judged against the retrieved sources, not the whole world.
