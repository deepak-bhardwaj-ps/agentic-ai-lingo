---
title: Behaviour Drift
short_description: Behaviour Drift is a label for an AI agent gradually changing how it behaves compared with the behaviour people expected.
category: Governance
tags:
  - agent behaviour
  - drift
  - governance
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a formal industry standard with one agreed definition.
  - Confusing it with a single wrong answer or a one-off tool error.
  - Using it as a catch-all for any performance problem.
related_terms:
  - goal drift
  - mission drift
  - context drift
  - memory drift
  - behavioural anomaly
evidence:
  - source_title: AGENTOPS05-BP02 Monitor agent behavior patterns and detect anomalies
    source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops05-bp02.html
    source_type: official_docs
    relevance: AWS describes behavioural drift as something to detect against a baseline of normal agent behaviour, which matches this term's use in governance and monitoring.
    key_point: Baselines are maintained per agent and changes in reasoning, tool use, or performance are treated as drift or anomalies to investigate.
  - source_title: Continuous evaluation with online monitors
    source_url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-online
    source_type: official_docs
    relevance: Google Cloud uses 'quality drift' for a measurable drop in agent performance over time, showing that drift is a monitoring problem rather than a single mistake.
    key_point: Drift is an observable decline in production agent quality that can happen even when the underlying model has not changed.
  - source_title: Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions
    source_url: https://arxiv.org/abs/2601.04170
    source_type: research_paper
    relevance: This paper gives a recent research framing for agent drift as progressive behavioural degradation over long interaction sequences, including changes in tool use and response consistency.
    key_point: Behavioural drift is presented as a gradual shift away from the original pattern of behaviour, not a one-off failure.
---

Behaviour Drift is when an AI agent slowly starts acting differently from what people expected.

In practice, this means the agent may become less consistent, follow the task less well, or begin using tools in a different way after many steps, retries, or conversations.

It matters because small changes can build up. An agent that looks fine at first can later make worse decisions, break rules, or need more human correction.

It is not the same as a one-off mistake. It is also not a fixed technical standard. The phrase is used to describe a pattern of gradual change, especially in risk reviews and evaluation work.
