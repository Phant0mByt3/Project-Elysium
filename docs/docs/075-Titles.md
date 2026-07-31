# 75 — Titles

## Overview
Titles are cosmetic name modifiers displayed above or below a character's name, earned primarily through achievements ([74-Achievements.md](74-Achievements.md)) and select major story/raid milestones.

## Examples
* **"the Reclaimer"** — earned for completing the full main story ([37-Main-Story.md](37-Main-Story.md)).
* **"of the Sunken Concord"** — earned for clearing the launch raid ([17-Raids.md](17-Raids.md)) on Heroic difficulty.
* **"Cartographer"** — earned for fully exploring both launch continents ([22-Maps.md](22-Maps.md), [15-Landmarks.md](15-Landmarks.md)).
* **"Warmonger"** — earned through PvP achievement milestones ([84-PvP.md](84-PvP.md)).

## Design Rules
* Titles are purely cosmetic; no title should grant a stat or gameplay bonus.
* Rarer titles (Mythic raid clears, top PvP tiers) should be seasonally reset or otherwise time-limited where appropriate, to preserve prestige.
* Every title should be selectable/togglable independently by the player, never forced.

## Technical Notes
Title unlock state is stored per-character; see [121-Database.md](121-Database.md) for schema considerations.
