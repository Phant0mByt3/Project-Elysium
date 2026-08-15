# 0803 — Dungeon Finder

**Category:** Multiplayer
**Status:** Living Document
**Related:** [0106-Dungeons.md](../0100-World/0106-Dungeons.md) · [0813-Group-Roles.md](0813-Group-Roles.md)

---

## 1. Overview

The Dungeon Finder is an automated grouping tool that matches players into a 5-player group for a chosen dungeon, removing the friction of manually assembling a group described in older MMORPGs, per Pillar 4 in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).

## 2. Queue Options

* **Specific Dungeon** — queue directly for a chosen dungeon at the appropriate difficulty.
* **Random Dungeon (Level-Appropriate)** — queue for any dungeon in the player's level range, typically with bonus rewards to incentivize flexibility.
* **Heroic/Mythic Queue** — max-level queue options for Heroic difficulty (Mythic requires premade groups; see [0106-Dungeons.md](../0100-World/0106-Dungeons.md)).

## 3. Role-Based Queuing

Players queue as Tank, Healer, or Damage (see [0813-Group-Roles.md](0813-Group-Roles.md)), with queue times displayed per role so players understand the tradeoffs of role scarcity in real time.

## 4. Cross-Faction Queuing

To keep queue times reasonable, Dungeon Finder groups may match players across the Dawnbound Concord and Duskward Pact factions for PvE-only instanced content, with appropriate narrative framing (a temporary truce) explaining the cooperation without undermining the factions' broader rivalry.

## 5. Incentives and Rewards

Random Dungeon queuing grants bonus currency and reputation beyond a direct dungeon queue, encouraging players to fill queue gaps for underserved dungeons rather than only running the currently "best" dungeon.

## 6. Vote Kick and Etiquette Tools

A vote-kick system allows a group to remove a disruptive or unresponsive member after a cooldown period, paired with a lightweight reporting tool feeding into the moderation systems described in [2003-Moderation.md](../2000-Operations/2003-Moderation.md).

## 7. Technical Notes

Matchmaking runs through a dedicated queue service that balances role composition and approximate item level, detailed further in [1225-Matchmaking-Architecture.md](../1200-Technical/1225-Matchmaking-Architecture.md).
