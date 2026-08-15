# 0715 — Dynamic Quests

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0109-World-Events.md](../0100-World/0109-World-Events.md) · [0700-Quests.md](0700-Quests.md) · [0716-World-Quest-System.md](0716-World-Quest-System.md) · [0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md)

---

## 1. Overview

Dynamic quests are objectives that appear, change, or expire based on world state, time, or event conditions rather than being permanently available from a fixed NPC. They support the living-world fantasy and give returning players new things to do in familiar spaces.

---

## 2. Examples

- Defend a village during a recurring undead uprising.
- Escort a merchant caravan that only spawns under certain conditions.
- Temporary “help the researchers” objectives that appear while a world event is active.
- Seasonal variants of existing quest hubs.

---

## 3. Design Rules

1. Dynamic quests should feel like natural extensions of the world, not random pop-ups.
2. Failure or expiration of a dynamic quest never blocks permanent progression.
3. Rewards are tuned for the time investment and may include event-specific currencies or cosmetics.
4. Clear UI indication shows that a quest is time-limited or event-tied.

---

## 4. Relationship to World Events & World Quests

Dynamic quests often sit on top of or feed into the systems described in [0109-World-Events.md](../0100-World/0109-World-Events.md) and [0716-World-Quest-System.md](0716-World-Quest-System.md). The distinction is mainly one of scope and permanence.


## 5. Frequency Tuning

Dynamic quests are tuned to appear often enough that returning players regularly encounter something new, but not so often that the world feels chaotic or unpredictable — early playtesting will calibrate the exact spawn cadence per region.

## 6. Narrative Consistency

Even though dynamic quests are procedurally scheduled, their content is entirely hand-authored, ensuring they meet the same writing quality bar as fixed quests per [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md).
