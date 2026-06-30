---
title: Docker sandbox
short_description: Docker’s isolated environment for letting an AI coding agent work without direct access to your host machine.
category: Tools and products
tags:
- docker
- sandbox
- agents
- isolation
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as any normal Docker container
- Confusing it with the model itself
- Using it as a generic word for all sandboxing
related_terms:
- Docker Sandboxes
- sandbox
- execution environment
- agent runtime
- control plane
- microVM
evidence:
  - source_title: Docker Sandboxes
    source_url: https://docs.docker.com/ai/sandboxes/
    source_type: official_docs
    relevance: This is Docker’s current product page and the clearest source for what the term means in practice.
    key_point: Docker says its sandboxes run AI coding agents in isolated microVM sandboxes, each with its own Docker daemon, filesystem, and network.
  - source_title: Security model
    source_url: https://docs.docker.com/ai/sandboxes/security/
    source_type: official_docs
    relevance: This explains the isolation model behind the sandbox, which is important for defining the term accurately.
    key_point: Docker describes layered isolation across the VM, network, Docker Engine, workspace, and credentials.
  - source_title: Sandbox Agents
    source_url: https://developers.openai.com/api/docs/guides/agents/sandboxes
    source_type: official_docs
    relevance: This helps distinguish the sandbox from the surrounding agent system and shows the common architecture pattern.
    key_point: OpenAI separates the harness or control plane from the sandbox execution plane, where files are changed and commands run.
---

A Docker sandbox is an isolated place where an AI coding agent can do work without touching your host computer directly.

In practice, Docker gives the agent its own small machine space, with its own files, network, and Docker environment. The agent can build software, install packages, run commands, and change files inside that space.

This matters because AI agents can make mistakes. A sandbox helps limit the damage if the agent breaks something, downloads the wrong thing, or runs the wrong command.

It is not the AI model itself. It is also not just a normal Docker container, if the product is using microVM isolation. In this glossary, the term refers to Docker’s agent sandbox product, not to every kind of sandboxed Docker setup.
