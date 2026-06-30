---
title: BIRD
short_description: A benchmark for testing how well systems turn plain English questions into SQL on real databases
category: Evals
tags:
  - benchmark
  - text-to-sql
  - database
  - evaluation
status: draft
aliases:
  - BIRD-bench
  - BIRD-SQL
  - Bird
meaning_type: novel
novelty_level: medium
maturity_level: established
common_misuse:
  - Treating BIRD as a general AI benchmark instead of a text-to-SQL benchmark.
  - Assuming a high score on BIRD means the system will work well on every database.
  - Ignoring that the benchmark has been criticised for noisy questions and gold SQL in some analyses.
related_terms:
  - text-to-SQL
  - SQL
  - benchmark
  - execution accuracy
  - Spider benchmark
evidence:
  - source_title: Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs
    source_url: https://arxiv.org/abs/2305.03111
    source_type: research_paper
    relevance: This is the original BIRD paper and defines what the benchmark is and why it exists.
    key_point: The paper introduces BIRD as a large benchmark for database-grounded text-to-SQL, with 12,751 questions, 95 databases, and a focus on real-world database values and SQL efficiency.
  - source_title: BIRD-bench
    source_url: https://bird-bench.github.io/
    source_type: official_docs
    relevance: This is the project site and gives the shortest current description of the benchmark.
    key_point: The site describes BIRD as the first text-to-SQL benchmark aimed at producing SQL that is both correct and efficient.
  - source_title: Understanding the Effects of Noise in Text-to-SQL: An Examination of the BIRD-Bench Benchmark
    source_url: https://aclanthology.org/2024.acl-short.34.pdf
    source_type: research_paper
    relevance: This shows that BIRD is widely used, but also that some parts of the dataset have quality issues.
    key_point: The paper reports noise in BIRD questions and gold SQL queries, which means scores on the benchmark need careful interpretation.
---
BIRD is a benchmark for testing whether an AI system can turn a plain English question into a correct SQL query on a real database.

In practice, BIRD gives a system a question and database context, then checks whether the SQL it produces gets the right answer when run on the database. It is designed to be harder and more realistic than simple schoolbook examples, because the databases are large and messy.

The term matters because it helps teams measure text-to-SQL systems in a way that is closer to real business use. It also tests more than just syntax: the system has to understand table data, not just table names.

BIRD is not a general test of “how smart” an AI is. It is also not the same as a normal chatbot benchmark. Some researchers have found noise in parts of the dataset, so a BIRD score should be read as one signal, not final proof that a system is reliable everywhere.
