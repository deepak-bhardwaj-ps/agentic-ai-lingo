---
title: Replay cache
short_description: A stored copy of agent run outputs that lets a benchmark or debugger replay the same trace without rerunning everything.
category: Evals and benchmarks
tags:
  - evals
  - benchmarking
  - replay
  - traces
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating replay cache as the same thing as prompt caching.
  - Assuming a replay cache guarantees the run will behave exactly the same outside the cached replay.
  - Assuming it stores the whole system state rather than the recorded inputs and outputs needed for replay.
related_terms:
  - behaviour replay
  - trace
  - agent evaluation
  - checkpoint
  - prompt caching
  - reproducibility
evidence:
  - source_title: OpenBioRQ: Unsolved Biomedical Research Questions for Agents
    source_url: https://arxiv.org/html/2606.21959v1
    source_type: research_paper
    relevance: This paper uses the term directly in a current agent benchmark and explains that the replay cache is part of the release used to reproduce graded runs.
    key_point: OpenBioRQ says it ships a replay cache of the harness's truncated response previews so reviewers can reproduce what each agent saw.
  - source_title: Macro Evals for Agentic Systems
    source_url: https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems
    source_type: official_docs
    relevance: Shows why replay-style storage matters in eval work: teams need to inspect recurring behaviour across many traced runs, not just one final answer.
    key_point: OpenAI describes macro evals as working from traced agent runs and saved labels so the evidence can be revisited across the whole population of traces.
  - source_title: Use time-travel
    source_url: https://docs.langchain.com/oss/python/langgraph/use-time-travel
    source_type: official_docs
    relevance: Gives a clear baseline for replay in agent systems and helps distinguish replay from cache-based shortcuts.
    key_point: LangGraph says replay re-executes nodes and does not just read from cache, which shows that a replay cache is a separate idea from replay itself.
---

Replay cache is a saved copy of the outputs an agent produced during a run so that the same trace can be replayed later without doing all the work again.

In practice, a replay cache is used when people want to review or reproduce an eval run. It may store tool responses, model outputs, or short response previews, depending on the system. The point is to make the run easier to inspect and compare later.

This matters because agent evals often involve many steps. If you can replay a run from stored outputs, you can debug faster, compare changes more fairly, and check what the agent actually saw.

It is not the same as prompt caching, which mainly speeds up repeated prompt reuse. It is also not proof that the live system will behave exactly the same again, because models, tools, and external data can still change outside the replayed run.
