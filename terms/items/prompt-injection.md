---
title: Prompt injection
short_description: An attack where malicious instructions are hidden inside text or data so an AI follows them instead of the user’s request.
category: Governance
tags:
  - security
  - ai-agents
  - governance
  - prompt-injection
status: established
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: established
common_misuse:
  - Treating it as the same thing as a jailbreak, when jailbreaks are usually direct attempts by the user and prompt injection can also come from external content
  - Thinking it only happens in chat text, when it can also arrive through web pages, emails, documents, tool results, or other data an agent reads
  - Assuming one good system prompt can fully prevent it
related_terms:
  - jailbreak
  - indirect prompt injection
  - social engineering
  - confused deputy
  - tool use
  - agent security
evidence:
  - source_title: Understanding prompt injections: a frontier security challenge
    source_url: https://openai.com/index/prompt-injections/
    source_type: official_docs
    relevance: OpenAI gives a current plain-language definition and explains that the attack often arrives through third-party content an AI reads while doing a task.
    key_point: Prompt injection is a social engineering attack that tries to trick an AI into doing something the user did not ask for, often by hiding instructions in ordinary content.
  - source_title: Mitigate jailbreaks and prompt injections
    source_url: https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
    source_type: official_docs
    relevance: Anthropic clearly separates direct prompt injection from indirect prompt injection, which helps pin down the scope of the term.
    key_point: The attack can be direct, from a malicious user, or indirect, from untrusted content such as web pages, emails, documents, and tool results.
  - source_title: LLM Prompt Injection Prevention Cheat Sheet
    source_url: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
    source_type: standards_doc
    relevance: OWASP summarises the security impact and the common ways the attack works in real LLM applications.
    key_point: Prompt injection can change an LLM’s intended output and can lead to data leakage, unsafe actions, and bypassing safety controls.
  - source_title: Prompt Injection attack against LLM-integrated Applications
    source_url: https://arxiv.org/abs/2306.05499
    source_type: research_paper
    relevance: This paper shows prompt injection in real LLM-integrated systems and explains why the risk matters once models are connected to tools and services.
    key_point: Prompt injection can cause serious application-level harm, including prompt theft, arbitrary model use, and unintended actions.
---
Prompt injection is when someone hides instructions inside text or data so an AI system follows those instructions instead of the user’s real request.

In practice, it often happens when an AI reads a web page, email, document, chat message, or tool result that contains secret instructions written for the model. The AI may treat that hidden instruction as if it were part of the task. Direct prompt injection is when the attacker sends the harmful instruction straight to the AI. Indirect prompt injection is when the instruction is hidden inside content the AI reads on the user’s behalf.

This matters because many modern AI systems can read external content and take actions. If the injection works, the AI may ignore the user, reveal private information, or do the wrong thing in a connected app.

It is not just a bad prompt. It is not the same as a normal typo or a simple wrong answer. It is also not fully solved by writing a stronger system prompt, because the risky text can come from outside the chat and still influence the model.
