# 1220 — Database Schema

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1201-Database.md](1201-Database.md) · [1219-Data-Storage.md](1219-Data-Storage.md) · [1228-Account-System.md](1228-Account-System.md) · [1229-Player-Data-System.md](1229-Player-Data-System.md)

---

## 1. Overview

The Database Schema defines the tables, relationships, and constraints that store accounts, characters, items, guilds, quests, economy, and related systems. This document is the high-level design reference; the living schema lives in migration code.

---

## 2. Major Domains

| Domain | Examples |
|--------|----------|
| **Account** | Credentials, session metadata, account-wide unlocks |
| **Character** | Core stats, position, specialisation, appearance |
| **Inventory & Items** | Item instances, bindings, durability, storage location |
| **Progression** | Quests, achievements, reputation, talents |
| **Social** | Friends, guilds, ranks, guild bank |
| **Economy** | Currency balances, auction listings, transaction log |
| **World / Instance** | Instance metadata, lockouts, world-state flags |

---

## 3. Design Rules

1. Schema changes go through review and migration scripts.
2. Foreign keys and constraints protect referential integrity for critical relationships.
3. Hot-path queries are indexed and reviewed against performance targets.
4. Soft-delete or archival strategies are preferred over hard deletes for player-facing history where recovery may be needed.
