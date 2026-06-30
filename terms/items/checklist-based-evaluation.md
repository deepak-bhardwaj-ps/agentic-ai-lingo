---
title: Checklist-based evaluation
short_description: An evaluation method that scores work by checking whether it meets a list of specific criteria.
category: Evals
tags:
- evals
- benchmarks
- judging
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: medium
maturity_level: emerging
common_misuse:
- Treating it as a full benchmark rather than one way to score a benchmark or output.
- Assuming a checklist makes the evaluation objective or complete by itself.
related_terms:
- rubric-based evaluation
- LLM-as-a-judge
- benchmark design
- evaluation harness
- criteria-based evaluation
evidence:
  - source_title: CheckEval: A reliable LLM-as-a-Judge framework for evaluating text generation using checklists
    source_url: https://aclanthology.org/2025.emnlp-main.796.pdf
    source_type: research_paper
    relevance: This paper gives a clear current example of checklist-based evaluation in LLM judging and shows how the term is used in practice.
    key_point: The paper defines checklist-based evaluation as breaking a subjective judgement into smaller binary questions, which improves reliability and makes the scoring easier to inspect.
  - source_title: Evaluation best practices
    source_url: https://developers.openai.com/api/docs/guides/evaluation-best-practices
    source_type: official_docs
    relevance: This official guide supports the core idea that evaluation should use specific criteria and comparison methods instead of vague open-ended judgement.
    key_point: The guide recommends focusing on pairwise comparisons, classification, or scoring against specific criteria because those formats are more reliable for model evaluation.
  - source_title: Demystifying evals for AI agents
    source_url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
    source_type: engineering_blog
    relevance: This lab blog explains why agent evaluations need structured tasks, scoring, and harnesses, which is the practical setting where checklists are often used.
    key_point: Anthropic describes agent evaluation as a structured process rather than a loose opinion, which supports checklist-based scoring as one way to make evaluation more repeatable.
---
Checklist-based evaluation is a way of judging an answer, tool result, or benchmark run by checking a list of specific yes-or-no points.

In practice, someone writes down the things that should be true, then checks each item one by one. The final score can be the number of boxes ticked, or a pass/fail result.

This matters because it makes judging easier to repeat and easier to inspect. It can also reduce vague scoring, where two people give different scores for the same answer.

It is not a full benchmark by itself. It is also not the same as a broad human review. A checklist can miss important quality problems if the items were chosen badly or if the list is too narrow.
