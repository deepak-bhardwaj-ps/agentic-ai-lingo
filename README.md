# Agentic AI Buzzword Dictionary

A living dictionary of agentic AI terminology, runtime language, governance terms, protocol vocabulary, and meme slang.

## Core

- [AI Agents](terms/items/ai-agents.md): Software that can work towards a goal by choosing next steps, using tools, and learning from what happens after it acts.
- [Agentic AI](terms/items/agentic-ai.md): A broad and still debated term for AI systems that can plan steps, use tools, and carry out tasks.
- [Agentic Browser](terms/items/agentic-browser.md): A browser that lets an AI read web pages and carry out tasks for a user.
- [Agentic Coding](terms/items/agentic-coding.md): Coding where an AI system can plan, use tools, test changes, and improve its work over more than one step.
- [Agentic Commerce](terms/items/agentic-commerce.md): Buying and selling where an AI agent helps a person discover, choose, order, or pay for goods or services.
- [Agentic Delivery](terms/items/agentic-delivery.md): A loosely used term for getting work done with AI agents that can take steps, use tools, and hand control back to a person when needed.
- [Agentic Trust](terms/items/agentic-trust.md): How much freedom an AI agent should get before a person needs to check its actions.
- [Agentic Workflow](terms/items/agentic-workflow.md): An agentic workflow is a planned sequence of steps where an AI system can use tools and sometimes other agents to finish a task.
- [Browser Use](terms/items/browser-use.md): Browser use means letting an agent interact with a website through a browser instead of an API.
- [Computer Use](terms/items/computer-use.md): Computer use is when a model interacts with a computer by looking at the screen and using mouse and keyboard actions.
- [Web Agent](terms/items/web-agent.md): An agent that uses a browser or web tools to complete tasks on the web.

## Runtime

