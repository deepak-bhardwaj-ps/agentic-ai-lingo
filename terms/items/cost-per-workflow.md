---
slug: cost-per-workflow
title: Cost per Workflow
short_description: The average total cost of completing one workflow from start to
  finish.
category: AgentOps
tags:
- agentic-ai
- cost
- metrics
- unit-economics
- workflows
status: active
aliases:
- workflow cost
- cost per task
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse: Treating it as only model token spend, or comparing workflows without
  defining the same start, finish, and cost items.
related_terms:
- unit economics
- token cost
- workflow
- evaluation
- observability
evidence:
- source_title: Evaluation best practices
  source_url: https://developers.openai.com/api/docs/guides/evaluation-best-practices
  source_type: official_docs
  relevance: Shows that evals should define success criteria and metrics before comparing
    systems.
  key_point: OpenAI recommends defining the evaluation objective and metrics first,
    which supports measuring the cost of one complete workflow in a consistent way.
- source_title: Evals guide
  source_url: https://platform.openai.com/docs/guides/evals
  source_type: official_docs
  relevance: Shows that running evals uses real API calls and therefore real cost.
  key_point: OpenAI's evals workflow makes cost a real operational concern because
    tests and model graders consume API usage.
- source_title: A guide to cloud unit economics
  source_url: https://www.datadoghq.com/blog/cloud-unit-economics/
  source_type: industry_article
  relevance: Explains the idea of measuring cost per discrete business outcome.
  key_point: Datadog describes unit economics as measuring the cost of achieving a
    specific outcome, which is the same idea behind cost per workflow.
---

Cost per Workflow is the average cost of completing one workflow from start to finish.

In practice, it means adding up all the costs tied to that workflow, then dividing by the number of workflows completed. Those costs may include model calls, tool calls, storage, human review, and other operating costs if they are part of the workflow.

This matters because two agent systems can look similar on the surface but cost very different amounts to run. A lower cost per workflow can make a system easier to scale, while a higher one may still be worth it if the workflow is more accurate or saves more time.

It is not just token cost. It is also not a universal standard metric with one fixed formula. The exact boundary has to be defined first, or the number can be misleading.
