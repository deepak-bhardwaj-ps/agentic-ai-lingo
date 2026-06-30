---
title: Patient dialogue agent
short_description: A patient-facing healthcare conversational agent that talks with patients, answers questions, and helps route basic tasks.
category: Industry verticals
tags:
  - healthcare
  - conversational-ai
  - patient-engagement
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating it as a formal clinical role instead of software.
  - Assuming it can safely diagnose, triage, or give medical advice on its own.
  - Using it as if it meant any chatbot, even when the context is specifically patient communication.
related_terms:
  - conversational agent
  - healthcare chatbot
  - patient engagement
  - nurse triage agent
  - healthcare AI agent
evidence:
  - source_title: Conversational agents in healthcare: a systematic review
    source_url: https://pubmed.ncbi.nlm.nih.gov/30010941/
    source_type: research_paper
    relevance: Shows that conversational agents in healthcare are used for patient-facing health tasks such as self-care, but the field is still emerging and safety is not always well studied.
    key_point: The review says many healthcare conversational agents support consumers with health tasks, especially self-care, and notes that safety was rarely evaluated.
  - source_title: Handoff - Healthcare agent service
    source_url: https://learn.microsoft.com/en-us/azure/health-bot/handoff
    source_type: official_docs
    relevance: Shows the patient-support pattern where a bot talks with a patient first and then hands the conversation to a human when the issue needs escalation.
    key_point: Microsoft describes a healthcare bot service that can transfer end users from a bot interaction to a human conversation, including telehealth support.
  - source_title: Helping healthcare move from data to agentic action
    source_url: https://cloud.google.com/transform/helping-healthcare-move-from-data-to-agentic-action-himms
    source_type: engineering_blog
    relevance: Shows that modern healthcare conversational agents are being built for patient and member service, with both conversation and task execution.
    key_point: Google Cloud says healthcare customer-experience agents combine conversational AI with automated task execution for patient and member services.
---

Patient dialogue agent is not a strict standard term. It usually means software in healthcare that talks with patients in plain language.

In practice, it may answer common questions, collect details before an appointment, help with bookings or reminders, and pass the conversation to a nurse, doctor, or support worker when needed.

The term matters because patient communication is a real part of care. A well-designed dialogue agent can save time, reduce wait times, and help patients get to the right next step faster.

It is not the same as a doctor, nurse, or diagnosis system. It is also not a guarantee of safe medical advice. In healthcare, these tools usually need clear limits, human oversight, and escalation paths for anything important or risky.