- [Agent Control Plane](terms/items/agent-control-plane.md): A central management layer for registering, governing, monitoring, and retiring AI agents.
- [Agent Kernel](terms/items/agent-kernel.md): The small runtime loop that lets an agent keep state, choose its next step, and use tools.
- [Agent Loop](terms/items/agent-loop.md): A repeating cycle where an AI system does something, checks the result, and decides the next step.
- [Agent Runtime](terms/items/agent-runtime.md): The software layer that keeps an AI agent going across steps, tool calls, and pauses.
- [Agent Swarm](terms/items/agent-swarm.md): A group of AI agents that split work, share results, and coordinate to finish one task.
- [Agentic Rendering](terms/items/agentic-rendering.md): A loose term for a screen or interface that changes because an agent has made a choice, used a tool, or updated its state.
- [Dynamic Skill Routing](terms/items/dynamic-skill-routing.md): Choosing, at run time, which skill or capability should handle a request.
- [Dynamic Teaming](terms/items/dynamic-teaming.md): Dynamic teaming is a loose term for forming and changing teams at runtime instead of relying on fixed groups.
- [Execution Boundary](terms/items/execution-boundary.md): The point where an AI system stops deciding and something else starts carrying out, checking, or blocking the action.
- [Execution Graph](terms/items/execution-graph.md): A way to show the steps in a task, what depends on what, and when things happen.
- [Execution State](terms/items/execution-state.md): The mutable record an agent runtime uses to continue a run after each step.
- [Hierarchical Agent Architecture](terms/items/hierarchical-agent-architecture.md): A way of organising agents into layers, where higher-level agents break work down, assign tasks, and check results from lower-level agents.
- [Inference Runtime](terms/items/inference-runtime.md): The software layer that runs a trained model and handles incoming requests
- [Long-Horizon Tasks](terms/items/long-horizon-tasks.md): Tasks that take many dependent steps to finish and need the work to stay on track over time.
- [Long-Horizon Workflow](terms/items/long-horizon-workflow.md): A long-horizon workflow is a task that must stay coherent across many steps, interruptions, and corrections.
- [Loop Engineering](terms/items/loop-engineering.md): Designing the repeated decide, act, and check cycle an agent uses to make progress.
- [Orchestration Loop](terms/items/orchestration-loop.md): A control cycle that decides what an AI system should do next, checks the result, and either stops or tries again.
- [Pilot-to-Production Gap](terms/items/pilot-to-production-gap.md): The missing work between a pilot that looks good and a system that can safely run for real users.
- [ReAct](terms/items/react.md): ReAct is a way for an AI system to think, take an action, then use what it learned to keep going.
- [Reasoning Runtime](terms/items/reasoning-runtime.md): The part of an agent system that manages thinking, choosing the next step, and keeping state across steps.
- [Runtime Contract](terms/items/runtime-contract.md): A runtime contract is a clear agreement about what a component will accept, produce, and rely on while it is running.
- [Runtime Governance](terms/items/runtime-governance.md): Runtime governance is the set of controls that decides what an AI system can do while it is running.
- [Safety Monitor](terms/items/safety-monitor.md): A safety monitor is a check that watches an agent's actions and stops or flags unsafe behaviour.
- [Skill Routing](terms/items/skill-routing.md): Choosing which skill, tool, or sub-task should handle a request.
- [Star Topology](terms/items/star-topology.md): A communication shape where one central node talks to several others.
- [Stop-Anywhere Architecture](terms/items/stop-anywhere-architecture.md): A stop-anywhere architecture is a way of building an agent so it can be paused or stopped without losing track of what it was doing.
- [Sub-Agent Swarm](terms/items/sub-agent-swarm.md): A sub-agent swarm is a group of smaller agents that a main agent coordinates to split up work.
- [Supervisor Agent](terms/items/supervisor-agent.md): A supervisor agent is the main agent that assigns tasks to other agents, checks their work, and decides what happens next.
- [Task Assignment](terms/items/task-assignment.md): Task Assignment means deciding which agent or worker should do which piece of work.
- [Test-Driven Agentic Workflow](terms/items/test-driven-agentic-workflow.md): A test-driven agentic workflow is a way of building an agent where checks and evaluations define what “good” looks like before the agent is changed.
- [Tool Router](terms/items/tool-router.md): A tool router decides which tool an agent should use for a request.
- [Tooling Layer](terms/items/tooling-layer.md): The tooling layer is the part of an agent system that connects the model to tools, data, and outside systems.
- [Trajectory Quality](terms/items/trajectory-quality.md): How good the step-by-step path an agent takes is, not just whether it ends with the right answer.
- [Verification Loop](terms/items/verification-loop.md): A verification loop is a repeating check-and-fix cycle that tests a result before the system moves on.
- [Verifier](terms/items/verifier.md): A verifier checks whether an output or action meets a set of rules.
- [Workflow Runtime](terms/items/workflow-runtime.md): The software layer that runs a workflow step by step and keeps it going across failures or pauses.

## Memory

