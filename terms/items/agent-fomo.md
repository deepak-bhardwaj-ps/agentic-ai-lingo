---
slug: agent-fomo
name: Agent FOMO
title: Agent FOMO
short_description: Slang for adding an AI agent because it feels trendy, not because the job really needs one.
category: Slang
tags: []
status: active
aliases: []
meaning_type: overloaded_buzzword
novelty_level: low
maturity_level: emerging
common_misuse: Used as a shortcut for rejecting any agent idea, instead of checking whether the task really needs an agent.
related_terms:
  - agent design
  - automation
  - prompt chaining
evidence:
  - source_title: Building Effective AI Agents
    source_url: https://www.anthropic.com/research/building-effective-agents
    source_type: engineering_blog
    relevance: Shows that experienced teams treat agent design as a choice that should be kept simple unless the task really needs more autonomy.
    key_point: Anthropic says successful agent systems usually use simple, composable patterns rather than complex frameworks.
  - source_title: A practical guide to building agents
    source_url: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
    source_type: engineering_blog
    relevance: Explains that teams should start by checking whether an agent is the right fit and should optimise for accuracy, cost, latency, and safety.
    key_point: OpenAI presents agents as something to choose carefully, with guidance for identifying promising use cases and avoiding unnecessary complexity.
  - source_title: Building Effective AI Agents: Architecture Patterns and Implementation Frameworks
    source_url: https://cdn.openai.com/business-guides-and-resources/a-business-leaders-guide-to-working-with-agents.pdf
    source_type: industry_article
    relevance: Supports the idea that agent adoption is a business and design decision, not something to do just because it is fashionable.
    key_point: The guide frames agents as a shift that needs guardrails, safe use, and careful rollout rather than blind enthusiasm.
---

Agent FOMO is slang for adding an AI agent because it feels fashionable, not because the task actually needs one.

In practice, it means someone wants an agent first and only then looks for a problem it can solve. A better approach is to ask whether the job is already simple enough for a normal app, a fixed workflow, or a plain automation rule.

The term matters because agents can be useful, but they also add cost, complexity, and risk. If the task is predictable, an agent may make the system harder to test and easier to break.

It is not a formal technical term. It does not mean agents are always a bad idea. It means the decision was driven by hype instead of by the actual job to be done.
