# Agentic AI Buzzwords Dictionary

A consolidated map of agentic-AI buzzwords, vendor coinages, meme slang, and adjacent operational terms.

## 1. Core agentic terms

- **Agentic AI**: AI that plans, uses tools, and acts with partial autonomy.
- **AI agents**: the concrete implementation term; often used interchangeably with agentic AI.
- **Agentic coding**: coding with more autonomous agents than classic copilots.
- **Agentic workflow**: a task flow executed by agents with tools, memory, and control logic.
- **Agentic delivery**: running AI projects as delivery systems, not feature demos.
- **Agentic browser**: browser-native agent execution that can navigate, click, and fill forms.
- **Computer use**: agents operating software through the UI.
- **Browser use**: browser-native execution by agents.
- **Web agent**: an agent that operates across websites and web apps.
- **Agentic commerce**: autonomous buying, checkout, and payment flows.
- **Agentic trust**: trust language specific to delegated, autonomous systems.

## 2. Runtime, loop, and execution

- **Agent runtime**: the execution environment responsible for planning, tool use, memory access, policy enforcement, state management, and lifecycle control.
- **Workflow runtime**: execution layer for multi-step workflows.
- **Reasoning runtime**: runtime specialised for planning and decision-making.
- **Inference runtime**: infrastructure executing model inference.
- **Agent kernel**: minimal runtime responsible for core agent behaviour.
- **Runtime contract**: explicit guarantees governing agent behaviour during execution.
- **Runtime governance**: governance mechanisms embedded into execution.
- **Execution boundary**: boundary between reasoning and action.
- **Execution state**: current operational state of an agent.
- **Execution graph**: graph representation of workflow execution.
- **Loop engineering**: designing reusable agent loops rather than one-off prompts.
- **Agent loop**: the plan-act-observe-refine cycle.
- **Orchestration loop**: repeated coordination across agents and tools.
- **ReAct**: reasoning + acting architecture.
- **Supervisor agent**: central orchestrator that routes work to specialised agents.
- **Hierarchical agent architecture**: top-down multi-agent structure.
- **Star topology**: supervisor-in-the-middle agent layout.
- **Agent swarm**: coordinated mass of agents working in parallel.
- **Sub-agent swarm**: multiple specialised agents working on different parts of a goal.
- **Dynamic teaming**: runtime formation of agent teams.
- **Skill routing**: directing tasks to the right skill, tool, or sub-agent.
- **Dynamic skill routing**: selecting the right skill at runtime.
- **Tool router**: a layer that chooses the correct tool or action path.
- **Verifier**: the component that checks outputs or intermediate steps.
- **Safety monitor**: the component that blocks unsafe or untrusted actions.
- **Verification loop**: repeated checking and correction.
- **Trajectory quality**: judging the quality of the agent’s path, not only the final answer.
- **Long-horizon workflow**: multi-step work that persists over time.
- **Long-horizon tasks**: tasks requiring state, retries, and persistence.
- **Stop-anywhere architecture**: a runtime that can pause, inspect, redirect, or terminate actions safely.
- **Task assignment**: selecting which agent handles which subtask.
- **Agentic rendering**: using agents to produce structured outputs or content pipelines.
- **Test-driven agentic workflow**: agentic development structured around tests.
- **Pilot-to-production gap**: the recurring failure to operationalise agentic AI beyond experiments.

## 3. Context, memory, and data

