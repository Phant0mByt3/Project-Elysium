# 0914 — Bank System

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [1006-Banking.md](../1000-Economy/1006-Banking.md) · [0519-Item-Storage.md](../0500-Items/0519-Item-Storage.md) · [0913-Inventory-System.md](0913-Inventory-System.md) · [0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md)

---

## 1. Overview

The Bank System provides persistent storage beyond the character’s carried inventory. It includes personal bank tabs and, where applicable, shared account or guild storage.

---

## 2. Storage Types

| Type | Scope | Access |
|------|-------|--------|
| **Personal Bank** | Character (with possible account-wide tabs) | City bank NPCs / UI |
| **Guild Bank** | Guild | Guild hall or city access with rank permissions |
| **Reagent / Material Bank** | Character or account | Specialised tabs for crafting materials |

---

## 3. Design Rules

1. Bank space is a meaningful but attainable upgrade path.
2. Guild bank permissions are granular enough for large organisations.
3. Materials-focused storage reduces the need to ferry reagents constantly.
4. All deposits and withdrawals are logged for the owner (and for guild officers where relevant) to support trust and moderation.

---

## 4. Technical Notes

Bank contents are stored in the central database and are available regardless of which instance the player is in. Operations are transactional and protected against duplication.
