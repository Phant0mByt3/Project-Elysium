# 0616 — Profession Mastery

**Project:** Elysium MMORPG  
**Category:** Professions  
**Status:** Design Complete — Implementation Pending  
**Related:** [0611-Profession-Progression.md](0611-Profession-Progression.md) · [0615-Profession-Specialisations.md](0615-Profession-Specialisations.md) · [0600-Professions.md](0600-Professions.md) · [0905-Player-Progression.md](../0900-Player-Systems/0905-Player-Progression.md)

---

## 1. Overview

Profession Mastery is the long-term, post-cap progression track for each profession. Once a player has reached maximum skill and chosen a specialisation, Mastery provides ongoing goals, small power or convenience rewards, and collection-style satisfaction.

---

## 2. Mastery Tracks

Each profession has one or more mastery tracks that are advanced by:

- Crafting high-tier recipes
- Gathering rare materials
- Completing profession-related achievements or weekly objectives
- Discovering rare recipes or experimental crafts

Rewards include:

- Permanent passive bonuses (slightly improved yields, reduced material costs, higher proc chances)
- Exclusive cosmetic tools or outfits
- Titles and achievement points
- Access to a small number of prestige recipes

---

## 3. Design Rules

1. Mastery should never feel mandatory for competing in group content; it is a horizontal progression layer.
2. Progress is steady and visible so that dedicated crafters feel continuous advancement.
3. Mastery rewards favour convenience, identity, and mild economic advantage over raw power that would unbalance combat.

---

## 4. Technical Notes

Mastery progress is stored per character (or per account for certain cosmetic unlocks). All advancement and reward grants are server-authoritative.
