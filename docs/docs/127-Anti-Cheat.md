# 127 — Anti-Cheat

## Overview
Anti-cheat systems protect the integrity of Elysium's PvE and PvP content against speed hacks, reach hacks, autoclickers/macros, and duplication exploits — critical given the game's competitive raid ([82-Raiding.md](82-Raiding.md)) and PvP ([84-PvP.md](84-PvP.md)) systems.

## Approach
* **Server Authority** — all combat, movement, and economy actions are validated server-side; the client is never trusted for outcome-determining logic, consistent with the plugin architecture's design in [120-Plugin-Architecture.md](120-Plugin-Architecture.md).
* **Movement Validation** — server-side checks against physically implausible movement (speed hacks, flight where not permitted).
* **Action Rate Limiting** — server-side cooldown enforcement independent of client-reported cooldown state, preventing ability-spam macros.
* **Duplication Prevention** — transactional integrity on all item-moving operations (trade, mail, auction house, guild bank) at the database layer ([121-Database.md](121-Database.md)).

## Enforcement
Suspected violations should be logged for review rather than always auto-banning, to avoid false-positive punishment of legitimate high-latency or unusual-but-valid play. Ban/mute policy and appeals process to be defined ahead of Closed Beta.

## Relationship to Security
Anti-cheat is one pillar of the broader security posture described in [126-Security.md](126-Security.md).
