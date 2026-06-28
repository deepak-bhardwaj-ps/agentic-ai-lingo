---
title: Context Poisoning
short_description: Context poisoning is when untrusted text is put into an AI agent's
  working context and changes what it does.
category: Context
tags:
- agentic-ai
- security
- prompt-injection
- context
status: emerging
aliases:
- Memory poisoning
- Working memory poisoning
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as training-data poisoning
- Assuming the model can safely ignore malicious instructions on its own
- Using the term for any bad answer, even when no untrusted context was involved
related_terms:
- Prompt injection
- Indirect prompt injection
- RAG poisoning
- Data poisoning
- Tool manipulation
evidence:
- source_title: LLM Prompt Injection Prevention Cheat Sheet
  source_url: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
  source_type: official_docs
  relevance: Defines context poisoning as false information injected into an agent's
    working memory and lists it as an agent-specific attack.
  key_point: Untrusted content in the agent's context can steer later model behaviour
    and tool use.
- source_title: Architecting Security for Agentic Capabilities in Chrome
  source_url: https://blog.google/security/architecting-security-for-agentic/
  source_type: engineering_blog
  relevance: Shows how indirect prompt injection in web content can make an agent
    take unwanted actions.
  key_point: Content the agent reads from the web can change its decisions unless
    the system adds isolation and confirmation controls.
- source_title: OWASP Top 10 for Agentic Applications for 2026
  source_url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
  source_type: standards_doc
  relevance: Confirms that memory and context poisoning is treated as a major risk
    for agentic systems.
  key_point: OWASP treats poisoned context as a real security problem for systems
    that plan and act on behalf of users.
---

Context poisoning is when untrusted information gets into an AI agent's working context and changes what it does next.

In practice, this can happen when an agent reads a web page, document, email, chat message, or tool output that contains hidden or misleading instructions. The agent may then follow those instructions instead of the user's request.

This matters because agents often act on what they read. If bad content reaches the agent's [[Working Memory|working memory]], it can make the system leak information, call the wrong tool, or take an action the user did not want.

It is not the same as normal bad input or a simple wrong answer. It is also not fixed by telling the model to "ignore malicious text". Real defences usually need trusted and untrusted content to be kept separate, with checks before the agent can act.
