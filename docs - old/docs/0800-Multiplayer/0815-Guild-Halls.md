# 0815 — Guild Halls

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0800-Guilds.md](0800-Guilds.md) · [0814-Guild-Progression.md](0814-Guild-Progression.md) · [0900-Housing.md](../0900-Player-Systems/0900-Housing.md) · [0103-Cities.md](../0100-World/0103-Cities.md)

---

## 1. Overview

Guild Halls are shared spaces that belong to a guild. They serve as social hubs, trophy rooms, and light functional bases (bank access, repair, meeting areas). They are distinct from personal housing and from the future guild-owned neighbourhood concept noted in Future Plans.

---

## 2. Features

- Persistent instance or instanced wing attached to a major city or dedicated guild district
- Customisable décor and trophy displays (raid kills, achievements, member highlights)
- Basic services (guild bank access, repair, vendor)
- Meeting and roleplay space
- Upgrade path tied to Guild Progression

---

## 3. Design Rules

1. Guild Halls should feel like a home for the guild without requiring constant upkeep that becomes a chore.
2. Access is controlled by guild rank permissions.
3. Visual upgrades and trophies are the primary long-term rewards; power gains are secondary or absent.
4. The system is designed to scale from small friend guilds to large raiding organisations.

---

## 4. Technical Notes

Guild Hall instances are managed by the Instance System. Customisation data and trophy state are stored on the guild record and loaded when the hall is entered.
