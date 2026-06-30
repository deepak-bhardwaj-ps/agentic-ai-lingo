---
slug: goal-drift
title: Goal Drift
short_description: Goal drift is when an agent gradually stops following the original goal it was given.
category: Governance
tags:
- agentic-ai
- governance
- safety
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating any wrong answer or normal task change as goal drift.
- Confusing goal drift with general model drift, which usually means changes in model behaviour or performance over time.
related_terms:
- agentic-misalignment
- instruction-following
- distribution-drift
- reasoning-drift
evidence:
- source_title: Technical Report - Evaluating Goal Drift in Language Model Agents
  source_url: https://arxiv.org/abs/2505.02709
  source_type: research_paper
  relevance: This paper uses the term directly and defines it as an agent deviating from its original objective over time, which is the closest match to the glossary term.
  key_point: Goal drift can happen gradually in long-running agents, so the change may be subtle rather than a single obvious failure.
- source_title: Harness engineering: leveraging Codex in an agent-first world
  source_url: https://openai.com/index/harness-engineering/
  source_type: engineering_blog
  relevance: OpenAI describes how agent systems can drift over time as they reproduce patterns already present in their environment, which supports the idea of gradual loss of the intended direction.
  key_point: Long-running agent systems need scaffolding, cleanup, and feedback loops because drift can build up over time.
- source_title: Demystifying evals for AI agents
  source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  source_type: engineering_blog
  relevance: Anthropic explains that agent systems need ongoing monitoring and maintenance to avoid drift as the product and model change, which matches the governance meaning of the term.
  key_point: Ongoing evaluation is needed because behaviour can shift as systems evolve and real-world usage changes.
---

Goal drift is when an AI agent gradually stops following the original goal it was given.

In practice, this means the agent starts on the right task, but its actions slowly move towards something else. This can happen in long jobs when the agent sees new instructions, unclear feedback, or confusing tool results.

This matters because an agent can look busy and still be heading in the wrong direction. A team may think it is following policy or business rules when it is actually drifting away from the intended outcome.

Goal drift is not the same as one bad answer. It is not just “the AI made a mistake”. It means the agent slowly loses track of the goal it was supposed to keep following.
