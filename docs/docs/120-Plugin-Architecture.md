# 120 — Plugin Architecture

## Overview
The Elysium server runs on Paper (Java) as a modular collection of purpose-built plugins rather than one monolithic codebase, per the README's technology stack (Java, Paper, PostgreSQL, Gradle).

## Design Principles
* **Modularity** — each major game system (classes, quests, economy, guilds, PvP) lives in its own plugin module with a clearly defined API surface, so systems can be developed, tested, and updated independently.
* **Shared Core Library** — common utilities (data models, event bus, database access layer) live in a shared core plugin that all feature plugins depend on, avoiding duplicated logic.
* **Event-Driven Communication** — plugins communicate primarily through a custom event bus layered on top of Paper's event system, keeping modules decoupled.

## Module Breakdown (illustrative)
* `elysium-core` — shared data models, database access, event bus.
* `elysium-combat` — combat resolution, stats, status effects ([44-Combat.md](44-Combat.md), [45-Stats.md](45-Stats.md), [47-Status-Effects.md](47-Status-Effects.md)).
* `elysium-quests` — quest state machine ([70-Quests.md](70-Quests.md)).
* `elysium-economy` — currency, auction house, trading, mail, banking ([100-Economy.md](100-Economy.md) through [106-Banking.md](106-Banking.md)).
* `elysium-social` — guilds, parties ([80-Guilds.md](80-Guilds.md), [81-Parties.md](81-Parties.md)).
* `elysium-pvp` — arenas, territory control ([85-Arenas.md](85-Arenas.md), [86-Territory-Control.md](86-Territory-Control.md)).

## Data Persistence
All plugins persist state through the shared PostgreSQL database described in [121-Database.md](121-Database.md), never through flat files, to support the scalable architecture goal in the README.
