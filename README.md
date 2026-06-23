# Agentic AI Buzzword Dictionary

A living dictionary of agentic AI terminology, runtime language, governance terms, protocol vocabulary, and meme slang.

## Core

- [AI Agents](terms/items/ai-agents.md): AI Agents is a general label for software systems that can choose actions, use tools, and pursue a goal across steps.
- [Agentic AI](terms/items/agentic-ai.md): Agentic AI is an umbrella term for AI systems that can take bounded actions, not just generate text.
- [Agentic Browser](terms/items/agentic-browser.md): Agentic Browser is a browser-driven agent that can navigate pages, inspect content, and take actions on the web.
- [Agentic Coding](terms/items/agentic-coding.md): Agentic Coding is coding in which an AI system can propose, edit, run, and revise code with limited supervision.
- [Agentic Commerce](terms/items/agentic-commerce.md): Agentic Commerce is commerce in which an agent can compare options, negotiate constraints, or complete transactions.
- [Agentic Delivery](terms/items/agentic-delivery.md): Agentic Delivery is a label for systems that turn intent into executed work across steps, hand-offs, and checks.
- [Agentic Trust](terms/items/agentic-trust.md): Agentic Trust is the degree of confidence that an agent can be allowed to act without creating unacceptable risk.
- [Agentic Workflow](terms/items/agentic-workflow.md): Agentic Workflow is a workflow that includes planning, tool use, state, and recovery rather than a single model call.
- [Browser Use](terms/items/browser-use.md): Browser Use is browser automation or page interaction performed by a model-driven agent.
- [Computer Use](terms/items/computer-use.md): Computer Use is model-driven interaction with a desktop through cursor, keyboard, and screen control.
- [Web Agent](terms/items/web-agent.md): Web Agent is an agent whose main operating environment is the web.

## Runtime