- [Agent Memory](terms/items/agent-memory.md): Information kept outside the model so an agent can remember useful facts, preferences, and past steps across turns or sessions.
- [Episodic Memory](terms/items/episodic-memory.md): Memory for specific events, times, and experiences; in AI, a metaphor for storing past interactions so they can be recalled later.
- [Memory Architecture](terms/items/memory-architecture.md): The way an AI system stores, finds, updates, and forgets information it needs later.
- [Memory Compaction](terms/items/memory-compaction.md): Memory compaction is shortening stored context so an agent can keep working without carrying every detail.
- [Memory Contamination](terms/items/memory-contamination.md): Memory contamination is when a system stores, retrieves, or reuses bad memory so later decisions are based on false or irrelevant information.
- [Memory Debt](terms/items/memory-debt.md): A phrase for the growing mess that builds up when an agent’s memory is not cleaned, checked, or updated properly.
- [Memory Drift](terms/items/memory-drift.md): Gradual change in what an agent remembers, how it stores it, or how it later uses that memory.
- [Memory Engineering](terms/items/memory-engineering.md): The practice of designing how an agent stores, updates, retrieves, and forgets information over time.
- [Memory Federation](terms/items/memory-federation.md): A way of linking several memory stores so an agent can look across them through one shared interface.
- [Memory Governance](terms/items/memory-governance.md): Rules for who can store, read, change, keep, and delete an agent's memory.
- [Memory Graph](terms/items/memory-graph.md): A memory graph stores facts, people, events, and links between them so an AI agent can find related information more easily.
- [Memory Hallucination](terms/items/memory-hallucination.md): A memory failure where an agent stores, recalls, or uses the wrong information.
- [Memory Hygiene](terms/items/memory-hygiene.md): Routine care for an agent's stored memories so they stay accurate, current, and useful.
- [Memory Substrate](terms/items/memory-substrate.md): A memory substrate is the shared storage layer that lets an AI agent keep useful information beyond one chat turn.
- [Memory Systems](terms/items/memory-systems.md): A memory system is the part of an agent that decides what to keep, what to look up, what to update, and what to forget over time.
- [Procedural Memory](terms/items/procedural-memory.md): Memory for how to do a task, like following a workflow or using a skill.
- [Semantic Memory](terms/items/semantic-memory.md): Semantic memory is stored facts and concepts that can be reused later.
- [State Lifecycle](terms/items/state-lifecycle.md): A state lifecycle is the set of steps a piece of agent state goes through from creation to deletion.
- [Working Memory](terms/items/working-memory.md): The small, temporary set of information an agent is using right now.

## Governance

