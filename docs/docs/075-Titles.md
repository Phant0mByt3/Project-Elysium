# 75 — Titles

## Overview
Titles are cosmetic name modifiers displayed above or below a character's name, earned primarily through achievements ([074-Achievements.md](074-Achievements.md)) and select major story/raid milestones.

## Examples
* **"the Reclaimer"** — earned for completing the full main story ([037-Main-Story.md](037-Main-Story.md)).
* **"of the Sunken Concord"** — earned for clearing the launch raid ([017-Raids.md](017-Raids.md)) on Heroic difficulty.
* **"Cartographer"** — earned for fully exploring both launch continents ([022-Maps.md](022-Maps.md), [015-Landmarks.md](015-Landmarks.md)).
* **"Warmonger"** — earned through PvP achievement milestones ([084-PvP.md](084-PvP.md)).

## Design Rules
* Titles are purely cosmetic; no title should grant a stat or gameplay bonus.
* Rarer titles (Mythic raid clears, top PvP tiers) should be seasonally reset or otherwise time-limited where appropriate, to preserve prestige.
* Every title should be selectable/togglable independently by the player, never forced.

## Technical Notes
Title unlock state is stored per-character; see [121-Database.md](121-Database.md) for schema considerations.
