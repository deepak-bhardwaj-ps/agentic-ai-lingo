---
title: Tamper-evident audit trail
short_description: A record of actions that makes later editing, deletion, or forgery visible.
category: Agentic patterns
tags:
- audit
- logging
- security
- governance
status: active
aliases:
- tamper evident audit trail
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating a normal log as tamper-evident without protecting it from editing or deletion
- Assuming tamper-evident means tamper-proof
- Confusing a secure storage system with the audit trail itself
related_terms:
- audit trail
- audit log
- immutable log
- hash chain
- log integrity
evidence:
- source_title: Hash chain - NIST CSRC Glossary
  source_url: https://csrc.nist.gov/glossary/term/hash_chain
  source_type: standards_doc
  relevance: Defines the cryptographic idea that makes tampering visible by linking each record to the one before it.
  key_point: A hash chain is append-only data where each block includes the hash of the previous block, so changing one record changes later hashes and reveals tampering.
- source_title: AGENTSEC05-BP01 Implement comprehensive logging and audit trails - AWS Well-Architected Agentic AI Lens
  source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec05-bp01.html
  source_type: official_docs
  relevance: Shows a current platform recommendation that audit trails for agent systems should be immutable and tamper-evident.
  key_point: AWS says audit trails should be immutable and tamper-evident, and describes log file validation with SHA-256 hashes and RSA signatures to detect modification, deletion, or forgery.
- source_title: Logging Cheat Sheet - OWASP Cheat Sheet Series
  source_url: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
  source_type: standards_doc
  relevance: Gives practical guidance that logs must be protected against tampering, which is the core requirement behind a tamper-evident audit trail.
  key_point: OWASP says security logs should be protected from tampering so they can be trusted later for review and investigation.
---

## Meaning

A tamper-evident audit trail is a record of actions that is set up so later changes, deletions, or fake entries are easier to spot.

In practice, it usually means the log is append-only, protected by hashes or signatures, and stored somewhere the system cannot quietly rewrite.

## Why it matters

This matters because people need to trust the record after something goes wrong. If an agent, user, or attacker changes the log, the trail is less useful for checking what happened.

For agent systems, it helps teams review actions, investigate mistakes, and prove that the record was not quietly altered after the fact.

## What it is not

It is not the same as a normal audit trail. A normal audit trail may record events, but it may still be easy to edit.

It is also not fully tamper-proof. It tries to make tampering visible, not impossible.