- [Act-on-Behalf](terms/items/act-on-behalf.md): Acting on behalf means an agent is allowed to do one specific task for someone else, with clear limits.
- [Action Governance](terms/items/action-governance.md): The rules, checks, and approvals that decide whether an AI agent is allowed to take a specific action.
- [Action Plane](terms/items/action-plane.md): A design label for the part of an agent system that checks, allows, blocks, changes, or logs an action before it reaches the real world.
- [Agent Identity](terms/items/agent-identity.md): The separate identity an AI agent uses so systems can recognise it, control what it can do, and trace its actions
- [Agentic Misalignment](terms/items/agentic-misalignment.md): When an AI agent’s actions stop matching the goal, limits, or rules it was meant to follow.
- [Alignment Verification](terms/items/alignment-verification.md): Checking whether an AI agent keeps to its stated rules, purpose, and limits.
- [Autonomy Boundaries](terms/items/autonomy-boundaries.md): Rules that say what an AI agent may do on its own and what needs approval.
- [Behaviour Assurance](terms/items/behaviour-assurance.md): Evidence that an agent stays within its allowed actions and can be checked, limited, and stopped when needed.
- [Behaviour Contract](terms/items/behaviour-contract.md): A behaviour contract is a clear written description of what an agent is allowed to do, what it must do, and when a person must step in.
- [Behaviour Drift](terms/items/behaviour-drift.md): Behaviour Drift is a label for an agent gradually changing how it behaves compared with the behaviour people expected.
- [Behaviour Replay](terms/items/behaviour-replay.md): Behaviour Replay means running a recorded agent trace again so you can inspect what happened or try to reproduce a result.
- [Blast Radius](terms/items/blast-radius.md): How much damage a mistake, bug, or security problem could cause before it is stopped.
- [Composite Principal](terms/items/composite-principal.md): A composite principal is one acting identity made from more than one identity or delegated role.
- [Confused Deputy](terms/items/confused-deputy.md): A confused deputy is a trusted system tricked into using its own permissions for the wrong person.
- [Control Plane Architecture](terms/items/control-plane-architecture.md): A control plane is the part of a system that manages policy, permissions, and system-wide actions.
- [Decision Plane](terms/items/decision-plane.md): A decision plane is the part of a system where permission, approval, logging, and escalation rules are decided and recorded.
- [Decision Sovereignty](terms/items/decision-sovereignty.md): Decision sovereignty means deciding who has the final say, who can override an AI system, and how that authority is checked and recorded.
- [Delegated Authority](terms/items/delegated-authority.md): Delegated authority is permission given by one person or system to another to act within a set limit.
- [Delegation Audit Trail](terms/items/delegation-audit-trail.md): A record showing who gave an agent permission to act, what it was allowed to do, and when that permission changed.
- [Delegation Boundary](terms/items/delegation-boundary.md): The point where one person or system is allowed to act for another, with clear limits.
- [Delegation Chain](terms/items/delegation-chain.md): A delegation chain is the line of people or systems that pass authority from one to another.
- [Delegation Contract](terms/items/delegation-contract.md): A delegation contract is a clear record of what authority an agent has, who gave it, and where the limits are.
- [Delegation Failure](terms/items/delegation-failure.md): A delegation failure happens when an agent is given authority it should not have, cannot prove who allowed it to act, or keeps acting outside its limits.
- [Delegation Graph](terms/items/delegation-graph.md): A delegation graph shows who gave an agent permission to act, what it may do, and how that permission passes along a chain.
- [Delegation Layer](terms/items/delegation-layer.md): A delegation layer is the part of a system that defines who can act for whom, what they may do, and how that permission is checked.
- [Delegation Policy](terms/items/delegation-policy.md): Rules that define what an agent is allowed to do on someone else’s behalf.
- [Delegation Recovery](terms/items/delegation-recovery.md): The steps for giving an agent back the right level of access, or safely replacing its access, after something goes wrong.
- [Delegation Scope](terms/items/delegation-scope.md): Delegation scope is the exact boundary of what an agent or system is allowed to do on behalf of someone else.
- [Delegation-Aware Observability](terms/items/delegation-aware-observability.md): Observability for agent actions that keeps track of who delegated the work, what the agent was allowed to do, and what it actually did.
- [Evidence-Based Execution](terms/items/evidence-based-execution.md): A rule that an agent may act only when the required proof, permission, or record has been checked.
- [Goal Drift](terms/items/goal-drift.md): Goal drift is when an agent slowly moves away from the goal it was meant to follow.
- [Governance Plane](terms/items/governance-plane.md): The governance plane is the layer that sets, checks, and records the rules an AI system must follow.
- [Governance by Design](terms/items/governance-by-design.md): Building rules, checks, and human oversight into a system from the start.
- [Guardrails](terms/items/guardrails.md): Rules and checks that limit what an AI agent can do, say, or use.
- [Human Oversight](terms/items/human-oversight.md): Human oversight means a person is able to watch, review, and if needed stop or change what an AI system does.
- [Identity Plane](terms/items/identity-plane.md): A layer that decides which person, app, or service is allowed to act, and what they are allowed to do.
- [Least Privilege](terms/items/least-privilege.md): Giving an agent only the access it needs for the task at hand.
- [Mission Drift](terms/items/mission-drift.md): Mission drift is a gradual shift away from the goal, rules, or limits an agent was meant to follow.
- [Permission Gates](terms/items/permission-gates.md): A permission gate is a check that decides whether an action is allowed before an agent or system can do it.
- [Policy Interceptor](terms/items/policy-interceptor.md): A Policy Interceptor is a place in a system where a requested action is checked against policy before it is allowed to continue.
- [Policy Plane](terms/items/policy-plane.md): A policy plane is the part of a system that checks rules and decides whether an action should be allowed.
- [Specification Engineering](terms/items/specification-engineering.md): Specification Engineering is the practice of writing behaviour as clear, testable rules that can be checked and enforced.
- [Tool Authorization](terms/items/tool-authorization.md): Rules that decide whether an agent may use a tool or take an action.
- [Traceable Accountability](terms/items/traceable-accountability.md): Traceable accountability means being able to show who is responsible, what they were allowed to do, and what happened.
- [Trust Plane](terms/items/trust-plane.md): A trust plane is a proposed layer for deciding what an AI agent is allowed to do, proving why it was allowed, and keeping a record of it.
- [Trust-by-Design](terms/items/trust-by-design.md): A way of designing an AI system so trust comes from clear roles, controls, records, and human oversight rather than blind confidence.
- [Trustworthy Autonomy](terms/items/trustworthy-autonomy.md): A coined label for autonomy that is limited by controls, oversight, and proof of what the system is allowed to do.
- [Ultimate Human Control](terms/items/ultimate-human-control.md): A term for making sure a person can review, stop, approve, or override an AI agent before important actions happen.
- [Verifiable Action](terms/items/verifiable-action.md): A verifiable action is one that can be checked against a clear rule, approval, or record before it counts.

