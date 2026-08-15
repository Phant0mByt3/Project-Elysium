# 0111 — Fast Travel

**Category:** World
**Status:** Living Document
**Related:** [0110-Travel.md](0110-Travel.md) · [0112-Maps.md](0112-Maps.md)

---

## 1. Overview

Fast travel lets players teleport between discovered waypoints once they've physically visited them, balancing convenience for repeat trips against the exploration incentive described in [0110-Travel.md](0110-Travel.md).

## 2. Waypoint Network

Waypoints are placed at every major city, most villages, and select landmarks. A waypoint must be physically discovered (visited once) before it appears on the fast travel map.

## 3. Cost and Cooldown

Fast travel costs a small amount of currency ([1001-Currency.md](../1000-Economy/1001-Currency.md)) scaled to distance, functioning as a minor economy sink (see [1010-Currency-Sinks.md](../1000-Economy/1010-Currency-Sinks.md)). There is no cooldown, but combat lockout prevents use while flagged in combat.

## 4. Mage Portal Network

At higher levels, players unlock access to a mage-run portal network offering near-instant travel between major cities, including cross-continent travel between Solmere and Ironpeak Hold/Ashka Vor, unlocked through a mid-game main story quest.

## 5. Restrictions

* Fast travel is disabled inside dungeons and raids (see [0106-Dungeons.md](0106-Dungeons.md), [0107-Raids.md](0107-Raids.md)).
* Fast travel to a continent the player has not yet unlocked via story progression is not possible, preserving the intended pacing of [0101-Continents.md](0101-Continents.md).

## 6. UI Integration

The fast travel map is accessed via the world map interface ([0112-Maps.md](0112-Maps.md)) and shows discovered waypoints with distance-based cost previewed before confirming travel.
