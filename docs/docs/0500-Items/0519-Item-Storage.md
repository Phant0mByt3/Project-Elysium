# 0519 — Item Storage

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [1006-Banking.md](../1000-Economy/1006-Banking.md) · [0913-Inventory-System.md](../0900-Player-Systems/0913-Inventory-System.md) · [0914-Bank-System.md](../0900-Player-Systems/0914-Bank-System.md) · [0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md)

---

## 1. Overview

Item storage covers how players hold, organise, and access items across inventory, bank, guild bank, and specialised bags. The system aims for clarity and convenience without removing all inventory management as a light gameplay element.

---

## 2. Storage Layers

| Layer | Scope | Notes |
|-------|-------|-------|
| **Personal Inventory** | Character | Limited slots; bags expand capacity |
| **Personal Bank** | Character (or account tabs) | Accessed in cities; larger capacity |
| **Guild Bank** | Guild | Shared storage with rank-based permissions |
| **Specialised Bags** | Character | Profession bags, reagent bags, etc. that only hold certain item types |
| **Void / Overflow** | Temporary | Prevents item loss on full inventory in edge cases (mail, etc.) |

---

## 3. Design Rules

1. Inventory pressure should encourage use of the bank and Auction House rather than constant vendor trash decisions.
2. Stack sizes for materials and consumables are generous enough to support profession and raiding play without constant bank trips.
3. Guild bank permissions are granular enough for large guilds to manage without constant officer intervention.
4. No item is ever silently deleted; full inventory results in clear feedback and recovery options (mail, temporary holding).

---

## 4. Technical Notes

All storage operations (move, stack, split, deposit, withdraw) are transactional and server-authoritative. The client displays the current state and sends intent; the server confirms or rejects each action. See also [1211-Server-Synchronisation.md](../1200-Technical/1211-Server-Synchronisation.md) for cross-instance consistency.


---

## 5. Cross-Character Access

Account-wide bank tabs allow certain material types (crafting reagents, cosmetic tokens) to be shared across a player's characters, reducing the friction of playing multiple classes without undermining the value of character-specific soulbound progression.

## 6. Mail System Integration

The mail system serves as an overflow and cross-character transfer mechanism, holding items temporarily when storage is full and allowing account-bound items to move between characters — see [1004-Trading.md](../1000-Economy/1004-Trading.md) for its economic role.
