---
slug: procedural-memory
name: Procedural Memory
category: Memory
title: Procedural Memory
aliases:
- how-to memory
short_description: Memory for how to do a task, like following a workflow or using
  a skill.
status: established
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Using it to mean any stored memory, including facts or chat history.
- Treating it as model training or a weight update.
related_terms:
- declarative memory
- semantic memory
- episodic memory
- nondeclarative memory
- agent memory
evidence:
- source_title: Procedural-Memory, Working-Memory, and Declarative-Memory in the Brain
  source_url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6175975/
  source_type: research_paper
  relevance: Gives a standard cognitive-science definition of procedural memory as
    learned skills and sequences.
  key_point: Procedural memory supports skills and learned action sequences that become
    more automatic with practice.
- source_title: Nondeclarative memory
  source_url: https://dictionary.apa.org/nondeclarative-memory
  source_type: standards_doc
  relevance: Shows the mainstream psychology framing of procedural learning as part
    of nondeclarative memory.
  key_point: Nondeclarative memory includes procedural learning and is different from
    memories you can state in words.
- source_title: Memory overview
  source_url: https://docs.langchain.com/oss/python/concepts/memory
  source_type: industry_article
  relevance: Shows how modern agent systems use procedural memory as instructions,
    prompts, and code that shape behaviour.
  key_point: In agent systems, procedural memory is the rules and instructions that
    tell the agent how to act.
- source_title: 'MemGPT: Towards LLMs as Operating Systems'
  source_url: https://arxiv.org/abs/2310.08560
  source_type: research_paper
  relevance: Important AI reference for memory tiers in LLM agents, including the
    idea of storing reusable operating instructions separately from facts.
  key_point: MemGPT uses separate memory layers so an LLM can manage long-term context
    and control behaviour more effectively.
---

Procedural memory is memory for how to do something.

In people, it means learned skills and habits that can run almost automatically after enough practice, like typing, riding a bike, or using a familiar routine. In AI agents, the term is often used for the instructions, tools, prompts, and code that tell the agent how to behave.

It matters because knowing how to do a task is different from knowing facts about the world. A system can remember a fact and still not know the right steps to act on it.

It is not the same as chat history, facts, or model training. It is also not a model weight update. In agent design, it is better thought of as the system’s playbook than its memory of events.
