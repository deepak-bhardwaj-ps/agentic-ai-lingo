---
slug: agent-debt
name: Agent Debt
category: AgentOps
title: Agent Debt
aliases: null
short_description: Agent Debt is the accumulated operational risk created by shortcuts,
termStatus: Operational metric/practice
researchBasis: OpenAI, Evals design guide
sources:
- https://platform.openai.com/docs/guides/prompting
---

## Term status

Operational metric/practice.

## Meaning

Agent debt is a useful adaptation of technical debt for the liabilities hidden in an agent system: untested tool choices, opaque hand-offs, prompt changes without regression evidence, broad credentials, brittle recovery logic, and unowned production traces. The debt is not the defect itself; it is the growing cost and risk of changing or operating the system while that defect remains unresolved.

This is an operational practice, not a recognised metric or formal discipline.

## Common misconceptions

Model error rate is not agent debt. A model may be imperfect while the surrounding system has good evaluation coverage, safe fallbacks, and clear ownership. Conversely, an agent with apparently good headline accuracy can carry serious debt if nobody can explain a tool call or safely roll back a prompt.

Do not turn the label into a vanity KPI. Counting “debt items” conflates an expired credential with an untested payment action. Record severity, [[Blast Radius|blast radius]], exploitability, owner, evidence gap, and a remediation decision.

## How it is used

After a failed procurement-agent run, a team might log three debt items: no test set covering supplier-name ambiguity, no trace grader for approval bypass, and no circuit breaker around a vendor API. Each item needs a named owner and a release or risk deadline; “improve reliability” is not a debt register entry.

OpenAI’s evaluation guidance reinforces the practical discipline: agent architecture choices introduce distinct nondeterminism and should be supported by reproducible evals and trace-level evidence. Treat unresolved gaps in that evidence as debt before expanding autonomy or permissions.

## Evidence

“Agent debt” has no canonical definition. The operational basis comes from [OpenAI’s evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices), [agent evals](https://platform.openai.com/docs/guides/agent-evals), [trace grading](https://platform.openai.com/docs/guides/trace-grading), and the recommendation to run linked evals when publishing a prompt in the [prompting guide](https://platform.openai.com/docs/guides/prompting).
