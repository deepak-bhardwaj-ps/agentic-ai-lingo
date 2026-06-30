---
title: Red-team benchmark
short_description: A benchmark that uses adversarial prompts, attacks, or probes to test how a model or agent fails under pressure
category: Evals
tags: [benchmark, red-teaming, evals, safety, security]
status: draft
aliases: []
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a normal benchmark with no adversarial setup.
  - Assuming one red-team score proves the system is safe in real use.
  - Mixing up safety red teaming with offensive security testing or with general evaluation.
related_terms:
  - red teaming
  - adversarial evaluation
  - safety benchmark
  - prompt injection
  - jailbreak
  - security benchmark
evidence:
  - source_title: OpenAI's Approach to External Red Teaming for AI Models and Systems
    source_url: https://cdn.openai.com/papers/openais-approach-to-external-red-teaming.pdf
    source_type: research_paper
    relevance: Defines red teaming as a way to probe AI systems for issues, attacks, and failure modes, which is the core idea behind a red-team benchmark.
    key_point: OpenAI describes red teaming as part of AI risk assessment and notes that it can be paired with benchmarks, showing that adversarial testing is adjacent to, and often measured by, benchmark-style evaluation.
  - source_title: Advancing red teaming with people and AI
    source_url: https://openai.com/index/advancing-red-teaming-with-people-and-ai/
    source_type: engineering_blog
    relevance: Shows the practical meaning of red teaming in current AI work and how automated attacks are used to find weaknesses at scale.
    key_point: OpenAI says red teaming probes an AI model or system to identify issues and attacks, and that automated red teaming can generate examples at larger scale.
  - source_title: ALERT: A Comprehensive Benchmark for Assessing Large Language Models' Safety through Red Teaming
    source_url: https://arxiv.org/abs/2404.08676
    source_type: research_paper
    relevance: Directly uses red teaming as a benchmark method for safety evaluation, which supports the benchmark reading of the term.
    key_point: The paper presents ALERT as a large-scale benchmark that assesses safety through red-teaming methods and adversarial testing scenarios.
  - source_title: AIRTBench: Measuring Autonomous AI Red Teaming Capabilities in Language Models
    source_url: https://arxiv.org/abs/2506.14682
    source_type: research_paper
    relevance: Shows the term being used today for a concrete benchmark name, not just a general testing approach.
    key_point: The paper defines AIRTBench as an AI red teaming benchmark for evaluating whether models can autonomously find and exploit security weaknesses.
---
Red-team benchmark is a benchmark that uses adversarial prompts, attacks, or probes to see how a model or agent fails under pressure.

In practice, people use it to test for weak spots such as unsafe answers, prompt injection, jailbreaks, or other ways the system can be pushed off course. The test is usually set up so the same model or agent can be checked against the same kinds of attacks and compared with other systems.

It matters because a model can look fine in ordinary use but break when someone tries to trick it. A red-team benchmark helps teams find those failures before users or attackers do.

It is not the same as a normal benchmark with friendly test questions. It is also not proof that a system is safe in every real situation. The term is a bit loose, so it can mean a safety benchmark, a security benchmark, or a benchmark built around adversarial attacks.
