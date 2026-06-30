---
title: Reflection
short_description: A reflection step is when an agent looks back at what it just did, spots mistakes, and adjusts the next step.
category: Agentic patterns
tags:
- agentic-ai
- self-critique
- self-refinement
- agent-loop
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating reflection as proof that the model is correct.
- Confusing it with a separate verification step that uses outside evidence.
- Assuming every agent needs reflection in every turn.
related_terms:
- verification-loop
- self-refinement
- Reflexion
- ReAct
- reasoning-runtime
evidence:
  - source_title: Self-Refine: Iterative Refinement with Self-Feedback
    source_url: https://arxiv.org/abs/2303.17651
    source_type: research_paper
    relevance: Defines the basic self-critique-and-revise pattern that many agent teams mean when they say reflection.
    key_point: The same model can generate feedback on its own output and use that feedback to improve the next version.
  - source_title: Reflexion: Language Agents with Verbal Reinforcement Learning
    source_url: https://arxiv.org/abs/2303.11366
    source_type: research_paper
    relevance: Shows reflection used inside an agent loop with memory, not just as a one-off prompt trick.
    key_point: The agent verbally reflects on task feedback and stores that reflection to improve later decisions.
  - source_title: GPT-4.1 Prompting Guide
    source_url: https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide
    source_type: official_docs
    relevance: Shows current OpenAI guidance that agents can be prompted to plan and reflect between tool calls.
    key_point: Reflection is presented as an explicit step in an agent loop, especially between actions and tool calls.
  - source_title: The "think" tool: Enabling Claude to stop and think in complex tool use situations
    source_url: https://www.anthropic.com/engineering/claude-think-tool
    source_type: engineering_blog
    relevance: Describes a modern production pattern where the model pauses to review new information before continuing.
    key_point: A dedicated thinking step helps the agent inspect tool results and decide the next move.
---

## Meaning

Reflection is a step where an AI agent looks back at what it just did, checks what went wrong or what it learned, and uses that to choose a better next step.

In practice, the agent may review its last answer, its tool results, or a failed attempt. It then writes a short critique, updates its plan, or tries again with a better approach.

This matters because agents often get stuck, miss details, or repeat mistakes. Reflection helps them recover and improve without retraining the model.

Reflection is not the same as being self-aware. It is also not a guarantee of correctness. Good reflection usually works with other checks, such as tests, rules, or human review.
