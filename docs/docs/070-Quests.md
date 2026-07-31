# 70 — Quests

## Overview
Quests are the primary content delivery mechanism in Elysium, driving both leveling ([46-Leveling.md](46-Leveling.md)) and narrative ([37-Main-Story.md](37-Main-Story.md), [38-Side-Stories.md](38-Side-Stories.md)).

## Quest Types
* **Main Story Quests** — critical-path, single-per-character-active, drive the central narrative.
* **Side Quests** — optional, tied to regions or side stories.
* **Quest Chains** — multi-step questlines, covered in more detail in [71-Quest-Chains.md](71-Quest-Chains.md).
* **Daily/Weekly Quests** — repeatable endgame content, see [72-Daily-Quests.md](72-Daily-Quests.md) and [73-Weekly-Quests.md](73-Weekly-Quests.md).

## Quest Anatomy
Every quest should define: giver NPC ([39-NPCs.md](39-NPCs.md)), objective(s), narrative framing (why does this matter?), reward (experience, Aurum, item, reputation), and follow-up (does it lead anywhere?).

## Design Standards
* No fetch quest without narrative framing — "kill 10 wolves" should always be in service of a stated reason.
* Quest text should respect the writing guide in [143-Quest-Writing-Guide.md](143-Quest-Writing-Guide.md).
* Quests should never be the sole source of a mandatory grind — repeatable content belongs in dailies/weeklies, not infinitely repeatable one-off quests.

## Rewards
Quest rewards should scale meaningfully with the region's level range ([12-Regions.md](12-Regions.md)) and occasionally offer a choice between reward items to add a small moment of player decision-making.
