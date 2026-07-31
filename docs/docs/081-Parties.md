# 81 — Parties

## Overview
Parties are temporary, small-group formations (up to 5 players) used for questing and dungeon content ([016-Dungeons.md](016-Dungeons.md)), distinct from the larger, persistent guild structure ([080-Guilds.md](080-Guilds.md)) and raid groups ([082-Raiding.md](082-Raiding.md)).

## Core Features
* **Party Formation** — invite directly or form automatically via the Dungeon Finder ([083-Dungeon-Finder.md](083-Dungeon-Finder.md)).
* **Shared Quest Credit** — party members near each other receive credit for shared kill/objective quests, reducing competition for tags.
* **Loot Rules** — need/greed/pass or personal loot, set by the party leader (see [053-Loot.md](053-Loot.md)).
* **Party Chat & Markers** — a dedicated chat channel and map/world ping markers for coordination.

## Cross-Faction Restriction
Like guilds, parties are single-faction only at launch, consistent with the faction-based PvP structure ([084-PvP.md](084-PvP.md)) — a possible future cross-faction party exception is noted for event content in [005-Future-Plans.md](005-Future-Plans.md).

## Design Rules
Party-scaling for open-world content (quest mobs, mini-events) should scale enemy difficulty up gracefully with party size, so grouping is always a net positive, never a "trivializes everything" or "not worth the split rewards" tradeoff.
