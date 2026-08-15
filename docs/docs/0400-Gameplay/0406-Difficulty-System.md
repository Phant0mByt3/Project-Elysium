# 0406 — Difficulty System

**Project:** Elysium MMORPG
**Category:** Gameplay
**Status:** Living Document
**Related:** [0403-Boss-Mechanics.md](0403-Boss-Mechanics.md) · [0106-Dungeons.md](../0100-World/0106-Dungeons.md) · [0108-World-Bosses.md](../0100-World/0108-World-Bosses.md)

---

## 1. Overview

The difficulty system governs how content scales across the game's Normal/Heroic/Mythic tiers and the dynamic scaling used for world content, ensuring the same encounter design can serve a wide range of player skill and gear levels.

## 2. Difficulty Tiers

| Tier | Applies To | Design Intent |
| --- | --- | --- |
| Normal | Dungeons, raids | Learn the encounter; forgiving margin for error |
| Heroic | Dungeons, raids | Requires coordination and correct execution |
| Mythic | Dungeons, raids | Precise execution, minimal margin for error |
| Dynamic Scaling | World bosses, world events | Scales to concurrent participant count |

## 3. Tuning Levers

Difficulty tiers are differentiated primarily through:

* Enemy health and damage multipliers.
* Additional or modified mechanics (see [0403-Boss-Mechanics.md](0403-Boss-Mechanics.md), Section 3).
* Tighter enrage timers or stricter mechanic timing windows.
* Reduced margin for individual player mistakes (fewer "free" mechanic failures before a wipe).

## 4. Solo and Leveling Content Difficulty

Open-world leveling content is tuned so a player of the appropriate level, in appropriate gear, can complete solo content without needing a group, while still requiring attentive play against elites and named enemies (see [0402-Enemy-Design.md](../0400-Gameplay/0402-Enemy-Design.md)).

## 5. Dynamic Scaling for World Content

World bosses and events scale health, damage, and mechanic frequency based on concurrent participants, targeting a consistent completion window regardless of group size — see [0108-World-Bosses.md](../0100-World/0108-World-Bosses.md), Section 4 for the specific formula approach.

## 6. Design Philosophy

Difficulty comes primarily from mechanics and required coordination, not from inflating enemy health into a damage sponge. See Pillar 5 (Quality Over Quantity) in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md) — a Mythic encounter should feel like a sharper test of skill, not a longer grind of the same fight.

## 7. Accessibility Considerations

Normal difficulty across all content types is tuned to be achievable by an attentive but non-expert player or group, ensuring the story and world content is accessible to the broadest possible audience while Heroic and Mythic remain aspirational challenge tiers.
