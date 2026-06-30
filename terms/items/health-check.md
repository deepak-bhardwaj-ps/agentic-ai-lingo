---
title: Health check
short_description: A health check is a quick check that a service is alive and responding.
category: Knowledge and wiki systems
tags:
- reliability
- monitoring
- infrastructure
- ops
status: draft
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Treating a health check as proof that the whole system works correctly.
- Confusing it with a full test suite or a business KPI.
- Assuming every health check means the same thing across tools and platforms.
related_terms:
- liveness probe
- readiness probe
- startup probe
- monitoring
- uptime
evidence:
- source_title: Liveness, Readiness, and Startup Probes
  source_url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
  source_type: official_docs
  relevance: Shows the common Kubernetes meaning of health checks as small periodic diagnostics on containers.
  key_point: Kubernetes describes probes as periodic diagnostics that let the platform restart unhealthy containers or stop sending traffic to ones that are not ready.
- source_title: Use health checks - Load Balancing
  source_url: https://docs.cloud.google.com/load-balancing/docs/health-checks
  source_type: official_docs
  relevance: Shows that health checks are used to probe backend services and decide whether they should receive traffic.
  key_point: Google Cloud explains health checks as probes whose success or failure is recorded so load balancers can route traffic safely.
- source_title: Health checks for Application Load Balancer target groups
  source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html
  source_type: official_docs
  relevance: Shows the load-balancing meaning of health checks in production systems.
  key_point: AWS says load balancers route requests only to healthy targets, and a target must pass health checks before it is considered healthy.
---

Health check means a quick check that a system or service is alive and responding.

In practice, a program, load balancer, or orchestrator sends a small request and watches for a sensible reply. If the reply comes back the right way, the service is treated as healthy. If not, traffic may be reduced, stopped, or sent elsewhere.

Health checks matter because they help systems avoid sending users to broken parts of the service. They also help machines decide when to restart something, wait for it to finish starting, or move traffic away from it.

A health check is not the same as a full test. It usually checks a small sign of life, not every feature. It also does not prove that the whole application is correct, safe, or bug-free.
