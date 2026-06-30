---
title: Git worktree automation
short_description: Using Git worktrees to let automated coding tasks run in separate, isolated copies of the same repository.
category: Tools and products
tags:
- git
- worktree
- automation
- agents
- coding
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a formal Git feature name
- Confusing it with ordinary branching or cloning
- Assuming it removes the need to review agent changes
related_terms:
- git worktree
- coding agent
- branch
- pull request automation
- parallel agent sessions
evidence:
- source_title: git-worktree Documentation
  source_url: https://git-scm.com/docs/git-worktree
  source_type: official_docs
  relevance: Defines the underlying Git feature this term is built on.
  key_point: Git worktree lets one repository have multiple working trees, so you can check out more than one branch at the same time.
- source_title: Working with agent sessions in the GitHub Copilot app
  source_url: https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions
  source_type: official_docs
  relevance: Shows the current agent workflow pattern that worktree automation supports.
  key_point: GitHub says you can run multiple isolated agent sessions at the same time, each with its own branch.
- source_title: GitHub Copilot app: The agent-native desktop experience
  source_url: https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/
  source_type: engineering_blog
  relevance: Shows how a mainstream agent product uses worktrees in practice.
  key_point: GitHub says each session runs in its own git worktree so parallel agent sessions do not step on each other.
---

Git worktree automation means using Git worktrees to help automated coding tasks work in separate copies of the same project.

In practice, this lets one agent or one person run several tasks at once without every task changing the same files. Each worktree has its own checked-out branch, so the work stays separated until it is ready to merge.

The term matters because agent tools often need to do parallel work. Worktrees make that easier by reducing branch switching, file clashes, and accidental overlap between sessions.

It is not a special Git command name for automation. It is also not the same as creating a new clone for every task. The point is isolation inside one repository, not a new copy of the whole project.
