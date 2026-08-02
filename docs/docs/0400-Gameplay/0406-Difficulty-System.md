# 0406 — Difficulty System

**Project:** Elysium MMORPG  
**Category:** Gameplay  
**Status:** Design Complete — Implementation Pending  
**Related:** [0106-Dungeons.md](../0100-World/0106-Dungeons.md) · [0107-Raids.md](../0100-World/0107-Raids.md) · [0403-Boss-Mechanics.md](0403-Boss-Mechanics.md) · [0309-Balance.md](../0300-Characters/0309-Balance.md)

---

## 1. Overview

Difficulty in Elysium is expressed through discrete tiers rather than a continuous slider. This keeps expectations clear for players and makes balance and reward tuning tractable.

---

## 2. Content Difficulty Tiers

| Content | Tiers | Notes |
|---------|-------|-------|
| Open-world questing & elites | Single baseline | Tuned to the region’s level band |
| Dungeons | Normal / Heroic / Mythic | See [0106-Dungeons.md](../0100-World/0106-Dungeons.md) |
| Raids | Normal / Heroic / Mythic | See [0107-Raids.md](../0100-World/0107-Raids.md) |
| World Bosses | Scaled by participant count | Soft scaling, not full dynamic |

---

## 3. What Changes Between Tiers

- Enemy health and damage
- Presence or strictness of additional mechanics
- Enrage / soft-enrage pressure
- Loot quality and quantity
- Requirement for coordination and specific roles

Normal is intended to be clearable by a competent pickup group of the appropriate level. Heroic expects solid execution. Mythic is aimed at organised groups seeking the highest rewards and prestige.

---

## 4. Design Philosophy

- Difficulty should come primarily from mechanics and coordination, not from inflated numbers alone.
- Lower difficulties must remain rewarding; they are not “practice modes” with worthless loot.
- Players should be able to understand why they failed a pull (telegraphs, UI feedback, death recap).

---

## 5. Future Considerations

A Mythic+ style key system for dungeons is listed in [9999-Ideas.md](../9000-Future/9999-Ideas.md) and may be explored post-launch once the base three tiers are solid.
