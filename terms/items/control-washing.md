---
slug: control-washing
title: Control Washing
short_description: A claim that something is tightly controlled when the real controls are weak, missing, or hard to prove.
category: Slang
tags:
  - ai-governance
  - safety
  - misleading-claims
status: Informal slang
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Used as if it means the same thing as a formal audit finding; it is really a criticism that the control story does not match the evidence.
  - Used to describe any system with controls, even when the issue is only that the controls are weak or not independently checked.
related_terms:
  - guardrails
  - human approval
  - ai washing
  - agent washing
evidence:
  - source_title: Guardrails and human review | OpenAI API
    source_url: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
    source_type: official_docs
    relevance: Shows what real controls look like in an agent workflow: automatic checks, pauses, and approval decisions.
    key_point: OpenAI separates guardrails from human review and says they decide whether a run should continue, pause, or stop.
  - source_title: AI Risk Management Framework 1.0
    source_url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
    source_type: standards_doc
    relevance: Supports the idea that control claims need monitoring, documentation, and accountability, not just a label.
    key_point: NIST says AI risks are hard to detect in complex systems and that trustworthiness depends on accountability, transparency, and ongoing risk management.
  - source_title: Truth in Advertising | Federal Trade Commission
    source_url: https://www.ftc.gov/news-events/topics/truth-advertising
    source_type: official_docs
    relevance: Gives the broader evidence rule behind the term: claims must be truthful, not misleading, and backed by evidence.
    key_point: The FTC says ads must be truthful, not misleading, and, when appropriate, backed by scientific evidence.
  - source_title: The dangers of AI agentwashing
    source_url: https://www.thoughtworks.com/en-us/insights/blog/generative-ai/Agentwashing-and-how-AI-agents-fail-us
    source_type: engineering_blog
    relevance: Shows the broader "-washing" pattern used in AI discussions when a label makes something sound more capable or controlled than it really is.
    key_point: Thoughtworks argues that "agentwashing" is overused, overhyped, and often misapplied, which matches the style of criticism behind control washing.
---

Control washing is when something is described as tightly controlled, but the real controls are weak, missing, or hard to verify.

In practice, it means looking past the promise and checking the facts. Are there real [[Guardrails|guardrails]]? Can people override the system? Is there logging, human review, and a named owner who is accountable? If not, the control claim may be overstated.

The term matters because people can trust a system too much if the controls only exist on paper. That can lead to bad decisions, unsafe behaviour, or problems nobody is clearly responsible for.

Control washing is not a formal technical test. It is a criticism of how something is described. It does not prove a system is unsafe by itself. It says the claim of strong control needs evidence.
