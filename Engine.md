# Elysium Engine Architecture

## Purpose

This document defines the technical foundation of Elysium.

It describes the server software, client architecture, networking, instance management, performance settings, databases, and core technologies required to operate a large-scale Minecraft MMORPG.

This file acts as the technical blueprint for the entire project.

---

# Engine Philosophy

Elysium is not designed as a traditional Minecraft server.

It is designed as a standalone MMORPG experience built using Minecraft technology as the foundation.

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

## Purpur

Purpose:

High-performance Minecraft server foundation with advanced configuration options.

Advantages:

* Paper compatibility
* Bukkit plugin support
* Additional performance settings
* More control over gameplay behaviour
* Large plugin ecosystem

---

## Alternative

## Paper

Purpose:

Stable and reliable server foundation.

Advantages:

* Strong community support
* Wide plugin compatibility
* Excellent optimisation
* Reliable for production environments

---

## Future Possibility

Custom Elysium Server Fork

Purpose:

A dedicated server engine based on Minecraft server technology.

Possible improvements:

* Custom chunk management
* Improved NPC processing
* MMO-specific optimisations
* Custom networking
* Better world streaming
* Reduced unnecessary Minecraft systems

---

# Engine Version Target

## Current Target

```text
Minecraft:
1.21.1

Server:
Purpur 1.21.1

Java:
21
```

Reason:

Chosen for:

* Long-term stability
* Plugin compatibility
* Client modification support
* Reliable development environment

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

                    Velocity Proxy

                           |

        ┌──────────────────┼──────────────────┐

        ↓                  ↓                  ↓

  Valoria Server    Frostheim Server    Dungeon Server

        ↓                  ↓                  ↓

      World             World              Instance

```

---

# Proxy System

## Velocity

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

Velocity Proxy

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

Elysium will use a dedicated client.

The client replaces the need for public Minecraft launcher compatibility.

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
├── Mod Management
├── Resource Pack Management
├── Shader Configuration
├── News
├── Patch Notes
└── Server Connection
```

---

# Elysium Client

Required environment:

```text
Elysium Client

├── Fixed Minecraft Version
├── Required Mods
├── Custom UI
├── Custom Rendering
├── Resource Packs
├── Models
├── Sounds
└── Client Features
```

---

# Client Technologies

Possible base:

* Fabric
* NeoForge

Used for:

* Client-side features
* Visual improvements
* Custom interfaces
* Additional rendering systems

---

# Visual Engine

## Distant Horizons

Purpose:

Large-scale world visibility.

Features:

* Long-distance terrain rendering
* Large landscape views
* Open-world feeling

---

## Shader Support

Possible:

* Iris-compatible shaders
* Custom Elysium shader profiles

Used for:

* Atmosphere
* Lighting
* Weather
* Environment effects

---

# World Management

Worlds are handcrafted and pre-generated.

The server does not generate new terrain during gameplay.

Benefits:

* Reduced lag
* Stable performance
* Consistent world design
* Better exploration experience

Tools:

* WorldPainter
* WorldEdit
* Chunk pre-generation tools

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

# Plugin Architecture

Core plugin structure:

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

* Stable TPS
* Low latency
* Fast world transfers
* Minimal chunk lag
* Efficient NPC simulation

---

# Scaling Architecture

Early development:

```text
Single Machine

├── Velocity
├── Database
├── Multiple Worlds
└── Development Servers
```

---

Large scale:

```text
Multiple Machines

Machine 1:
Proxy + Authentication

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

# Future Engine Development

Possible future systems:

* Custom launcher
* Custom client
* Custom rendering engine
* AI-driven NPC systems
* Advanced world simulation
* Custom networking layer
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
