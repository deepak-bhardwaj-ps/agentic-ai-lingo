---
title: CAJAL
short_description: 'A local model family for generating scientific papers.'
category: Evals and benchmarks
tags:
  - scientific-writing
  - local-models
status: active
aliases: []
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating CAJAL as a benchmark instead of a model family and paper-writing system.
  - Assuming it is a general-purpose chat model when the published materials present it as specialised for scientific writing.
related_terms:
  - CAJAL-9B
  - scientific writing
  - local LLM
  - benchmark
evidence:
  - source_title: CAJAL GitHub repository
    source_url: https://github.com/Agnuxo1/CAJAL
    source_type: official_docs
    relevance: The project’s own README gives the clearest definition of what CAJAL is and what it is for.
    key_point: CAJAL is described as a local scientific paper generator and as a project for generating publication-ready scientific papers on the user’s machine.
  - source_title: CAJAL-4B-P2PCLAW model card
    source_url: https://huggingface.co/Agnuxo/CAJAL-4B-P2PCLAW
    source_type: official_docs
    relevance: The model card shows how the term is used in practice inside the model family and confirms the scientific-writing focus.
    key_point: The model card labels CAJAL as a scientific paper generation model, gives a 4B parameter size, and presents it as fully local.
  - source_title: P2PCLAW paper on arXiv
    source_url: https://arxiv.org/abs/2604.19792
    source_type: research_paper
    relevance: This paper matters because CAJAL is presented as part of the wider P2PCLAW ecosystem, so it helps separate the model family from the broader platform.
    key_point: The paper describes P2PCLAW as a decentralised autonomous peer-review network for scientific research, which is the broader system around CAJAL.
---

CAJAL is a local model family and tool for writing scientific papers.

In practice, it is meant to help produce structured academic text on a user’s own computer, rather than sending the work to a cloud service. The published materials describe it as a specialised system for scientific paper generation.

The term matters because it is not a general chat model and not the same thing as a benchmark. It names a specific project with a narrow use case: drafting scientific papers, often with related tools in the P2PCLAW ecosystem.

CAJAL is not a standard evaluation name by itself. If someone uses it that way, they are probably mixing it up with the benchmark or the wider platform around it.
