---
title: Capability benchmark
short_description: A test used to check what an AI system can do in a specific task area.
category: Evals and benchmarks
tags:
  - benchmark
  - evaluation
  - capabilities
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it like a single score for general intelligence.
  - Assuming one benchmark covers every real-world use of a model.
  - Using it as a vague label for any AI test.
related_terms:
  - benchmark
  - evaluation
  - model capability
  - agent evaluation
  - task benchmark
evidence:
  - source_title: Practices for Automated Benchmark Evaluations of Language Models
    source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-2.ipd.pdf
    source_type: standards_doc
    relevance: NIST explains how benchmarks are selected to evaluate AI capabilities, which is the closest formal framing for this term.
    key_point: NIST says the first stage of effective AI capability evaluation is to select benchmarks that fit the evaluation objective.
  - source_title: Measuring the performance of our models on real-world tasks
    source_url: https://openai.com/index/gdpval/
    source_type: engineering_blog
    relevance: Shows the term in current use for benchmarks that measure model ability on practical tasks, not just toy questions.
    key_point: OpenAI describes GDPval as a benchmark that measures model capabilities on real-world economically valuable tasks.
  - source_title: A new initiative for developing third-party model evaluations
    source_url: https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations
    source_type: engineering_blog
    relevance: Confirms that capability-focused evaluations are used to assess model abilities and risks, while also showing that such evaluations are still limited.
    key_point: Anthropic says third-party evaluations are needed to measure advanced capabilities in AI models.
---

A capability benchmark is a test that checks what an AI system can do in a specific area.

In practice, it gives the model a set of tasks and then scores how well it performs. The tasks might check reasoning, coding, scientific thinking, or another skill. The point is to see the model’s ability in that area, not to judge every part of the model at once.

This matters because people use these benchmarks to compare models, track progress, and see where a system is still weak. A model can be strong on one capability benchmark and still fail on real work that needs more steps, more context, or better judgement.

It is not a full measure of intelligence. It is also not the same as a real job, a live product, or a general claim that the model is “capable” at everything. The term is not perfectly standard, so people should check which task area the benchmark is meant to measure.