- **Context engineering**: designing the agent’s informational environment.
- **Governed context**: context with provenance, permissions, freshness, and retention controls.
- **Shared context layer**: reusable organisational context across agents and workflows.
- **Context freshness**: how current the context is, often treated as a runtime SLO.
- **Context rot**: stale or bloated context that degrades performance.
- **Context collapse**: context becoming over-mixed or operationally unusable.
- **Context constructor**: the layer that assembles working context.
- **Context operating system**: a metaphor for the layered context/memory/retrieval stack.
- **Context graph**: graph representation of organisational context.
- **Context mesh**: distributed context architecture.
- **Context fabric**: unified context infrastructure.
- **Context topology**: structural arrangement of context.
- **Context federation**: linking context across domains.
- **Context supply chain**: lifecycle of context from source to consumption.
- **Context debt**: accumulated problems caused by poor context management.
- **Context drift**: gradual deviation of context quality.
- **Context poisoning**: malicious or accidental corruption of context.
- **Context saturation**: excessive context reducing effectiveness.
- **Context fragmentation**: context distributed across disconnected systems.
- **Agent memory**: persistent state across sessions.
- **Memory engineering**: discipline of designing memory systems for agents.
- **Memory architecture**: structural design of memory layers.
- **Memory substrate**: the underlying storage layer for memory.
- **Memory graph**: graph-based representation of memory.
- **Memory federation**: distributed memory architecture.
- **Working memory**: temporary memory for active reasoning.
- **Episodic memory**: memory of events and interactions.
- **Semantic memory**: memory of facts and knowledge.
- **Procedural memory**: memory of skills and processes.
- **Memory governance**: lifecycle and compliance controls for memory.
- **Memory hygiene**: curation, retirement, deduplication, and lifecycle control.
- **Memory drift**: divergence between memory and reality.
- **Memory hallucination**: inaccurate memory retrieval.
- **Memory contamination**: introduction of poor-quality memory.
- **Memory debt**: unmanaged memory accumulation.
- **Memory compaction**: reducing memory footprint while preserving usefulness.
- **State lifecycle**: create, store, refresh, expire, delete, audit.
- **RAG**: retrieval-augmented generation; increasingly treated as part of a larger context stack.
- **Identity-resolved data**: data tied to clear actors, permissions, or entities.
- **Data fabric**: unified data layer used as context infrastructure for agents.
- **Data mesh**: decentralised data architecture often contrasted with fabric.
- **Shared meanings**: consistent semantics across agents and systems.
- **Agentic hub**: central enterprise environment for governed agent operation.
- **Explicit provenance**: causal traceability for agent actions and responsibility.
- **Provenance tensor**: formalised provenance across the agent lifecycle.
- **Causal attribution**: tying outcomes back to actions, principals, or sub-agents.
- **Verification cost**: the cost of checking agent outputs and actions.
- **Safe evolution**: controlled change of skills or behaviours over time.

## 4. Identity, delegation, and governance

