# 70 — Quests

## Overview
Quests are the primary content delivery mechanism in Elysium, driving both leveling ([0305-Leveling.md](../0300-Characters/0305-Leveling.md)) and narrative ([0207-Main-Story.md](../0200-Lore/0207-Main-Story.md), [0208-Side-Stories.md](../0200-Lore/0208-Side-Stories.md)).

## Quest Types
* **Main Story Quests** — critical-path, single-per-character-active, drive the central narrative.
* **Side Quests** — optional, tied to regions or side stories.
* **Quest Chains** — multi-step questlines, covered in more detail in [0701-Quest-Chains.md](0701-Quest-Chains.md).
* **Daily/Weekly Quests** — repeatable endgame content, see [0702-Daily-Quests.md](0702-Daily-Quests.md) and [0703-Weekly-Quests.md](0703-Weekly-Quests.md).

## Quest Anatomy
Every quest should define: giver NPC ([0209-NPCs.md](../0200-Lore/0209-NPCs.md)), objective(s), narrative framing (why does this matter?), reward (experience, Aurum, item, reputation), and follow-up (does it lead anywhere?).

## Design Standards
* No fetch quest without narrative framing — "kill 10 wolves" should always be in service of a stated reason.
* Quest text should respect the writing guide in [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md).
* Quests should never be the sole source of a mandatory grind — repeatable content belongs in dailies/weeklies, not infinitely repeatable one-off quests.

## Rewards
Quest rewards should scale meaningfully with the region's level range ([0102-Regions.md](../0100-World/0102-Regions.md)) and occasionally offer a choice between reward items to add a small moment of player decision-making.
