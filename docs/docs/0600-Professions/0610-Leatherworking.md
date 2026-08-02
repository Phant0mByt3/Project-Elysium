# 0610 — Leatherworking

**Project:** Elysium MMORPG  
**Category:** Professions  
**Status:** Design Complete — Implementation Pending  
**Related:** [0600-Professions.md](0600-Professions.md) · [0501-Armour.md](../0500-Items/0501-Armour.md) · [0609-Tailoring.md](0609-Tailoring.md) · [0611-Profession-Progression.md](0611-Profession-Progression.md)

---

## 1. Overview

Leatherworking is the crafting profession focused on leather and hide-based armour, gear, and utility items. It primarily serves leather-wearing classes (Rogue, Ranger, some Druid and Monk-style fantasy) and produces bags, drums, and other consumable or utility goods.

---

## 2. Fantasy & Identity

Leatherworkers are the practical artisans of the wilds and the road — tanners, armourers, and outfitters who turn the hides of beasts into protection and tools. Their work sits between the heavy forges of Blacksmithing and the finer cloth of Tailoring.

---

## 3. Core Outputs

| Category | Examples |
|----------|----------|
| **Armour** | Leather chest, legs, gloves, boots, helms, shoulders |
| **Utility** | Bags, quivers, weapon wraps, repair kits |
| **Consumables / Buffs** | Drums, battle standards, temporary armour kits |
| **Optional** | Light mounts or cosmetic gear (later content) |

---

## 4. Materials

Primary materials come from skinning (a gathering activity tied to combat or specific nodes) and from vendors or the Auction House. Higher-tier leathers are region- and level-gated, matching the progression curve in [0611-Profession-Progression.md](0611-Profession-Progression.md) and [0612-Profession-Materials.md](0612-Profession-Materials.md).

---

## 5. Design Rules

1. Leatherworking must remain relevant at max level through utility items and competitive armour pieces, not only early-game greens.
2. Recipes should offer meaningful choices (stamina-focused vs agility-focused, etc.) rather than a single optimal craft.
3. Cross-profession synergy exists (e.g. Blacksmithing buckles, Jewelcrafting adornments) without making Leatherworking dependent on another profession to function.

---

## 6. Technical Notes

Recipes and skill progression follow the shared profession framework. Crafting is performed at designated stations or via the profession UI; all material consumption and item creation is server-authoritative.
