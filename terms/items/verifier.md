---
slug: verifier
title: Verifier
short_description: A verifier checks whether an output or action meets a set of rules.
category: Runtime
tags:
- runtime
- checking
- evaluation
status: Architecture component
aliases:
- checker
- validation component
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating a verifier as if it guarantees correctness in every case.
- Using a model-based judge when a simple rule or test would be safer.
related_terms:
- eval
- grader
- guardrail
- policy engine
- test suite
evidence:
- source_title: Working with evals
  source_url: https://developers.openai.com/api/docs/guides/evals
  source_type: official_docs
  relevance: OpenAI describes evals as tests that check model outputs against criteria
    you define.
  key_point: Evals are used to judge whether outputs meet style and content requirements,
    which is the basic job of a verifier.
- source_title: Reduce hallucinations
  source_url: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
  source_type: official_docs
  relevance: Anthropic explains verification as checking claims against quotes, sources,
    and repeated runs.
  key_point: Verification can mean checking evidence after generation and removing
    claims that cannot be supported.
- source_title: verifier - Glossary
  source_url: https://csrc.nist.gov/glossary/term/verifier
  source_type: standards_doc
  relevance: NIST uses verifier for a party or device that checks identity, authenticity,
    or signatures.
  key_point: The term has a long history outside AI and generally means something
    that checks whether a claim is valid.
---

A verifier is a checker. It looks at an answer, action, or result and decides whether it matches the rules it was given.

In practice, a verifier can be a test suite, a policy check, a type checker, a rule engine, or a separate model that judges another model’s output. The important part is that it checks something against a clear standard instead of just making a new guess.

Verifiers matter because they help catch mistakes before a result is used, shown to a user, or sent to another system. They are useful when the cost of a wrong answer is high and when the rule can be checked more reliably than the original output.

A verifier is not the same as the thing it checks. It does not make a system correct by itself, and if it uses another model, it can still make mistakes. It is best thought of as a guard that checks for obvious or defined failures, not as perfect proof.
