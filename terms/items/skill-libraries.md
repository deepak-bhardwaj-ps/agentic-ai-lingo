---
slug: skill-libraries
name: Skill Libraries
category: Protocols
title: Skill Libraries
aliases:
- skill library
- agent skill libraries
short_description: Skill libraries are reusable bundles of instructions, examples,
  tools, and sometimes code that help an agent do a task the same way each time.
status: active
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating a skill library as if it were the model itself
- Treating a loose folder of prompts as a tested, versioned package
- Assuming the name means the same thing on every platform
related_terms:
- skills
- prompt library
- tool
- agent workflow
- AGENTS.md
evidence:
- source_title: Skills
  source_url: https://developers.openai.com/api/docs/guides/tools-skills
  source_type: official_docs
  relevance: Shows skills as reusable, versioned bundles of files that can be attached
    to environments.
  key_point: OpenAI describes skills as reusable bundles that can be uploaded, managed,
    and attached to environments.
- source_title: Skills in ChatGPT
  source_url: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
  source_type: official_docs
  relevance: Defines skills as reusable workflows that can include instructions, examples,
    and code.
  key_point: OpenAI says skills are reusable, shareable workflows that can include
    instructions, examples, and code.
- source_title: Extend Claude with skills
  source_url: https://docs.anthropic.com/en/docs/claude-code/skills
  source_type: official_docs
  relevance: Confirms the same pattern in another major agent tool.
  key_point: Anthropic describes skills as a way to create, manage, and share reusable
    capability packs.
- source_title: Using skills to accelerate OSS maintenance
  source_url: https://developers.openai.com/blog/skills-agents-sdk
  source_type: engineering_blog
  relevance: Shows skills being used as repository-level instructions that travel
    with code.
  key_point: OpenAI recommends keeping workflow instructions small and letting them
    travel with the repository.
---

Skill libraries are collections of reusable instructions, examples, tools, and sometimes code that help an agent do a task in a repeatable way.

In practice, a team uses a skill library when it wants the same job to be done the same way across different agents or projects. The skill is usually stored as a separate package or folder so it can be updated, tested, shared, and given the right permissions.

This matters because it stops useful know-how from being copied into lots of prompts by hand. It also makes agent behaviour easier to control, review, and improve.

A skill library is not the model itself. It is also not a formal protocol with one fixed standard. Different platforms use the term slightly differently, so the label is still a bit loose.
