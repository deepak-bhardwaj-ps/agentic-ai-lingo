---
title: BioASQ
short_description: Biomedical question-answering and semantic indexing challenge and benchmark.
category: Evals
tags:
  - biomedical
  - question-answering
  - benchmark
status: draft
aliases: []
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
  - Treating BioASQ as a model or dataset instead of a challenge with benchmark tasks.
  - Assuming it covers general-purpose question answering rather than biomedical search and QA.
related_terms:
  - biomedical question answering
  - semantic indexing
  - benchmark dataset
  - information retrieval
evidence:
  - source_title: The Challenge | BioASQ
    source_url: https://www.bioasq.org/
    source_type: official_docs
    relevance: Official project page describing what BioASQ is and the kinds of tasks it runs.
    key_point: BioASQ organises challenges in biomedical semantic indexing and question answering.
  - source_title: Challenge Overview | BioASQ
    source_url: https://www.bioasq.org/participate/challenges
    source_type: official_docs
    relevance: Shows the current task structure and how systems are evaluated.
    key_point: BioASQ tasks use benchmark datasets with training and test biomedical questions, gold answers, relevant articles, snippets, exact answers, and ideal answers.
  - source_title: An overview of the BIOASQ large-scale biomedical semantic indexing and question answering competition
    source_url: https://link.springer.com/article/10.1186/s12859-015-0564-6
    source_type: research_paper
    relevance: Peer-reviewed overview paper that defines the scope of the competition.
    key_point: BioASQ is a competition for semantic indexing of biomedical articles and for answering natural-language biomedical questions using biomedical articles and ontologies.
---
BioASQ is a biomedical question-answering challenge and benchmark.

It is used to test systems that can search biomedical sources and answer questions in a way people can use. The tasks are not just about picking a label. They can also ask a system to find relevant articles, choose supporting snippets, give a short exact answer, and write a fuller answer.

BioASQ matters because biomedical text is large, technical, and hard to search well. A benchmark like this helps researchers compare systems on the same questions and see which ones do better at finding and summarising the right evidence.

BioASQ is not a general chat assistant and not just a single dataset. It is a long-running challenge with several tasks, and the exact format can change by year. It is also not the same thing as biomedical question answering in general, though it is one of the best-known benchmarks in that area.
