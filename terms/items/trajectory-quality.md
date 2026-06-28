---
slug: trajectory-quality
title: Trajectory Quality
short_description: How good the step-by-step path an agent takes is, not just whether
  it ends with the right answer.
category: Runtime
tags:
- agents
- evaluation
- runtime
status: emerging practitioner shorthand
aliases:
- agent trajectory quality
- execution trajectory quality
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a standard, widely defined metric
- Judging only the final answer and ignoring the steps taken
- Using it without a clear scoring rule
related_terms:
- agent evaluation
- tool use
- reasoning trace
- recovery behaviour
evidence:
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Anthropic explains that agents should be judged on whether they can choose
    tools, recover from errors, and complete tasks reliably, which is the core idea
    behind trajectory quality.
  key_point: Effective agent evaluation needs to look at the path an agent takes,
    not just the final output.
- source_title: Demystifying evals for AI agents
  source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  source_type: engineering_blog
  relevance: Shows that agent evals often score transcript steps as well as outcomes,
    which supports evaluating the quality of a trajectory.
  key_point: Good agent evals can judge the actions, tool choices, and recovery steps
    in a run.
- source_title: Macro Evals for Agentic Systems
  source_url: https://developers.openai.com/cookbook/examples/partners/macro_evals_for_agentic_systems/macro_evals_for_agentic_systems
  source_type: official_docs
  relevance: OpenAI describes evaluating whether an agent used the right tools, delegated
    well, paused for review when needed, and stayed grounded in context.
  key_point: Agent quality is broader than the final answer and includes how the system
    behaved during the task.
---

Trajectory quality is how good an agent’s step-by-step path is while it works towards a goal.

In practice, it means checking more than the final answer. You also look at whether the agent chose sensible tools, used evidence well, fixed mistakes, avoided wasted steps, and followed the rules while working.

This matters because two agents can end with the same answer, but one may have done it in a careful, cheap, and safe way, while the other took a messy route, used the wrong tools, or needed lots of retries. If you only score the final result, you miss that difference.

This is not a single official standard metric. Different teams use the phrase in slightly different ways, so it should be defined clearly in each project.

It is also not the same as “accuracy”. Accuracy asks whether the result is correct. Trajectory quality asks whether the process was good.
