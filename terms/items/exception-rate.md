---
slug: exception-rate
name: Exception Rate
category: AgentOps
title: Exception Rate
aliases: null
short_description: The share of workflows that need manual handling, escalation, or
  fallback instead of finishing automatically.
status: active
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a universal standard KPI
- Using it without defining what counts as an exception
- Mixing manual review, escalation, retries, and fallback into one number
related_terms:
- escalation rate
- fallback rate
- error rate
- success rate
evidence:
- source_title: OpenAI Evals guide
  source_url: https://platform.openai.com/docs/guides/evals
  source_type: official_docs
  relevance: Shows how teams evaluate model and workflow behaviour against defined
    success criteria.
  key_point: Evaluation only works when the team defines the exact event being measured
    and what counts as success or failure.
- source_title: Agent metrics reference
  source_url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/agent-business-value-metrics-reference
  source_type: official_docs
  relevance: Uses escalation rate as a close operational measure for when a session
    is handed to a human.
  key_point: A practical measure for this space is the share of sessions that leave
    the automated path.
- source_title: Agent evaluation and decision engines
  source_url: https://aws.amazon.com/marketplace/build-learn/ai-agent-learning-series/agent-evaluation-and-decision-engines
  source_type: engineering_blog
  relevance: Recommends tracking error and fallback rates for agent systems over time.
  key_point: Teams should monitor how often systems fail over to backup behaviour,
    not just whether they sometimes succeed.
- source_title: Agentic AI Lens
  source_url: https://docs.aws.amazon.com/pdfs/wellarchitected/latest/agentic-ai-lens/agentic-ai-lens.pdf
  source_type: standards_doc
  relevance: Describes fallback behaviour and error handling for tool invocations
    in agent systems.
  key_point: Good agent design includes clear fallback paths when tools fail or time
    out.
---

Exception rate is the share of workflows that cannot finish on their own and need a person, a backup path, or a special fix.

In practice, it tells you how often the system leaves the normal path. A high exception rate means more work is being pushed to humans or fallback steps instead of being handled automatically.

This matters because it shows where automation is still weak. If the number is rising, the system may be failing more often, using the wrong tool, or needing better rules.

It is not a universal industry KPI with one fixed meaning. Teams must define exactly what counts as an exception, what the total is, and whether they are measuring manual review, escalation, retries, or fallback behaviour.
