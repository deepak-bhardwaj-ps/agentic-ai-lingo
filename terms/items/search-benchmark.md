---
title: Search benchmark
short_description: A fixed test used to measure how well a search system finds the right information.
category: Evals
tags:
  - benchmark
  - search
  - retrieval
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
  - Treating any search-related test as a benchmark, even when the tasks or scoring change from run to run.
  - Assuming a good benchmark score means the search system will work equally well for real users.
  - Confusing search benchmarks with agent benchmarks that also check tool use, planning, or long multi-step behaviour.
related_terms:
  - Information retrieval
  - Retrieval benchmark
  - Benchmark suite
  - Search evaluation
  - Ranking metric
evidence:
  - source_title: Text Retrieval Conference (TREC)
    source_url: https://trec.nist.gov/
    source_type: standards_doc
    relevance: NIST’s long-running retrieval programme is a direct example of search benchmarking with shared tasks and scoring.
    key_point: TREC is an evaluation workshop series for measuring the effectiveness of search algorithms and other technologies that help people find information.
  - source_title: TREC Video Retrieval Evaluation Home Page
    source_url: https://www.nist.gov/programs-projects/trec-video-retrieval-evaluation-trecvid
    source_type: standards_doc
    relevance: Shows that search benchmarks are built around a fixed test collection and uniform scoring procedures, not ad hoc judgments.
    key_point: NIST says the goal is to provide a large test collection, uniform scoring procedures, and a way to compare results.
  - source_title: BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models
    source_url: https://arxiv.org/abs/2104.08663
    source_type: research_paper
    relevance: Gives a modern, widely used example of a search benchmark for text retrieval across multiple datasets and domains.
    key_point: BEIR is presented as a robust benchmark for information retrieval that combines 18 public datasets from diverse text retrieval tasks.
  - source_title: BrowseComp: a benchmark for browsing agents
    source_url: https://openai.com/index/browsecomp/
    source_type: official_docs
    relevance: Helps distinguish search benchmarks from agent benchmarks that involve browsing as part of a larger task.
    key_point: OpenAI describes BrowseComp as a benchmark for browsing agents that measures the ability to locate hard-to-find information.
---
Search benchmark is a fixed test used to measure how well a search system finds the right information.

In practice, people give the same search tasks to different systems and score how well each one finds the right results. The test may measure things like whether the best answer appears near the top, whether the system retrieves enough relevant items, or how well it handles different topics.

This matters because it gives teams a fair way to compare search systems over time and against each other. It can show whether a change really improved search quality, instead of just making the system look better in a demo.

A search benchmark is not the same as a live search product. A high score does not prove that real users will always get good results. It is also not the same as an agent benchmark, which checks whether an AI system can take actions, use tools, and complete a longer task.
