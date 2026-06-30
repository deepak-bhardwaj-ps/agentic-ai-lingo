---
title: LongBench
short_description: A bilingual benchmark for testing long-context understanding in large language models
category: Evals
tags: [benchmark, long-context, evals, llm]
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating LongBench as a model, product, or dataset name instead of a benchmark.
  - Assuming a good LongBench score means a model is reliable on every long-document task.
  - Mixing up LongBench with LongBench v2, which is a later and separate benchmark.
related_terms:
  - long-context benchmark
  - long-context understanding
  - LongBench v2
  - L-Eval
evidence:
  - source_title: LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding
    source_url: https://arxiv.org/abs/2308.14508
    source_type: research_paper
    relevance: This is the original paper that defines LongBench and explains what tasks it covers.
    key_point: LongBench is introduced as the first bilingual, multi-task benchmark for long-context understanding, with 21 datasets across six task categories in English and Chinese.
  - source_title: LongBench README
    source_url: https://github.com/THUDM/LongBench/blob/main/LongBench/README.md
    source_type: engineering_blog
    relevance: This is the project’s own documentation and confirms how the benchmark is described for users.
    key_point: The repository describes LongBench as a benchmark for bilingual, multitask assessment of long-context understanding in large language models.
  - source_title: LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding
    source_url: https://aclanthology.org/2024.acl-long.172/
    source_type: research_paper
    relevance: This is the ACL publication of the benchmark and reinforces the formal definition.
    key_point: The paper says LongBench standardises datasets into a unified format for automatic evaluation of long-context understanding.
---
LongBench is a benchmark for checking how well a large language model understands long pieces of text.

In practice, it gives a model long documents, long chats, or other extended text and tests whether it can answer questions, summarise, or complete tasks from that context. It was designed for both English and Chinese, which makes it more than a single-language test.

It matters because many models work well on short text but struggle when the useful information is spread across a long document. LongBench helps compare models on that specific weakness.

LongBench is not a model, and it is not proof that a model will work well in real work with long documents. It is also not the same thing as LongBench v2, which is a later benchmark with a different design.
