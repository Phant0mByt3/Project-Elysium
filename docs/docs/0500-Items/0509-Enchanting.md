# 0509 — Enchanting

**Category:** Items
**Status:** Living Document
**Related:** [0508-Crafting.md](0508-Crafting.md) · [0304-Stats.md](../0300-Characters/0304-Stats.md)

---

## 1. Overview

Enchanting allows players to apply permanent stat-boosting effects to weapons and armor, layered on top of an item's base stats ([0304-Stats.md](../0300-Characters/0304-Stats.md)) rather than replacing them.

## 2. Core Loop

1. Disenchant unwanted gear (Rare-or-higher quality) into enchanting materials.
2. Learn enchant recipes from trainers or rare drops.
3. Apply an enchant to a compatible weapon/armor slot for a material cost.

## 3. Design Rules

* Enchants should scale in power roughly with the level range they're taught in, giving a steady mid-level Aurum sink and profession revenue stream (see [1000-Economy.md](../1000-Economy/1000-Economy.md)).
* Slot-specific enchant pools (weapon vs. chest vs. cloak, etc.) should each offer at least 2–3 viable options per role, avoiding a single "best in slot" enchant with no alternatives.
* High-end enchants (raid-tier) should require raid-drop materials, tying the profession into endgame content loops.

## 4. Enchant Slot Table

| Slot | Typical Enchant Focus |
| --- | --- |
| Weapon | Primary damage/healing stat, or on-hit proc |
| Chest | Primary stat or general survivability |
| Cloak | Secondary/utility stat |
| Boots | Movement-related utility |
| Rings | Small secondary stat boosts |

## 5. Relationship to Crafting

Enchanting is trained and practiced separately from the gathering/production professions in [0600-Professions.md](../0600-Professions/0600-Professions.md), but shares the profession leveling and trainer infrastructure described there.

## 6. Environmental Resistance Enchants

Certain enchants specifically counter environmental hazards described in [0117-Environmental-Hazards.md](../0100-World/0117-Environmental-Hazards.md) — cold resistance for Ashenclaw Tundra content, heat resistance for the Ember Deeps — giving enchanting a direct tie to regional world design as well as combat itemization.

## 7. Disenchanting and the Economy

Disenchanting acts as both a material source for enchanters and a soft loot sink, converting unwanted gear into a usable resource rather than pure vendor filler — see [1010-Currency-Sinks.md](../1000-Economy/1010-Currency-Sinks.md).
