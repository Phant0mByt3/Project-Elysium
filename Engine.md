# Elysium Engine Architecture

## Purpose

This document defines the technical foundation of Elysium.

It describes the server software, client architecture, networking, instance management, performance settings, databases, and core technologies required to operate a large-scale standalone MMORPG.

This file acts as the technical blueprint for the entire project.

---

# Engine Philosophy

Elysium is a fully standalone MMORPG built natively on Unreal Engine.

There is no base game underneath it — Elysium is the whole game, from rendering to networking to gameplay systems.

The goal:

* Multiple connected worlds
* Dedicated game client
* Persistent player progression
* Large handcrafted environments
* MMO-style systems
* Expandable architecture

The player should experience:

> One massive fantasy universe.

The technology should operate as:

> Many connected worlds running through a shared ecosystem.

---

# Server Engine

## Primary Server Software

Recommended:

## Unreal Engine Dedicated Server

Purpose:

High-performance, headless build of the Unreal Engine game server, compiled directly from the Elysium codebase.

Advantages:

* Full control over gameplay code (C++ and Blueprints)
* No dependence on a third-party game's server binary
* Native replication and networking stack built for the same engine as the client
* Deep profiling and optimisation tooling (Unreal Insights)
* Direct access to the same physics, animation, and simulation systems as the client

---

## Alternative

## Third-Party Backend Services

Purpose:

Managed services layered around the dedicated server for account, matchmaking, and orchestration needs.

Advantages:

* Reduces custom infrastructure work for solved problems (auth, matchmaking, container orchestration)
* Battle-tested at scale
* Frees the team to focus on gameplay-specific backend systems

---

## Future Possibility

Custom Elysium Server Fork / Framework

Purpose:

A dedicated, purpose-built server framework layered on top of the Unreal Engine dedicated server.

Possible improvements:

* Custom world-partition and level-streaming management
* Improved NPC and AI processing at scale
* MMO-specific optimisations (entity LOD, interest management)
* Custom networking and replication graph tuning
* Better world streaming across zone boundaries
* Reduced overhead from unused engine subsystems

---

# Engine Version Target

## Current Target

```text
Engine:
Unreal Engine 5.4 (LTS)

Server:
Unreal Engine Dedicated Server (Linux, headless)

Language:
C++ / Blueprints
```

Reason:

Chosen for:

* Long-term stability (LTS branch)
* First-class support for large open worlds (World Partition, Nanite, Lumen)
* Strong networking and replication framework out of the box
* Reliable development environment with mature tooling

The engine version should remain fixed during major development periods.

---

# Network Architecture

Elysium uses a multi-instance server structure.

The player sees one connected world.

The backend operates multiple independent servers.

```text
                     Elysium Client

                           |

                           ↓

                     Elysium Gateway

                           |

        ┌──────────────────┼──────────────────┐

        ↓                  ↓                  ↓

  Valoria Server    Frostheim Server    Dungeon Server

        ↓                  ↓                  ↓

      World              World             Instance

```

---

# Proxy System

## Elysium Gateway

Purpose:

Handles communication between the Elysium Client and server instances.

Responsibilities:

* Player routing
* Server transfers
* Authentication handling
* Load distribution
* Network security

Example:

```text
Player launches Elysium

↓

Authentication

↓

Elysium Gateway

↓

Login Server

↓

World Server

```

---

# Server Types

## Login Server

Purpose:

First connection point.

Functions:

* Account authentication
* Character loading
* Client verification
* News and announcements

---

## World Servers

Purpose:

Permanent playable areas.

Examples:

```text
Valoria
Frostheim
Ashlands
Celestia
```

Each world has:

* Independent server instance
* Own terrain
* Own NPC systems
* Own events
* Own quests
* Own simulation systems

---

## Dungeon Servers

Purpose:

Private or group-based instances.

Example:

```text
Party enters dungeon

↓

Dungeon Server created

↓

Players complete objectives

↓

Rewards saved

↓

Instance removed
```

Used for:

* Dungeons
* Raids
* Trials
* Boss encounters

---

## Event Servers

Purpose:

Temporary content.

Examples:

* World bosses
* Seasonal events
* Expansion events
* Special encounters

---

# Client Architecture

Elysium uses a fully custom Unreal Engine client. There is no reliance on any other game's launcher, account system, or client binary.

---

# Elysium Launcher

Purpose:

Controls the complete player experience.

Functions:

```text
Elysium Launcher

├── Authentication
├── Game Updates
├── File Verification
├── Content Pack Management
├── Graphics Configuration
├── News
├── Patch Notes
└── Server Connection
```

---

# Elysium Client

Required environment:

```text
Elysium Client

├── Unreal Engine 5.4 Runtime
├── Custom Gameplay Modules
├── Custom UI (UMG)
├── Custom Rendering Pipeline
├── Content Packs
├── Models
├── Sounds
└── Client Features
```

---

# Client Technologies

Base:

* Unreal Engine 5.4 (C++ and Blueprints)

Used for:

* Client-side features
* Visual improvements
* Custom interfaces
* Additional rendering systems

---

