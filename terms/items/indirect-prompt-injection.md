---
title: Indirect prompt injection
short_description: Malicious instructions hidden inside content an AI system reads later, such as a web page, file, email, or tool output.
category: Governance and security
tags:
  - security
  - prompt-injection
  - agentic-ai
status: emerging
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the same thing as direct prompt injection
  - Assuming it only matters when the attacker talks to the user directly
  - Assuming the model can safely ignore hostile text without system controls
related_terms:
  - Prompt injection
  - Context poisoning
  - Confused deputy
  - Tool manipulation
  - Data exfiltration
evidence:
  - source_title: Prompt Injection
    source_url: https://owasp.org/www-community/attacks/PromptInjection
    source_type: standards_doc
    relevance: OWASP gives a clear, current security classification that separates direct and indirect delivery paths.
    key_point: Indirect prompt injection is when malicious prompts are embedded in content like a web page or email that the model processes later.
  - source_title: Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection
    source_url: https://arxiv.org/abs/2302.12173
    source_type: research_paper
    relevance: Foundational paper that coined and demonstrated the attack against real LLM-integrated applications.
    key_point: External data can carry instructions that are followed by the model even though the user did not intend them.
  - source_title: Mitigate jailbreaks and prompt injections
    source_url: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
    source_type: official_docs
    relevance: Current product guidance that explicitly names indirect prompt injection as a live risk in agent workflows.
    key_point: Third-party content such as web pages, emails, documents, and tool results can contain adversarial instructions.
  - source_title: Understanding prompt injections: a frontier security challenge
    source_url: https://openai.com/index/prompt-injections/
    source_type: engineering_blog
    relevance: Current explanation from a major lab showing why third-party content in agent context is the core problem.
    key_point: The threat comes from content from many sources being mixed into the conversation context, not just the user prompt.
---

Indirect prompt injection is when harmful instructions are hidden inside content that an AI system reads later.

In practice, the attacker does not need to talk to the model directly. They can hide instructions in a web page, document, email, chat message, or tool result. If the agent reads that content as part of its task, it may follow the hidden instructions instead of the user's request.

This matters because AI agents often trust what they read. A successful attack can make the system leak information, use the wrong tool, or take an action the user did not want.

It is not the same as direct prompt injection, where the attacker puts the bad instructions straight into the prompt. It is also not just a normal wrong answer. The problem is that untrusted content was mixed into the agent's working context.
