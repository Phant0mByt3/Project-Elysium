# 59 — Enchanting

## Overview
Enchanting allows players to apply permanent stat-boosting effects to weapons and armor, layered on top of an item's base stats ([45-Stats.md](45-Stats.md)) rather than replacing them.

## Core Loop
1. Disenchant unwanted gear (Rare-or-higher quality) into enchanting materials.
2. Learn enchant recipes from trainers or rare drops.
3. Apply an enchant to a compatible weapon/armor slot for a material cost.

## Design Rules
* Enchants should scale in power roughly with the level range they're taught in, giving a steady mid-level Aurum sink and profession revenue stream (see [100-Economy.md](100-Economy.md)).
* Slot-specific enchant pools (weapon vs. chest vs. cloak, etc.) should each offer at least 2–3 viable options per role, avoiding a single "best in slot" enchant with no alternatives.
* High-end enchants (raid-tier) should require raid-drop materials, tying the profession into endgame content loops.

## Relationship to Crafting
Enchanting is trained and practiced separately from the gathering/production professions in [60-Professions.md](60-Professions.md), but shares the profession leveling and trainer infrastructure described there.