- [Agent Control Plane](terms/items/agent-control-plane.md): Agent Control Plane is the service layer that coordinates fleet-level policy, configuration, identity, and lifecycle.
- [Agent Kernel](terms/items/agent-kernel.md): Agent Kernel is the core execution loop that turns observations into decisions and tool calls for one agent.
- [Agent Loop](terms/items/agent-loop.md): Agent Loop is the repeated cycle of planning, acting, and incorporating observations.
- [Agent Runtime](terms/items/agent-runtime.md): Agent Runtime is the execution environment that hosts an agent’s loop, tools, memory, and side effects.
- [Agent Swarm](terms/items/agent-swarm.md): Agent Swarm is a loosely coordinated pool of agents working on related tasks in parallel.
- [Agentic Rendering](terms/items/agentic-rendering.md): Agentic Rendering is rendering that changes output or interface state in response to agent decisions.
- [Dynamic Skill Routing](terms/items/dynamic-skill-routing.md): Dynamic Skill Routing is run-time selection of the most appropriate capability from available tools or skills.
- [Dynamic Teaming](terms/items/dynamic-teaming.md): Dynamic Teaming is runtime allocation of work to the most suitable available agent or worker.
- [Execution Boundary](terms/items/execution-boundary.md): Execution Boundary is used to mark the hand-off between model reasoning and an external execution environment.
- [Execution Graph](terms/items/execution-graph.md): Execution Graph is the graph of steps, dependencies, and side effects that defines how work proceeds.
- [Execution State](terms/items/execution-state.md): Execution State is used for the mutable record that lets an orchestrator continue a run: plan, observations, tool results, checkpoints and budgets.
- [Hierarchical Agent Architecture](terms/items/hierarchical-agent-architecture.md): Hierarchical Agent Architecture is a multi-level system with supervisors, delegates, and lower-level workers.
- [Inference Runtime](terms/items/inference-runtime.md): Inference Runtime is the serving layer that executes model calls inside a larger agent system.
- [Long-Horizon Tasks](terms/items/long-horizon-tasks.md): Long-Horizon Tasks are tasks that unfold over many steps and require persistence, recovery, and state.
- [Long-Horizon Workflow](terms/items/long-horizon-workflow.md): Long-Horizon Workflow is a workflow that must remain coherent across many turns, retries, and state changes.
- [Loop Engineering](terms/items/loop-engineering.md): Loop Engineering is the practice of designing repeated plan-act-observe cycles with explicit stops and limits.
- [Orchestration Loop](terms/items/orchestration-loop.md): Orchestration Loop is the control cycle that schedules work, checks results, and decides the next step.
- [Pilot-to-Production Gap](terms/items/pilot-to-production-gap.md): Pilot-to-Production Gap is the gap between a successful pilot and a system that is actually production-ready.
- [ReAct](terms/items/react.md): ReAct is the reasoning-plus-action pattern that interleaves thought, tool use, and observation.
- [Reasoning Runtime](terms/items/reasoning-runtime.md): Reasoning Runtime is the part of the system responsible for deliberation, state updates, and decision-making.
- [Runtime Contract](terms/items/runtime-contract.md): Runtime Contract is the specification for what a runtime component accepts, does, retries, and returns.
- [Runtime Governance](terms/items/runtime-governance.md): Runtime Governance is the set of controls that constrains what a runtime can do and how it is supervised.
- [Safety Monitor](terms/items/safety-monitor.md): Safety Monitor is the component that watches agent actions for policy violations and interrupts unsafe behaviour.
- [Skill Routing](terms/items/skill-routing.md): Skill Routing is selecting the right capability from a tool or skill set at run time.
- [Star Topology](terms/items/star-topology.md): Star Topology is used to explain the communication shape among coordinator and worker agents.
- [Stop-Anywhere Architecture](terms/items/stop-anywhere-architecture.md): Stop-Anywhere Architecture is an architecture that lets an agent be interrupted safely at any point.
- [Sub-agent Swarm](terms/items/sub-agent-swarm.md): Sub-agent Swarm is a swarm of subordinate agents under a coordinating runtime.
- [Supervisor Agent](terms/items/supervisor-agent.md): Supervisor Agent is the top-level agent that delegates, checks, and decides whether work should continue.
- [Task Assignment](terms/items/task-assignment.md): Task Assignment is the mechanism that allocates work to agents or workers.
- [Test-Driven Agentic Workflow](terms/items/test-driven-agentic-workflow.md): Test-Driven Agentic Workflow is a workflow where tests define the agent’s target behaviour and acceptance checks.
- [Tool Router](terms/items/tool-router.md): Tool Router is the component that selects and routes tool calls based on task, context, or policy.
- [Tooling Layer](terms/items/tooling-layer.md): Tooling Layer is the set of integrations and adapters that let an agent use external tools.
- [Trajectory Quality](terms/items/trajectory-quality.md): Trajectory Quality is used in evaluations to separate a correct final result from a safe, efficient execution path.
- [Verification Loop](terms/items/verification-loop.md): Verification Loop is the cycle of checking results, feeding back evidence, and deciding whether to continue.
- [Verifier](terms/items/verifier.md): Verifier is the component that checks whether outputs or actions satisfy the required criteria.
- [Workflow Runtime](terms/items/workflow-runtime.md): Workflow Runtime is the execution environment that runs a workflow and manages its state, retries, and termination.
- [Agent Control Plane](terms/items/agent-control-plane.md): The governance layer for deploying, observing, and steering agent fleets.
- [Agent Kernel](terms/items/agent-kernel.md): Agent Kernel is part of the execution layer for agents.
- [Agent Loop](terms/items/agent-loop.md): Agent Loop is the repeating cycle of reasoning, action, and feedback.
- [Agent Runtime](terms/items/agent-runtime.md): The execution environment that runs agent planning, tools, memory, and policy.
- [Agent Swarm](terms/items/agent-swarm.md): Agent Swarm is a coordinated group of agents working in parallel.
- [Agentic Rendering](terms/items/agentic-rendering.md): Using agents to generate structured output or content pipelines.
- [Dynamic Skill Routing](terms/items/dynamic-skill-routing.md): Dynamic Skill Routing is part of the execution layer for agents.
- [Dynamic Teaming](terms/items/dynamic-teaming.md): Dynamic Teaming is a persistent group of agents working together.
- [Execution Boundary](terms/items/execution-boundary.md): Execution Boundary is part of the execution layer for agents.
- [Execution Graph](terms/items/execution-graph.md): Execution Graph is a graph-based model for representing relationships, context, or memory.
- [Execution State](terms/items/execution-state.md): Execution State is part of the execution layer for agents.
- [Hierarchical Agent Architecture](terms/items/hierarchical-agent-architecture.md): Hierarchical Agent Architecture is part of the execution layer for agents.
- [Inference Runtime](terms/items/inference-runtime.md): Inference Runtime is the execution environment where an agent runs.
- [Long-Horizon Tasks](terms/items/long-horizon-tasks.md): Long-Horizon Tasks is part of the execution layer for agents.
- [Long-Horizon Workflow](terms/items/long-horizon-workflow.md): Long-Horizon Workflow is a multi-step process that an agent or agent system executes.
- [Loop Engineering](terms/items/loop-engineering.md): Loop Engineering is the repeating cycle of reasoning, action, and feedback.
- [Orchestration Loop](terms/items/orchestration-loop.md): Orchestration Loop is the repeating cycle of reasoning, action, and feedback.
- [Pilot-to-Production Gap](terms/items/pilot-to-production-gap.md): Pilot-to-Production Gap is part of the execution layer for agents.
- [ReAct](terms/items/react.md): A reasoning-and-acting loop that alternates thought and tool use.
- [Reasoning Runtime](terms/items/reasoning-runtime.md): Reasoning Runtime is the execution environment where an agent runs.
- [Runtime Contract](terms/items/runtime-contract.md): Runtime Contract is a formal agreement that defines behaviour, permissions, or runtime guarantees.
- [Runtime Governance](terms/items/runtime-governance.md): Runtime Governance is the mechanism for applying control, oversight, and accountability.
- [Safety Monitor](terms/items/safety-monitor.md): Safety Monitor is a control that reduces risk when agents take actions.
- [Skill Routing](terms/items/skill-routing.md): Skill Routing is part of the execution layer for agents.
- [Star Topology](terms/items/star-topology.md): Star Topology is part of the execution layer for agents.
- [Stop-Anywhere Architecture](terms/items/stop-anywhere-architecture.md): Stop-Anywhere Architecture is part of the execution layer for agents.
- [Sub-agent Swarm](terms/items/sub-agent-swarm.md): Sub-agent Swarm is a coordinated group of agents working in parallel.
- [Supervisor Agent](terms/items/supervisor-agent.md): Supervisor Agent is part of the execution layer for agents.
- [Task Assignment](terms/items/task-assignment.md): Task Assignment is part of the execution layer for agents.
- [Test-Driven Agentic Workflow](terms/items/test-driven-agentic-workflow.md): Test-Driven Agentic Workflow is a multi-step process that an agent or agent system executes.
- [Tool Router](terms/items/tool-router.md): Tool Router is the capability an agent invokes to do work outside the model itself.
- [Tooling Layer](terms/items/tooling-layer.md): Tooling Layer is an abstraction layer that mediates capabilities, context, or governance.
- [Trajectory Quality](terms/items/trajectory-quality.md): Trajectory Quality is a measure of how consistently an agent produces useful results.
- [Verification Loop](terms/items/verification-loop.md): Verification Loop is the act of checking that an agent's output or action is correct.
- [Verifier](terms/items/verifier.md): Verifier is part of the execution layer for agents.
- [Workflow Runtime](terms/items/workflow-runtime.md): Workflow Runtime is the execution environment where an agent runs.

