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


---

## Additional Detail: Command Permission Tiers

Commands are grouped into tiers (player-facing social commands, GM support commands, full admin commands) each requiring the appropriate permission level from [1227-Permission-System.md](1227-Permission-System.md), preventing accidental or malicious misuse of powerful commands.

## Extensibility

The command system is designed to be extended by new plugins without modifying core command-parsing logic, allowing feature plugins to register their own commands (a guild-specific command, a profession-specific command) in a self-contained way.
