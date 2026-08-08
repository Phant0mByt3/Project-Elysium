# 0001 — Vision

# Elysium Vision

> *"Every journey begins with a single step. Every legend begins with a single player."*

---

# Vision Statement

Elysium is a fantasy MMORPG built on Unreal Engine.

It is not designed to be a mod or reskin of another game.

It is designed to be a completely standalone game built natively on Unreal Engine for its rendering, simulation, and networking.

Unreal Engine provides the technology.

Elysium provides the world.

---

# Mission

Create a living fantasy universe that players want to return to for years.

Every city should feel inhabited.

Every road should have a destination.

Every dungeon should have a story.

Every kingdom should have a history.

Every continent should feel like a different part of the world.

The player should feel like they are living in a real fantasy world, not sitting inside a game engine.

---

# Design Philosophy

Unreal Engine is the foundation.

Elysium is the experience.

Every design decision should support the MMORPG experience rather than default engine behaviour.

If a default engine behaviour improves immersion, it may remain.

If a default engine behaviour limits the experience, it should be redesigned or replaced.

---

# Unreal Engine as an Engine

Unreal Engine is used as a general-purpose game engine, the same way any AAA studio would use it.

It provides:

* Rendering
* Physics
* Networking
* World simulation
* Multiplayer
* Basic entity systems

Everything else is designed specifically for Elysium.

This includes:

* Character progression
* Combat
* Quests
* Economy
* NPCs
* Dialogue
* Reputation
* Classes
* Dungeons
* Raids
* World events
* Civilisation simulation

---

## Default Engine Mechanics

Default engine templates and behaviours are intentionally reviewed and redesigned to support the MMORPG experience.

The goal is not to remove mechanics for the sake of it, but to ensure every mechanic supports exploration, progression, immersion, and world integrity.

| Mechanic     | Status                | Reason                                      |
| ------------ | --------------------- | ------------------------------------------- |
| Building     | Restricted            | Preserve handcrafted world                  |
| Mining       | Profession/Quest Only | Controlled progression                      |
| Ender Pearls | Removed               | Prevent sequence breaking                   |
| Elytra       | Removed               | Bypasses exploration and level design       |
| TNT          | Removed               | Protect world integrity                     |
| Beds         | Custom Behaviour      | Respawn system tied to inns and checkpoints |
| Villagers    | Replaced              | Custom NPC system                           |
| Villages     | Replaced              | Handcrafted settlements                     |
| Hunger       | Custom or Removed     | Depends on gameplay design                  |
| XP Levels    | Replaced              | Character progression system                |

The handcrafted world always takes priority over sandbox freedom.

---

## World Design Philosophy

Elysium is not a procedurally generated sandbox explored through mining and digging.

Every part of the world exists because it serves a gameplay, visual, or narrative purpose.

Example:

```text
Visible Terrain
████████████████

Only where needed:
    Cave
████    ████

Unused underground:
Removed
```

Large underground cave systems are only created when they support:

* Quests
* Dungeons
* Mining professions
* Hidden locations
* World lore
* Secret exploration

If an underground area serves no purpose, it does not need to exist.

The world is designed, not randomly generated.

---

## Building at Scale

Elysium is designed around realistic, human-proportioned scale rather than a blocky, grid-based scale.

Cities should not resemble generic template settlements.

Instead, they should function as believable capitals with specialised districts.

Example:

```text
Capital City

├── Castle District
├── Noble Quarter
├── Market District
├── Harbour
├── Cathedral
├── Mage Academy
├── Slums
├── Military Barracks
├── Farms
└── Outer Villages
```

Every district should have its own:

* Architecture
* NPC population
* Economy
* Purpose
* Atmosphere
* Story

Cities should feel like places where thousands of people could realistically live.

---

## World Scale

Elysium consists of multiple handcrafted continents connected through a shared MMORPG infrastructure.

Example world sizes:

```text
Elysium

Valoria
≈ 12,000 × 12,000

Frostheim
≈ 10,000 × 10,000

Ashlands
≈ 8,000 × 8,000

Celestia
≈ 6,000 × 6,000

Dungeon Worlds
Hundreds of smaller handcrafted instances
```

Every continent operates as its own server instance while remaining part of one persistent universe.

This architecture allows:

* Larger environments
* Better performance
* Independent development
* Easier expansion
* Seamless long-term growth

Players should experience one connected world, while the technology quietly manages many specialised worlds behind the scenes.

---

# A Handcrafted Universe

Every continent is built by hand.

Every mountain is intentionally placed.

Every cave exists for a reason.

Every dungeon has purpose.

Every ruin tells part of the world's history.

The world is not procedurally generated during gameplay.

Players explore an authored universe rather than an infinite sandbox.

---

# Living Civilisation

The world exists independently of its players.

Cities continue operating.

NPCs follow routines.

Merchants travel between settlements.

Kingdoms function regardless of player activity.

Guards patrol.

Citizens work.

Taverns become busy at night.

Festivals occur throughout the year.

The world should feel alive even if no player is nearby.

---

# Exploration

Exploration is one of the core pillars of Elysium.

Players should constantly discover:

* Hidden caves
* Ancient temples
* Forgotten ruins
* Secret passages
* World bosses
* Rare NPCs
* Dynamic encounters
* Hidden treasures

Curiosity should always be rewarded.

---

# Scale

Elysium is designed around large handcrafted environments.

Players should experience:

* Massive continents
* Towering mountain ranges
* Dense forests
* Large cities
* Deep valleys
* Ancient kingdoms
* Vast oceans

The world should feel enormous.

Distant landmarks should inspire players to travel rather than simply teleport.

---

# Technology Philosophy

The player experiences one seamless universe.

Internally, Elysium operates as multiple connected server instances.

Each continent, dungeon, raid, and event may operate independently while sharing a central backend.

This architecture allows the world to continue growing without technical limitations.

---

# Dedicated Client

Elysium uses its own launcher and client.

The client provides:

* Controlled game version
* Required modifications
* Resource management
* Custom user interface
* Custom visual effects
* Long-term compatibility

Players launch Elysium directly — there is no separate base game to launch.

---

# Long-Term Development

Elysium is designed to grow for many years.

Development includes:

* New continents
* New kingdoms
* New classes
* New professions
* New stories
* New raids
* New world events
* Major expansions

The world should always have another adventure waiting beyond the horizon.

---

# Final Vision

The greatest compliment Elysium can receive is not:

> "This is an amazing MMORPG."

It is:

> "I forgot this was built in a game engine at all."

When players stop seeing blocks and begin seeing kingdoms, legends, civilizations, and adventures, Elysium has achieved its purpose.