## Memory

- [Agent Memory](terms/items/agent-memory.md): Agent Memory is externally managed state for carrying facts, preferences, and past work across turns.
- [Episodic Memory](terms/items/episodic-memory.md): Episodic Memory is stored memory of specific interactions, events, or episodes.
- [Memory Architecture](terms/items/memory-architecture.md): Memory Architecture is the design of storage, retrieval, and correction for agent memory.
- [Memory Compaction](terms/items/memory-compaction.md): Memory Compaction is compressing memory into smaller summaries without losing decision-critical detail.
- [Memory Contamination](terms/items/memory-contamination.md): Memory Contamination is false, irrelevant, malicious, or misretrieved state that later affects decisions.
- [Memory Debt](terms/items/memory-debt.md): Memory Debt is used for accumulated shortcuts in storage, retrieval and summarisation that make an agent’s state unreliable or expensive to change.
- [Memory Drift](terms/items/memory-drift.md): Memory Drift is gradual change in stored state or retrieval behaviour that shifts later decisions.
- [Memory Engineering](terms/items/memory-engineering.md): Memory Engineering is the practice of designing and operating agent memory systems.
- [Memory Federation](terms/items/memory-federation.md): Memory Federation is separate memory stores exposed through a common access pattern.
- [Memory Governance](terms/items/memory-governance.md): Memory Governance is policy for who can read, write, retain, or delete agent memory.
- [Memory Graph](terms/items/memory-graph.md): Memory Graph is used where entities, facts and relationships need traversable structure rather than flat retrieved chunks.
- [Memory Hallucination](terms/items/memory-hallucination.md): Memory Hallucination is false, irrelevant, malicious, or misretrieved state that later affects decisions.
- [Memory Hygiene](terms/items/memory-hygiene.md): Memory Hygiene is routine cleanup that keeps memory accurate, current, and usable.
- [Memory Substrate](terms/items/memory-substrate.md): Memory Substrate is the persistence layer beneath an agent’s working context.
- [Memory Systems](terms/items/memory-systems.md): Memory Systems is the full stack that stores, retrieves, updates, and retires agent memory.
- [Procedural Memory](terms/items/procedural-memory.md): Procedural Memory is stored patterns for how an agent should do tasks.
- [Semantic Memory](terms/items/semantic-memory.md): Semantic Memory is stored facts and concepts an agent can reuse across tasks.
- [State Lifecycle](terms/items/state-lifecycle.md): State Lifecycle is the phases an agent state item passes through from creation to retirement.
- [Working Memory](terms/items/working-memory.md): Working Memory is task-local state currently kept in active context.

## Governance

