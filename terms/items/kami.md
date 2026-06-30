---
title: KAMI
short_description: A benchmark for testing enterprise-focused agentic AI performance, including tool use and multi-step tasks.
category: Evals
tags:
  - benchmark
  - evals
  - agentic-ai
  - enterprise-ai
status: active
aliases:
  - Kamiwaza Agentic Merit Index
  - KAMI benchmark
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating KAMI as a general score for all AI models instead of a benchmark for agentic enterprise tasks.
  - Confusing KAMI with a product, model, or dataset rather than an evaluation framework and leaderboard.
  - Assuming one KAMI result proves a model is ready for every real business setting.
related_terms:
  - agent evaluation
  - benchmark suite
  - agentic AI
  - enterprise benchmark
  - contamination resistance
evidence:
  - source_title: KAMI v0.1: Enterprise-Relevant Agentic AI Benchmark
    source_url: https://docs.kamiwaza.ai/research/papers/kami-v0-1
    source_type: official_docs
    relevance: The vendor’s own paper gives the clearest definition of what KAMI means and what it is designed to measure.
    key_point: Kamiwaza describes KAMI v0.1 as an enterprise-focused benchmark for contamination resistance and agentic evaluation, including multi-step tool use and decision-making under uncertainty.
  - source_title: Towards a Standard, Enterprise-Relevant Agentic AI Benchmark
    source_url: https://docs.kamiwaza.ai/assets/files/KAMI_v0_1-6e4aecf4e5d27dd967f81eeb8c953621.pdf
    source_type: research_paper
    relevance: This paper is the formal research version of the benchmark and explains why it was built.
    key_point: The paper says KAMI was created because ordinary LLM benchmarks can be vulnerable to training-data contamination and may miss real agent behaviour in enterprise tasks.
  - source_title: Benchmarking Leadership in Open and Proprietary Models
    source_url: https://signal65.com/research/ai/benchmarking-leadership-in-open-and-proprietary-models/
    source_type: industry_article
    relevance: This later industry report shows how the benchmark is being used and framed outside the originating team.
    key_point: Signal65 says KAMI measures AI model accuracy on enterprise-focused agentic workloads and extends earlier KAMI v0.1 results.
  - source_title: Measured Leadership with Agentic AI on Open Models
    source_url: https://signal65.com/research/ai/measured-leadership-with-agentic-ai-on-open-models/
    source_type: industry_article
    relevance: This earlier report helps confirm the name and practical use of KAMI as a benchmark for agentic tasks.
    key_point: Signal65 says it collaborated with Kamiwaza to establish the KAMI benchmark for enterprise-focused agentic tasks.
---
KAMI is a benchmark for testing how well an AI agent handles enterprise-style tasks.

In practice, it checks things like whether the agent can use tools, follow a sequence of steps, handle uncertainty, and avoid making things up. It is meant to measure more than a single chat reply.

The term matters because real business work often takes several steps and depends on using the right information at the right time. A benchmark like KAMI helps people compare models on that kind of work instead of only on short question-and-answer tests.

KAMI is not a product, and it is not proof that a model is safe for every real business task. It is also not just a general AI score. It is a specific benchmark for agentic, enterprise-focused evaluation.
