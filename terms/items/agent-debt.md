---
title: Agent Debt
short_description: Agent debt is the build-up of weak spots in an AI agent system that make it harder, riskier, or more expensive to change and run safely.
category: AgentOps
tags:
- ai
- agentops
- governance
status: active
aliases: []
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it like a formal score or standard when it is mostly a shorthand for accumulated system weaknesses.
- Using it to mean a single bad model answer instead of problems in the wider agent setup.
related_terms:
- technical debt
- cognitive debt
- architectural debt
- agent governance
- agent security
evidence:
- source_title: Technical Debt
  source_url: https://martinfowler.com/bliki/TechnicalDebt.html
  source_type: industry_article
  relevance: Gives the original debt metaphor that agent debt borrows from.
  key_point: Fowler describes technical debt as the build-up of cruft that makes systems harder to change, with extra effort showing up as "interest" later.
- source_title: Harness engineering for coding agent users
  source_url: https://martinfowler.com/articles/harness-engineering.html
  source_type: industry_article
  relevance: Shows why agent systems need surrounding controls, not just a capable model.
  key_point: Fowler says developers carry context, conventions, and quality judgement as a harness; agent systems need equivalent guardrails or they become harder to trust and maintain.
- source_title: Safe and trustworthy agents
  source_url: https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents
  source_type: engineering_blog
  relevance: Explains that autonomous agents can act in ways that do not match user intent, which is one source of operational debt.
  key_point: Anthropic notes that when systems pursue goals autonomously, they can take actions that seem reasonable to the system but violate what humans wanted.
- source_title: Why governance, security, and operations matter for AI agents
  source_url: https://learn.microsoft.com/en-us/agents/adoption-maturity-model/maturity-model-security-governance
  source_type: official_docs
  relevance: Supports the idea that weak permissions, unclear accountability, and poor operations become practical risk in agent systems.
  key_point: Microsoft says agents amplify intent through identity, data, and permissions, and without governance they can create unintended exposure, inconsistent behaviour, and rising costs.
---

Agent debt is the build-up of weak spots around an AI agent system that make it harder, riskier, or more expensive to change and run safely.

In practice, it means the agent has grown in a messy way. Its prompts may not be tested. Its tool use may not be monitored. Its permissions may be too broad. Its fallback steps may fail when something goes wrong. The more of these gaps there are, the more work it takes to trust the system.

This matters because an agent can do more than write text. It can choose actions, use tools, and pass work to other systems. If those parts are not checked well, a small mistake can become a bigger problem.

Agent debt is not the same as one bad answer from a model. A model can make mistakes without the whole system being in bad shape. This term is about the system around the model becoming harder to understand, control, and improve.

It is also not a formal industry score. People use it as a useful label, but there is no single agreed way to measure it.