- **Agent identity**: unique identity and lifecycle for an agent, separate from the human user.
- **Delegated authority**: what an agent is allowed to do on behalf of a user or system.
- **Act-on-behalf**: an agent acting under scoped user or service authority.
- **Composite principal**: human + agent + sub-agent identity chain.
- **Delegation layer**: architectural layer governing delegation.
- **Delegation boundary**: limit of delegated authority.
- **Delegation contract**: formalised authority relationship.
- **Delegation scope**: permissions delegated to an agent.
- **Delegation policy**: rules governing delegation.
- **Delegation graph**: chain of delegated authority.
- **Delegation chain / delegation chains**: traceable authority lineage in multi-agent workflows.
- **Delegation audit trail**: traceability of delegated actions.
- **Delegation-aware observability**: tracing which delegated authority caused which action.
- **Delegation failure**: breakdown of delegated execution.
- **Delegation recovery**: remediation after failure.
- **Tool authorization**: deciding whether an agent can call a tool or action.
- **Action governance**: deciding whether an agent may execute a side effect.
- **Permission gates**: approval points before risky actions.
- **Policy interceptor**: runtime control that checks or blocks actions before execution.
- **Least privilege**: tight scoping of tool and data access.
- **Blast radius**: the maximum damage a single agent action can cause.
- **Autonomy boundaries**: the line between safe automation and risky delegation.
- **Decision sovereignty**: keeping final authority over agent outcomes and transactions.
- **Governance by design**: embedding governance in the system rather than bolting it on.
- **Runtime governance**: governance mechanisms embedded into execution.
- **Control plane architecture**: enterprise architecture governing agent populations.
- **Agent control plane**: governance, identity, policy, observability, evaluation, and operational layer above agent execution.
- **Policy plane**: layer enforcing policy decisions.
- **Identity plane**: layer managing identities and delegation.
- **Trust plane**: layer establishing trust and accountability.
- **Decision plane**: layer governing autonomous decisions.
- **Governance plane**: layer managing risk and compliance.
- **Action plane**: execution surface for delegated actions.
- **Trust-by-design**: embedding trust, governance, and observability into the system.
- **Human oversight**: human supervision over autonomous or semi-autonomous execution.
- **Ultimate human control**: governance language asserting a human override boundary.
- **Traceable accountability**: a formal claim that delegated actions can be audited back to a principal.
- **Guardrails**: constraints on what agentic systems may do.
- **Agentic misalignment**: when an agent’s actions diverge from intended goals.
- **Confused deputy**: the classic failure mode where an agent misuses someone else’s authority.
- **Behaviour assurance**: ensuring acceptable agent behaviour.
- **Behaviour contract**: expected behavioural constraints.
- **Behaviour drift**: gradual deviation from expected behaviour.
- **Goal drift**: deviation from intended objective.
- **Mission drift**: long-term divergence from mission.
- **Alignment verification**: validating intended behaviour.
- **Trustworthy autonomy**: autonomy operating within acceptable risk.
- **Evidence-based execution**: actions supported by evidence.
- **Behaviour replay**: replaying agent behaviour for analysis.

## 5. Protocols, integration, and platform language

- **MCP**: Model Context Protocol.
- **A2A**: agent-to-agent protocols and communications patterns.
- **Agentic web**: browsers, APIs, payments, and identity becoming agent-native.
- **Agent-ready software**: software designed to be machine-readable and callable by agents.
- **Registry**: catalogues of agents, tools, actions, or MCP servers.
- **Agent registry**: authoritative record of agents and capabilities.
- **Tool gateway**: centralised access point for tools, auth, policy, and audit.
- **Agent architect**: the role of designing the agent environment, not just prompts.
- **Intent engineering**: encoding goals, trade-offs, and organisational intent into the agent system.
- **Specification engineering**: turning policies and standards into machine-readable constraints.
- **Agent training**: in agentic circles, usually shaping behaviour, workflow, or skills rather than model pretraining.
- **Skill libraries**: reusable agent capabilities or procedures.
- **Agentic multi-agent architecture**: formal label for a multi-agent orchestration stack.
- **Agent marketplace**: environment where agents provide capabilities.
- **Agent assembly**: temporary grouping of agents.
- **Agent coalition**: goal-oriented group of agents.
- **Agent federation**: collaboration across independent agent groups.
- **Agent mesh**: distributed network of agents.
- **Agent society**: large-scale interacting agent ecosystem.
- **Agent collective**: coordinated group of agents.
- **Ambient team**: persistent team of specialised agents sharing context.
- **Collective intelligence layer**: emergent intelligence from collaboration.

## 6. Evaluation, reliability, and operations

