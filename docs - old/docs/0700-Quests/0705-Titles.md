# 0705 — Titles

## Overview
Titles are cosmetic name modifiers displayed above or below a character's name, earned primarily through achievements ([0704-Achievements.md](0704-Achievements.md)) and select major story/raid milestones.

## Examples
* **"the Reclaimer"** — earned for completing the full main story ([0207-Main-Story.md](../0200-Lore/0207-Main-Story.md)).
* **"of the Sunken Concord"** — earned for clearing the launch raid ([0107-Raids.md](../0100-World/0107-Raids.md)) on Heroic difficulty.
* **"Cartographer"** — earned for fully exploring both launch continents ([0112-Maps.md](../0100-World/0112-Maps.md), [0105-Landmarks.md](../0100-World/0105-Landmarks.md)).
* **"Warmonger"** — earned through PvP achievement milestones ([0804-PvP.md](../0800-Multiplayer/0804-PvP.md)).

## Historical Titles

**Examples:**

* First Fleet Member
* First Guild to Conquer The Ruined Portal
* Ancient Architect
* Divine Creator

These are identity rewards, not power rewards.

## Design Rules
* Titles are purely cosmetic; no title should grant a stat or gameplay bonus.
* Rarer titles (Mythic raid clears, top PvP tiers) should be seasonally reset or otherwise time-limited where appropriate, to preserve prestige.
* Every title should be selectable/togglable independently by the player, never forced.

## Technical Notes
Title unlock state is stored per-character; see [1201-Database.md](../1200-Technical/1201-Database.md) for schema considerations.
