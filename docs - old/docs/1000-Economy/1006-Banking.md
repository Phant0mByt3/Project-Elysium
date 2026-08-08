# 1006 — Banking

## Overview
Banks provide expanded, secure item storage beyond a character's personal inventory, accessible from any city ([0103-Cities.md](../0100-World/0103-Cities.md)).

## Core Features
* **Personal Bank** — additional storage tabs, purchasable/expandable with Aurum, for items not actively carried.
* **Guild Bank** — shared storage for guild members with rank-based withdrawal limits, covered in [0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md).
* **Account-Wide Storage** — a limited shared tab accessible by all characters on an account, primarily for cosmetics and crafting materials, reducing friction for players running multiple characters.

## Design Rules
* Bank tab expansion costs should scale, providing a mid-game Aurum sink ([1000-Economy.md](1000-Economy.md)) without ever hard-blocking a player's core item storage needs.
* Bank access should never be possible from the open field — a deliberate friction point that keeps cities relevant as hubs (Pillar in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md)) rather than everything being accessible remotely.
