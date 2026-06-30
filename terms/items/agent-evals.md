---
slug: agent-evals
title: Agent Evals
short_description: Tests that check whether an AI agent can complete real tasks correctly
category: AgentOps
tags:
  - evaluation
  - testing
  - agents
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: maturing
common_misuse:
  - Treating agent evals as the same thing as a normal model benchmark or a single prompt test.
  - Judging only the final answer and ignoring the steps, tool use, or errors along the way.
related_terms:
  - model evals
  - benchmarks
  - task success
  - traces
  - graders
evidence:
  - source_title: Evaluate agent workflows
    source_url: https://developers.openai.com/api/docs/guides/agent-evals
    source_type: official_docs
    relevance: Directly describes how to evaluate agent workflows, which matches this term closely.
    key_point: OpenAI frames agent evaluation as using traces, graders, datasets, and eval runs to check how agents perform across workflows.
  - source_title: Demystifying evals for AI agents
    source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    source_type: engineering_blog
    relevance: Explains the main ways teams score agent behaviour and why transcript and outcome both matter.
    key_point: Anthropic says agent evaluations often use code-based, model-based, and human graders, because agents need assessment of both the steps they took and the result they reached.
  - source_title: Evaluation and Benchmarking of LLM Agents: A Survey
    source_url: https://arxiv.org/html/2507.21504v1
    source_type: research_paper
    relevance: Supports the broader academic view that task completion and end-to-end performance are central in agent evaluation.
    key_point: The survey treats task completion as a core objective and emphasises checking whether an agent reaches the desired state for the task.
---

Agent evals are tests that check whether an AI agent can complete a task correctly from start to finish.

In practice, you give the agent the same kind of job many times and inspect what it does along the way. You look at the steps it took, the tools it chose, how it handled mistakes, and whether it reached the right result.

This matters because an agent can sound confident and still fail. It might open the wrong file, call the wrong tool, or miss an important error. Agent evals help catch those problems before people rely on the agent.

Agent evals are not just one chatbot answer scored on its own. They are not the same as a general model benchmark. They test the whole task, from the request to the final outcome.
