---
title: Agentic security
short_description: Security for AI systems that can plan, use tools, and take actions on a user's behalf.
category: Governance
tags:
- agentic-ai
- security
- ai-safety
- governance
status: active
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as general cybersecurity
- Assuming prompt rules alone can keep an agent safe
- Using it to mean a security operations product rather than the broader security discipline
related_terms:
- agentic AI
- prompt injection
- least privilege
- human-in-the-loop
- context poisoning
- agent identity
evidence:
- source_title: Agentic Security Initiative
  source_url: https://genai.owasp.org/initiatives/agentic-security-initiative/
  source_type: standards_doc
  relevance: OWASP names agentic security as a distinct initiative focused on securing autonomous agents and multi-step AI workflows, which supports using the term as a security discipline rather than a product name.
  key_point: The field is about securing systems that plan, act, and coordinate over multiple steps.
- source_title: Four security principles for agentic AI systems
  source_url: https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/
  source_type: engineering_blog
  relevance: AWS explains that agentic AI needs existing security practices plus new controls for autonomy, identity, access, and deterministic enforcement, which is directly relevant to what agentic security covers.
  key_point: Security for agents must be enforced outside the model's reasoning loop, with least privilege and earned autonomy.
- source_title: Architecting Security for Agentic Capabilities in Chrome
  source_url: https://blog.google/security/architecting-security-for-agentic/
  source_type: engineering_blog
  relevance: Google shows concrete security controls for agentic systems, including limited origin access, read-vs-write boundaries, and confirmation for sensitive actions.
  key_point: Agentic security is about limiting what the agent can see and do, not just telling it to behave.
- source_title: OWASP Top 10 for Agentic Applications for 2026
  source_url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
  source_type: standards_doc
  relevance: OWASP treats agentic applications as having their own major risk areas, which shows the term is emerging but increasingly formalised.
  key_point: Agentic systems create security risks such as tool misuse, identity abuse, memory poisoning, and goal hijacking.
---
Agentic security means keeping AI systems safe when they can plan, use tools, and take actions instead of only answering questions.

In practice, it means putting clear limits around what the system can see, what it can change, and when a person must approve an action. It also means checking identity, permissions, logs, and outside controls, because the AI itself should not be the thing that enforces safety.

This matters because an agent can do real-world things quickly, like send messages, move data, or make purchases. If it is tricked or given too much access, the damage can happen fast.

It is not just ordinary cybersecurity with a new name. It is also not fixed by a clever prompt or a polite instruction to the model. The term is still emerging, so people may use it slightly differently, but the core idea is security for AI systems that act on their own within limits.
