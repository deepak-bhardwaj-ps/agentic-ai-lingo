---
title: Lab automation agent
short_description: A lab automation agent is software that helps plan, control, or adjust laboratory work, often by working with robots, instruments, and experiment data.
category: Industry verticals
tags: [ai-agents, life-sciences, laboratory-automation, autonomous-lab]
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Treating any lab software or dashboard as an agent
  - Assuming the agent can run a lab safely without human review
  - Using the term as if it meant the same thing as a self-driving lab in every case
related_terms:
  - autonomous lab
  - self-driving laboratory
  - laboratory automation
  - scientific agent
  - lab robot
evidence:
  - source_title: Autonomous Lab
    source_url: https://www.ginkgo.bio/autonomous-lab
    source_type: official_docs
    relevance: Ginkgo gives one of the clearest current industry descriptions of lab autonomy levels and explicitly says an AI agent can turn human-language research plans into work for an autonomous lab.
    key_point: The source shows that a lab automation agent can sit between a scientist’s goal and the lab hardware, turning a research plan into executable lab work.
  - source_title: Science acceleration and accessibility with self-driving labs
    source_url: https://www.nature.com/articles/s41467-025-59231-1
    source_type: research_paper
    relevance: This Nature Communications paper describes self-driving labs as systems that automate experiment tasks and experiment selection, which is the closest established scientific meaning to a lab automation agent.
    key_point: Self-driving labs are described as automating experimental tasks and the design and selection of experiments, which helps define what a lab automation agent usually does in practice.
  - source_title: Toward Full Autonomous Laboratory Instrumentation Control with Large Language Models
    source_url: https://arxiv.org/abs/2604.03286
    source_type: research_paper
    relevance: This paper directly links LLM agents to controlling laboratory instruments and to automating scientific equipment, showing the term is used for software that operates lab hardware rather than a simple chatbot.
    key_point: The paper frames AI agents as able to operate lab instruments and refine control strategies, which matches the likely meaning of the glossary term.
---

A lab automation agent is software that helps run parts of a laboratory workflow.

It can turn a scientist’s instructions into actions for lab instruments, robots, scheduling tools, or analysis software. In some systems it may help choose the next experiment, but people still need to set the goal, check the plan, and review the results.

The term matters because lab work is full of repeated steps, careful measurements, and equipment that must be used correctly. An agent can reduce manual effort and help experiments move faster.

It is not the same as ordinary lab software that only stores data or shows charts. It is also not the same as a fully autonomous lab in every case. The phrase is still a bit unsettled, so different teams may use it to mean slightly different levels of control.
