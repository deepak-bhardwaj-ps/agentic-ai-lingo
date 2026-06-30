---
title: Zero-trust identity
short_description: Identity-focused zero trust that checks who or what is asking for access every time.
category: Protocols and standards
tags:
  - security
  - identity
  - zero-trust
status: stable
aliases: []
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: maturing
common_misuse:
  - Treating it as a separate product or standard instead of a way of applying zero trust to identity checks.
  - Using it to mean only one-time login verification, instead of ongoing access decisions.
related_terms:
  - zero trust
  - identity and access management
  - conditional access
  - identity governance
  - trusted identity management
evidence:
  - source_title: Zero Trust Architecture
    source_url: https://csrc.nist.gov/pubs/sp/800/207/final
    source_type: standards_doc
    relevance: NIST defines zero trust as a cybersecurity approach that removes implicit trust and requires authentication and authorisation before access.
    key_point: This supports the idea that identity is checked as part of access decisions, not trusted just because someone is on the network.
  - source_title: Identity, the first pillar of a Zero Trust security architecture
    source_url: https://learn.microsoft.com/en-us/security/zero-trust/deploy/identity
    source_type: official_docs
    relevance: Microsoft explicitly uses the phrase "Identity Zero Trust" and describes it as putting identity checks, conditional access, and identity governance into the access path.
    key_point: This shows how the term is used in practice: identity becomes the control point for zero trust decisions.
  - source_title: Final Draft NSTAC Report to the President on Zero Trust and Trusted Identity Management
    source_url: https://www.cisa.gov/sites/default/files/publications/Final%20Draft%20NSTAC%20Report%20to%20the%20President%20on%20Zero%20Trust%20and%20Trusted%20Identity%20Management.pdf
    source_type: standards_doc
    relevance: CISA's NSTAC report links zero trust directly with trusted identity management, showing that the identity side of zero trust is a recognised government framing.
    key_point: This supports the term as identity-centred zero trust rather than a separate security model.
---

Zero-trust identity means using identity checks as the main gate for access in a zero trust system.

In practice, that means a system does not trust a person, device, or app just because it is inside a company network. It checks who or what is asking, whether the device looks safe, and whether the request should be allowed right now.

This matters because stolen passwords, risky devices, and strange login locations can be caught before access is granted. It also helps organisations give people the access they need without opening everything up all the time.

This is not a separate security product or a formally agreed standard. It is a phrase people use to describe the identity part of zero trust. It is also not just a one-time login check, because zero trust keeps re-evaluating access as conditions change.
