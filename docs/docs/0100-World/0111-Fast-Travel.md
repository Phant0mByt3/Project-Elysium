# 0111 — Fast Travel

## Overview
Fast travel systems unlock progressively as players explore, rewarding exploration (Pillar 1, [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md)) rather than being available from the start.

## Waypoint Shrines
Physical structures placed at regional landmarks and city centers. Walking within range of an unvisited shrine unlocks it permanently for that character. Once unlocked, players can teleport between any two discovered shrines from a map UI, for a small Aurum cost ([1001-Currency.md](../1000-Economy/1001-Currency.md)) that scales with distance.

## Flight Routes
NPC-piloted flight paths connecting major cities and key waypoints, more befitting the fantasy tone for cross-continent travel. Distinct from the future player-flying-mount system noted in [0901-Mounts.md](../0900-Player-Systems/0901-Mounts.md).

## Hearth / Recall
Each character can bind a "Hearthstone" recall point at any city, usable on a cooldown to return there instantly — the primary "get back to civilization" safety valve.

## Restrictions
* Fast travel is disabled inside instances (dungeons/raids) and most active world events, to preserve the tension of those systems.
* Newly discovered shrines in contested Vethmoor territory can be temporarily locked by faction control shifts — see [0806-Territory-Control.md](../0800-Multiplayer/0806-Territory-Control.md).

## Technical Notes
Waypoint state is stored per-character server-side; see [1201-Database.md](../1200-Technical/1201-Database.md) for schema ownership.
