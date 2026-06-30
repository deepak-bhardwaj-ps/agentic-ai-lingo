---
title: Abstention
short_description: A model or evaluator chooses not to give an answer when it is unsure or the question cannot be answered safely.
category: Evals
tags:
  - evaluation
  - uncertainty
  - selective-classification
  - refusal
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating abstention as the same as safety refusal. In evals, abstention often means “I don’t know” or “no answer” because the model is unsure, not because the request is unsafe.
  - Treating it as a failure by default. In many benchmarks, a correct abstention is better than a wrong answer.
  - Using it to mean silence or empty output. Abstention usually means an explicit choice not to answer.
related_terms:
  - selective-classification
  - uncertainty
  - refusal
  - hallucination
  - confidence-calibration
evidence:
  - source_title: Know Your Limits: A Survey of Abstention in Large Language Models
    source_url: https://arxiv.org/html/2407.18418v3
    source_type: research_paper
    relevance: This survey gives the clearest current definition of abstention in LLMs and shows how the term is used across queries, models, and human-value constraints.
    key_point: Abstention is the refusal of an LLM to provide an answer, especially when the query is unanswerable, the model is uncertain, or the response would be misaligned with human values.
  - source_title: Optimal Strategies for Reject Option Classifiers
    source_url: https://jmlr.org/papers/v24/21-0048.html
    source_type: research_paper
    relevance: This is the classic machine-learning framing behind abstention: a classifier may reject or abstain instead of forcing a prediction.
    key_point: In classification with a reject option, the model is allowed to abstain on uncertain cases, trading off fewer wrong answers against lower coverage.
  - source_title: Why language models hallucinate
    source_url: https://openai.com/index/why-language-models-hallucinate/
    source_type: engineering_blog
    relevance: This explains why modern LLM evaluations matter for abstention: if tests reward guessing, models learn to answer when they should say they are unsure.
    key_point: Standard training and evaluation can reward guessing over admitting uncertainty, which encourages hallucinations instead of abstention.
---
Abstention is when a model decides not to answer a question.

In evaluation work, this usually means the model says, in effect, “I do not know,” “I cannot tell from the information given,” or gives no answer on purpose. The point is to avoid making up a confident but wrong response.

This matters because a system that knows when to stop is often safer and more useful than one that guesses. In benchmarks, abstention is usually scored as part of a trade-off: the model can answer more questions, but it may also make more mistakes. A good system should answer when it has enough evidence and abstain when it does not.

Abstention is not the same as refusing for safety reasons. A safety refusal is about not producing harmful content. Abstention is about uncertainty or missing information. It is also not the same as being silent by accident. It is a deliberate choice.
