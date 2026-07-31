# 147 — Bug Tracking

## Overview
Standards for logging, triaging, and resolving bugs found during testing ([146-Testing.md](146-Testing.md)) or reported by players during Alpha/Beta/Live phases.

## Bug Report Requirements
Every bug report should include: reproduction steps, expected vs. actual behavior, severity, affected system (referencing the relevant docs file where possible, e.g. "combat," "auction house"), and environment details (client version, server, etc.).

## Severity Levels
* **Critical** — crashes, data loss, game-breaking exploits (especially economy/anti-cheat related, see [126-Security.md](126-Security.md), [127-Anti-Cheat.md](127-Anti-Cheat.md)).
* **Major** — a system is unusable or significantly broken, but doesn't crash the game or corrupt data.
* **Minor** — cosmetic, small QoL, or edge-case issues.
* **Trivial** — typos, minor visual polish items.

## Triage Cadence
Critical and Major bugs are triaged immediately; Minor/Trivial bugs are batched into upcoming patch cycles per the release process in [148-Release-Process.md](148-Release-Process.md).

## Resolution Tracking
Fixed bugs should be reflected in the changelog entries of [004-Version-History.md](004-Version-History.md) once shipped.
