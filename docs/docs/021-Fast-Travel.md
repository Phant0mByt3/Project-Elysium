# 21 — Fast Travel

## Overview
Fast travel systems unlock progressively as players explore, rewarding exploration (Pillar 1, [002-Core-Pillars.md](002-Core-Pillars.md)) rather than being available from the start.

## Waypoint Shrines
Physical structures placed at regional landmarks and city centers. Walking within range of an unvisited shrine unlocks it permanently for that character. Once unlocked, players can teleport between any two discovered shrines from a map UI, for a small Aurum cost ([101-Currency.md](101-Currency.md)) that scales with distance.

## Flight Routes
NPC-piloted flight paths connecting major cities and key waypoints, more befitting the fantasy tone for cross-continent travel. Distinct from the future player-flying-mount system noted in [091-Mounts.md](091-Mounts.md).

## Hearth / Recall
Each character can bind a "Hearthstone" recall point at any city, usable on a cooldown to return there instantly — the primary "get back to civilization" safety valve.

## Restrictions
* Fast travel is disabled inside instances (dungeons/raids) and most active world events, to preserve the tension of those systems.
* Newly discovered shrines in contested Vethmoor territory can be temporarily locked by faction control shifts — see [086-Territory-Control.md](086-Territory-Control.md).

## Technical Notes
Waypoint state is stored per-character server-side; see [121-Database.md](121-Database.md) for schema ownership.
