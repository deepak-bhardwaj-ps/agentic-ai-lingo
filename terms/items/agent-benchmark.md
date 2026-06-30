---
title: Agent benchmark
short_description: A fixed test used to compare how well AI agents do a task
category: Evals and benchmarks
tags: [agent, benchmark, evals]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating any agent test as a benchmark, even when the tasks, scoring, or dataset are not fixed.
  - Using benchmark scores as proof that an agent works well in the real world.
  - Confusing an agent benchmark with a general model benchmark that does not include tool use or multi-step action.
related_terms:
  - Agent evals
  - Agent evaluation
  - Evals
  - Interactive benchmark
  - Multi-step task benchmark
  - Contamination-resistant benchmark
evidence:
  - source_title: Introducing SWE-bench Verified
    source_url: https://openai.com/index/introducing-swe-bench-verified/
    source_type: official_docs
    relevance: Shows a benchmark used to measure agent-like software-engineering performance on real issues.
    key_point: OpenAI describes SWE-bench as a benchmark for evaluating models on real software issues, where agents get a repository and issue description and must produce a patch.
  - source_title: MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering
    source_url: https://openai.com/index/mle-bench/
    source_type: official_docs
    relevance: Shows that agent benchmarks can target a specific job, not just general chat.
    key_point: OpenAI presents MLE-bench as a benchmark for measuring how well AI agents perform machine-learning engineering tasks drawn from real competitions.
  - source_title: BrowseComp: a benchmark for browsing agents
    source_url: https://openai.com/index/browsecomp/
    source_type: official_docs
    relevance: Shows a benchmark built for a browsing agent and explains why hard-to-find, easy-to-check tasks are useful.
    key_point: OpenAI says BrowseComp measures how well AI agents locate hard-to-find information and that benchmark tasks should be challenging but easy to verify.
  - source_title: Evaluation and Benchmarking of LLM Agents: A Survey
    source_url: https://arxiv.org/abs/2507.21504
    source_type: research_paper
    relevance: Shows that agent benchmarking is still a developing area with many different task types and scoring methods.
    key_point: The survey says LLM agent evaluation is an emerging, underdeveloped field and includes datasets and benchmarks as one part of the process.
  - source_title: Demystifying evals for AI agents
    source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    source_type: engineering_blog
    relevance: Explains why agent benchmarks and evals must measure multi-step behaviour, not just one final answer.
    key_point: Anthropic says agents act over many turns, using tools and changing state, which makes them harder to evaluate than single-response systems.
---

An agent benchmark is a fixed test used to compare how well AI agents do a task.

In practice, a benchmark gives every agent the same kind of task, the same rules, and the same way of scoring. For agent benchmarks, the task often involves more than one step, such as using tools, browsing, editing files, or making a plan and then acting on it.

This matters because it lets teams compare versions of an agent over time and compare one agent with another. A good benchmark can show whether the agent is actually getting better, not just sounding better.

An agent benchmark is not the same as a real deployment. A high score does not prove the agent will work safely or well in every situation. It is also not just a loose test someone runs once; the benchmark needs stable tasks and stable scoring, or the score is not very useful.

The term is still a bit unsettled because people use it for different kinds of agent tasks, from coding to browsing to planning. The core idea is the same: a repeatable test for measuring agent performance.
