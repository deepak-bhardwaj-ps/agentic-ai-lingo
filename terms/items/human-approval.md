---
title: Human approval
short_description: A pause in a workflow where a person must approve a sensitive action before it continues.
category: Governance and security
tags:
  - agent safety
  - human-in-the-loop
  - approvals
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as the same thing as human oversight or general supervision.
  - Assuming it means the human checks every step, instead of only the risky one.
related_terms:
  - human-in-the-loop
  - human oversight
  - approval gate
  - tool approval
  - guardrails
evidence:
  - source_title: Guardrails and human review
    source_url: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
    source_type: official_docs
    relevance: OpenAI defines human review as the approval decision point in an agent workflow.
    key_point: Human review pauses the run so a person or policy can approve or reject a sensitive action.
  - source_title: Human approval
    source_url: https://developers.openai.com/api/docs/guides/node-reference
    source_type: official_docs
    relevance: Shows how the term is used in practice inside a workflow builder.
    key_point: A human approval node defers to end-users for approval before the workflow continues.
  - source_title: Deploying a workflow that waits for human approval in Step Functions
    source_url: https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html
    source_type: official_docs
    relevance: Shows the classic workflow meaning outside AI tooling: a process pauses until a person approves it.
    key_point: The workflow pauses during a task and continues only after the user approves it.
  - source_title: App. C: AI Risk Management and Human-AI Interaction
    source_url: https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/
    source_type: standards_doc
    relevance: Explains why human approval is part of broader human-AI decision-making and risk control.
    key_point: NIST says human roles and responsibilities in AI decision making need to be clearly defined, with some systems specifically requiring human oversight.
---
Human approval is when a person must say yes before a system carries out a sensitive action.

In practice, the system stops at a checkpoint and waits. The person can approve, reject, or sometimes change the request before it continues. This is common when an AI agent is about to send an email, make a payment, delete data, or do anything with real-world effects.

It matters because it reduces the chance that a system makes a risky mistake on its own. It gives a person the final say on actions that could affect money, private data, or important decisions.

Human approval is not the same as general human oversight. Oversight is broader and can mean watching, reviewing, or setting rules across a whole system. Human approval is narrower: it is a specific pause where a human must authorise one action.
