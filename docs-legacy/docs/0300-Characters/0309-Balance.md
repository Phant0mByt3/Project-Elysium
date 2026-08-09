# 0309 — Balance

## Philosophy
Balance in Elysium is treated as an ongoing process, not a pre-launch checkbox. This document tracks the standards and cadence for balance work, not specific number values (which belong in version-specific patch notes, [0004-Version-History.md](../0000-Project/0004-Version-History.md)).

## Goals
* Every class/specialization should be viable for questing, dungeons, and at least one raid role.
* No specialization should dominate every content type (solo, group PvE, PvP) simultaneously.
* PvP and PvE balance are tuned somewhat independently where needed — see [0804-PvP.md](../0800-Multiplayer/0804-PvP.md) for PvP-specific modifiers.

## Review Cadence
* **Pre-launch**: internal playtesting passes at the end of each major system's implementation (classes, itemization, dungeons).
* **Alpha/Beta**: structured feedback collection and iteration against player data.
* **Live service**: balance patches reviewed each content patch, following the process in [1408-Release-Process.md](../1400-Development/1408-Release-Process.md).

## Data Sources
Balance decisions should be informed by combat logs and aggregate performance data wherever possible, not solely developer intuition — see [1205-API.md](../1200-Technical/1205-API.md) for planned combat logging/analytics hooks.

## Escalation
Significant balance changes (talent reworks, specialization identity shifts) should be documented as deliberate design decisions in [0004-Version-History.md](../0000-Project/0004-Version-History.md), not silently patched.
