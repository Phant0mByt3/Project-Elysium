# 0913 — Inventory System

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0519-Item-Storage.md](../0500-Items/0519-Item-Storage.md) · [0914-Bank-System.md](0914-Bank-System.md) · [1004-Trading.md](../1000-Economy/1004-Trading.md) · [1118-Inventory-UI.md](../1100-Client/1118-Inventory-UI.md)

---

## 1. Overview

The Inventory System manages the player’s personal carried items: bags, equipment slots, key items, and currency displays. It is the day-to-day interface for looting, equipping, using, and organising gear and materials.

---

## 2. Core Behaviours

- Auto-loot and manual loot options
- Equip / unequip with stat comparison tooltips
- Use / consume items
- Stacking and splitting of stackable items
- Sorting and filtering helpers
- Full-inventory handling (warnings, overflow to mail where appropriate)

---

## 3. Design Rules

1. Inventory management should be light friction, not a constant chore.
2. Bag space expands through rewards and purchases at a controlled rate.
3. Critical quest items are protected from accidental destruction or vendor sale.
4. The UI remains clear even when the player is carrying a large variety of item types.

---

## 4. Technical Notes

Inventory state is fully server-authoritative. Client predictions exist for responsiveness, but every move, equip, and use is confirmed by the server. See also synchronisation rules in [1211-Server-Synchronisation.md](../1200-Technical/1211-Server-Synchronisation.md).


---

## Additional Detail: Sorting and Filtering

The inventory UI supports automatic sorting by item type, rarity, and recency, plus a search/filter bar, keeping inventory management fast even for players carrying large quantities of profession materials alongside standard gear.

## Quick-Sell and Junk Marking

Items can be manually flagged as "junk," enabling a single quick-sell action at any vendor rather than requiring the player to individually right-click each low-value item, reducing a common source of tedious inventory upkeep.
