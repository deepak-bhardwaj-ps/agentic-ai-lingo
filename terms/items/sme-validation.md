---
title: SME validation
short_description: A check where a subject matter expert reviews an AI evaluation, label set, or output to see whether it matches real domain judgement.
category: Evals
tags:
  - evaluation
  - human-in-the-loop
  - expert-review
status: draft
aliases:
  - subject matter expert validation
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating SME review as proof that a model is safe, correct, or ready for production.
  - Assuming one expert’s opinion settles a disputed benchmark or rubric.
  - Using the term to sound more rigorous when the work is just informal review.
related_terms:
  - expert review
  - human evaluation
  - annotation
  - benchmark validation
  - validation set
evidence:
  - source_title: Building resilient prompts using an evaluation flywheel
    source_url: https://developers.openai.com/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel
    source_type: official_docs
    relevance: Shows the term in a current AI evaluation workflow where human subject-matter experts are used as the reference point for judging output quality.
    key_point: OpenAI says performance should be measured against a human subject-matter expert using a gold-standard dataset.
  - source_title: Getting started with datasets
    source_url: https://developers.openai.com/api/docs/guides/evaluation-getting-started
    source_type: official_docs
    relevance: Confirms that subject matter experts are the right people to annotate data when the evaluator is not the domain expert.
    key_point: OpenAI recommends using a subject matter expert for annotation if you are not one yourself.
  - source_title: AI test, evaluation, validation and verification (TEVV)
    source_url: https://www.nist.gov/ai-test-evaluation-validation-and-verification-tevv
    source_type: official_docs
    relevance: Grounds the term in NIST’s broader AI testing and validation vocabulary, where validation is one part of a formal evaluation process.
    key_point: NIST treats validation as part of AI TEVV work across the lifecycle, not as a casual label for any human review.
---
SME validation means asking a subject matter expert to check whether an AI evaluation, label, or output matches real knowledge in that field.

In practice, the expert may review examples, correct labels, judge answer quality, or help write the rules used to score the system.

It matters because some things are too domain-specific for a general reviewer to judge well. A good SME can catch mistakes that look fine on paper but are wrong in practice.

It is not the same as proving a system is safe for real use. It is also not the same as full clinical, legal, or engineering validation unless the expert review is part of that larger process.
