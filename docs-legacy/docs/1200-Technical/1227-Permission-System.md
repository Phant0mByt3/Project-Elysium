# 1227 — Permission System

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1226-Command-System.md](1226-Command-System.md) · [1214-Admin-Tools.md](1214-Admin-Tools.md) · [0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md) · [1206-Security.md](1206-Security.md)

---

## 1. Overview

The Permission System answers “is this actor allowed to perform this action?” for players, guild ranks, and staff. It underpins commands, admin tools, guild features, and certain world interactions.

---

## 2. Layers

| Layer | Examples |
|-------|----------|
| **Player** | Default abilities, unlock-gated actions |
| **Guild Rank** | Bank access, invite, kick, rank management |
| **Staff / Admin** | Moderation, investigation, server control |
| **System** | Internal service-to-service authorisation |

---

## 3. Design Rules

1. Permissions are explicit and least-privilege by default.
2. Guild permissions are configurable by the guild within defined bounds.
3. Staff permissions are role-based and auditable.
4. Permission checks are performed server-side on every sensitive action.
