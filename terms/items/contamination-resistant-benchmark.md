---
title: Contamination-resistant benchmark
short_description: A benchmark designed to stay useful even if models have seen similar tasks during training.
category: Evals
tags:
  - benchmark
  - evaluation
  - contamination
  - llm-evals
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a guarantee that the benchmark was never seen during training
  - Using the term for any recent benchmark, even if it does not try to reduce leakage or memorisation
  - Assuming a contamination-resistant benchmark proves real-world performance on its own
related_terms:
  - benchmark contamination
  - contamination
  - live benchmark
  - benchmark leakage
  - evaluation design
evidence:
  - source_title: Towards Contamination Resistant Benchmarks
    source_url: https://arxiv.org/abs/2505.08389
    source_type: research_paper
    relevance: This paper directly introduces the term and explains the idea of building benchmarks that still work when contamination is controlled.
    key_point: The authors propose contamination resistance as a benchmark property and show that a benchmark can be built to resist memorisation effects.
  - source_title: LLM Benchmark Datasets Should Be Contamination-Resistant
    source_url: https://arxiv.org/abs/2605.19999
    source_type: research_paper
    relevance: This is a current paper that defines the term in a stricter way and explains why ordinary public benchmarks become less reliable over time.
    key_point: The paper argues benchmark datasets should be unlearnable by training but still usable for inference, which is the core meaning of contamination-resistant.
  - source_title: A shared playbook for trustworthy third party evaluations
    source_url: https://openai.com/index/trustworthy-third-party-evaluations-foundations/
    source_type: official_docs
    relevance: This official guidance explains why contamination is a real problem for public or reused benchmarks and why new or private tasks are preferred.
    key_point: OpenAI says contamination matters most for public or reused benchmarks because models may memorise tasks, answers, or close variants.
  - source_title: LiveBench: A Challenging, Contamination-Free LLM Benchmark
    source_url: https://arxiv.org/abs/2406.19314
    source_type: research_paper
    relevance: This benchmark paper shows a concrete design pattern for contamination resistance: new questions, recent sources, and objective scoring.
    key_point: LiveBench is described as designed to be resistant to test set contamination by using frequently updated questions and verifiable answers.
---
Contamination-resistant benchmark is a benchmark designed so training leakage does not make the score misleading.

In practice, that means the benchmark tries to avoid problems where a model has already seen the questions, answers, or very similar examples during training. Good designs often use fresh tasks, private data, changing question sets, or answers that can be checked objectively.

This matters because a benchmark is only useful if it still tells you something real about the model. If the model has memorised the test, the score can look better than the model really is.

It is not the same as a normal benchmark, and it is not a promise that no contamination exists. It is also not a proof that a model will work well in the real world. The term is still emerging, so different papers use it a little differently, but the core idea is always about resisting memorisation and leakage.