## Protocols

- [A2A](terms/items/a2a.md): A2A is an open standard that lets one AI agent find, talk to, and hand work to another AI agent.
- [Agent Architect](terms/items/agent-architect.md): A loose name for the person who designs how an agent system is set up, connected, and controlled.
- [Agent Assembly](terms/items/agent-assembly.md): A way of arranging several AI agents so they share work and act like one system.
- [Agent Coalition](terms/items/agent-coalition.md): A loose term for several separate agents that choose to work together on one goal.
- [Agent Collective](terms/items/agent-collective.md): A loose term for several agents that coordinate their actions instead of working in isolation.
- [Agent Federation](terms/items/agent-federation.md): A loose term for separate agents that can discover, trust, and work with each other across boundaries.
- [Agent Marketplace](terms/items/agent-marketplace.md): A catalogue where people can find, compare, and install AI agents or skills from different creators.
- [Agent Mesh](terms/items/agent-mesh.md): A loose term for a network of AI agents that can find each other and hand work around without one central controller.
- [Agent Registry](terms/items/agent-registry.md): A directory of agents and their basic details so other systems can find them.
- [Agent Society](terms/items/agent-society.md): A loose term for a group of AI agents that follow shared rules, roles, or norms.
- [Agent Training](terms/items/agent-training.md): A loose term for getting an AI agent ready to do a job, usually by setting up its instructions, tools, permissions, and checks rather than changing the model itself.
- [Agent-Ready Software](terms/items/agent-ready-software.md): Software designed so an AI agent can find, call, and recover from tools with clear rules, structured results, and less guessing.
- [Agentic Multi-Agent Architecture](terms/items/agentic-multi-agent-architecture.md): A way of building AI systems where several agents share a job and coordinate with each other.
- [Agentic Web](terms/items/agentic-web.md): A loose term for web services designed so software agents can find them, understand them, and use them with permission.
- [Ambient Team](terms/items/ambient-team.md): A coined label for a persistent group of agents that works around a person or team in the background.
- [Collective Intelligence Layer](terms/items/collective-intelligence-layer.md): A collective intelligence layer is a shared coordination layer that helps several AI agents or tools work together by passing tasks, context, and results around.
- [Intent Engineering](terms/items/intent-engineering.md): Intent engineering is the work of turning a person’s goal into a clear, testable task that a system can carry out.
- [Intent Mesh](terms/items/intent-mesh.md): A loose term for routing a user's intent across multiple agents, tools, or services before action is taken.
- [MCP](terms/items/mcp.md): MCP is the Model Context Protocol, a standard way for AI apps to connect to tools and data.
- [Registry](terms/items/registry.md): A registry is a catalogue that helps people or software find named things such as servers, tools, or packages.
- [Skill Libraries](terms/items/skill-libraries.md): Skill libraries are reusable bundles of instructions, examples, tools, and sometimes code that help an agent do a task the same way each time.

## AgentOps

