# Elysium Engine Architecture

## Purpose

This document defines the technical foundation of Elysium.

It describes the server software, network architecture, instance management, performance settings, databases, proxies, and core technologies required to operate a large-scale Minecraft MMORPG.

This file acts as the technical blueprint for the entire project.

---

# Engine Philosophy

Elysium is not designed as a traditional Minecraft server.

It is designed as a distributed MMORPG platform built using Minecraft as the world engine.

The goal:

* Multiple connected worlds
* Independent server instances
* Persistent player progression
* Large handcrafted environments
* MMO-style systems
* Expandable architecture

The player should experience:

> One massive world.

The technology should operate as:

> Many connected worlds.

---

# Server Engine

## Primary Server Software

Recommended:

## Purpur

Purpose:

* High performance Minecraft server
* Paper compatibility
* Additional optimisation settings
* More gameplay configuration options

Advantages:

* Supports Bukkit plugins
* Supports Paper plugins
* More configurable than Paper
* Better control over entity behaviour

---

## Alternative

## Paper

Purpose:

Stable foundation for production servers.

Advantages:

* Large plugin ecosystem
* Strong community support
* Reliable performance
* Good optimisation compared to Vanilla

---

## Possible Future Options

Custom server fork:

Purpose:

For extreme optimisation and custom Elysium features.

Possible improvements:

* Custom chunk loading
* Better NPC handling
* Custom networking
* MMO-specific optimisations

---

# Server Architecture

Elysium uses a multi-instance structure.

```text
                    Elysium Network

                         Player

                           |
                           ↓

                    Proxy Layer

                           |
        ┌──────────────────┼──────────────────┐

        ↓                  ↓                  ↓

  Valoria Server    Frostheim Server    Dungeon Server

        ↓                  ↓                  ↓

      World             World              Instance

```

---

# Proxy System

## Recommended Proxy

## Velocity

Purpose:

Handles player connections and server transfers.

Responsibilities:

* Authentication
* Routing players
* Server switching
* Load balancing
* Network security

Example:

```text
Player joins

↓

Velocity Proxy

↓

Login Server

↓

Starting Area Server

↓

Open World Server

```

---

# Server Types

## Login Server

Purpose:

First connection point.

Features:

* Authentication
* Character selection
* Updates
* Launcher verification

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

* Own server instance
* Own plugins
* Own loaded chunks
* Own NPCs
* Own events

---

## Dungeon Servers

Purpose:

Private player instances.

Examples:

```text
Crystal Caverns

Player Party

↓

Dungeon Instance

↓

Boss Fight

↓

Rewards Saved

↓

Instance Closed

```

---

## Event Servers

Purpose:

Temporary content.

Examples:

* World bosses
* Seasonal events
* Special expansions
* PvP events

---

# Server Settings

## View Distance

Recommended:

```yaml
view-distance: 8-12
```

Reason:

Players use Distant Horizons for extreme viewing distances.

Server only handles nearby chunks.

---

## Simulation Distance

Recommended:

```yaml
simulation-distance: 6-8
```

Controls:

* Mob AI
* Redstone
* Entity updates

---

## Entity Limits

Important for cities.

Settings:

* Limit unnecessary mobs
* Control villager AI
* Reduce inactive entity processing

---

## Chunk Management

Requirements:

* Pre-generated worlds
* Chunk caching
* Controlled loading
* World border management

Tools:

* Chunky
* Custom world generation tools

---

# Client Technology

## Required Mods

Possible client pack:

```text
Client

├── Fabric/NeoForge
├── Distant Horizons
├── Sodium
├── Iris Shaders
├── Custom UI
├── Resource Pack
└── Elysium Client Systems
```

---

# Visual Engine

## Distant Horizons

Purpose:

Large-scale world visibility.

Allows:

* Seeing cities from kilometres away
* Large mountain views
* Open-world feeling

---

## Shaders

Possible:

* Iris compatible shaders
* Custom Elysium shader profile

Used for:

* Atmosphere
* Lighting
* Weather
* Environment

---

# Backend Architecture

Central systems must not depend on one server.

Example:

```text
Database

Player Data

├── Character
├── Inventory
├── Skills
├── Quests
├── Reputation
├── Achievements
└── Currency

```

---

# Database

Possible:

## PostgreSQL

Recommended for:

* Large player counts
* Complex data
* Reliability

---

## Redis

Used for:

* Temporary data
* Caching
* Fast communication

---

# Server Communication

Possible technologies:

* Redis messaging
* Plugin messaging channels
* Custom API

Example:

```text
Valoria Server

Player completes quest

↓

Backend Database

↓

Player enters Frostheim

↓

Progress loaded

```

---

# Plugin Architecture

Core plugins:

```text
Elysium-Core

├── Player System
├── Character System
├── Quest System
├── Economy System
├── Faction System
├── Combat System
├── World Transfer
└── API
```

---

# Performance Goals

Target:

## Stable gameplay

* Low latency
* High TPS
* Minimal chunk lag
* Fast server transfers

---

# Scaling Plan

Early:

```text
1 Machine

├── Proxy
├── Database
├── Several Worlds
```

---

Large Scale:

```text
Multiple Machines

Machine 1:
Proxy + Login

Machine 2:
World Servers

Machine 3:
Dungeon Servers

Machine 4:
Database

Machine 5:
Storage
```

---

# Future Engine Development

Possible custom systems:

* Custom launcher
* Custom client
* Custom rendering features
* Custom networking layer
* AI NPC management
* Dynamic world simulation

---

# Final Goal

The Elysium Engine should allow:

* Unlimited expansion
* New continents
* New worlds
* New gameplay systems
* Long-term development

The engine should not limit the world.

The engine should allow the world to grow.
