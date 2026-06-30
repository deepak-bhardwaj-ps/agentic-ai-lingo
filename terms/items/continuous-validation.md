---
slug: continuous-validation
title: Continuous Validation
short_description: Ongoing checks that an AI system still behaves as expected after launch.
category: AgentOps
tags:
- evaluation
- monitoring
- testing
- agents
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a single fixed industry standard
- Confusing it with one-off testing before launch
- Using it as a vague name for any monitoring tool
related_terms:
- continuous evaluation
- online evaluation
- monitoring
- regression testing
- drift detection
evidence:
- source_title: Evaluation best practices
  source_url: https://developers.openai.com/api/docs/guides/evaluation-best-practices
  source_type: official_docs
  relevance: Directly describes the idea of running evals on every change and monitoring production behaviour over time.
  key_point: OpenAI recommends continuous evaluation to run evals on every change, watch for nondeterminism, and grow the eval set over time.
- source_title: Evaluation concepts
  source_url: https://docs.langchain.com/langsmith/evaluation-concepts
  source_type: official_docs
  relevance: Shows the split between offline testing and online monitoring, which matches how this term is used in practice.
  key_point: LangChain says offline evaluations validate against curated data during development, while online evaluations monitor production behaviour on live traffic.
- source_title: Challenges to the monitoring of deployed AI systems
  source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-4.pdf
  source_type: standards_doc
  relevance: Grounds the term in post-deployment monitoring and the idea that measurement can be continuous.
  key_point: NIST defines monitoring as measurement that may be continuous and focuses on post-deployment AI systems.
---

Continuous validation means checking again and again that an AI system still behaves as expected after it has been launched.

In practice, it means running tests on new changes, watching real-world behaviour, and comparing results over time. If the system starts making worse choices, ignoring instructions, or failing on new cases, the checks should catch that early.

This matters because AI systems can change when the model, prompts, tools, data, or surrounding systems change. Regular checks help teams notice problems before users do.

It is not a single fixed rule or universal industry standard. People often use the term to mean continuous evaluation, online monitoring, or repeated regression testing. The term is still a bit loose, so the exact meaning depends on the team using it.