- [Agent Debt](terms/items/agent-debt.md): Agent debt is the build-up of weak spots in an AI agent system that make it harder, riskier, or more expensive to change and run safely.
- [Agent Estate](terms/items/agent-estate.md): The full live set of AI agents an organisation runs, plus the people, rules, tools, permissions, and controls around them.
- [Agent Evals](terms/items/agent-evals.md): Tests that check whether an AI agent can complete real tasks correctly
- [Agent Inventory](terms/items/agent-inventory.md): A live record of the AI agents an organisation uses, who owns them, and where they run.
- [Agent Lifecycle Management](terms/items/agent-lifecycle-management.md): Managing an AI agent from approval and launch through updates, monitoring, suspension, and retirement.
- [Agent Ownership Model](terms/items/agent-ownership-model.md): A clear way to decide which people are responsible for an AI agent and what they must do.
- [Agent Portfolio](terms/items/agent-portfolio.md): A group of AI agents that are owned, compared, and managed together.
- [Agent Sprawl](terms/items/agent-sprawl.md): Agent sprawl is when AI agents spread faster than an organisation can track, own, control, and retire them.
- [AgentOps](terms/items/agentops.md): AgentOps is the work of running AI agents safely in real use, with monitoring, testing, release control, and governance.
- [Agentic Evaluation](terms/items/agentic-evaluation.md): Testing an AI agent by looking at its steps, tool use, and decisions, not just its final answer.
- [Autonomous Workflow](terms/items/autonomous-workflow.md): A workflow that can keep moving and recover from common problems with limited human help.
- [Continuous Validation](terms/items/continuous-validation.md): Ongoing checks that an agent or AI system still behaves the way it should.
- [Cost per Workflow](terms/items/cost-per-workflow.md): The average total cost of completing one workflow from start to finish.
- [Evidence-Grade Audit Trail](terms/items/evidence-grade-audit-trail.md): A detailed record of actions and events that is good enough to review, explain, and check what happened.
- [Exception Rate](terms/items/exception-rate.md): The share of workflows that need manual handling, escalation, or fallback instead of finishing automatically.
- [Execution Quality](terms/items/execution-quality.md): How well an agent finishes a task in a real run.
- [Ghost Agent](terms/items/ghost-agent.md): A ghost agent is an agent that still appears in records, but is no longer really active, owned, or doing useful work.
- [Harness Engineering](terms/items/harness-engineering.md): The work of shaping the tools, rules, checks, and safe workspace around an AI agent so it can do tasks reliably.
- [Multi-Agent Governance](terms/items/multi-agent-governance.md): The rules, checks, and ownership that keep several AI agents working safely together.
- [Orphan Agent](terms/items/orphan-agent.md): An orphan agent is an agent with no clear owner for its behaviour, upkeep, or retirement.
- [Outcome Reliability](terms/items/outcome-reliability.md): How often an agent reaches the result it was meant to achieve.
- [Pilot Purgatory](terms/items/pilot-purgatory.md): A project gets stuck after a promising pilot and never becomes a reliable, owned production service.
- [Proof-of-Concept Graveyard](terms/items/proof-of-concept-graveyard.md): A proof-of-concept graveyard is a pile-up of demos or pilots that never become real products.
- [Recovery Readiness](terms/items/recovery-readiness.md): Recovery Readiness is a measure of how well an agent system can be restored after something goes wrong.
- [Shadow Agent](terms/items/shadow-agent.md): An agent that runs without the normal visibility, approval, or oversight from the team that owns it.
- [Trajectory Evaluation](terms/items/trajectory-evaluation.md): Checking the steps an agent took, not just the final answer.
- [Verified Outcome](terms/items/verified-outcome.md): A result that has been checked against a clear rule, test, or piece of evidence.

## Slang

