---
title: Human evaluation
short_description: Judging an AI system by having people review its outputs or task results.
category: Evals and benchmarks
tags:
  - evals
  - benchmarks
  - human-judgement
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating it as the same as an automated benchmark score.
  - Assuming it is always more objective or more reliable than a well-designed rubric or test set.
  - Confusing it with human-in-the-loop approval for taking actions.
related_terms:
  - evaluation
  - benchmark
  - rubric
  - grader
  - human-in-the-loop
evidence:
  - source_title: GenAI - Evaluating Generative AI
    source_url: https://ai-challenges.nist.gov/genai
    source_type: official_docs
    relevance: NIST treats human studies as part of evaluation for generative AI, which matches the term's use in modern AI testing.
    key_point: NIST includes conducting human studies to compare human performance with AI system performance as part of GenAI evaluation.
  - source_title: Evaluation best practices
    source_url: https://developers.openai.com/api/docs/guides/evaluation-best-practices
    source_type: official_docs
    relevance: Shows that AI evaluation is based on clear criteria, which human reviewers can apply directly when judging outputs.
    key_point: OpenAI describes evals as structured tests with specific criteria for measuring model performance.
  - source_title: Rethinking Human Evaluation for Generative Large Language Models
    source_url: https://arxiv.org/html/2405.18638v1
    source_type: research_paper
    relevance: Explains why human evaluation is important for generative models and why it needs careful design.
    key_point: The paper argues that human evaluation is useful for generative LLMs, but it must be designed well to measure the right thing.
---
Human evaluation is a way of testing an AI system by asking people to judge its outputs or results.

In practice, humans may rate answers, compare two outputs, check whether a response follows a rubric, or decide whether a task was completed well. This is often used when the thing being tested is hard to measure with a simple number, such as helpfulness, clarity, safety, or whether an answer really makes sense.

It matters because some AI behaviour is too messy for a fully automatic score. A person can notice mistakes, weak reasoning, rude language, or other problems that a simple metric might miss.

Human evaluation is not the same as human-in-the-loop approval. Human evaluation is about judging quality. Human-in-the-loop is about a person stepping in while the system is running or before it takes an action.
