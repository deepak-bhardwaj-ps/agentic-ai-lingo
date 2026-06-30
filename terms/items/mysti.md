---
title: Mysti
short_description: A VS Code extension that lets several AI coding tools work together on the same task.
category: Tools and products
tags:
  - VS Code
  - AI coding
  - developer tools
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating Mysti as a general term for any AI coding assistant instead of a specific VS Code extension.
related_terms:
  - VS Code extension
  - coding agent
  - AI coding assistant
  - Brainstorm Mode
  - multi-agent collaboration
  - model routing
evidence:
  - source_title: Mysti - AI Coding Agent - Visual Studio Marketplace
    source_url: https://marketplace.visualstudio.com/items?itemName=DeepMyst.mysti
    source_type: official_docs
    relevance: The marketplace listing is the most direct product description for Mysti and confirms what it is used for.
    key_point: Mysti is listed as an AI coding agent for Visual Studio Code and describes support for multiple providers and local models.
  - source_title: Mysti/README.md at main - DeepMyst/Mysti
    source_url: https://github.com/DeepMyst/Mysti/blob/main/README.md
    source_type: official_docs
    relevance: The project README explains the intended workflow and shows that Mysti is an extension built around coding tasks inside VS Code.
    key_point: Mysti is presented as an AI coding tool for VS Code with a Brainstorm Mode where two AI tools can work together.
  - source_title: Mysti docs - PROVIDERS.md
    source_url: https://github.com/DeepMyst/Mysti/blob/main/docs/PROVIDERS.md
    source_type: official_docs
    relevance: This documentation shows how Mysti is implemented as a wrapper over several coding providers rather than a single model.
    key_point: Mysti supports multiple AI providers and says you can unlock Brainstorm Mode by installing two of them.
---

Mysti is a VS Code extension that helps you code with AI. It is built around several AI coding tools, so you can use one tool or let two of them work on the same problem together.

In practice, Mysti sits inside Visual Studio Code and gives you a chat and task workflow for coding help. It can connect to different providers, including cloud and local ones, and it has a Brainstorm Mode for getting two AI tools to compare ideas.

This matters because it is meant to reduce single-tool lock-in and make coding help more flexible. It is especially useful when you want a second opinion from another AI tool instead of trusting one answer.

Mysti is not a general word for all AI coding assistants. It is a specific product, and its features may change as the extension evolves.
