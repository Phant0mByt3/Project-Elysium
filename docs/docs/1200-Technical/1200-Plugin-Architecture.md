# 1200 — Plugin Architecture

## Overview
The Elysium server runs on Unreal Engine (C++) as a modular collection of purpose-built gameplay modules rather than one monolithic codebase, per the README's technology stack (C++, Unreal Engine dedicated server, PostgreSQL, Unreal Build Tool).

## Design Principles
* **Modularity** — each major game system (classes, quests, economy, guilds, PvP) lives in its own plugin module with a clearly defined API surface, so systems can be developed, tested, and updated independently.
* **Shared Core Library** — common utilities (data models, event bus, database access layer) live in a shared core plugin that all feature plugins depend on, avoiding duplicated logic.
* **Event-Driven Communication** — plugins communicate primarily through a custom event bus layered on top of Unreal Engine's gameplay event system, keeping modules decoupled.

## Module Breakdown (illustrative)
* `elysium-core` — shared data models, database access, event bus.
* `elysium-combat` — combat resolution, stats, status effects ([0401-Combat.md](../0400-Gameplay/0401-Combat.md), [0304-Stats.md](../0300-Characters/0304-Stats.md), [0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)).
* `elysium-quests` — quest state machine ([0700-Quests.md](../0700-Quests/0700-Quests.md)).
* `elysium-economy` — currency, auction house, trading, mail, banking ([1000-Economy.md](../1000-Economy/1000-Economy.md) through [1006-Banking.md](../1000-Economy/1006-Banking.md)).
* `elysium-social` — guilds, parties ([0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md), [0801-Parties.md](../0800-Multiplayer/0801-Parties.md)).
* `elysium-pvp` — arenas, territory control ([0805-Arenas.md](../0800-Multiplayer/0805-Arenas.md), [0806-Territory-Control.md](../0800-Multiplayer/0806-Territory-Control.md)).

## Data Persistence
All plugins persist state through the shared PostgreSQL database described in [1201-Database.md](1201-Database.md), never through flat files, to support the scalable architecture goal in the README.
