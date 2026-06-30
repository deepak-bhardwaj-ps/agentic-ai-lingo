---
title: Maker-checker loop
short_description: A maker-checker loop is a review cycle where one agent or person makes a draft and another checks it, then the draft is revised until it passes or the loop stops.
category: Agentic patterns
tags:
  - agentic-ai
  - orchestration
  - review
  - verification
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as the same thing as a single model checking its own work.
  - Assuming the loop should run forever instead of stopping at a clear limit.
  - Using it for any feedback step, even when there is no separate checker or pass/fail test.
related_terms:
  - verification loop
  - critic loop
  - generator-verifier
  - human approval
  - group chat orchestration
evidence:
  - source_title: AI Agent Orchestration Patterns
    source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
    source_type: official_docs
    relevance: Microsoft explicitly defines maker-checker loops as an agent orchestration pattern, so this is the strongest current source for the term in AI systems.
    key_point: One agent makes or proposes something, another checks it against criteria, and the loop repeats until it is approved or a limit is reached.
  - source_title: BSA/AML Internal Controls
    source_url: https://bsaaml.ffiec.gov/manual/AssessingTheBSAAMLComplianceProgram/02
    source_type: official_docs
    relevance: Shows the long-standing banking meaning behind maker-checker style controls, where the person who makes a record should not also make the approval decision.
    key_point: Internal controls should incorporate dual controls and segregation of duties so the same employee does not both prepare and approve certain filings.
  - source_title: Enhanced Security Requirements for Protecting Controlled Unclassified Information
    source_url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-172.pdf
    source_type: standards_doc
    relevance: Gives the security-control basis for the pattern by defining dual authorization and two-person control.
    key_point: Dual authorization requires two authorised individuals to approve sensitive actions, reducing insider-risk and supporting the maker-checker idea.
---

## Meaning

A maker-checker loop is a repeat-and-review cycle where one person or agent makes a draft and another person or agent checks it before it is accepted.

In practice, the maker does the first version of the work. The checker looks at it against rules, quality goals, or safety limits. If the checker finds a problem, the draft goes back for revision. If it passes, the work moves on.

This matters because first drafts can be wrong, incomplete, or unsafe. A second check helps catch mistakes before a message is sent, a change is deployed, or a decision is finalised.

It is not the same as a system checking itself and calling that a review. The checker should be separate from the maker, or at least use a separate role and clear criteria. It is also not endless back-and-forth. Good maker-checker loops stop after a set number of tries and then escalate if needed.

The term comes from older approval and control workflows, especially in banking and security. In agent systems, it now often means one agent creates and another agent reviews.
