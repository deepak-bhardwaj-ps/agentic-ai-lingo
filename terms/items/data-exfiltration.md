---
title: Data exfiltration
short_description: Data exfiltration is the unauthorised transfer of data out of a system.
category: Governance and security
tags:
- security
- governance
- data-protection
status: active
aliases:
- exfiltration
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Using it for any data movement, even when the transfer is allowed
- Treating it as the same thing as data leakage, which can also happen by accident
- Assuming it only means copying files, when it can also happen through APIs, cloud storage, email, or other channels
related_terms:
- data breach
- data leakage
- exfiltration
- data staging
- double extortion
evidence:
  - source_title: Exfiltration, Tactic TA0010 - Enterprise - MITRE ATT&CK®
    source_url: https://attack.mitre.org/tactics/TA0010/
    source_type: standards_doc
    relevance: MITRE is a widely used threat model, and this tactic explains how attackers move stolen data out of a target network.
    key_point: Exfiltration is the phase where an adversary tries to steal data and remove it from the target, often while trying to avoid detection.
  - source_title: exfiltration - Glossary - NIST CSRC
    source_url: https://csrc.nist.gov/glossary/term/exfiltration
    source_type: standards_doc
    relevance: NIST provides a plain, authoritative cybersecurity definition that matches how the term is used in security work.
    key_point: Exfiltration means the unauthorised transfer of information from an information system.
  - source_title: I've Been Hit By Ransomware! - CISA
    source_url: https://www.cisa.gov/stopransomware/ive-been-hit-ransomware
    source_type: official_docs
    relevance: CISA shows how the term is used in incident response, especially when attackers steal data before or during extortion.
    key_point: Data exfiltration is a real incident sign that defenders look for, and it often appears in ransomware cases alongside threats to publish stolen data.
---

Data exfiltration is the unauthorised transfer of data out of a system.

In practice, it means someone gets data out of a computer, network, app, or cloud service without permission. The data might be copied to another server, sent through an API, uploaded to cloud storage, emailed out, or packaged and hidden to avoid detection.

This matters because stolen data can be sold, exposed, or used for extortion. In security incidents, exfiltration often turns a break-in into a serious breach.

It is not the same as normal data movement. It is also not the same as a data leak caused by a mistake, although both can expose information.

The term is well established in cybersecurity. In some contexts, people shorten it to just "exfiltration".