- [AI Ribbon-Cutting](terms/items/ai-ribbon-cutting.md): Slang for an AI launch that looks impressive but does not yet deliver real use or value.
- [AI Slop](terms/items/ai-slop.md): A rude term for low-quality AI-generated content that is made in large amounts and is often messy, generic, or poorly checked.
- [AI Sprawl](terms/items/ai-sprawl.md): A messy situation where too many AI tools, pilots, or agents are created without shared control.
- [AI Washing](terms/items/ai-washing.md): A claim that something is branded as AI even though the real system uses little AI, or far less than the marketing suggests.
- [Agent FOMO](terms/items/agent-fomo.md): Slang for adding an AI agent because it is trendy, not because the job actually needs one.
- [Agent Theatre](terms/items/agent-theatre.md): Slang for an agent demo that looks self-running, but is quietly helped by people, scripts, or hidden manual steps.
- [Agent Washing](terms/items/agent-washing.md): A marketing trick where simple automation is presented as if it were a real agent.
- [Agentmaxxing](terms/items/agentmaxxing.md): Slang for pushing AI agent use as far as possible, often by stacking more agents, tools, and automation.
- [Architecture Washing](terms/items/architecture-washing.md): A criticism for making a system look more carefully designed, governed, or advanced than it really is.
- [Auto-bullshit](terms/items/auto-bullshit.md): Informal slang for AI output that sounds confident but is wrong, unsupported, or meaningless.
- [Autonomy Theatre](terms/items/autonomy-theatre.md): A criticism for AI systems that look self-directing, but still depend on people for the important decisions.
- [Chatbot Theatre](terms/items/chatbot-theatre.md): A criticism for chat interfaces that look useful but do not actually get the work done
- [Clanker](terms/items/clanker.md): A rude slang word for robots, chatbots, and other AI systems, usually used to mock or criticise them.
- [Control Washing](terms/items/control-washing.md): A claim that something is described as tightly controlled when the real controls are weak or hard to prove.
- [Dead Internet](terms/items/dead-internet.md): A label for the belief that much of the internet is now dominated by bots, spam, and machine-made content.
- [Demo-ware](terms/items/demo-ware.md): Demo-ware is software that looks good in a prepared demo but does not hold up in normal use.
- [Governance Theatre](terms/items/governance-theatre.md): Governance theatre means having rules, meetings, or approval steps that look like control but do not really change what happens.
- [Microslop](terms/items/microslop.md): A mocking nickname for Microsoft software or AI features that people think are bloated, intrusive, or low quality.
- [Productivity Cosplay](terms/items/productivity-cosplay.md): A slang term for looking productive without producing much real value.
- [Prompt Goblin](terms/items/prompt-goblin.md): Slang for a person who keeps tweaking prompts and prompt wrappers in search of small improvements.
- [Prompt Slop](terms/items/prompt-slop.md): A slang term for messy, overstuffed, or low-value prompts that are hard for a model or person to use well.
- [Promptmaxxing](terms/items/promptmaxxing.md): Slang for pushing prompt writing, formatting, and instruction detail as far as possible to squeeze out small gains from a model.
- [Saaspocalypse](terms/items/saaspocalypse.md): A slang term for the idea that AI could weaken the value of traditional SaaS by making software easier to copy or replace.
- [Slopaganda](terms/items/slopaganda.md): Slopaganda is slang for AI-made content that is low quality, repeated, or promoted more for persuasion than for usefulness.
- [Slopcoding](terms/items/slopcoding.md): A rude term for code that is produced quickly by AI but is messy, weakly checked, or costly to maintain.
- [Synthetic Sludge](terms/items/synthetic-sludge.md): A slang term for piles of machine-made content that are low value, repetitive, and hard to sort through.
- [Tokenmaxxing](terms/items/tokenmaxxing.md): Informal slang for trying to use as many tokens as possible in an AI prompt or response.
- [Trendslop](terms/items/trendslop.md): A slang term for AI-generated output that chases buzzwords or trends instead of giving useful, well-checked advice.
- [Vibe Coding](terms/items/vibe-coding.md): Vibe coding means using natural language to steer an AI coding tool, often with little line-by-line writing by the person.
- [Vibe Valuation](terms/items/vibe-valuation.md): A slang term for valuing a company more by story, buzz, or polished demos than by real business results.
- [Workslop](terms/items/workslop.md): Workslop is AI-made work that looks polished but creates extra work for the person who receives it.
- [Zombie Internet](terms/items/zombie-internet.md): A slang term for a web that feels crowded with copied, automated, stale, or low-trust content.

## Context

