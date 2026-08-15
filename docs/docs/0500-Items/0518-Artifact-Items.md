# 0518 — Artifact Items

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0505-Legendary-Items.md](0505-Legendary-Items.md) · [0506-Relics.md](0506-Relics.md) · [0202-Gods.md](../0200-Lore/0202-Gods.md) · [0206-History.md](../0200-Lore/0206-History.md)

---

## 1. Overview

Artifact items are a special tier of powerful, story-rich items that sit above or alongside Legendaries in fantasy weight. They are typically tied to the gods, the Age of Concord, or major historical events and often have multi-stage acquisition and upgrade paths.

---

## 2. Distinguishing Features

- Strong narrative framing and unique acquisition (long quest chains, raid discoveries, exploration secrets).
- Multiple upgrade ranks or “awakening” stages that unlock additional visual and mechanical power.
- Often account-wide or have cosmetic unlocks that persist across characters.
- Visual design is deliberately iconic so that other players recognise the artifact at a glance.

---

## 3. Relationship to Other Systems

- Artifacts may share the Legendary colour treatment or receive a distinct treatment (to be finalised with Art).
- They interact with the same binding, upgrading, and transmog rules unless a specific exception is documented.
- Future expansions may introduce new artifact lines or further awakenings of existing ones.

---

## 4. Design Rules

1. Artifacts should feel like genuine discoveries, not just another loot table entry.
2. Power level is high but not so high that they make all other gear irrelevant.
3. Acquisition should be achievable by dedicated players without requiring the absolute top guild clear of every tier.

---

## 5. Technical Notes

Artifact state (rank, unlocks, appearance) is stored on the character or account. Upgrade operations follow the same transactional patterns as other item systems.


---

## 6. Example Artifact Concept

**The Concord Diadem** — a crown-shaped headpiece said to have been worn by the last steward of Aethercrest before the Sundering; acquired through a long multi-raid-tier questline, with each awakening stage tied to a specific lore revelation about the fall of the original capital, directly enriching [0206-History.md](../0200-Lore/0206-History.md) as players progress it.

## 7. Long-Term Role

Artifact items are intended to be a recurring feature across expansions, giving each major content season a signature, story-driven item chase alongside standard raid progression.
