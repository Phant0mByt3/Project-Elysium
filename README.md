# Project-Elysium
An MMORPG built on Minecraft

# Project Elysium

### "An MMORPG built on Minecraft"

---

# 1. Vision

**Project Name**

> Elysium (working title)

**Genre**

* Open World MMORPG
* Story-driven
* PvE-first
* Optional PvP
* Handcrafted world
* Persistent online world
* Live-service updates
* Custom launcher
* Modded client
* Plugin-driven server

**Goal**

Create a game where players forget they're playing Minecraft after the first few minutes.

This is not a survival server.

This is an MMO that uses Minecraft as its engine.

---

# 2. Core Pillars

### Massive World

* 10 handcrafted continents
* 70+ regions
* No procedural generation
* Every cave and structure is intentional

---

### RPG Progression

* Classes
* Talent trees
* Skills
* Levels
* Dungeons
* Raids
* Professions
* Reputation
* Factions

---

### Living World

* World events
* Dynamic NPCs
* Seasons
* Economy
* Housing
* Guilds
* PvP territories

---

### Accessibility

The launcher installs everything automatically.

Players click **Play** and they're in.

---

# 3. Technology Stack

## Server

* Java 21
* Paper (or a high-performance Paper fork if it still meets your needs)
* Gradle
* Kotlin or Java for plugins (Kotlin can reduce boilerplate, Java has the larger plugin ecosystem)

## Client

Fabric

Reason:

* Lightweight
* Excellent performance mods
* Strong API
* Easier to distribute a curated modpack

---

# 4. Launcher

Your launcher should feel like the game's launcher, not Minecraft's.

## Written in

Since you're already comfortable with Python and PyQt:

* Python
* PyQt6

Later, if you ever want a native executable with lower memory usage, you could rewrite it in C# or another desktop framework, but Python is perfectly fine to start.

---

## Features

### Login

* Username/password
* OAuth later
* Remember login

---

### News

Latest updates

Maintenance

Patch notes

Events

---

### Downloader

Automatically downloads:

* Fabric Loader
* Java (optional bundled runtime)
* Mods
* Resource packs
* Shader packs (optional)
* Music packs
* Maps if needed

---

### Auto Update

Checks version manifest.

Downloads only changed files.

No full reinstall.

---

### Integrity

SHA-256 verification.

Re-download corrupted files.

---

### Settings

Memory allocation

Graphics presets

Language

Audio

Accessibility

---

### Screenshots

Gallery

---

### Character Select

Later

---

# 5. Server Architecture

```text
Launcher
      │
      ▼
Login API
      │
      ▼
Gateway
      │
      ▼
Lobby
      │
      ▼
World Servers
      │
      ├── Valoria
      ├── Frostheim
      ├── Sylvaris
      ├── Solkara
      └── ...
            │
            ▼
Dungeon Servers
            │
            ▼
Raid Servers
            │
            ▼
Database
```

---

# 6. Database

PostgreSQL is a great fit for a large MMO.

Tables for:

* Accounts
* Characters
* Inventory
* Guilds
* Quests
* Skills
* Stats
* Reputation
* Friends
* Mail
* Auction House
* Housing
* World State
* Achievements

---

# 7. Plugin Ecosystem

```
Elysium-Core

Accounts

Characters

Combat

Stats

Classes

Skills

Talents

Quests

NPCs

Dialogue

AI

Items

Equipment

Crafting

Professions

Mounts

Pets

Housing

Guilds

Parties

Friends

Mail

Marketplace

Auction House

Bank

Dungeons

Raids

World Events

Reputation

Factions

PvP

Achievements

Leaderboards

Cosmetics

API

Developer Tools
```

---

# 8. Client Mods

These are the kinds of mods I'd consider. Check they're available for the Minecraft version you choose before locking in your stack.

### Performance

* Sodium
* Lithium
* FerriteCore
* Entity Culling
* ImmediatelyFast

---

### Visual

