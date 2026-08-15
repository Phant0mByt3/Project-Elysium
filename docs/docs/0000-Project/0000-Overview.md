# 0000 — Overview

**Project:** Elysium MMORPG
**Category:** Project
**Status:** Living Document
**Related:** [0001-Vision.md](0001-Vision.md) · [0002-Core-Pillars.md](0002-Core-Pillars.md) · [0006-Documentation-Guide.md](0006-Documentation-Guide.md)

---

## 1. What is Project Elysium?

Project Elysium is a handcrafted MMORPG built natively on Unreal Engine, using it as a full rendering, physics, and simulation foundation rather than as a survival sandbox. Every continent, dungeon, city, and quest is hand-built by the design and building teams — nothing in the world is procedurally generated.

The player steps into **Elysium**, a fractured realm slowly being pieced back together eight centuries after a cataclysm known as the Sundering. They choose a race, a class, and a faction, and begin a persistent journey of exploration, story, combat, and community that is intended to run for years across expansions.

This document is the front door to the entire Game Design Document (GDD). Everything else in `docs/` builds on the premise established here.

---

## 2. The One-Sentence Pitch

> A handcrafted, story-driven MMORPG where two rival factions rebuild a shattered world — with the polish of a themepark MMO and the intimacy of a game built by people who love the genre.

---

## 3. Target Audience

* Players who grew up on classic themepark MMORPGs (World of Warcraft, Final Fantasy XIV, Guild Wars) and want that experience with modern, fully custom visuals.
* Sandbox-survival players looking for structured, story-driven progression rather than open survival.
* Roleplayers and worldbuilding enthusiasts drawn to a deep, internally consistent fantasy setting.
* Guild- and community-oriented players who enjoy raiding, PvP, and long-term server relationships.
* Solo and casual players who want a rich world to explore without being forced into mandatory group content to see it.

---

## 4. Overall Direction

Elysium is not "a survival game with quests bolted on." The UI, combat feel, progression curve, and world logic are designed first as an MMORPG, and Unreal Engine's fully custom 3D world-building tools are used as the canvas to build it. Survival mechanics (hunger, mining for its own sake, open-world griefing) are disabled or replaced by systems native to the genre: talent trees, gear scores, instanced dungeons, raid lockouts, and a driven main story.

This direction touches every discipline:

| Discipline | Default Engine Behaviour | Elysium Behaviour |
| --- | --- | --- |
| World | Procedural, player-editable terrain | Hand-authored continents, restricted terrain editing |
| Combat | Simple hit-based swings | Ability-driven combat with cooldowns, resource bars, and positioning |
| Progression | Gear/skill grind with no narrative frame | Leveling, talents, and gear tied to story and class identity |
| Social | Loose, unstructured multiplayer | Guilds, parties, raids, dungeon finder, factions |
| Economy | Player-crafted barter | Currency-driven economy with auction house, professions, sinks |

---

## 5. Core Fantasy

Players are not colonists surviving in a hostile wilderness. They are heroes of a world that used to be whole, walking through the wreckage of a golden age, deciding — through their faction choice and their actions — what kind of world gets rebuilt. Every zone, quest line, and piece of lore reinforces this: the world remembers what it lost, and the player is part of putting it back together.

---

## 6. What This Documentation Is

The `docs/` directory is the Game Design Document (GDD) for Project Elysium — the single source of truth for every system in the game, from lore to combat math to launcher architecture. See [0006-Documentation-Guide.md](0006-Documentation-Guide.md) for what each file covers, and [0001-Vision.md](0001-Vision.md) for the philosophy behind these decisions.

The GDD is organized into numbered top-level categories:

| Range | Category | Covers |
| --- | --- | --- |
| 0000 | Project | Vision, pillars, roadmap, team, glossary |
| 0100 | World | Continents, regions, cities, dungeons, travel |
| 0200 | Lore | Timeline, gods, factions, races, history, mythology |
| 0300 | Characters | Classes, skills, stats, leveling, customisation |
| 0400 | Gameplay | Combat, AI, difficulty, physics, tutorials |
| 0500 | Items | Equipment, crafting materials, enchanting, item rarity |
| 0600 | Professions | Gathering and crafting professions |
| 0700 | Quests | Quest types, structure, tracking, rewards |
| 0800 | Multiplayer | Guilds, parties, raids, PvP, dungeon finder |
| 0900 | Player Systems | Housing, mounts, pets, achievements, titles |
| 1000 | Economy | Currency, auction house, trading, sinks and sources |
| 1100 | Client | Launcher, UI/HUD, settings, accessibility |
| 1200 | Technical | Server architecture, database, networking, security |
| 1300 | Art | Visual style, models, textures, VFX, audio |
| 1400 | Development | Standards, workflows, testing, release process |
| 1500 | Expansions | Planned post-launch content |
| 2000 | Operations | Live service, moderation, community, analytics |
| 9000 | Future | Long-term ideas, unused concepts, mysteries |

---

## 7. What This Documentation Is Not

* It is not a marketing document — internal disagreements and unresolved design questions are recorded, not hidden.
* It is not a promise of feature scope to any external audience; see [0003-Roadmap.md](0003-Roadmap.md) for what is actually committed versus [0005-Future-Plans.md](0005-Future-Plans.md) for aspirational direction.
* It is not static — every file here is expected to be revised as systems are built and playtested. See [0004-Version-History.md](0004-Version-History.md) for how changes are logged once the game ships.

---

## 8. How to Read This Document Set

New contributors should read in this order:

1. This overview.
2. [0001-Vision.md](0001-Vision.md) — the "why" behind the game.
3. [0002-Core-Pillars.md](0002-Core-Pillars.md) — the design filter every feature passes through.
4. [0200-Lore.md](../0200-Lore/0200-Lore.md) — the world itself.
5. Their specific discipline's section (World, Characters, Technical, Art, etc.).

Everyone, regardless of discipline, is expected to have read documents 1–4 before contributing.

---

## 9. Living Document Notice

Elysium is currently in Pre-Production (see [0003-Roadmap.md](0003-Roadmap.md)). Numbers, names, and systems described throughout this GDD are the current best design intent and will shift as prototypes are built and playtested. Where a system is confirmed and stable, it is written in the present tense. Where it is still speculative, it is marked as such or lives in [0005-Future-Plans.md](0005-Future-Plans.md) / [9000-Future/](../9000-Future/) instead.
