# 0611 — Profession Progression

**Project:** Elysium MMORPG  
**Category:** Professions  
**Status:** Design Complete — Implementation Pending  
**Related:** [0600-Professions.md](0600-Professions.md) · [0305-Leveling.md](../0300-Characters/0305-Leveling.md) · [0615-Profession-Specialisations.md](0615-Profession-Specialisations.md) · [0616-Profession-Mastery.md](0616-Profession-Mastery.md)

---

## 1. Overview

Profession progression runs in parallel with character leveling but is not tightly gated by it. Players can advance gathering and crafting at their own pace, with higher-tier materials and recipes unlocking as they explore higher-level regions and content.

---

## 2. Progression Structure

| Stage | Description |
|-------|-------------|
| **Apprentice** | Basic recipes and low-level nodes; available almost immediately |
| **Journeyman** | Mid-tier materials and more complex crafts |
| **Expert** | High-level regional materials and competitive gear crafts |
| **Artisan / Master** | Max-level recipes, specialisations, and mastery tracks |
| **Specialisation & Mastery** | See [0615-Profession-Specialisations.md](0615-Profession-Specialisations.md) and [0616-Profession-Mastery.md](0616-Profession-Mastery.md) |

Skill points are earned primarily by successfully crafting or gathering, with diminishing returns on repeated low-tier actions so that players are encouraged to move into new content.

---

## 3. Design Rules

1. Profession leveling should feel rewarding on its own, not only as a means to an end.
2. No profession is required to progress the main story or clear core group content.
3. Catch-up mechanisms (or simply faster gains on lower content once the player is higher level) exist so alts and late starters are not heavily punished.
4. The pacing of new material tiers roughly follows the regional level bands in [0102-Regions.md](../0100-World/0102-Regions.md).

---

## 4. Technical Notes

Profession skill and recipe knowledge are stored per character. All skill-up rolls and recipe unlocks are server-side.
