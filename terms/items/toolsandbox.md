---
title: ToolSandbox
short_description: Apple's benchmark for testing how well LLMs use tools in multi-turn, stateful conversations.
category: Evals and benchmarks
tags:
  - benchmark
  - evals
  - tool-use
  - llm-agents
status: draft
aliases: []
meaning_type: emerging_unsettled
novelty_level: medium
maturity_level: emerging
common_misuse:
  - Using ToolSandbox as a general name for any safe testing sandbox.
  - Treating it as a simple one-turn tool-calling test instead of a stateful, conversational benchmark.
  - Assuming a strong score means an agent will work safely or reliably in real use.
related_terms:
  - Tool-use benchmark
  - Agent benchmark
  - Tool calling
  - Function calling
  - Interactive benchmark
evidence:
  - source_title: ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities
    source_url: https://machinelearning.apple.com/research/toolsandbox-stateful-conversational-llm-benchmark
    source_type: official_docs
    relevance: Apple’s own research page states the term and frames it as an evaluation benchmark, which is the most authoritative source for what the name refers to.
    key_point: Apple describes ToolSandbox as a stateful, conversational, interactive evaluation benchmark for LLM tool use capabilities.
  - source_title: ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark for LLM Tool Use Capabilities
    source_url: https://arxiv.org/abs/2408.04682
    source_type: research_paper
    relevance: The paper gives the technical definition and explains how ToolSandbox differs from earlier tool-use evaluations.
    key_point: The benchmark includes stateful tool execution, implicit dependencies between tools, a built-in user simulator, and dynamic scoring across a conversation.
  - source_title: apple/ToolSandbox
    source_url: https://github.com/apple/ToolSandbox
    source_type: engineering_blog
    relevance: The repository shows how the benchmark is packaged and confirms it is a concrete evaluation suite, not a vague concept.
    key_point: The project README says the software accompanies the paper and repeats the stateful, conversational benchmark framing.
---

ToolSandbox is Apple’s benchmark for testing how well an LLM uses tools in a conversation that changes over time.

In practice, it checks whether a model can keep track of what has already happened, use the right tool, and handle results across several steps. It is meant for tasks where one choice affects the next one, not just for a single question and answer.

This matters because real tool use is messier than simple chat. A model can look good on one reply and still fail when it has to remember state, follow a chain of tool calls, or deal with missing information.

ToolSandbox is not a general sandbox for running code safely. It is also not just a basic function-calling test. It is a specific benchmark for evaluating tool use in interactive, stateful settings.
