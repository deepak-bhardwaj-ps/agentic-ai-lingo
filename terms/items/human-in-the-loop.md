---
title: Human-in-the-loop
short_description: A system design where a person checks, guides, or approves part of the work instead of letting software act alone.
category: Agentic patterns
tags:
- human oversight
- approval workflow
- feedback loop
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating it as fully automatic, when a person still has an important role.
- Using it as a vague label for any AI system with a chat box or a feedback button.
related_terms:
- human-on-the-loop
- human oversight
- active learning
- reinforcement learning from human feedback
- approval workflow
evidence:
- source_title: What Is Human In The Loop | Google Cloud
  source_url: https://cloud.google.com/discover/human-in-the-loop
  source_type: official_docs
  relevance: Gives a current vendor definition used in AI and machine learning practice.
  key_point: Human-in-the-loop includes human input during training, evaluation, or operation, not just after the system has finished.
- source_title: AI Risk Management Framework | NIST
  source_url: https://www.nist.gov/itl/ai-risk-management-framework
  source_type: standards_doc
  relevance: Shows that human involvement is part of risk management, not just a product feature.
  key_point: NIST treats human oversight as a way to manage AI risks, which supports the idea that humans stay involved when the stakes are high.
- source_title: A Survey of Human-in-the-loop for Machine Learning
  source_url: https://arxiv.org/abs/2108.00941
  source_type: research_paper
  relevance: Summarises the research literature and shows that the term covers human help in data, training, and system design.
  key_point: Human-in-the-loop is a broad, established idea in machine learning where human knowledge is added to improve model results.
---

Human-in-the-loop means a system where a person checks, guides, or approves part of the work before the system goes ahead.

In practice, the software does some work first, then hands a step to a person for review, correction, or a yes/no decision. The person might label data, approve a suggested answer, or stop the system when something looks wrong.

This matters because it can make systems safer and more accurate, especially when mistakes would be costly or harmful.

It is not the same as a fully automatic system. It is also not a perfect guarantee that the AI is right. The term is broad, so people sometimes use it loosely, but the core idea is simple: a human stays involved in the loop.