- [Act-on-Behalf](terms/items/act-on-behalf.md): Act-on-Behalf is acting under delegated authority for a specific principal and purpose.
- [Action Governance](terms/items/action-governance.md): Action Governance is the control layer that decides whether an agent may take a specific action.
- [Action Plane](terms/items/action-plane.md): Action Plane is the enforcement layer that actually blocks, approves, or logs an action.
- [Agent Identity](terms/items/agent-identity.md): Agent Identity is the principal identity under which an agent acts and is audited.
- [Agentic Misalignment](terms/items/agentic-misalignment.md): Agentic Misalignment is when an agent’s behaviour diverges from the operator’s intent or policy.
- [Alignment Verification](terms/items/alignment-verification.md): Alignment Verification is checking that agent behaviour matches the stated objective or policy.
- [Autonomy Boundaries](terms/items/autonomy-boundaries.md): Autonomy Boundaries define where the agent can decide alone and where approval is required.
- [Behaviour Assurance](terms/items/behaviour-assurance.md): Behaviour Assurance is evidence that an agent reliably stays within its intended behaviour.
- [Behaviour Contract](terms/items/behaviour-contract.md): Behaviour Contract is used to document what an agent or delegate is allowed and expected to do.
- [Behaviour Drift](terms/items/behaviour-drift.md): Behaviour Drift is used in risk reviews for a gradual divergence from a stated goal, policy or expected behaviour.
- [Behaviour Replay](terms/items/behaviour-replay.md): Behaviour Replay is rerunning traces to inspect or reproduce an agent’s decisions.
- [Blast Radius](terms/items/blast-radius.md): Blast Radius is the maximum damage an agent failure or mistake can cause.
- [Composite Principal](terms/items/composite-principal.md): Composite Principal is a principal made from multiple identities or delegated authorities.
- [Confused Deputy](terms/items/confused-deputy.md): Confused Deputy is an agent tricked into using delegated authority for the wrong purpose.
- [Control Plane Architecture](terms/items/control-plane-architecture.md): Control Plane Architecture is the service layer that enforces policy, configuration, and lifecycle control.
- [Decision Plane](terms/items/decision-plane.md): Decision Plane is the service layer that applies decision policy and records what was decided.
- [Decision Sovereignty](terms/items/decision-sovereignty.md): Decision Sovereignty is who retains final decision rights in an agentic system.
- [Delegated Authority](terms/items/delegated-authority.md): Delegated Authority is authority passed from one principal to another for a bounded purpose.
- [Delegation Audit Trail](terms/items/delegation-audit-trail.md): Delegation Audit Trail is the record of who delegated what, to whom, and under which constraints.
- [Delegation Boundary](terms/items/delegation-boundary.md): Delegation Boundary is the edge where authority moves from one principal to another.
- [Delegation Chain](terms/items/delegation-chain.md): Delegation Chain is the sequence of principals and hand-offs involved in a delegated action.
- [Delegation Contract](terms/items/delegation-contract.md): Delegation Contract is the agreement that defines delegated authority, limits, and revocation.
- [Delegation Failure](terms/items/delegation-failure.md): Delegation Failure is a break in the chain of authority, constraint, or revocation.
- [Delegation Graph](terms/items/delegation-graph.md): Delegation Graph is the graph of principals, delegated capabilities, and hand-offs.
- [Delegation Layer](terms/items/delegation-layer.md): Delegation Layer is the policy and enforcement layer for delegated authority.
- [Delegation Policy](terms/items/delegation-policy.md): Delegation Policy is the rule set that decides what can be delegated and under what limits.
- [Delegation Recovery](terms/items/delegation-recovery.md): Delegation Recovery is the process for restoring or reassigning authority after a failed hand-off.
- [Delegation Scope](terms/items/delegation-scope.md): Delegation Scope is the bounded range of actions, data, and time covered by a delegation.
- [Delegation-Aware Observability](terms/items/delegation-aware-observability.md): Delegation-Aware Observability is observability that preserves who delegated what and why.
- [Evidence-Based Execution](terms/items/evidence-based-execution.md): Evidence-Based Execution is taking action only when the evidence meets the required threshold.
- [Goal Drift](terms/items/goal-drift.md): Goal Drift is used in risk reviews for a gradual divergence from a stated goal, policy or expected behaviour.
- [Governance Plane](terms/items/governance-plane.md): Governance Plane is the service layer that applies rules, oversight, and audit controls.
- [Governance by Design](terms/items/governance-by-design.md): Governance by Design is governance built into the system rather than added afterwards.
- [Guardrails](terms/items/guardrails.md): Guardrails are the rules and constraints that limit what an agent may do.
- [Human Oversight](terms/items/human-oversight.md): Human Oversight is used to specify where a human reviews, approves, interrupts or overrides an agent.
- [Identity Plane](terms/items/identity-plane.md): Identity Plane is the service layer that resolves who or what is acting.
- [Least Privilege](terms/items/least-privilege.md): Least Privilege is the principle of giving an agent only the access it needs.
- [Mission Drift](terms/items/mission-drift.md): Mission Drift is used in risk reviews for a gradual divergence from a stated goal, policy or expected behaviour.
- [Permission Gates](terms/items/permission-gates.md): Permission Gates is used to govern whether a requested action is allowed for a particular agent and principal.
- [Policy Interceptor](terms/items/policy-interceptor.md): Policy Interceptor is used to govern whether a requested action is allowed for a particular agent and principal.
- [Policy Plane](terms/items/policy-plane.md): Policy Plane is the service layer that evaluates rules before an action is allowed.
- [Specification Engineering](terms/items/specification-engineering.md): Specification Engineering is turning behaviour into testable, enforceable specifications.
- [Tool Authorization](terms/items/tool-authorization.md): Tool Authorization is used to govern whether a requested action is allowed for a particular agent and principal.
- [Traceable Accountability](terms/items/traceable-accountability.md): Traceable Accountability is accountability that can be traced back to a principal and an event record.
- [Trust Plane](terms/items/trust-plane.md): Trust Plane is the service layer that establishes whether an agent can be trusted to act.
- [Trust-by-Design](terms/items/trust-by-design.md): Trust-by-Design is designing the system so trust is earned by evidence and controls.
- [Trustworthy Autonomy](terms/items/trustworthy-autonomy.md): Trustworthy Autonomy is autonomy backed by controls, evidence, and revocation paths.
- [Ultimate Human Control](terms/items/ultimate-human-control.md): Ultimate Human Control is used to specify where a human reviews, approves, interrupts or overrides an agent.
- [Verifiable Action](terms/items/verifiable-action.md): Verifiable Action is an action that can be checked against a defined record or criterion.

