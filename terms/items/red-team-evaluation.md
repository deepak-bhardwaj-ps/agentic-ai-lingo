---
title: Red team evaluation
short_description: A structured test that tries to break an AI system by using adversarial, harmful, or unexpected inputs.
category: Evals and benchmarks
tags:
- evals
- safety
- security
status: active
aliases: []
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as the same thing as a normal benchmark with friendly test cases
- Assuming one red team run proves the system is safe
- Using it as a vague label for any AI test, without adversarial probing
related_terms:
- red teaming
- evaluation
- adversarial evaluation
- safety benchmark
- prompt injection
- jailbreak
evidence:
- source_title: Red teaming
  source_url: https://developers.openai.com/api/docs/guides/red-teaming
  source_type: official_docs
  relevance: This is the clearest current product guidance on how OpenAI distinguishes red teaming from ordinary evals, which is central to this term.
  key_point: OpenAI says evals measure whether a system behaves as intended, while red teaming probes adversarial, abusive, or unexpected inputs.
- source_title: Artificial Intelligence Risk Management Framework: Generative AI Profile
  source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
  source_type: standards_doc
  relevance: NIST gives a formal definition of AI red-teaming that fits the meaning behind a red team evaluation.
  key_point: NIST defines AI red-teaming as a structured testing exercise used to probe an AI system for flaws and vulnerabilities such as inaccurate, harmful, or discriminatory outputs.
- source_title: Managing Misuse Risk for Dual-Use Foundation Models
  source_url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd2.pdf
  source_type: standards_doc
  relevance: Reinforces that red teaming is an adversarial testing method focused on flaws, vulnerabilities, and misuse risk.
  key_point: NIST says AI red-teaming uses adversarial methods to find flaws and vulnerabilities, including unforeseen or undesirable system behaviour and misuse risks.
- source_title: Anthropic Transparency Hub
  source_url: https://www.anthropic.com/transparency
  source_type: engineering_blog
  relevance: Shows current industry use of red-team exercises for specific safety and abuse tests such as prompt injection.
  key_point: Anthropic describes externally conducted red-team exercises and prompt-injection evaluations as ways to measure whether attacks succeed.
---

Red team evaluation is a structured test that tries to break an AI system by using adversarial, harmful, or unexpected inputs.

In practice, people use a red team evaluation to see how a system behaves when someone tries to trick it, overload it, or make it do the wrong thing. The test may look for unsafe answers, prompt injection, jailbreaks, or other failures that do not show up in ordinary testing.

The term matters because a system can look fine in normal use and still fail badly under pressure. Red team evaluation helps teams find weak spots before users or attackers do.

It is not the same as a normal benchmark with friendly test cases. It is also not a guarantee that the system is safe in every real-world situation. The term is a bit loose, so people sometimes use it to mean red teaming itself, or a benchmark built around adversarial attacks.
