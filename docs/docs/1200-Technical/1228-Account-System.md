# 1228 — Account System

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1204-Authentication.md](1204-Authentication.md) · [1220-Database-Schema.md](1220-Database-Schema.md) · [0917-Account-Progression.md](../0900-Player-Systems/0917-Account-Progression.md) · [1100-Launcher.md](../1100-Client/1100-Launcher.md)

---

## 1. Overview

The Account System manages the top-level player identity: credentials, session lifecycle, account-wide unlocks, and the link between the launcher, authentication service, and in-game characters.

---

## 2. Responsibilities

- Account creation and credential storage (hashed)
- Login, logout, and session token management
- Link to characters and account-wide collection/progress data
- Support for future features (2FA, family sharing policies, etc.)
- Integration with ban and security state

---

## 3. Design Rules

1. Passwords and secrets never leave the auth boundary in recoverable form.
2. Session tokens are short-lived and bound to expected client behaviour.
3. Account-level actions (bans, unlocks) apply consistently across all characters.
4. The launcher is the primary entry point for authentication before the game client connects.


---

## Additional Detail: Account-Character Relationship

An account can hold multiple characters up to the slot limit described in [1115-Character-Select.md](../1100-Client/1115-Character-Select.md), with account-level data (achievements, collections, account-wide currency) stored separately from character-specific data, supporting the account-wide progression systems in [0917-Account-Progression.md](../0900-Player-Systems/0917-Account-Progression.md).

## Account Recovery

A documented account recovery process (verified through registered email and, where enabled, two-factor authentication) allows legitimate account owners to regain access after a lost password or compromised account, coordinated with the support system in [2005-Support-System.md](../2000-Operations/2005-Support-System.md).
