---
title: LongBench-Chat
short_description: Benchmark for testing whether LLMs can follow instructions across very long chat or document contexts.
category: Evals and benchmarks
tags:
  - long-context
  - benchmark
  - llm-evaluation
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a model or product instead of an evaluation benchmark
  - Assuming it measures general intelligence rather than long-context instruction-following
  - Confusing it with the broader LongBench benchmark
related_terms:
  - LongBench
  - long-context evaluation
  - instruction tuning
  - long-context alignment
evidence:
  - source_title: LongAlign: A Recipe for Long Context Alignment of Large Language Models
    source_url: https://arxiv.org/abs/2401.18058
    source_type: research_paper
    relevance: This is the paper that introduced LongBench-Chat, so it is the primary source for what the term means.
    key_point: The paper presents LongBench-Chat as a benchmark for evaluating instruction-following on long-context inputs, with queries in the 10k to 100k range.
  - source_title: THUDM/LongAlign
    source_url: https://github.com/THUDM/LongAlign
    source_type: engineering_blog
    relevance: The project repository states how the benchmark is used in practice and clarifies that it is part of the long-context alignment work.
    key_point: The README describes LongBench-Chat as a benchmark for real-user long-context queries and notes GPT-4 is used as the evaluator.
  - source_title: GATEAU: Selecting Influential Sample for Long Context Alignment
    source_url: https://arxiv.org/abs/2410.15633
    source_type: research_paper
    relevance: This later paper summarises LongBench-Chat’s size and task mix, which helps confirm the benchmark’s scope.
    key_point: It describes LongBench-Chat as 50 real-world queries spanning reasoning, coding, summarisation, and multilingual translation over long contexts.
---

LongBench-Chat is a benchmark used to test whether a language model can follow instructions when the input is very long.

In practice, it gives a model long prompts or chat histories and checks how well the answer matches the task. The focus is on long-context instruction-following, not on training the model.

It matters because many models work well on short prompts but lose track when they must read a lot of text first. LongBench-Chat helps compare models on that harder case.

It is not the same as LongBench. LongBench is the broader benchmark family for long-context understanding, while LongBench-Chat is the chat and instruction-following part of that work.
