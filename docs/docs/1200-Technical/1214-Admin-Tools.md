# 1214 — Admin Tools

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1226-Command-System.md](1226-Command-System.md) · [1227-Permission-System.md](1227-Permission-System.md) · [1206-Security.md](1206-Security.md) · [2008-Staff-Tools.md](../2000-Operations/2008-Staff-Tools.md)

---

## 1. Overview

Admin Tools are the in-game and web/console interfaces used by staff to moderate, investigate, and support players, and to perform operational tasks on the live game.

---

## 2. Capabilities

- Player lookup (account, characters, inventory, history)
- Kick, mute, ban, and warning tools with audit logging
- Item and currency adjustment with full logging
- Teleport and instance inspection
- Event and world-state controls
- Ticket / support integration points

---

## 3. Design Rules

1. Every privileged action is logged with actor, target, and reason.
2. Permissions are granular; not every staff role has every tool.
3. Tools favour safety (confirmation, soft-delete, rollback where possible) over speed alone.
4. Interface design reduces the chance of mis-clicks on irreversible actions.
