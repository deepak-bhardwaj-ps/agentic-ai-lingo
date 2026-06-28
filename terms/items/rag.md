---
slug: rag
title: RAG
short_description: RAG means a language model looks up relevant information before
  it answers.
category: Context
tags: []
status: Established
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse: []
related_terms: []
evidence: []
---

RAG means retrieval-augmented generation. It is a way for a language model to look up relevant information before it writes an answer.

In practice, the system searches a set of documents, picks the most useful parts, and gives them to the model as extra context. The model then uses that context to answer the question. This helps when the answer needs current, private, or specialised information.

RAG matters because language models do not automatically know everything, and their built-in knowledge can be incomplete or out of date. Looking up the right source first can make answers more useful and easier to check.

RAG is not the same as memory. It is not a guarantee that the answer is right. If the search step finds the wrong material, the answer can still be wrong. It is also not just "using search" unless the retrieved text is actually used to shape the answer.
