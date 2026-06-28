---
slug: agent-theatre
title: Agent Theatre
short_description: Slang for an agent demo that looks self-running, but is quietly
  helped by people, scripts, or hidden manual steps.
category: Slang
tags:
- agentic-ai
- slang
- evaluation
- demos
status: active
aliases:
- AI theatre
- agent theatre
meaning_type: overloaded_buzzword
novelty_level: low
maturity_level: established
common_misuse:
- Used as a blanket insult for any AI demo, even when the system does useful work.
- Used for normal product demos that are not claiming to be autonomous.
related_terms:
- human-in-the-loop
- autonomy
- agentic-ai
- AI washing
evidence:
- source_title: A practical guide to building agents
  source_url: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
  source_type: official_docs
  relevance: Defines agents as systems that independently accomplish tasks and says
    simple chatbots or single-turn LLMs are not agents.
  key_point: A real agent must control the work it does, not just look clever in a
    demo.
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Describes agents as useful when they combine conversation with action,
    clear success criteria, feedback loops, and human oversight.
  key_point: A demo can look agent-like without proving the system works reliably
    in practice.
- source_title: Demystifying evals for AI agents
  source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
  source_type: engineering_blog
  relevance: Explains why agents need evaluations that expose behaviour across turns,
    tools, and runtime changes.
  key_point: Good-looking outputs can hide failures that only show up during real
    use.
- source_title: AI RMF Playbook
  source_url: https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
  source_type: official_docs
  relevance: Gives a governance and measurement lens for judging AI systems by outcomes,
    not appearances.
  key_point: NIST stresses govern, map, measure, and manage, which supports checking
    what a system actually does.
---

Agent theatre is slang for an AI demo that seems to work by itself, but is actually helped by people, scripts, or hidden manual steps.

In practice, it means the system may sound like it is planning, deciding, and acting on its own, while people behind the scenes are filling the gaps. The demo can look smart even if the system cannot reliably finish the job alone.

The term matters because a polished demo is not the same as a working system. Real agent use needs evidence that the system can do the task, recover from mistakes, use tools safely, and behave sensibly outside the demo.

It is not a formal technical term. It is a criticism of the gap between what is shown and what actually works.
