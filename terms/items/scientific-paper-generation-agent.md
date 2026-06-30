---
title: Scientific paper generation agent
short_description: An AI system that drafts scientific papers, usually from prompts, notes, or research materials.
category: Industry verticals
tags:
  - scientific-writing
  - research-agent
  - paper-generation
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a settled technical standard when it is mostly an emerging label.
  - Confusing paper generation with research idea generation, literature search, or peer review.
related_terms:
  - scientific writing
  - research agent
  - literature review
  - peer review
evidence:
  - source_title: CAJAL GitHub repository
    source_url: https://github.com/Agnuxo1/CAJAL
    source_type: official_docs
    relevance: The project describes a concrete local system for generating scientific papers, which shows how the term is used in practice.
    key_point: CAJAL is presented as a local scientific paper generator that runs on the user’s machine and is meant to produce publication-style academic text.
  - source_title: ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models
    source_url: https://arxiv.org/abs/2404.07738
    source_type: research_paper
    relevance: This paper shows the adjacent research pattern of agents that generate and refine scientific work from literature and feedback.
    key_point: ResearchAgent automatically defines problems, proposes methods, designs experiments, and iteratively revises them with LLM-based reviewing agents.
  - source_title: BadScientist: Can a Research Agent Write Convincing but Unsound Papers?
    source_url: https://openreview.net/forum?id=7MPstNz66e
    source_type: research_paper
    relevance: This paper matters because it names a paper-generation agent directly and shows the risk that generated papers can look convincing without being sound.
    key_point: BadScientist evaluates whether fabrication-oriented paper generation agents can produce papers that fool LLM reviewers, which makes clear that paper generation is an agent task, not just text summarisation.
---

Scientific paper generation agent is an AI system that tries to draft a scientific paper for you.

In practice, it usually takes prompts, notes, or research material and turns them into a paper-shaped draft with sections such as the introduction, methods, results, and conclusion. Some systems also add citations or formatting.

The term matters because it describes a more specific job than “chatbot”. A paper generation agent is meant to help with writing a research paper, not just answer questions about science.

It is not the same as a literature search tool, a peer-review agent, or a research-idea generator. The phrase is still emerging, so different projects may use it in slightly different ways.
