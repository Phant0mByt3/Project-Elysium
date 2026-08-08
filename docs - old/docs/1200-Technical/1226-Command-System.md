# 1226 — Command System

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1227-Permission-System.md](1227-Permission-System.md) · [1214-Admin-Tools.md](1214-Admin-Tools.md) · [1200-Plugin-Architecture.md](1200-Plugin-Architecture.md)

---

## 1. Overview

The Command System provides a unified way to register, parse, permission-check, and execute text commands for players, moderators, and developers.

---

## 2. Features

- Consistent syntax and help text
- Permission gating per command and subcommand
- Tab completion where useful
- Audit logging for privileged commands
- Support for both player-facing and staff-only commands

---

## 3. Design Rules

1. Player commands are discoverable and documented in-game where appropriate.
2. Staff commands are never exposed in public help without permission.
3. Dangerous commands require confirmation or additional safeguards.
4. Commands that modify player or world state go through the same authoritative services as the rest of the game.