## Protocols

- [A2A](terms/items/a2a.md): A2A is a protocol label for one agent asking another agent or service to take part in work.
- [Agent Architect](terms/items/agent-architect.md): Agent Architect is the role that defines how an agent system is structured, integrated, and governed.
- [Agent Assembly](terms/items/agent-assembly.md): Agent Assembly is the composition of multiple agents into one coordinated system.
- [Agent Coalition](terms/items/agent-coalition.md): Agent Coalition is a set of separately owned agents that cooperate under shared constraints.
- [Agent Collective](terms/items/agent-collective.md): Agent Collective is a group of agents that share a common coordination model or resource pool.
- [Agent Federation](terms/items/agent-federation.md): Agent Federation is a set of interoperating agents that stay independently owned.
- [Agent Marketplace](terms/items/agent-marketplace.md): Agent Marketplace is a directory or market where agents advertise capabilities and can be selected or bought.
- [Agent Mesh](terms/items/agent-mesh.md): Agent Mesh is a loosely coupled network of agents that can discover and route work to each other.
- [Agent Registry](terms/items/agent-registry.md): Agent Registry is a catalogue of agent identities, capabilities, endpoints, versions, and owners.
- [Agent Society](terms/items/agent-society.md): Agent Society is a population of agents that interact under shared norms or incentives.
- [Agent Training](terms/items/agent-training.md): Agent Training is the onboarding or preparation of agents to operate in a shared ecosystem.
- [Agent-Ready Software](terms/items/agent-ready-software.md): Agent-Ready Software is software designed for reliable agent calling, inspection, and safe use.
- [Agentic Multi-Agent Architecture](terms/items/agentic-multi-agent-architecture.md): Agentic Multi-Agent Architecture is a design where multiple specialised agents coordinate on one task or system.
- [Agentic Web](terms/items/agentic-web.md): Agentic Web is a web designed so agents can discover information and complete tasks through structured interfaces.
- [Ambient Team](terms/items/ambient-team.md): Ambient Team is a persistent set of agents that supports a human team in the background.
- [Collective Intelligence Layer](terms/items/collective-intelligence-layer.md): Collective Intelligence Layer is shared coordination that combines multiple agents or sources.
- [Intent Engineering](terms/items/intent-engineering.md): Intent Engineering is turning user intent into tasks or machine-executable objectives.
- [Intent Mesh](terms/items/intent-mesh.md): Intent Mesh is a routing layer that moves intents across agents, tools, or services.
- [MCP](terms/items/mcp.md): MCP is the Model Context Protocol for connecting models to tools, resources, and prompts through a standard interface.
- [Registry](terms/items/registry.md): Registry is a catalogue of agents, services, or resources that can be discovered and referenced consistently.
- [Skill Libraries](terms/items/skill-libraries.md): Skill Libraries are reusable packages of instructions, tools, examples, or code that give agents repeatable capabilities.
- [Tool Gateway](terms/items/tool-gateway.md): Tool Gateway is a control point that brokers access to tools and applies policy before execution.

## AgentOps

