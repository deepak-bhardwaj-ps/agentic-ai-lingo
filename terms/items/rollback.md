---
title: Rollback
short_description: Returning a system to an earlier version or state after a change causes problems.
category: Agentic patterns
tags:
- agentic-ai
- deployment
- recovery
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: emerging
common_misuse:
- Treating rollback as if it erases every effect of the failed change.
- Confusing rollback with pause, retry, or simply hiding the problem.
- Using it as a vague safety word without saying what state is restored.
related_terms:
- deployment rollback
- rollback plan
- recovery
- checkpoint
- canary deployment
- feature flag
evidence:
- source_title: Roll back a target - Google Cloud Documentation
  source_url: https://docs.cloud.google.com/deploy/docs/roll-back
  source_type: official_docs
  relevance: Shows the standard deployment meaning of rollback as moving back to an earlier release.
  key_point: Cloud Deploy rolls a target back by creating a new rollout based on a previous release.
- source_title: Deployments - Kubernetes
  source_url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
  source_type: official_docs
  relevance: Gives a widely used infrastructure definition and shows rollback as part of normal deployment control.
  key_point: Kubernetes explicitly supports rolling back to an earlier Deployment revision when the current one is not stable.
- source_title: Redeploy and roll back a deployment with CodeDeploy
  source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html
  source_type: official_docs
  relevance: Explains that rollback is often implemented as a new deployment of a previously known-good version, not magic reversal.
  key_point: AWS CodeDeploy rolls back by redeploying a previously deployed revision as a new deployment.
- source_title: Feature Toggles (aka Feature Flags)
  source_url: https://martinfowler.com/articles/feature-toggles.html
  source_type: engineering_blog
  relevance: Helps distinguish rollback from feature flags, which reduce risk before a full change is rolled out.
  key_point: Feature flags let teams switch behaviour on and off, which is different from undoing a bad release after the fact.
---

## Meaning

Rollback means returning a system to an earlier version or state after a change goes wrong.

In practice, this usually means putting back the previous release, config, or settings that worked before the problem started. In software systems, rollback is often part of deployment and recovery work.

Rollback matters because new changes can break a working system. If teams can go back quickly, they can limit damage and restore service sooner.

Rollback is not the same as fixing the problem in place. It does not always undo every side effect, especially if the bad change already affected data or users.
