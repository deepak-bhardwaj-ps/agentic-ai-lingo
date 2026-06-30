---
title: AML agent
short_description: An AI agent used for anti-money laundering work such as screening, investigation, and alert triage.
category: Industry verticals
tags:
  - finance
  - compliance
  - ai-agents
status: draft
aliases:
  - anti-money laundering agent
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as any banking chatbot rather than a tool for AML screening and investigation.
  - Assuming it can make final compliance decisions without human review.
related_terms:
  - anti-money laundering
  - financial crime compliance
  - sanctions screening
  - transaction monitoring
  - fraud detection agent
evidence:
  - source_title: FinCEN home page
    source_url: https://www.fincen.gov/
    source_type: official_docs
    relevance: Establishes what AML work is for in the US context.
    key_point: FinCEN says its mission is to counter money laundering and support analysis of financial intelligence, which is the work an AML agent is meant to help with.
  - source_title: Opportunities and Challenges of New Technologies for AML/CFT
    source_url: https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/Opportunities-Challenges-of-New-Technologies-for-AML-CFT.pdf
    source_type: standards_doc
    relevance: Shows how official AML standards describe technology use in AML/CFT.
    key_point: FATF says AI and machine learning can help monitor suspicious transactions, improve risk assessment, and reduce manual review, but human input still matters.
  - source_title: Robinhood transforms financial crimes investigations using Amazon Bedrock
    source_url: https://aws.amazon.com/solutions/case-studies/robinhood-case-study/
    source_type: engineering_blog
    relevance: Shows a real production-style agent used for financial-crime investigations.
    key_point: Robinhood describes a FinCrimes Agent that summarises records and supports investigator oversight for high-volume alerts.
---

An AML agent is an AI agent that helps with anti-money laundering work.

In practice, it can review transaction alerts, gather details about a customer or payment, spot patterns that look unusual, and draft a summary for a compliance analyst.

It matters because AML teams often face too many alerts and too much data for people to check quickly by hand.

It is not a magic fraud detector, and it does not replace the compliance team. A real AML agent still needs rules, human review, and clear records of what it did.
