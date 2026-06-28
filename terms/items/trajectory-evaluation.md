---
title: Trajectory Evaluation
short_description: Checking the steps an agent took, not just the final answer.
category: AgentOps
tags:
- agentops
- evaluation
- agents
- tool-use
status: active
aliases:
- Agent trajectory evaluation
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse:
- Treating a matching step-by-step path as the only way an agent can be correct.
- Using trajectory checks instead of checking whether the final answer is right.
- Assuming every agent should follow one fixed path.
related_terms:
- final response evaluation
- tool call evaluation
- agent observability
- evaluation
evidence:
- source_title: Evaluate Gen AI agents
  source_url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-agents
  source_type: official_docs
  relevance: Directly defines trajectory evaluation as evaluating the path, or sequence
    of tool calls, an agent took.
  key_point: Google Cloud describes trajectory evaluation as checking the path of
    tool calls an agent used to reach its final response.
- source_title: How to evaluate your agent with trajectory evaluations
  source_url: https://docs.langchain.com/langsmith/trajectory-evals
  source_type: official_docs
  relevance: Shows that trajectory evaluation is about the exact sequence of messages
    and tool calls, and can be checked against a reference path.
  key_point: LangChain explains that trajectory evaluation tests the steps an agent
    took, not only the final output.
- source_title: A dev's guide to production-ready AI agents
  source_url: https://cloud.google.com/blog/products/ai-machine-learning/a-devs-guide-to-production-ready-ai-agents
  source_type: engineering_blog
  relevance: Explains why process matters for agents and why the full sequence of
    decisions and actions should be reviewed.
  key_point: Google Cloud says good agent evaluation looks at the full trajectory,
    including tool choice, reasoning quality, error recovery, and clarifying questions.
---

Trajectory evaluation checks the steps an agent took on the way to its answer.

In practice, this means looking at the agent’s tool calls, decisions, and order of actions. A final answer can look fine even if the agent took a wasteful, risky, or confusing path to get there.

This matters because agents do not just produce text. They can search, call tools, ask questions, and act step by step. If you only check the final answer, you can miss bad behaviour in the middle.

It is not the same as outcome evaluation. Outcome evaluation asks, “Did the agent end up with the right answer?” Trajectory evaluation asks, “Did it get there in a sensible way?”

It is also not a demand that every correct agent must follow one exact route. Sometimes more than one path is acceptable. The point is to check whether the steps were safe, sensible, and fit for the task.
