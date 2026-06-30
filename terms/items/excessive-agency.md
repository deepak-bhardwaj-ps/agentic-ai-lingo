---
title: Excessive agency
short_description: An agent has excessive agency when it is given too much power, permission, or freedom to act, so it can do harmful things.
category: Governance and security
tags:
- governance
- security
- agentic-ai
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a general feeling of being overactive instead of a security risk about real actions
- Confusing it with prompt injection, which is about bad instructions, not the power to act
- Thinking a warning in the prompt is enough without real permission checks
related_terms:
- delegated authority
- permission gates
- least privilege
- human approval
- prompt injection
evidence:
- source_title: LLM06:2025 Excessive Agency
  source_url: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
  source_type: standards_doc
  relevance: OWASP is the main source that defines the term for LLM and agent security.
  key_point: Excessive agency is when unexpected, ambiguous, or manipulated model outputs can trigger damaging actions, usually because the system gives the model too much functionality, permission, or autonomy.
- source_title: Excessive agency - Generative AI Lens
  source_url: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec05.html
  source_type: official_docs
  relevance: AWS explains the term in practical agent design language.
  key_point: AWS says agents can take actions beyond their intended purpose, which is why least privilege and permission boundaries matter.
- source_title: AGENTSEC04-BP02 Human-in-the-loop for critical decisions
  source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04-bp02.html
  source_type: official_docs
  relevance: Shows how to reduce the risk by adding review at high-risk decision points.
  key_point: AWS recommends risk-tiered approval, auditable human review, and deterministic policy checks instead of unbounded autonomy.
- source_title: Safety in building agents
  source_url: https://developers.openai.com/api/docs/guides/agent-builder-safety
  source_type: official_docs
  relevance: Shows a current vendor recommendation to keep tool approvals on for agent actions.
  key_point: OpenAI advises enabling tool approvals so users can review and confirm operations, including reads and writes, before they happen.
---

Excessive agency means an AI agent has too much power to act on its own.

In practice, this usually means the agent can call tools, change data, send messages, or make other real-world changes when it should have been more limited.

The term matters because the damage comes from the actions the agent is allowed to take, not just from the words it produces. If the agent has too much access, a bad instruction, a mistake, or a tricked model can cause harm quickly.

It is not the same as prompt injection. Prompt injection is about harmful instructions getting into the model’s input. Excessive agency is about the system giving the model too much ability to act.

The usual fix is to limit what the agent can do, use the least possible permissions, and require human approval for high-risk actions.
