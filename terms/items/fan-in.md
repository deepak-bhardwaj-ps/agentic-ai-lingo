---
title: Fan-in
short_description: A step where several parallel tasks send their results back to one place to be combined.
category: Agentic patterns
tags:
- agentic-ai
- orchestration
- multi-agent
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating it as the same thing as fan-out, which is the splitting step
- Using it to mean any final answer, even when no parallel work happened
related_terms:
- fan-out
- concurrent orchestration
- parallel pattern
- coordinator pattern
- aggregation
evidence:
- source_title: Parallel Agents with the OpenAI Agents SDK
  source_url: https://developers.openai.com/cookbook/examples/agents_sdk/parallel_agents
  source_type: official_docs
  relevance: Shows the exact fan-out/fan-in wording used in a current agent workflow and makes the combining step explicit.
  key_point: OpenAI describes fan-in as collecting the outputs from multiple specialised agents after they run in parallel, then passing them to a final meta agent.
- source_title: Choose a design pattern for your agentic AI system
  source_url: https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
  source_type: official_docs
  relevance: Gives a current vendor definition of the parallel agent pattern, which is the broader pattern that fan-in belongs to.
  key_point: Google Cloud says parallel agent workflows split work across specialised agents at the same time and then combine their outputs.
- source_title: Building Effective AI Agents: Architecture Patterns and Implementation Frameworks
  source_url: https://resources.anthropic.com/hubfs/Building%20Effective%20AI%20Agents-%20Architecture%20Patterns%20and%20Implementation%20Frameworks.pdf
  source_type: engineering_blog
  relevance: Confirms that fan-out/fan-in is a recognised design pattern in agent systems and explains why the merge step matters.
  key_point: Anthropic describes the pattern as parallel work that is later aggregated, with results often combined after the independent tasks finish.
---

Fan-in is the step where several separate tasks send their results back to one place so they can be combined.

In an agent workflow, this usually happens after fan-out. One controller or coordinator waits for the smaller tasks to finish, then joins their answers into one summary, decision, or next action.

It matters because some jobs are faster and clearer when the work can happen in parallel first and be joined afterwards. Fan-in is the part that turns many partial results into one usable result.

Fan-in is not fan-out. Fan-out means splitting one job into many smaller jobs. Fan-in means bringing those results back together.

It is also not just “the final answer”. A workflow can have a final answer without any fan-in if nothing was done in parallel.