- [Agentic Hub](terms/items/agentic-hub.md): A central layer that helps an AI agent find and use tools, data, and services.
- [Causal Attribution](terms/items/causal-attribution.md): A loose term for working out which source, step, or action actually caused an AI result.
- [Context Collapse](terms/items/context-collapse.md): A failure mode where an agent gets too much, too little, or the wrong context to do the task well.
- [Context Constructor](terms/items/context-constructor.md): A context constructor is the part of an AI system that chooses and assembles the information sent to the model for one request.
- [Context Debt](terms/items/context-debt.md): The build-up of stale, duplicated, missing, or poorly delivered context that makes an AI agent less accurate and more expensive to run.
- [Context Drift](terms/items/context-drift.md): A gradual change in the information an AI system uses, which can quietly change its answers or actions.
- [Context Engineering](terms/items/context-engineering.md): The deliberate work of choosing, shaping, and updating the information an AI model sees before it answers.
- [Context Fabric](terms/items/context-fabric.md): A context fabric is a shared layer that helps different AI agents and tools store, find, and pass along the information they need.
- [Context Federation](terms/items/context-federation.md): Context Federation is a loose term for coordinating context across several systems so an AI agent gets the right information at the right time.
- [Context Fragmentation](terms/items/context-fragmentation.md): Context fragmentation is when the information an AI agent needs is split across too many places, so no single, clear picture is available at decision time.
- [Context Freshness](terms/items/context-freshness.md): How recent and relevant the information in an agent's working context is.
- [Context Graph](terms/items/context-graph.md): A context graph is a connected way to store facts, relationships, and task history so an AI system can find what matters for the current job.
- [Context Mesh](terms/items/context-mesh.md): A context mesh is a way of moving the right information to the right AI tool or agent at the right time across several systems.
- [Context Operating System](terms/items/context-operating-system.md): A loose term for the layer that chooses, cleans, and delivers the information an AI agent can use at runtime.
- [Context Poisoning](terms/items/context-poisoning.md): Context poisoning is when untrusted text is put into an AI agent's working context and changes what it does.
- [Context Rot](terms/items/context-rot.md): A name for when an AI system gets worse at using its input as the context gets longer, messier, or less fresh.
- [Context Saturation](terms/items/context-saturation.md): Context saturation is when a model or agent has so much information in its working context that extra details stop helping and can start hurting.
- [Context Supply Chain](terms/items/context-supply-chain.md): The chain of people, systems, and steps that decide what information reaches an AI agent at the moment it answers.
- [Context Topology](terms/items/context-topology.md): A way of describing where an AI system gets its context, how that context is chosen, and how it moves between stores, tools, and model calls
- [Data Fabric](terms/items/data-fabric.md): A data fabric is a layer that helps people find, connect, govern, and use data across many systems.
- [Explicit Provenance](terms/items/explicit-provenance.md): Provenance that is made visible and machine-readable so an agent can trace where information came from and how it was used.
- [Governed Context](terms/items/governed-context.md): Governed context means the information given to an AI agent is chosen, checked, and controlled by rules.
- [Identity-Resolved Data](terms/items/identity-resolved-data.md): Data that has been matched to a real person, service, or role instead of staying anonymous or mixed up with other records.
- [Provenance Tensor](terms/items/provenance-tensor.md): A proposed way to describe where agent context came from, how trustworthy it is, and how it should be handled.
- [RAG](terms/items/rag.md): RAG means a language model looks up relevant information before it answers.
- [Safe Evolution](terms/items/safe-evolution.md): A term for changing an agent system in a controlled way so new behaviour can be tested, limited, and rolled back before it reaches everyone.
- [Shared Context Layer](terms/items/shared-context-layer.md): A shared layer that gives multiple agents the same trusted context, rules, and memory.
- [Shared Meanings](terms/items/shared-meanings.md): Shared meanings are the shared understanding that lets people and agents use words in the same way.
- [Verification Cost](terms/items/verification-cost.md): The work needed to check whether an AI answer or action is good enough to trust.

## Social

- [AI Bot Swarms](terms/items/ai-bot-swarms.md): A loose term for many automated or semi-automated accounts acting together online.
- [Agentic Propaganda](terms/items/agentic-propaganda.md): A loose label for propaganda spread by software that acts on its own or with little human help.
- [Bot Swarm](terms/items/bot-swarm.md): A bot swarm is a group of automated accounts or agents that act together to influence or overwhelm online activity.
- [Swarm Scanner](terms/items/swarm-scanner.md): A nonstandard label for a tool or process that looks for many accounts acting together, often to detect bots or coordinated manipulation.
