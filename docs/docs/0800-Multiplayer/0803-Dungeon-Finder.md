# 83 — Dungeon Finder

## Overview
The Dungeon Finder is an automated matchmaking tool that groups players into a party ([0801-Parties.md](0801-Parties.md)) for a queued dungeon ([0106-Dungeons.md](../0100-World/0106-Dungeons.md)), lowering the barrier to group content per Pillar 4 in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).

## How It Works
1. Player queues, selecting a role (Tank/Healer/Damage) and one or more eligible dungeons.
2. The system matches based on role balance (typically 1 tank, 1 healer, 3 damage) and approximate item level/gear readiness.
3. Once matched, the party is teleported to the dungeon entrance automatically.

## Incentives
Queueing for underrepresented roles (typically Tank/Healer) should offer a small bonus reward to help balance queue times — a standard MMORPG pattern applied here without altering core reward structures elsewhere.

## Cross-Faction Consideration
The Dungeon Finder pools players within the same faction only, consistent with party/guild restrictions ([0801-Parties.md](0801-Parties.md), [0800-Guilds.md](0800-Guilds.md)).

## Difficulty Availability
Normal difficulty is available at the dungeon's intended level range; Heroic difficulty is queueable at max level. Mythic difficulty is intentionally excluded from the automated finder, requiring a manually formed premade group, per [0106-Dungeons.md](../0100-World/0106-Dungeons.md)'s difficulty design.
