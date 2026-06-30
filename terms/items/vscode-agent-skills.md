---
title: vscode-agent-skills
short_description: A VS Code extension that helps users discover, install, and manage Agent Skills.
category: Tools and products
tags:
  - visual-studio-code
  - extensions
  - agent-skills
status: draft
aliases:
  - Agent Skills Marketplace for VS Code
meaning_type: rebranded_old_idea
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the Agent Skills standard itself instead of a VS Code extension that works with that standard.
  - Assuming it is built into VS Code rather than an extension you install.
related_terms:
  - Agent Skills
  - VS Code extension
  - GitHub Copilot
  - SKILL.md
  - custom instructions
evidence:
  - source_title: Agent Skills Marketplace for VS Code
    source_url: https://marketplace.visualstudio.com/items?itemName=formulahendry.agent-skills
    source_type: official_docs
    relevance: This is the product listing that most directly identifies what the term refers to.
    key_point: The listing describes it as a VS Code extension for discovering, installing, and managing Agent Skills.
  - source_title: formulahendry/vscode-agent-skills
    source_url: https://github.com/formulahendry/vscode-agent-skills
    source_type: engineering_blog
    relevance: The repository confirms the project name and its intended function, which helps distinguish the extension from the skills it manages.
    key_point: The README presents it as an Agent Skills marketplace for VS Code with browsing, search, install, and sync features.
  - source_title: Use Agent Skills in VS Code
    source_url: https://code.visualstudio.com/docs/agent-customization/agent-skills
    source_type: official_docs
    relevance: This is the authoritative VS Code documentation for what Agent Skills are, which is necessary to separate the extension from the underlying concept.
    key_point: VS Code defines Agent Skills as folders of instructions, scripts, and resources that Copilot can load for specialised tasks, and says they are an open standard.
---

vscode-agent-skills is a VS Code extension for finding, installing, and managing Agent Skills.

In practice, it works like a marketplace inside the editor. You use it to browse skills, install them into your workspace, and keep them updated.

The term matters because Agent Skills are not just prompts. They are reusable bundles of instructions, scripts, and other files, and this extension helps organise them inside VS Code.

It is not the Agent Skills standard itself, and it is not the coding assistant that uses the skills. It is the tool that helps you manage those skills in VS Code.
