# 0614 — Profession Recipes

**Project:** Elysium MMORPG  
**Category:** Professions  
**Status:** Design Complete — Implementation Pending  
**Related:** [0600-Professions.md](0600-Professions.md) · [0611-Profession-Progression.md](0611-Profession-Progression.md) · [0508-Crafting.md](../0500-Items/0508-Crafting.md) · [0612-Profession-Materials.md](0612-Profession-Materials.md)

---

## 1. Overview

Recipes define what a profession can create, the materials required, the skill threshold, and any special conditions (station type, optional reagents, specialisation requirements).

---

## 2. Recipe Properties

Every recipe records:

- Required profession and minimum skill
- Material list (with quantities)
- Optional / catalyst reagents that improve outcome or add effects
- Output item(s) and quantity range
- Crafting station requirement (if any)
- Specialisation or mastery gate (if any)
- Cooldown or daily limit (rare; used sparingly for powerful crafts)

---

## 3. Acquisition

Recipes are learned from:

- Profession trainers
- World drops and dungeon/raid drops
- Quest rewards
- Vendor purchases (limited)
- Discovery while crafting (optional system for certain professions)

---

## 4. Design Rules

1. Recipe lists should feel expansive but not overwhelming; UI filtering and search are essential.
2. Powerful or highly desirable recipes should have clear acquisition paths so players know how to work toward them.
3. “Green / yellow / orange / red” difficulty colouring (or equivalent) communicates skill-up chance at a glance.
4. Recipes that produce BoE gear or high-value consumables are important Auction House drivers and are balanced accordingly.

---

## 5. Technical Notes

Recipe data is versioned and loaded by the profession plugin. Crafting validation (materials, skill, station) is performed server-side before any items are consumed or created.


## 6. Recipe Discovery Systems

Select professions (particularly Alchemy) support an optional "experimentation" discovery mechanic where combining known materials at a crafting station has a chance to reveal a new recipe outright, rewarding curious players who tinker with material combinations beyond simply following known recipes.

## 7. Recipe Balance Review

Recipes producing tradeable BoE gear or high-demand consumables are reviewed during the same balance cadence as combat itemization ([0309-Balance.md](../0300-Characters/0309-Balance.md)), since a recipe that's too easy relative to its output value can destabilize material prices across the whole economy.
