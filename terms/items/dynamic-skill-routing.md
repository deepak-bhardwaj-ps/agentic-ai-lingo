---
slug: dynamic-skill-routing
title: Dynamic Skill Routing
short_description: Choosing, at run time, which skill or capability should handle
  a request.
category: Runtime
tags:
- agentic-ai
- routing
- skills
- orchestration
status: draft
aliases:
- skill routing
- dynamic routing
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a standard, widely agreed architecture name.
- Using it to describe any agent workflow, even when nothing is being selected at
  run time.
related_terms:
- agent skills
- tool routing
- orchestration
- workflow
evidence:
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Establishes the broader idea of simple agent patterns, including routing
    work between steps instead of using one large, fixed flow.
  key_point: Anthropic recommends simple, composable patterns and notes that routing
    and orchestration are part of effective agent design.
- source_title: Agent Skills - Claude Platform Docs
  source_url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
  source_type: official_docs
  relevance: Shows that skills can be loaded and used automatically when relevant.
  key_point: Claude uses skills when they match the request, which is the practical
    pattern behind dynamic skill routing.
- source_title: Skills for ADK agents
  source_url: https://adk.dev/skills/
  source_type: official_docs
  relevance: Shows an agent system that can load skills on demand.
  key_point: Skills can be loaded only when needed, which supports run-time selection
    instead of preloading everything.
---

Dynamic Skill Routing means choosing, while the system is running, which skill or capability should handle a request.

In practice, the system looks at the request, decides what kind of help is needed, and sends the work to the best skill for that moment. It may also skip skills that do not fit, fall back to another option, or ask for more detail if the choice is unclear.

This matters because it helps an agent do the right thing without loading every skill all the time. That can make the system simpler, faster, and easier to control.

It is not a fixed standard design. The important part is the decision rule: what gets chosen, when it gets chosen, what happens if the choice is wrong, and when the system stops trying.
