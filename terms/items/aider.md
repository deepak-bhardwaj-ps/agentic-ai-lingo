---
title: Aider
short_description: An AI pair-programming tool that edits code in your terminal and works with a local git repository.
category: Tools and products
tags:
  - coding-assistant
  - terminal-tool
  - git
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as a general chat bot instead of a code-editing tool.
  - Assuming it replaces git; it works with git rather than instead of it.
related_terms:
  - coding assistant
  - pair programming
  - git
  - terminal-based tool
evidence:
  - source_title: Aider homepage
    source_url: https://aider.chat/
    source_type: official_docs
    relevance: The project’s own homepage gives the clearest high-level definition of what Aider is and where it runs.
    key_point: Aider describes itself as AI pair programming in your terminal for starting new projects or building on an existing codebase.
  - source_title: Aider Documentation
    source_url: https://aider.chat/docs/
    source_type: official_docs
    relevance: The docs explain the main workflow: using Aider to pair program with AI and edit code in a local git repo.
    key_point: Aider is used to pair program with AI and edit code in your local git repository.
  - source_title: Git integration - aider
    source_url: https://aider.chat/docs/git.html
    source_type: official_docs
    relevance: This matters because Aider’s identity depends on git-aware editing, undo, and review rather than plain chat.
    key_point: Aider commits changes with descriptive messages and handles pre-existing changes carefully so edits can be reviewed and undone.
  - source_title: Chat modes | aider
    source_url: https://aider.chat/docs/usage/modes.html
    source_type: official_docs
    relevance: This shows Aider is not only a file editor; it also has different working modes for coding, architecture, asking questions, and help.
    key_point: Aider supports code, architect, ask, and help chat modes.
---

Aider is a tool that helps people write and change code with an AI inside a terminal.

In practice, you use it with a local git repository, tell it what you want changed, and it edits files for you. It also keeps the work tied to git commits so changes are easier to check, compare, and undo.

Aider matters because it turns AI coding help into a working edit flow, not just a chat. That makes it useful for real programming tasks where you need code changes, not only suggestions.

It is not the same as a general chatbot, and it is not a full replacement for version control. It is a coding assistant that works through your terminal and git history.
