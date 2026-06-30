---
title: LAB
short_description: A biology benchmark for testing whether an AI system can handle practical research tasks
category: Evals and benchmarks
tags:
  - benchmark
  - biology
  - evals
status: draft
aliases:
  - LAB-Bench
  - Language Agent Biology Benchmark
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating LAB as a general science benchmark instead of a biology-focused one.
  - Thinking a high score means the system can safely do real laboratory work on its own.
  - Treating LAB and LAB-Bench as different things when LAB is usually just the short form.
related_terms:
  - Biological reasoning benchmark
  - Biology benchmark
  - Bioinformatics benchmark
  - Scientific benchmark
  - Benchmark suite
evidence:
  - source_title: LAB-Bench: Measuring Capabilities of Language Models for Biology Research
    source_url: https://www.futurehouse.org/research-announcements/lab-bench-measuring-capabilities-of-language-models-for-biology-research
    source_type: official_docs
    relevance: Shows the term’s original public meaning and confirms that LAB stands for the biology benchmark.
    key_point: FutureHouse says its eval set is called the Language Agent Biology Benchmark, or LAB-Bench, and that it contains practical biology research tasks.
  - source_title: LAB-Bench: Measuring Capabilities of Language Models for Biology Research
    source_url: https://arxiv.org/abs/2407.10362
    source_type: research_paper
    relevance: Gives the technical definition of the benchmark and explains the kinds of tasks it measures.
    key_point: The paper defines LAB-Bench as a broad dataset for evaluating practical biology research capabilities such as literature reasoning, figure interpretation, database use, and DNA or protein sequence work.
  - source_title: futurehouse/lab-bench dataset card
    source_url: https://huggingface.co/datasets/futurehouse/lab-bench
    source_type: official_docs
    relevance: Confirms that LAB-Bench is a published evaluation dataset, not just a paper title.
    key_point: The dataset card describes LAB-Bench as an evaluation dataset for AI systems intended to benchmark capabilities needed for scientific research in biology.
---

LAB is short for LAB-Bench, which means Language Agent Biology Benchmark. It is a test set used to see how well an AI system can handle practical biology research tasks.

In practice, LAB asks the system to do things like read biology papers, understand figures or tables, work with DNA or protein sequences, and use biological databases.

This matters because biology work is more than memorising facts. A benchmark like LAB helps people check whether a system can deal with real research-style tasks, not just simple quiz questions.

LAB is not a real laboratory, and it does not prove that an AI system can do science safely or independently. It is also not a general science benchmark for all subjects.
