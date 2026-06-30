---
slug: autonomy-boundaries
name: Autonomy Boundaries
category: Governance
title: Autonomy Boundaries
aliases: []
short_description: Rules that define what an AI agent may do by itself and when a person must approve it.
status: active
meaning_type: rebranded_old_idea
novelty_level: low
maturity_level: established
common_misuse:
  - Treating it as the same thing as general automation
  - Treating it as a label instead of enforced limits
  - Assuming the model is autonomous just because it can make some choices
related_terms:
  - action governance
  - human approval
  - permissions
  - sandbox
  - human oversight
evidence:
  - source_title: Agent approvals & security
    source_url: https://developers.openai.com/codex/agent-approvals-security
    source_type: official_docs
    relevance: Shows that agent systems need technical boundaries and approval rules, not just a smart model.
    key_point: OpenAI separates sandbox limits from approval policy and says the agent can move freely only inside the defined boundary.
  - source_title: Sandbox
    source_url: https://developers.openai.com/codex/concepts/sandboxing
    source_type: official_docs
    relevance: Explains the idea of a technical boundary in a very direct way.
    key_point: OpenAI says the sandbox defines what the agent can do on its own, and approvals decide when it must stop and ask before crossing the boundary.
  - source_title: OWASP Top 10 for Large Language Model Applications
    source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
    source_type: standards_doc
    relevance: Grounds the term in a recognised security risk around too much unchecked autonomy.
    key_point: OWASP warns that excessive autonomy is risky when a system can take high-impact actions without independent checks and approval.
  - source_title: Secure autonomous agentic AI systems
    source_url: https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems
    source_type: official_docs
    relevance: Shows that agent behaviour should stay within defined intent, permissions, and boundaries.
    key_point: Microsoft says agents should operate within permissions and boundaries, and risky actions should require deterministic human approval.
---

Autonomy boundaries are the rules that say what an AI agent may do by itself and what needs a person to check first.

In practice, this means deciding which tools it can use, which actions it can take, which data it can reach, and when it must stop and ask for approval. It also means making those limits real in the software, not just writing them down.

The term matters because an agent that can act without clear limits can make mistakes faster than a person can notice them. Good boundaries reduce the chance of unsafe actions, surprise costs, data leaks, and changes that nobody approved.

Autonomy boundaries are not the same as “the model is smart” or “the system is automated”. They are not just a label on a diagram. If the limits are not enforced by permissions, sandboxing, or approval checks, there is no real boundary.
