---
title: Contradiction flagging
short_description: Marking statements that cannot both be true so a person can review them.
category: Knowledge and wiki systems
tags:
  - knowledge management
  - consistency checking
  - natural language processing
  - wiki systems
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating any disagreement or missing detail as a contradiction.
  - Assuming an automatic flag proves one statement is wrong.
  - Confusing this with general fact-checking, which is broader.
related_terms:
  - contradiction detection
  - inconsistency detection
  - natural language inference
  - fact-checking
  - hallucination detection
evidence:
  - source_title: Finding Contradictions in Text
    source_url: https://aclanthology.org/P08-1118.pdf
    source_type: research_paper
    relevance: Early foundational paper on automatically detecting contradictions between texts.
    key_point: It frames contradiction detection as identifying when two statements conflict, which matches the core idea behind flagging a contradiction for review.
  - source_title: Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models
    source_url: https://aclanthology.org/2025.emnlp-main.1765/
    source_type: research_paper
    relevance: Current Wikimedia-focused research showing how contradiction and inconsistency finding is used on a large wiki-like knowledge base.
    key_point: It treats contradictions as measurable inconsistencies in Wikipedia and describes systems that surface candidate contradictions for human editors, which is very close to contradiction flagging in practice.
  - source_title: Contradiction detection in dialogue natural language inference
    source_url: https://aclanthology.org/P19-1363.pdf
    source_type: research_paper
    relevance: Shows the standard NLP meaning of contradiction as a statement that conflicts with earlier text.
    key_point: It defines contradiction as a consistency error where one utterance conflicts with previous utterances, supporting the idea that flagging is about marking conflicts, not automatically resolving them.
---

Contradiction flagging is the act of marking two or more statements that cannot all be true at the same time.

In a wiki or knowledge base, this usually means a tool or editor spots a clash between claims and sends it for review.

The point is to help people find possible errors, outdated facts, or mismatched entries faster.

It is not the same as proving something false. A flag is only a warning that needs checking.

It is also not the same as general fact-checking. Fact-checking can look at whether a claim is true, while contradiction flagging looks for claims that conflict with each other.
