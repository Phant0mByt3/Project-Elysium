# 0515 — Item Durability

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0313-Death-System.md](../0300-Characters/0313-Death-System.md) · [1001-Currency.md](../1000-Economy/1001-Currency.md) · [1002-Vendors.md](../1000-Economy/1002-Vendors.md) · [0508-Crafting.md](0508-Crafting.md)

---

## 1. Overview

Durability is a light gold and material sink that gives death and heavy combat a small ongoing cost without becoming a major progression barrier. It is intentionally modest compared with classic “repair after every wipe” systems.

---

## 2. Core Rules

- Equipped gear loses a small amount of durability on death and a very small amount from normal combat wear.
- When durability reaches zero the item’s stats are greatly reduced until repaired; the item is not destroyed.
- Repair is performed by NPC vendors in cities and major hubs for Aurum, or via certain crafting professions for a materials + gold cost.
- Durability loss is never catastrophic; a full repair after a difficult session should feel like a minor expense, not a punishment.

---

## 3. Design Goals

- Create a steady, predictable currency sink.
- Give blacksmiths and other repair-capable professions a service role.
- Avoid making death feel expensive enough to discourage experimentation or progression.

---

## 4. Technical Notes

Durability is tracked per item instance on the server. Repair operations are transactional. Client only displays the current durability percentage and the broken-item visual state.


---

## 5. Regional Repair Access

Repair vendors are present in every major city ([0103-Cities.md](../0100-World/0103-Cities.md)) and select large villages, ensuring players are never far from a repair option even deep into a questing session.

## 6. Interaction with Death

Durability loss on death is intentionally light compared to older MMORPGs, in keeping with the death system's broader philosophy of consequence without excessive punishment — see [0313-Death-System.md](../0300-Characters/0313-Death-System.md).
