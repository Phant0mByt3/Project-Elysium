# 81 — Parties

## Overview
Parties are temporary, small-group formations (up to 5 players) used for questing and dungeon content ([16-Dungeons.md](16-Dungeons.md)), distinct from the larger, persistent guild structure ([80-Guilds.md](80-Guilds.md)) and raid groups ([82-Raiding.md](82-Raiding.md)).

## Core Features
* **Party Formation** — invite directly or form automatically via the Dungeon Finder ([83-Dungeon-Finder.md](83-Dungeon-Finder.md)).
* **Shared Quest Credit** — party members near each other receive credit for shared kill/objective quests, reducing competition for tags.
* **Loot Rules** — need/greed/pass or personal loot, set by the party leader (see [53-Loot.md](53-Loot.md)).
* **Party Chat & Markers** — a dedicated chat channel and map/world ping markers for coordination.

## Cross-Faction Restriction
Like guilds, parties are single-faction only at launch, consistent with the faction-based PvP structure ([84-PvP.md](84-PvP.md)) — a possible future cross-faction party exception is noted for event content in [05-Future-Plans.md](05-Future-Plans.md).

## Design Rules
Party-scaling for open-world content (quest mobs, mini-events) should scale enemy difficulty up gracefully with party size, so grouping is always a net positive, never a "trivializes everything" or "not worth the split rewards" tradeoff.