- [Agent Debt](terms/items/agent-debt.md): Agent Debt is the accumulated operational risk created by shortcuts, weak controls, and unresolved failure modes in an agent system.
- [Agent Estate](terms/items/agent-estate.md): Agent Estate is the collection of agents, workflows, and controls an organisation must run and maintain.
- [Agent Evals](terms/items/agent-evals.md): Agent Evals are tests and measurements that show how an agent behaves under controlled scenarios.
- [Agent Inventory](terms/items/agent-inventory.md): Agent Inventory is the list of agents, versions, capabilities, and owners that are currently in operation.
- [Agent Lifecycle Management](terms/items/agent-lifecycle-management.md): Agent Lifecycle Management is the discipline of introducing, operating, updating, and retiring agents safely.
- [Agent Ownership Model](terms/items/agent-ownership-model.md): Agent Ownership Model is the way responsibility for an agent’s operation, risk, and change is assigned.
- [Agent Portfolio](terms/items/agent-portfolio.md): Agent Portfolio is the set of agents an organisation operates as a managed portfolio.
- [Agent Sprawl](terms/items/agent-sprawl.md): Agent Sprawl is the uncontrolled growth of agents without matching ownership, standards, or lifecycle control.
- [AgentOps](terms/items/agentops.md): AgentOps is the operational practice of deploying, observing, evaluating, and governing agentic applications.
- [Agentic Evaluation](terms/items/agentic-evaluation.md): Agentic Evaluation is evaluation for multi-step, stateful, tool-using systems.
- [Autonomous Workflow](terms/items/autonomous-workflow.md): Autonomous Workflow is a workflow that can progress and recover with limited human intervention.
- [Continuous Validation](terms/items/continuous-validation.md): Continuous Validation is ongoing checking that an agent system still behaves within the expected envelope.
- [Cost per Workflow](terms/items/cost-per-workflow.md): Cost per Workflow is the average cost of completing one workflow end to end.
- [Evidence-Grade Audit Trail](terms/items/evidence-grade-audit-trail.md): Evidence-Grade Audit Trail is an audit trail detailed enough to support review, accountability, and reconstruction.
- [Exception Rate](terms/items/exception-rate.md): Exception Rate is the proportion of workflows that need manual handling, escalation, or fallback.
- [Execution Quality](terms/items/execution-quality.md): Execution Quality is the degree to which an agent completes work correctly, safely, and consistently.
- [Ghost Agent](terms/items/ghost-agent.md): Ghost Agent is an agent that exists on paper or in logs but is missing, inactive, or not behaving as expected.
- [Harness Engineering](terms/items/harness-engineering.md): Practitioners use Harness Engineering when they improve the operating environment around an agent after observing a failure—for example by adding repository guidance, a typed tool, a sandbox rule or an executable check.
- [Multi-Agent Governance](terms/items/multi-agent-governance.md): Multi-Agent Governance is the set of controls that keeps multiple agents from conflicting or exceeding their authority.
- [Orphan Agent](terms/items/orphan-agent.md): Orphan Agent is an agent that exists without a clear owner, support path, or lifecycle plan.
- [Outcome Reliability](terms/items/outcome-reliability.md): Outcome Reliability is the consistency with which an agent reaches the intended result under real conditions.
- [Pilot Purgatory](terms/items/pilot-purgatory.md): Pilot Purgatory is the state where a promising pilot never gets the investment needed to become production-ready.
- [Proof-of-Concept Graveyard](terms/items/proof-of-concept-graveyard.md): Proof-of-Concept Graveyard is the accumulation of pilots or prototypes that never made it into production.
- [Recovery Readiness](terms/items/recovery-readiness.md): Recovery Readiness is the degree to which an agent system can be restored after a failure or interruption.
- [Shadow Agent](terms/items/shadow-agent.md): Shadow Agent is an agent that runs without clear visibility, approval, or governance from the owning team.
- [Trajectory Evaluation](terms/items/trajectory-evaluation.md): Trajectory Evaluation is evaluation of the path an agent took, not just the final answer it produced.
- [Verified Outcome](terms/items/verified-outcome.md): Verified Outcome is an outcome that has been checked against a defined criterion or independent evidence.

## Slang

- [AI Leaderboards](terms/items/ai-leaderboards.md): AI Leaderboards is a label for treating model rankings or scoreboards as proxy evidence for purchase, adoption, or credibility.
- [AI Ribbon-Cutting](terms/items/ai-ribbon-cutting.md): AI Ribbon-Cutting is a label for ceremonial AI launches that create publicity without much operational change.
- [AI Slop](terms/items/ai-slop.md): AI Slop is a pejorative for low-value AI-generated output that needs substantial human clean-up before use.
- [AI Sprawl](terms/items/ai-sprawl.md): AI Sprawl is a label for AI tools and pilots multiplying faster than ownership, standards, or integration discipline.
- [AI Washing](terms/items/ai-washing.md): AI Washing is a label for products described as AI-powered when the AI contribution is thin, cosmetic, or absent.
- [Agent FOMO](terms/items/agent-fomo.md): Agent FOMO is a label for adding agents because competitors are doing so, not because the workflow needs one.
- [Agent Theatre](terms/items/agent-theatre.md): Agent Theatre is a label for demos that look autonomous while the useful work and recovery path are still missing.
- [Agent Washing](terms/items/agent-washing.md): Agent Washing is a label for relabelling ordinary automation as an agent to borrow market hype.
- [Agentmaxxing](terms/items/agentmaxxing.md): Agentmaxxing is a practitioner slang term for pushing an agent stack harder than is operationally necessary.
- [Architecture Washing](terms/items/architecture-washing.md): Architecture Washing is a label for using architecture language to make a thin AI feature sound rigorous.
- [Auto-bullshit](terms/items/auto-bullshit.md): Auto-bullshit is a blunt label for confident but false or meaningless AI output.
- [Autonomy Theatre](terms/items/autonomy-theatre.md): Autonomy Theatre is a label for systems that are described as self-directing while humans still make the real calls.
- [Chatbot Theatre](terms/items/chatbot-theatre.md): Chatbot Theatre is a label for chat interfaces that imply capability the backend workflow does not actually have.
- [Clanker](terms/items/clanker.md): Clanker is a blunt pejorative for noisy, brittle, or obviously machine-like AI systems.
- [Control Washing](terms/items/control-washing.md): Control Washing is a label for overstating guardrails, overrides, or governance in an AI system.
- [Dead Internet](terms/items/dead-internet.md): Dead Internet is a label for the belief that bots and synthetic content are overwhelming human activity online.
- [Demo-ware](terms/items/demo-ware.md): Demo-ware is a label for software that works in the polished demo path but not in normal production use.
- [Governance Theatre](terms/items/governance-theatre.md): Governance Theatre is a label for oversight structures that signal control without changing decisions.
- [Microslop](terms/items/microslop.md): Microslop is an insider jab at Microsoft-branded software or AI output that feels low-value or overhyped.
- [Productivity Cosplay](terms/items/productivity-cosplay.md): Productivity Cosplay is a label for appearing efficient with AI rather than actually improving throughput or quality.
- [Prompt Goblin](terms/items/prompt-goblin.md): Prompt Goblin is a term for someone who obsessively tweaks prompts for marginal gains.
- [Prompt Slop](terms/items/prompt-slop.md): Prompt Slop is a label for bloated, copied, or poorly structured prompts that are hard to trust or reuse.
- [Promptmaxxing](terms/items/promptmaxxing.md): Promptmaxxing is a slang term for extreme prompt tuning, usually with more status than operational value.
- [Saaspocalypse](terms/items/saaspocalypse.md): Saaspocalypse is a label for claims that AI will hollow out the SaaS layer or collapse app economics.
- [Slopaganda](terms/items/slopaganda.md): Slopaganda is a label for mediocre AI output being packaged as proof that the system is working.
- [Slopcoding](terms/items/slopcoding.md): Slopcoding is a label for code that is generated quickly but has poor structure, review, or maintainability.
- [Synthetic Sludge](terms/items/synthetic-sludge.md): Synthetic Sludge is a label for machine-generated content that builds a thick layer of low-signal material.
- [Tokenmaxxing](terms/items/tokenmaxxing.md): Tokenmaxxing is a term for pushing context, prompt length, or output length to extract more from the model.
- [Trendslop](terms/items/trendslop.md): Trendslop is a label for AI content assembled to match current trends rather than to be useful or durable.
- [Vibe Coding](terms/items/vibe-coding.md): Vibe Coding is Andrej Karpathy’s label for steering coding by natural language and light review.
- [Vibe Valuation](terms/items/vibe-valuation.md): Vibe Valuation is a label for valuation driven by narrative, demos, or AI momentum rather than durable economics.
- [Workslop](terms/items/workslop.md): Workslop is a label for polished-looking AI output that creates extra cleanup or rework downstream.
- [Zombie Internet](terms/items/zombie-internet.md): Zombie Internet is a label for a web increasingly filled with stale, duplicated, or machine-produced pages.

