# 0814 — Guild Progression

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0800-Guilds.md](0800-Guilds.md) · [0815-Guild-Halls.md](0815-Guild-Halls.md) · [0802-Raiding.md](0802-Raiding.md) · [0905-Player-Progression.md](../0900-Player-Systems/0905-Player-Progression.md)

---

## 1. Overview

Guild Progression gives guilds long-term goals and shared rewards beyond individual character power. It reinforces the social unit and gives officers and members something to work toward together.

---

## 2. Progression Elements

| Element | Description |
|---------|-------------|
| **Guild Level / Experience** | Earned from member activities (quests, dungeons, raids, world events) |
| **Perks** | Account-wide or character bonuses unlocked at guild level thresholds (experience, reputation, gathering, etc.) |
| **Achievements** | Guild-wide achievements for first kills, collective goals, and social milestones |
| **Guild Hall upgrades** | Visual and functional improvements to the guild’s shared space |
| **Reputation / Standing** | Optional tracks with specific factions or organisations |

---

## 3. Design Rules

1. Guild progression should reward consistent activity rather than only the highest-end clears.
2. Perks are meaningful but never so strong that unguilded players are heavily disadvantaged in core content.
3. Progress is visible to members so that contribution feels tangible.
4. Inactivity or membership changes do not harshly punish the remaining guild; systems are designed for natural fluctuation.

---

## 4. Technical Notes

Guild experience and unlocks are stored on the guild record. Contribution events are emitted by the relevant gameplay systems and aggregated by the guild service.
