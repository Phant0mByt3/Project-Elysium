# 0511 — Item Upgrading

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0503-Loot.md](0503-Loot.md) · [0508-Crafting.md](0508-Crafting.md) · [0509-Enchanting.md](0509-Enchanting.md) · [1001-Currency.md](../1000-Economy/1001-Currency.md)

---

## 1. Overview

Item upgrading allows players to invest in gear they like rather than constantly chasing the next pure item-level increase. It supports the “meaningful progression” pillar by letting talent and playstyle preferences persist across power growth.

---

## 2. Upgrade Paths

| Path | Description | Typical Cost |
|------|-------------|--------------|
| **Rank / Reinforcement** | Increases item level or primary stats within the same rarity | Crafting materials + Aurum |
| **Enchanting** | Adds or improves secondary effects | See [0509-Enchanting.md](0509-Enchanting.md) |
| **Socketing / Jewels** | Adds sockets or improves existing ones | Jewelcrafting |
| **Legendary Empowerment** | Unique upgrade tracks for Legendary items | Specific raid/currency sinks |

---

## 3. Design Rules

1. Upgrading should never feel mandatory for basic content clearance; it is an optimisation and investment path.
2. Materials and currency sinks created by upgrading help control inflation ([1009-Inflation-Control.md](../1000-Economy/1009-Inflation-Control.md)).
3. Players can always choose to replace a piece rather than upgrade it; both paths remain viable.
4. Visual changes from upgrading (glows, particle accents) are modest so that transmog and rarity colours remain the primary identity signals.

---

## 4. Technical Notes

Upgrade state is stored on the item instance. All upgrade operations are transactional and server-authoritative to prevent duplication or partial failures.
