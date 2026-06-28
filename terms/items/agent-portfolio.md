---
slug: agent-portfolio
name: Agent Portfolio
category: AgentOps
title: Agent Portfolio
aliases: []
short_description: A group of AI agents that are owned, compared, and managed together.
status: active
tags:
- agentops
- governance
- evaluation
- multi-agent-systems
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it like an official AI standard
- Mixing short experiments with production agents
- Confusing live agents with prompts, models, or test scripts
related_terms:
- agent lifecycle
- agent governance
- evals
- multi-agent system
- observability
evidence:
- source_title: Evaluate agent workflows
  source_url: https://developers.openai.com/api/docs/guides/agent-evals
  source_type: official_docs
  relevance: Shows that real agent systems are assessed with traces, datasets, graders,
    and eval runs, which fits the idea of managing several agents as a group.
  key_point: OpenAI recommends using traces, graders, datasets, and eval runs to improve
    agent quality.
- source_title: Evaluation best practices
  source_url: https://developers.openai.com/api/docs/guides/evaluation-best-practices
  source_type: official_docs
  relevance: Explains that AI systems vary in output and need repeated evaluation,
    which is important when comparing multiple agents over time.
  key_point: OpenAI says evals are needed because generative AI can give different
    outputs for the same input.
- source_title: AI Risk Management Framework
  source_url: https://www.nist.gov/itl/ai-risk-management-framework
  source_type: official_docs
  relevance: Supports the idea that AI should be managed through an organised risk
    process across systems, not as isolated tools.
  key_point: NIST says the framework helps manage AI risks to individuals, organisations,
    and society.
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Supports the idea that agent systems should be kept simple and composable,
    which helps define what belongs in a portfolio.
  key_point: Anthropic describes effective agent systems as simple, composable, and
    built with clear boundaries.
---

An agent portfolio is the group of AI agents that an organisation owns, compares, and manages together.

In practice, it means you do not look at each agent alone. You look at the whole set: what each agent does, how well it works, how much it costs, what risks it brings, and whether it should be kept, improved, or retired.

This matters because once a team has more than one agent, the real question is not just “does this one work?” It is also “which agents are worth using, which are safe enough, and which are wasting time or money?”

It is not a formal AI standard. It is not just a list of prompts. It is also not the same as a model list, because a portfolio is about live agents that are actually in use or under active review.
