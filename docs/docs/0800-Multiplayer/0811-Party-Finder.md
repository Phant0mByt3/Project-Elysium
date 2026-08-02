# 0811 — Party Finder

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0803-Dungeon-Finder.md](0803-Dungeon-Finder.md) · [0801-Parties.md](0801-Parties.md) · [0802-Raiding.md](0802-Raiding.md) · [0813-Group-Roles.md](0813-Group-Roles.md)

---

## 1. Overview

Party Finder is the player-driven tool for assembling groups outside of (or in addition to) the automated Dungeon Finder. It supports custom listings for dungeons, raids, world bosses, questing, and other activities.

---

## 2. Core Functionality

- Create a listing with activity type, required roles, item level or experience expectations, and free-text description
- Browse and filter open listings
- Apply or invite directly
- Integrate with the existing party and raid frames once the group forms

---

## 3. Design Rules

1. Party Finder complements the Dungeon Finder rather than replacing it; automated matchmaking remains the fast path for standard 5-player content.
2. Listings expire after a reasonable time to keep the board fresh.
3. Role and power requirements are visible up front to reduce failed invites and wasted time.
4. Abuse (spam listings, misleading requirements) is moderated through reporting and automated limits.

---

## 4. Technical Notes

Listings are stored and queried through a lightweight matchmaking/service layer. Once a group is formed, standard party/raid synchronisation takes over.