## Context

- [Agentic Hub](terms/items/agentic-hub.md): Agentic Hub is a central point for the context, tools, or services an agent needs.
- [Causal Attribution](terms/items/causal-attribution.md): Causal Attribution is the ability to explain which source or step caused a model to see or do something.
- [Context Collapse](terms/items/context-collapse.md): Context Collapse is the failure mode where too much or the wrong kind of information is packed into a model’s decision context.
- [Context Constructor](terms/items/context-constructor.md): Context Constructor is used for the component that assembles the actual model input from instructions, state, retrieved records and tool descriptions.
- [Context Debt](terms/items/context-debt.md): Context Debt is the accumulation of stale, duplicated, or hard-to-use context that makes future decisions worse.
- [Context Drift](terms/items/context-drift.md): Context Drift is the gradual change in what context a model sees or depends on over time.
- [Context Engineering](terms/items/context-engineering.md): Context Engineering is the deliberate construction of what information reaches a model at decision time.
- [Context Fabric](terms/items/context-fabric.md): Context Fabric is a shared layer for delivering context across systems.
- [Context Federation](terms/items/context-federation.md): Context Federation is the coordination of context across multiple systems or repositories.
- [Context Fragmentation](terms/items/context-fragmentation.md): Context Fragmentation is the splitting of context across too many places, making it hard to reconstruct a decision.
- [Context Freshness](terms/items/context-freshness.md): Context Freshness is the degree to which the model sees recent, relevant, unexpired information.
- [Context Graph](terms/items/context-graph.md): Context Graph is a graph representation of the entities and relationships available to an agent.
- [Context Mesh](terms/items/context-mesh.md): Context Mesh is a distributed layer for exchanging context across systems.
- [Context Operating System](terms/items/context-operating-system.md): Context Operating System is the control layer that manages how context is selected, assembled, and served to a model.
- [Context Poisoning](terms/items/context-poisoning.md): Context Poisoning is used for untrusted content that enters an agent’s active prompt or retrieved evidence and attempts to steer its tool use.
- [Context Rot](terms/items/context-rot.md): Context Rot is the gradual degradation of context quality as sources age, diverge, or become misleading.
- [Context Saturation](terms/items/context-saturation.md): Context Saturation is the point where adding more context stops helping and starts reducing decision quality.
- [Context Supply Chain](terms/items/context-supply-chain.md): Context Supply Chain is used to trace how source data, transformations, retrieval services and prompts contribute to an agent decision.
- [Context Topology](terms/items/context-topology.md): Context Topology is the map of where context lives and how it moves between systems.
- [Data Fabric](terms/items/data-fabric.md): Data Fabric is an integrated layer for connecting distributed data through metadata, governance, and access services.
- [Data Mesh](terms/items/data-mesh.md): Data Mesh is a decentralised data architecture based on domain-owned data products and federated governance.
- [Explicit Provenance](terms/items/explicit-provenance.md): Explicit Provenance is provenance that is visible, machine-readable, and carried with the context.
- [Governed Context](terms/items/governed-context.md): Governed Context is context assembled and delivered under explicit policy and access control.
- [Identity-Resolved Data](terms/items/identity-resolved-data.md): Identity-Resolved Data is data tied to a specific principal, role, or delegation boundary.
- [Provenance Tensor](terms/items/provenance-tensor.md): Provenance Tensor is a structured representation of where context came from and how trustworthy it is.
- [RAG](terms/items/rag.md): RAG is retrieval-augmented generation: retrieving external evidence at inference time and conditioning the output on it.
- [Safe Evolution](terms/items/safe-evolution.md): Safe Evolution is the controlled change of an agent system without breaking safety, policy, or reliability constraints.
- [Shared Context Layer](terms/items/shared-context-layer.md): Shared Context Layer is a common layer for serving context across multiple agentic systems.
- [Shared Meanings](terms/items/shared-meanings.md): Shared Meanings is the alignment layer that keeps people and agents using the same terms the same way.
- [Verification Cost](terms/items/verification-cost.md): Verification Cost is the cost of proving a model’s answer or action is correct enough to trust.

