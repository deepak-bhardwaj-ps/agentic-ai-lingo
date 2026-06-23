---
slug: agent-evals
name: Agent Evals
category: AgentOps
title: Agent Evals
aliases: null
short_description: Agent Evals are tests and measurements that show how an agent behaves
termStatus: Established practice, informal label
researchBasis: OpenAI, Evals design guide
sources:
- https://arxiv.org/abs/2308.03688
---

## Term status

Established practice, informal label.

## Meaning

Agent evals are reproducible tests that measure whether an agent completes a task safely and correctly across realistic scenarios. Unlike a model-only benchmark, they inspect the full action system: supplied context, routing, tool choice and arguments, side effects, hand-offs, recovery, cost, latency, and the final outcome.

“Evals” is established engineering shorthand rather than a single methodology. The exact design must follow the risk and behaviour of the workload.

## Common misconceptions

A favourable chat response is not proof that an agent works. A support agent can sound correct while selecting the wrong customer record; a research agent can produce a polished answer with unsupported sources. Test the action surface and the failure modes that matter, including malicious inputs and unavailable tools.

One aggregate score is not sufficient. Separate outcome quality from policy compliance, tool-call validity, approval behaviour, recovery, and operational limits. Automated graders need calibration against expert human judgement, particularly for consequential decisions.

## How it is used

For a finance-operations agent, an evaluation suite might replay ambiguous invoices, supplier-name collisions, policy exceptions, withheld approvals, API timeouts, and prompt-injection attempts. It should assert both the final disposition and the trace: whether the right account was queried, the payment action was withheld, and escalation occurred when evidence was insufficient.

Run the suite on prompt, model, tool, policy, and orchestration changes. Mine production traces for new cases, retain a held-out regression set, and treat evaluation gaps as a release risk rather than post-launch housekeeping.

## Evidence

[OpenAI’s evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices) and [agent evals guide](https://platform.openai.com/docs/guides/agent-evals) define current production practice, while [trace grading](https://platform.openai.com/docs/guides/trace-grading) addresses intermediate decisions and tool calls. [AgentBench](https://arxiv.org/abs/2308.03688) supplies research context for evaluating agents across multi-turn environments.
