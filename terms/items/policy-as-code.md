---
title: Policy-as-code
short_description: Writing rules as machine-readable code so they can be checked, tested,
  and enforced automatically.
category: Protocols and standards
tags:
- governance
- security
- compliance
- automation
status: active
aliases:
- PaC
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating any script or checklist as policy-as-code, when the term usually means
  a readable policy definition that can be versioned, tested, reviewed, and enforced
  by software.
- Confusing it with general programming. The code is for rules and decisions, not
  for building the whole application.
related_terms:
- policy engine
- guardrails
- compliance-as-code
- infrastructure as code
- access control
evidence:
  - source_title: Policy as Code
    source_url: https://openpolicyagent.org/docs
    source_type: official_docs
    relevance: Shows the term in current use by a major policy engine project and
      links it to automated policy decision-making across software systems.
    key_point: OPA describes policy as code as using a declarative language and APIs
      to offload policy decision-making from application code.
  - source_title: Policy as Code
    source_url: https://developer.hashicorp.com/sentinel/docs/concepts/policy-as-code
    source_type: official_docs
    relevance: Gives a clear, practical definition from a widely used policy product
      and explains the software engineering benefits.
    key_point: HashiCorp says policy as code means writing policies in a high-level
      language so they can be version controlled, tested, and deployed like software.
  - source_title: Policy as Code (PaC) - Cloud Native Glossary
    source_url: https://glossary.cncf.io/policy-as-code/
    source_type: standards_doc
    relevance: Provides a neutral glossary definition that is useful for keeping the
      term broad and not tied to one vendor.
    key_point: CNCF defines policy as code as storing policy definitions in machine-readable,
      processable files instead of only human-readable documents.
  - source_title: Introduction to Policy as Code
    source_url: https://www.cncf.io/blog/2025/07/29/introduction-to-policy-as-code/
    source_type: industry_article
    relevance: Confirms the term is still used in cloud-native practice and connects
      it to guardrails and declarative infrastructure workflows.
    key_point: CNCF’s newer explainer treats policy as code as a practical way to
      implement guardrails with code-like artefacts.
---

Policy-as-code means writing rules in a machine-readable form so software can check them automatically.

In practice, teams use it for things like security rules, access rules, cloud configuration checks, and deployment approvals. The policy is kept like software: it can be stored in version control, reviewed, tested, and updated over time.

This matters because it makes rules easier to apply consistently. A person does not need to check every change by hand. The system can stop unsafe or non-compliant changes before they go live.

Policy-as-code is not the same as writing the whole app in code. It is also not just a manual checklist saved in a file. The key idea is that the rules can be read by software and used to make an allow-or-block decision.
