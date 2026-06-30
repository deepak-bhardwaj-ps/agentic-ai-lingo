---
title: AgentClinic
short_description: A benchmark for testing clinical AI agents in simulated doctor-patient settings.
category: Evals
tags:
- benchmark
- evals
- healthcare
- clinical-ai
- agentic-ai
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: high
maturity_level: emerging
common_misuse:
- treating it as a medical chatbot instead of a test environment for AI agents
- assuming it measures real-world clinical safety or approval for use in hospitals
related_terms:
- benchmark
- evaluation set
- simulated environment
- clinical decision-making
- tool use
evidence:
- source_title: AgentClinic project site
  source_url: https://agentclinic.github.io/
  source_type: official_docs
  relevance: The project site gives the clearest current description of what AgentClinic is and how it is used.
  key_point: AgentClinic is presented as a multimodal benchmark for tool-using clinical AI agents in simulated clinical environments.
- source_title: AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments
  source_url: https://arxiv.org/abs/2405.07960
  source_type: research_paper
  relevance: This is the original paper that introduced the benchmark and explains its purpose and design.
  key_point: The paper defines AgentClinic as a benchmark for evaluating language models in sequential, interactive clinical scenarios with patient interaction and tool use.
- source_title: AgentClinic: a multimodal benchmark for tool-using clinical AI agents
  source_url: https://www.nature.com/articles/s41746-026-02674-7
  source_type: research_paper
  relevance: This newer journal publication confirms the term’s current framing and shows how the benchmark has been formalised.
  key_point: The article describes AgentClinic as a benchmark that tests clinical AI agents in simulated environments with multimodal data and tools.
---
AgentClinic is a benchmark for testing clinical AI agents in a simulated doctor-patient setting.

It is used to see how well an AI can ask questions, use tools, collect information, and reach a diagnosis step by step.

In practice, AgentClinic checks how an AI behaves in a more realistic medical flow than a simple quiz. The AI may need to talk to a patient, request tests, look at images, and update its judgement as new information appears.

The term matters because a model can score well on simple medical questions but still struggle when it has to make decisions over several turns.

AgentClinic is not a medical product, a doctor, or proof that an AI is safe to use in hospitals. It is a test, not a treatment system.
