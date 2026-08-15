# 1207 — Anti Cheat

## Overview
Anti-cheat systems protect the integrity of Elysium's PvE and PvP content against speed hacks, reach hacks, autoclickers/macros, and duplication exploits — critical given the game's competitive raid ([0802-Raiding.md](../0800-Multiplayer/0802-Raiding.md)) and PvP ([0804-PvP.md](../0800-Multiplayer/0804-PvP.md)) systems.

## Approach
* **Server Authority** — all combat, movement, and economy actions are validated server-side; the client is never trusted for outcome-determining logic, consistent with the plugin architecture's design in [1200-Plugin-Architecture.md](1200-Plugin-Architecture.md).
* **Movement Validation** — server-side checks against physically implausible movement (speed hacks, flight where not permitted).
* **Action Rate Limiting** — server-side cooldown enforcement independent of client-reported cooldown state, preventing ability-spam macros.
* **Duplication Prevention** — transactional integrity on all item-moving operations (trade, mail, auction house, guild bank) at the database layer ([1201-Database.md](1201-Database.md)).

## Enforcement
Suspected violations should be logged for review rather than always auto-banning, to avoid false-positive punishment of legitimate high-latency or unusual-but-valid play. Ban/mute policy and appeals process to be defined ahead of Closed Beta.

## Relationship to Security
Anti-cheat is one pillar of the broader security posture described in [1206-Security.md](1206-Security.md).


## Statistical Anomaly Detection

Beyond direct rule-based validation, aggregate statistical monitoring (unusual damage output, implausible resource gathering rates) flags accounts for manual review, catching sophisticated cheats that might evade simple rule-based detection.

## Fair Play Communication

Players can report suspected cheaters directly through the in-client reporting tool, feeding into the same review pipeline as automated detection, and the team communicates transparently (without revealing detection methods) about anti-cheat enforcement actions to maintain community trust.