- **Agent evals**: evaluation suites for agentic workflows and task performance.
- **AgentOps**: operational discipline for identity, tooling, evaluation, audit, cost, and recovery.
- **Evidence-grade audit trail**: audit logs sufficient to reconstruct what happened and why.
- **Recovery readiness**: rollback, replay, revoke, or correct after failure.
- **Exception rate**: the share of tasks requiring human intervention.
- **Verified outcome**: measuring completed work, not model output.
- **Cost per workflow**: a stronger metric than $/token.
- **Continuous validation**: ongoing checking rather than one-time testing.
- **Multi-agent governance**: control structures for multiple collaborating agents.
- **Autonomous workflow**: a business process executed with minimal human intervention.
- **Stop-anywhere architecture**: a runtime that can pause, inspect, redirect, or terminate actions safely.
- **Outcome reliability**: consistency of outcomes.
- **Execution quality**: quality of task execution.
- **Trajectory evaluation**: evaluation of execution path.
- **Behaviour assurance**: ensuring acceptable agent behaviour.
- **Agent estate**: the total governed population of agents operating across an organisation.
- **Agent inventory**: catalogue of deployed agents.
- **Agent portfolio**: collection of agents managed as a strategic capability.
- **Agent lifecycle management**: creation, deployment, modification, retirement.
- **Agent ownership model**: accountability structure for agents.
- **Agent sprawl**: uncontrolled growth of agents.
- **Ghost agent**: abandoned agent still operating without ownership.
- **Shadow agent**: agent operating outside governance structures.
- **Orphan agent**: agent without an accountable owner.
- **Agent debt**: operational debt created by poorly governed agents.
- **Pilot purgatory**: endless experimentation without production deployment.
- **Proof-of-concept graveyard**: accumulation of abandoned AI experiments.

## 7. Status signalling, meme slang, and anti-hype language

- **Tokenmaxxing**: maximising token spend or usage as a performative productivity signal.
- **Promptmaxxing**: maximising prompt length or prompt activity as a performative game.
- **Agentmaxxing**: overusing agents to signal output, scale, or productivity status.
- **Vibe coding**: building by prompt, steering, and accepting generated code with minimal manual coding.
- **Harness engineering**: the disciplined wrapper around AI tools, workflows, constraints, and controls.
- **Slopcoding**: code generated with low discernment and high acceptance of junk output.
- **AI slop**: low-quality, high-volume AI-generated content.
- **Workslop**: polished-looking but useless AI-generated workplace output.
- **Slopaganda**: AI-generated propaganda or persuasion content built for scale and virality.
- **AI washing**: overstating AI capability in product or company marketing.
- **Agent washing**: rebranding existing software as “agentic” without real autonomy.
- **Architecture washing**: marketing simple workflows as architectures.
- **Control washing**: claiming governance without enforcement.
- **Governance theatre**: superficial governance without control.
- **Agent theatre**: simulated autonomy with hidden human intervention.
- **Autonomy theatre**: claims of autonomy unsupported by reality.
- **Microslop**: mocking label for low-quality AI output or branding in Microsoft/Copilot-adjacent spaces.
- **Trendslop**: buzzy, AI-generated advice or trend content with weak reasoning.
- **Prompt slop**: noisy, bloated, or careless prompts and outputs.
- **Prompt goblin**: someone who hoards and hacks prompts for output chasing.
- **Vibe valuation**: startup valuation driven by narrative and vibes more than fundamentals.
- **Demo-ware**: impressive demos that do not survive contact with real workflows.
- **Chatbot theatre**: products that look agentic but only repackage a chat UI.
- **Synthetic sludge**: pejorative for high-volume, low-quality AI output.
- **Auto-bullshit**: fluent but ungrounded output.
- **Productivity cosplay**: performative AI use for appearances rather than actual leverage.
- **AI ribbon-cutting**: hype launch with weak substance.
- **AI sprawl**: uncontrolled proliferation of AI tools across teams.
- **Saaspocalypse**: meme term for AI pressure collapsing traditional SaaS moats.
- **Zombie internet**: feed and search environments saturated with synthetic content and bots.
- **Dead Internet**: the broader claim that online spaces are increasingly bot-driven.
- **Clanker**: insult for AI systems or bots, borrowed from online meme culture.
- **AI leaderboards**: workplace gamification around token use, prompts, or AI activity.
- **Agent FOMO**: adoption driven by fear of missing out.

## 8. Social / influence terms adjacent to agentic AI

- **Bot swarm**: coordinated autonomous agents used for influence or manipulation.
- **Swarm scanner**: defensive tooling to detect bot or swarm activity.
- **Agentic propaganda**: synthetic persuasion using autonomous agents and scale.
- **AI bot swarms**: coordinated bot networks that mimic human behaviour.