# Visual Engine

## World Partition & Nanite

Purpose:

Large-scale world visibility and streaming.

Features:

* Long-distance terrain rendering via Nanite virtualized geometry
* Automatic level streaming and HLOD generation via World Partition
* Open-world feeling without manual chunk management

---

## Lighting & Rendering

Built-in Unreal Engine systems:

* Lumen (dynamic global illumination and reflections)
* Niagara (VFX, weather, particle systems)
* Custom post-process materials and volumes

Used for:

* Atmosphere
* Lighting
* Weather
* Environment effects

---

# World Management

Worlds are handcrafted and pre-built inside the Unreal Editor.

The server does not generate new terrain during gameplay.

Benefits:

* Reduced runtime cost
* Stable performance
* Consistent world design
* Better exploration experience

Tools:

* Unreal Engine Landscape system
* Unreal Engine Modeling Tools
* World Partition streaming-cell pre-generation

---

# Backend Architecture

All important player data is stored separately from individual worlds.

Example:

```text
Database

Player

├── Character
├── Inventory
├── Equipment
├── Skills
├── Quests
├── Reputation
├── Achievements
├── Currency
└── Progression
```

---

# Database

Recommended:

## PostgreSQL

Used for:

* Player accounts
* Character data
* World data
* Economy
* Progression

---

## Redis

Used for:

* Temporary data
* Server communication
* Caching
* Real-time systems

---

# Gameplay Module Architecture

Core module structure:

```text
Elysium-Core

├── Player System
├── Character System
├── Quest System
├── Combat System
├── Economy System
├── Faction System
├── NPC System
├── World Transfer
├── Instance Management
└── API
```

---

# Performance Goals

Target:

* Stable server tick rate
* Low latency
* Fast world transfers
* Minimal streaming hitches
* Efficient NPC simulation

---

# Scaling Architecture

Early development:

```text
Single Machine

├── Elysium Gateway
├── Database
├── Multiple Worlds
└── Development Servers
```

---

Large scale:

```text
Multiple Machines

Machine 1:
Gateway + Authentication

Machine 2:
World Servers

Machine 3:
Dungeon Instances

Machine 4:
Database

Machine 5:
Storage + Backups
```

---

# Client Platform

## Custom Assets

Elysium ships entirely with its own client assets.

All content is built directly into the Elysium client rather than relying on downloadable resource packs for another game.

Included assets may include:

* Models
* Textures
* Sounds
* Music
* UI
* Fonts
* Icons
* Animations

Benefits:

* Faster loading
* Better integration
* More reliable asset management
* Consistent visual experience

---

## Custom Main Menu

Elysium ships with its own fully custom main menu, built natively in UMG.

Example:

```text
+------------------------------------+
|            ELYSIUM                 |
|                                    |
|        [ Enter Elysium ]           |
|                                    |
|        Character Preview           |
|                                    |
|  Character Selection               |
|  Character Creation                |
|  Settings                          |
|  Exit                              |
+------------------------------------+
```

Features:

* Character selection
* Character creation
* Character preview
* News
* Patch notes
* Settings
* Server status

---

## Character Management

Character data is never stored locally.

Every login retrieves the latest character information from the central backend.

Stored server-side:

* Characters
* Inventory
* Equipment
* Skills
* Quests
* Achievements
* Reputation
* Currency
* Progression

Benefits:

* Centralised saves
* Cross-server persistence
* Reduced save manipulation
* Easier backups

---

# Security & Integrity

## Client Verification

Every connection performs an integrity check before entering the game.

Possible verification:

* Client version
* Required modules
* Missing files
* Modified files
* Asset validation
* Resource integrity

Players with modified or incomplete installations may be denied access.

---

## Server Authority

The client is responsible only for presentation.

The server is authoritative for all gameplay systems.

Server-controlled systems include:

* Combat
* Inventory
* Currency
* Character progression
* Quest progression
* NPC interactions
* Item generation
* Loot tables

No gameplay-critical information should be trusted from the client.

---

## Account System

Elysium uses its own first-party account system rather than depending on a third-party game platform account.

Requirements:

* Valid Elysium account
* Authentication through Elysium's own account services

No offline or unauthenticated accounts are supported.

Benefits:

* Full control over account security and moderation
* Secure account authentication
* Reduced abuse from unauthorised accounts

---

# Client Philosophy

The Elysium Client exists solely to play Elysium.

It is not a general-purpose engine sandbox or toolset.

Features:

- No Singleplayer sandbox mode
- No third-party server browser
- Fixed engine version
- Managed by the Elysium Launcher
- Automatic updates
- Automatic integrity verification
- Official Elysium servers only

---

# Future Engine Development

Possible future systems:

* Custom launcher enhancements
* Additional client rendering features
* AI-driven NPC systems
* Advanced world simulation
* Custom networking layer improvements
* Dynamic civilisation simulation

---

# Final Goal

The Elysium Engine should allow unlimited growth.

The engine must support:

* New continents
* New worlds
* New expansions
* New gameplay systems
* Long-term development

The engine should not limit the world.

The engine should allow the world to grow.