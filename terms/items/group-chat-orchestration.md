---
title: Group chat orchestration
short_description: Multi-agent coordination where agents share one conversation thread and an orchestrator controls who speaks next.
category: Agentic patterns
tags:
- agents
- orchestration
- multi-agent
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating any multi-agent system as group chat, even when agents do not share one conversation thread
- Assuming the group chat format is always better than a simpler workflow
- Confusing the chat format with the actual decision logic that picks the next speaker
related_terms:
- Agent orchestration
- Multi-agent orchestration
- Handoff orchestration
- Supervisor agent
- Multi-agent system
evidence:
  - source_title: Group Chat orchestration
    source_url: https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/group-chat
    source_type: official_docs
    relevance: This is the clearest current product documentation for the term and defines it as a collaborative conversation among multiple agents managed by an orchestrator.
    key_point: The orchestrator decides speaker selection and conversation flow in a shared agent conversation.
  - source_title: Group Chat
    source_url: https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/group-chat.html
    source_type: official_docs
    relevance: AutoGen describes the underlying design pattern in practical terms, showing that agents share one message thread and often have specialised roles.
    key_point: Group chat is a shared message thread where each participant can publish and subscribe, usually with specialised agent roles.
  - source_title: Building Effective AI Agents
    source_url: https://www.anthropic.com/research/building-effective-agents
    source_type: engineering_blog
    relevance: Anthropic explains that useful agent systems are usually built from simple coordination patterns rather than one big autonomous system, which helps distinguish this term from vague multi-agent hype.
    key_point: Coordination should be explicit and composable, not left as an undefined blob of agent behaviour.
  - source_title: Group Chat orchestration pattern
    source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
    source_type: standards_doc
    relevance: This architecture guide confirms the pattern is used for iterative refinement, collaborative problem-solving, and quality gates, and that a manager controls who responds next.
    key_point: Group chat orchestration is a shared conversation pattern with controlled turn-taking and optional human input.
---

Group chat orchestration is a way of coordinating several AI agents through one shared conversation.

In practice, the agents do not work in separate silos. They talk in the same thread, and an orchestrator or manager decides who should speak next. That makes it useful when different agents have different jobs, such as planning, checking, or improving an answer.

The term matters because some tasks are easier to solve by letting agents discuss and refine work step by step. It can also support human review when a person needs to join the conversation.

It is not the same as just putting many agents in one system. It is also not the same as a simple pipeline, where each step always happens in a fixed order. The important part is the shared chat thread plus the control logic for turn-taking.