## Context

- [Agentic Hub](terms/items/agentic-hub.md): A governed enterprise environment for agent operation.
- [Causal Attribution](terms/items/causal-attribution.md): Causal Attribution is about how context is assembled, managed, or governed for agents.
- [Context Collapse](terms/items/context-collapse.md): Context Collapse is the point where context becomes mixed, noisy, or operationally unusable.
- [Context Constructor](terms/items/context-constructor.md): Context Constructor is how information is assembled and presented to an agent at runtime.
- [Context Debt](terms/items/context-debt.md): Context Debt is accumulated operational cost caused by weak governance or poor design.
- [Context Drift](terms/items/context-drift.md): Context Drift is gradual divergence from the intended state, meaning, or behaviour.
- [Context Engineering](terms/items/context-engineering.md): The discipline of designing the information agents reason over at each step.
- [Context Fabric](terms/items/context-fabric.md): Context Fabric is a shared substrate for moving context across systems and teams.
- [Context Federation](terms/items/context-federation.md): Context Federation is how information is assembled and presented to an agent at runtime.
- [Context Fragmentation](terms/items/context-fragmentation.md): Context Fragmentation is context split across disconnected systems and hard to reuse safely.
- [Context Freshness](terms/items/context-freshness.md): Context Freshness is how current the information is when an agent uses it.
- [Context Graph](terms/items/context-graph.md): Context Graph is a graph-based model for representing relationships, context, or memory.
- [Context Mesh](terms/items/context-mesh.md): Context Mesh is a distributed architecture where context or agents are connected across boundaries.
- [Context Operating System](terms/items/context-operating-system.md): Context Operating System is how information is assembled and presented to an agent at runtime.
- [Context Poisoning](terms/items/context-poisoning.md): Context Poisoning is context that has been corrupted, accidentally or deliberately.
- [Context Rot](terms/items/context-rot.md): Context Rot is stale or degraded context that no longer reflects the real system.
- [Context Saturation](terms/items/context-saturation.md): Context Saturation is the point where there is too much context for the agent to use well.
- [Context Supply Chain](terms/items/context-supply-chain.md): Context Supply Chain is how information is assembled and presented to an agent at runtime.
- [Context Topology](terms/items/context-topology.md): Context Topology is how information is assembled and presented to an agent at runtime.
- [Data Fabric](terms/items/data-fabric.md): Data Fabric is a shared substrate for moving context across systems and teams.
- [Data Mesh](terms/items/data-mesh.md): Data Mesh is a distributed architecture where context or agents are connected across boundaries.
- [Explicit Provenance](terms/items/explicit-provenance.md): Explicit Provenance is traceable origin information for actions, inputs, or outputs.
- [Governed Context](terms/items/governed-context.md): Governed Context is how information is assembled and presented to an agent at runtime.
- [Identity-Resolved Data](terms/items/identity-resolved-data.md): Identity-Resolved Data is how an agent is named, authenticated, and tracked separately from the human.
- [Provenance Tensor](terms/items/provenance-tensor.md): Provenance Tensor is traceable origin information for actions, inputs, or outputs.
- [RAG](terms/items/rag.md): Retrieval-augmented generation that grounds model output in external content.
- [Safe Evolution](terms/items/safe-evolution.md): Safe Evolution is about how context is assembled, managed, or governed for agents.
- [Shared Context Layer](terms/items/shared-context-layer.md): Shared Context Layer is an abstraction layer that mediates capabilities, context, or governance.
- [Shared Meanings](terms/items/shared-meanings.md): Shared Meanings is about how context is assembled, managed, or governed for agents.
- [Verification Cost](terms/items/verification-cost.md): Verification Cost is the act of checking that an agent's output or action is correct.

## Social

- [AI Bot Swarms](terms/items/ai-bot-swarms.md): AI Bot Swarms are coordinated automated accounts or the effects attributed to them.
- [Agentic Propaganda](terms/items/agentic-propaganda.md): Agentic Propaganda is coordinated automated messaging or the effects it creates.
- [Bot Swarm](terms/items/bot-swarm.md): Bot Swarm is a coordinated cluster of automated accounts or agents acting in concert.
- [Swarm Scanner](terms/items/swarm-scanner.md): Swarm Scanner is a tool or process for detecting coordinated bot activity.
