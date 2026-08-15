# 1407 — Bug Tracking

## Overview
Standards for logging, triaging, and resolving bugs found during testing ([1406-Testing.md](1406-Testing.md)) or reported by players during Alpha/Beta/Live phases.

## Bug Report Requirements
Every bug report should include: reproduction steps, expected vs. actual behavior, severity, affected system (referencing the relevant docs file where possible, e.g. "combat," "auction house"), and environment details (client version, server, etc.).

## Severity Levels
* **Critical** — crashes, data loss, game-breaking exploits (especially economy/anti-cheat related, see [1206-Security.md](../1200-Technical/1206-Security.md), [1207-Anti-Cheat.md](../1200-Technical/1207-Anti-Cheat.md)).
* **Major** — a system is unusable or significantly broken, but doesn't crash the game or corrupt data.
* **Minor** — cosmetic, small QoL, or edge-case issues.
* **Trivial** — typos, minor visual polish items.

## Triage Cadence
Critical and Major bugs are triaged immediately; Minor/Trivial bugs are batched into upcoming patch cycles per the release process in [1408-Release-Process.md](1408-Release-Process.md).

## Resolution Tracking
Fixed bugs should be reflected in the changelog entries of [0004-Version-History.md](../0000-Project/0004-Version-History.md) once shipped.


## Duplicate Detection

New bug reports are checked against existing open reports before being logged as new, using searchable tags tied to affected systems, keeping the bug tracker from becoming cluttered with duplicate entries for the same underlying issue.

## Player-Reported Bug Pipeline

Post-launch, player-submitted bug reports (via the support system, [2005-Support-System.md](../2000-Operations/2005-Support-System.md)) are triaged into the same tracking system as internally found bugs, with confirmed reports credited to the reporting player where the community team deems appropriate.
