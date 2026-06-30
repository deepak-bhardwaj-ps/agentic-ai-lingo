---
title: Feedback curator
short_description: A person or workflow that filters raw user feedback and keeps only the useful bits for later reuse.
category: Knowledge and wiki systems
tags:
- feedback
- knowledge management
- workflows
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as collecting every piece of feedback.
- Assuming it means automatic promotion with no human review.
- Using it as a general job title for moderation or support.
related_terms:
- Feedback collection
- Human review
- Evaluation loop
- Session memory
- Knowledge curation
evidence:
- source_title: LLM Wiki
  source_url: https://llm-wiki.net/
  source_type: industry_article
  relevance: This is the clearest source for the exact term as used in the surrounding glossary and shows the intended workflow.
  key_point: The project describes feedback curator as a step that captures high-signal corrections, preferences, approvals, and plan acceptance, ignores noise, and only promotes selected items explicitly.
- source_title: GitHub - nvk/llm-wiki
  source_url: https://github.com/nvk/llm-wiki
  source_type: industry_article
  relevance: The repository changelog gives the operational meaning of the term and shows how it behaves in practice.
  key_point: The changelog says feedback curator captures reviewable correction, preference, and approval candidates, ignores generic acknowledgements, and promotes only what matters.
- source_title: Build an Agent Improvement Loop with Traces, Evals, and Codex
  source_url: https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop
  source_type: official_docs
  relevance: This supports the broader idea that useful feedback is collected, reviewed, and turned into later improvements rather than being kept as raw noise.
  key_point: OpenAI describes an improvement loop where traces are combined with human and model feedback, then turned into evals and follow-up changes.
- source_title: Evaluation concepts | Docs by LangChain
  source_url: https://docs.langchain.com/langsmith/evaluation-concepts
  source_type: official_docs
  relevance: This shows that human feedback is usually attached to traces and managed through structured review, which matches the curation part of the term.
  key_point: LangSmith describes human evaluation as manual review of outputs and traces, with structured feedback collection through annotation workflows.
---

Feedback curator is a person or workflow that sorts through raw feedback and keeps the useful parts.

In practice, it looks at things like corrections, preferences, approvals, and task outcomes, then ignores low-value noise such as “ok” or “thanks”. The useful feedback is saved in a form that can be reviewed later or turned into better notes, rules, tests, or prompts.

The term matters because raw feedback is messy. If you keep everything, the important bits get buried. If you curate it well, the next version of the system can learn from real mistakes and real user needs.

It is not the same as collecting feedback from everyone. It is also not just moderation or support. A feedback curator decides what is worth keeping and what should be dropped, so the system does not fill up with noise.
