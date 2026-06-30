---
title: Hallucination benchmark
short_description: A test used to measure how often a model gives false or unsupported answers.
category: Evals
tags:
  - benchmark
  - evals
  - hallucination
  - factuality
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating any factuality test as a full hallucination benchmark, even when it only checks one narrow kind of error.
  - Assuming one score tells you how well a model avoids hallucinations in every setting.
  - Confusing a hallucination benchmark with a general benchmark for overall model quality.
related_terms:
  - Hallucination
  - Factuality benchmark
  - Evaluation
  - Benchmark suite
  - Abstention
  - Calibration
evidence:
  - source_title: Why language models hallucinate
    source_url: https://openai.com/index/why-language-models-hallucinate/
    source_type: official_docs
    relevance: Gives a current, plain definition of hallucinations as confident but false answers and explains why benchmarks can reward guessing.
    key_point: OpenAI describes hallucinations as instances where a model confidently generates an answer that is not true, and says many evaluations encourage guessing rather than honest uncertainty.
  - source_title: Introducing SimpleQA
    source_url: https://openai.com/index/introducing-simpleqa/
    source_type: official_docs
    relevance: Shows a current official example of a benchmark built to measure factuality and hallucination-like mistakes on short, fact-seeking questions.
    key_point: OpenAI describes SimpleQA as a factuality benchmark for short fact-seeking questions and says it was designed to measure hallucinations in a tractable way.
  - source_title: Demystifying evals for AI agents
    source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    source_type: engineering_blog
    relevance: Defines what an eval is and helps distinguish a benchmark or eval from a general product claim.
    key_point: Anthropic says an eval is a test for an AI system, with input and grading logic, which is the basic structure a hallucination benchmark uses.
  - source_title: HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models
    source_url: https://arxiv.org/abs/2305.11747
    source_type: research_paper
    relevance: Shows a well-known research benchmark built specifically to evaluate hallucination recognition, confirming the term is used for targeted test sets.
    key_point: The paper introduces HaluEval as a large collection of generated and human-annotated hallucinated samples for evaluating how well LLMs recognise hallucination.
---
A hallucination benchmark is a test that checks how often an AI model gives answers that are false, made up, or not supported by the evidence.

In practice, it gives the model questions or tasks with known answers, then scores whether the model stays accurate, admits uncertainty, or makes up details. Some hallucination benchmarks focus on short fact questions. Others test whether a model can spot hallucinated text.

This matters because a model can sound confident and still be wrong. A hallucination benchmark helps teams see that problem more clearly and compare models over time.

It is not a full measure of intelligence, and it is not proof that a model will be reliable in real use. It is also not the same as a general benchmark for coding, reasoning, or chat quality.
