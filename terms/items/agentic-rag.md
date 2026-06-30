---
title: Agentic RAG
short_description: A still-evolving term for RAG systems that can choose, repeat, or adjust retrieval steps while answering.
category: Agentic patterns
tags:
- retrieval-augmented generation
- agents
- tool use
- orchestration
status: active
aliases:
- agentic retrieval-augmented generation
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating any RAG system with search or reranking as agentic
- Using the term for a fully autonomous agent that is no longer doing RAG
related_terms:
- retrieval-augmented generation
- agentic workflow
- tool use
- orchestration
- multi-agent system
evidence:
- source_title: Agentic Retrieval Augmented Generation (RAG) in Amazon Q Business
  source_url: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/agentic-rag.html
  source_type: official_docs
  relevance: AWS uses the term directly and contrasts it with standard RAG, which helps define the core idea as retrieval plus more adaptive agent behaviour.
  key_point: Agentic RAG adds agentic retrieval and response steps on top of standard document retrieval and simple generation.
- source_title: Building Agents with Retrieval-Augmented Generation
  source_url: https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/7-advanced-agent-capabilities/building-agents-with-retrieval-augmented-generation
  source_type: industry_article
  relevance: Google Cloud uses the phrase for end-to-end systems that combine retrieval with agent behaviour, showing the term is applied to multi-step agentic applications rather than plain search.
  key_point: The lab describes building end-to-end agentic RAG applications that combine multiple sources and agent steps.
- source_title: Tool use with Claude
  source_url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
  source_type: official_docs
  relevance: Anthropic’s tool-use guidance explains the kind of model behaviour agentic RAG depends on, namely choosing when to call tools during a run.
  key_point: The model can decide when to call a tool based on the request and the tool description, which is the control pattern behind agentic retrieval.
- source_title: Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG
  source_url: https://arxiv.org/abs/2501.09136
  source_type: research_paper
  relevance: The survey shows that the term is still being formalised in research and is used to describe iterative retrieval, planning, and adaptive control.
  key_point: Agentic RAG is described as iterative, adaptive retrieval with autonomous decision-making, which supports treating it as an emerging and unsettled term.
---

Agentic RAG is a type of retrieval-augmented generation where the system does not just fetch information once and answer. It can choose, repeat, or change its retrieval steps while it works.

In practice, that means the system may search, notice the first results are not enough, try a different query, use another tool, or bring in more sources before giving an answer. The retrieval part is still important, but the system has more control over how it finds and uses information.

The term matters because some questions are too broad, messy, or changing too fast for a single search step to work well. Agentic RAG is meant to improve the chances of finding the right material, but it can also take more time and cost more to run.

It is not the same as plain RAG, where the system usually retrieves once and then answers. It is also not just any chatbot with search, and it is not the same as a fully autonomous agent that acts without a retrieval step.
