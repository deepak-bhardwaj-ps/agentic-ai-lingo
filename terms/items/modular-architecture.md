---
title: Modular architecture
short_description: A way of building software as separate parts with clear boundaries and interfaces.
category: Agentic patterns
tags:
- architecture
- modularity
- boundaries
status: active
aliases: []
meaning_type: old_idea_new_tools
novelty_level: low
maturity_level: established
common_misuse:
- Confusing modular architecture with microservices, which is a deployment style
- Assuming separate modules must be separate apps or servers
- Treating any folder structure as real modularity
related_terms:
- Module boundary
- Encapsulation
- Monolith
- Microservices
- Modular monolith
evidence:
  - source_title: Linking Modular Architecture to Development Teams
    source_url: https://martinfowler.com/articles/linking-modular-arch.html
    source_type: engineering_blog
    relevance: Fowler discusses modular architecture as a way to reduce coupling between parts of a system and align them with team ownership.
    key_point: Good modular architecture keeps parts of the system separated so they can change without constantly disturbing each other.
  - source_title: Architectural principles - .NET
    source_url: https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles
    source_type: official_docs
    relevance: Microsoft’s guidance shows how a system can be split so core business logic evolves separately from UI and infrastructure.
    key_point: Business logic should live in its own part of the application so it can evolve independently.
  - source_title: Foundational concepts
    source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/micro-frontend-concepts.html
    source_type: official_docs
    relevance: AWS distinguishes merely modular systems from independently deployable systems, which helps avoid confusing modular architecture with microservices.
    key_point: A modular system can have encapsulated modules with interfaces without each module being independently deployable.
  - source_title: Module Assembly
    source_url: https://martinfowler.com/articles/module-assembly.html
    source_type: engineering_blog
    relevance: This explains modular programming as assembling modules through interfaces rather than letting parts depend directly on each other’s internals.
    key_point: Modules should interact through their public interfaces, not by reaching into each other’s details.
---

Modular architecture is a way of building software from separate parts that each have a clear job.

In practice, each module hides its inner details and talks to other modules through a small, clear interface. That makes the system easier to understand, test, and change.

The term matters because big systems become hard to fix when everything depends on everything else. Good modular architecture lets teams update one part without breaking the rest so often.

It is not the same as microservices. A system can be modular and still run as one application. It is also not just tidy folders in a codebase. Real modularity means the parts are actually separated in the design, not only in name.
