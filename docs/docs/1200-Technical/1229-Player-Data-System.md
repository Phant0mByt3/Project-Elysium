# 1229 — Player Data System

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1220-Database-Schema.md](1220-Database-Schema.md) · [1211-Server-Synchronisation.md](1211-Server-Synchronisation.md) · [1228-Account-System.md](1228-Account-System.md) · [0913-Inventory-System.md](../0900-Player-Systems/0913-Inventory-System.md)

---

## 1. Overview

The Player Data System is the authoritative service layer for reading and writing character state: attributes, inventory, quests, talents, position, and related progressive data. It sits between gameplay plugins and the database/cache.

---

## 2. Responsibilities

- Load character state on instance entry
- Apply incremental updates (gear, XP, quest flags, etc.)
- Enforce transactional integrity for critical changes (items, currency)
- Provide consistent snapshots for transfers and disconnect recovery
- Expose safe query interfaces for other systems (profile, admin tools)

---

## 3. Design Rules

1. Gameplay code does not write raw SQL; it goes through this layer or equivalent approved APIs.
2. Critical mutations are atomic and recoverable.
3. Caching is used for performance but never at the expense of correctness for valued items and currency.
4. Cross-instance consistency follows the synchronisation rules already defined.


---

## Additional Detail: Data Consistency Across Systems

Player data spans many plugin-owned tables (inventory, quests, reputation, achievements); the player data system provides a consistent, transactional view across these tables for operations that touch multiple systems at once (e.g. a quest completion that grants items, currency, and reputation simultaneously).

## Data Export and Portability

Players can request an export of their own character data (a summary of achievements, statistics, and progression) through the support system, supporting transparency and giving players a personal record independent of the live game state.
