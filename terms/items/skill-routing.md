---
title: Skill Routing
short_description: Choosing which skill, tool, or sub-task should handle a request.
category: Runtime
tags:
- agentic-ai
- tools
- routing
- orchestration
status: glossary
aliases:
- tool routing
- capability routing
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating it as a single standard architecture instead of a design pattern.
- Confusing routing with the skill itself.
- Assuming the model always picks the best skill without rules or checks.
related_terms:
- tool use
- function calling
- orchestration
- agent routing
- sub-agent
evidence:
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Shows routing as a core agent pattern where a system chooses what to
    do next.
  key_point: Anthropic describes routing as a practical way to send a task to the
    right next step or specialist.
- source_title: Function calling
  source_url: https://developers.openai.com/api/docs/guides/function-calling
  source_type: official_docs
  relevance: Explains how a model can decide when to call a tool, which is the same
    basic choice skill routing makes.
  key_point: The model can choose whether to use a tool and which tool to use through
    the tool-choice flow.
- source_title: Extend Claude with skills
  source_url: https://docs.anthropic.com/en/docs/claude-code/skills
  source_type: official_docs
  relevance: Shows the modern product meaning of skills as reusable capability packs
    that can be applied to tasks.
  key_point: Skills are reusable instructions and resources that extend what the assistant
    can do on specific tasks.
---

Skill routing means choosing the right skill, tool, or helper for a job.

In practice, a system looks at the task, picks a matching capability, and sends the work there. If the chosen skill cannot handle it, the system may try another one or stop with an error.

This matters because a general assistant is usually better when it can hand a task to the most suitable specialist instead of trying to do everything itself. Good routing can make results faster, safer, and more accurate.

Skill routing is not a fixed standard design. It is a useful way to describe the decision step in an agent system.

It is also not the same as the skill itself. The skill is the thing that does the work. Routing is the part that decides which skill to use.