* Distant Horizons
* Iris Shaders
* Continuity

---

### Quality of Life

* Mod Menu
* Simple Voice Chat (optional)
* EMI (if you introduce crafting systems)

---

### Custom

You'll probably write your own client mods for:

* Quest UI
* Skill tree UI
* Party UI
* Dungeon finder
* World map
* Compass
* Cinematics
* Character sheet
* Cosmetics
* Notifications
* Minimap integration (or a custom map)

---

# 9. Resource Pack

One mandatory resource pack.

Contains:

* Custom GUI
* Icons
* Weapons
* Armor
* Music
* Ambient sounds
* Fonts
* Models
* Animations

---

# 10. Soundtrack

Every continent has:

* Ambient music
* Combat music
* Dungeon music
* Boss music
* City music
* Night music

The launcher downloads updates as the soundtrack grows.

---

# 11. Continents

* Valoria
* Frostheim
* Sylvaris
* Solkara
* Khor'Duun
* Aetheris
* Noxmoor
* Shattered Sea
* Void Expanse
* Celestial Dominion

---

# 12. Factions

* Kingdom of Valoria
* Sylvan Covenant
* Iron Dominion

Neutral:

* Merchants' Consortium
* Adventurers' Guild
* Ancient Order

Hostile:

* Void Legion
* Cult of Ash
* Crimson Brotherhood

---

# 13. Classes

Tank

* Guardian
* Paladin

Melee

* Warrior
* Berserker
* Assassin

Magic

* Mage
* Druid
* Necromancer

Ranged

* Ranger
* Hunter

Support

* Cleric
* Bard

---

# 14. Endgame

* Mythic Dungeons
* Raids
* World Bosses
* Guild Wars
* Territory Control
* Housing
* Legendary Equipment
* Seasonal Events
* Festivals
* PvP Arenas

---

# 15. Update System

I'd avoid changing the world constantly. Instead, expand it.

Example roadmap:

### Version 1.0

* Valoria
* Level 1-20

---

### Version 1.1

* Goblin Raid
* New dungeon
* Mounts

---

### Version 1.2

* Housing
* Fishing
* Guilds

---

### Version 2.0

* Frostheim
* New class
* New raid

---

### Version 3.0

* Solkara
* Desert expansion
* Profession overhaul

---

### Version 4.0

* Aetheris
* Flying mounts
* Sky dungeons

Each expansion feels like the world is growing, similar to major MMORPG releases.

---

# 16. Development Roadmap

## Phase 0 (2-4 weeks)

* Project documentation
* Git repository
* Coding standards
* Art direction
* Naming conventions
* Technology decisions
* Basic launcher prototype

## Phase 1 (2-3 months)

* Launcher
* Authentication
* Core plugin framework
* Database
* Character system
* Combat prototype
* Basic networking

## Phase 2 (2-4 months)

* Classes
* Skills
* Quests
* NPC framework
* Inventory
* Items
* First playable region of Valoria

## Phase 3 (3-6 months)

* World building
* Dungeons
* Boss mechanics
* Cities
* Factions
* Professions
* Economy

## Phase 4 (ongoing)

* Polish
* Content
* Optimisation
* Closed alpha
* Balancing
* Beta
* Launch

---

# 17. Team (Future)

If the project grows, you could divide responsibilities:

* Lead Developer
* Gameplay Programmer
* Backend Developer
* World Builder(s)
* Terrain Artist(s)
* Builder(s)
* Quest Designer
* Writer / Lore Designer
* Composer / Sound Designer
* Texture & Model Artist
* UI Designer
* QA Testers
* Community Manager

---

## One recommendation before you start

Pick a Minecraft version and stay on it for a long time. Chasing every new Minecraft release can consume months of work because mods, plugins, and APIs all need to catch up.

For a project that's expected to take a year or more, stability is usually more valuable than having the newest vanilla features. You can always build your own mechanics and content, while keeping the underlying platform stable until you're ready for a major engine upgrade.
