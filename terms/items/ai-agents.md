---
slug: ai-agents
name: AI Agents
title: AI Agents
category: Core
short_description: Software that can work towards a goal by choosing next steps, using
  tools, and learning from what happens after it acts.
aliases:
- agentic AI
status: Umbrella term
meaning_type: overloaded_buzzword
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating any chatbot as an agent
- Assuming the system is fully autonomous
- Using the word without saying what actions it can take, what tools it can use, or
  when a human must approve
related_terms:
- chatbot
- workflow
- tool use
- autonomy
- multi-agent system
evidence:
- source_title: Agents SDK
  source_url: https://developers.openai.com/api/docs/guides/agents
  source_type: official_docs
  relevance: Defines agents in terms of planning, tool use, coordination, and state.
  key_point: Agents are applications that plan, call tools, collaborate across specialists,
    and keep enough state to complete multi-step work.
- source_title: Building Effective AI Agents
  source_url: https://www.anthropic.com/research/building-effective-agents
  source_type: engineering_blog
  relevance: Shows the term is broad and that many useful agents are built from simple
    parts.
  key_point: Effective agent systems are usually combinations of a model, tools, memory,
    and control logic rather than one fixed design.
- source_title: AI Agent Standards Initiative
  source_url: https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative
  source_type: standards_doc
  relevance: Shows the term is now used in security and standards work around autonomous
    actions.
  key_point: NIST describes agents as systems capable of autonomous actions that need
    trusted, interoperable, secure behaviour.
- source_title: Software and AI Agent Identity and Authorization
  source_url: https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization
  source_type: official_docs
  relevance: Gives a government framing of agent systems and their risks.
  key_point: Agent systems can make decisions and take actions with limited human
    supervision to achieve complex goals.
---

An AI agent is software that can try to reach a goal by deciding what to do next, using tools, and changing its plan based on what happens.

In practice, that might mean it reads a request, picks a next step, uses something like search, a database, or email, checks the result, and then decides whether to continue or stop.

This matters because it describes software that does more than answer one question. An agent can carry out parts of a job, not just talk about the job.

It is not the same as a normal chatbot. A chatbot mostly replies to messages. An agent may also act. It is also not always fully autonomous. Many agents still need human approval, and many only work inside a fixed set of steps.

The term is broad and not tightly agreed. When someone says “agent”, ask what tools it can use, what actions it can take, what memory it keeps, and when a human must check the result.
