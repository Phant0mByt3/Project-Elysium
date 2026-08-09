# 0813 — Group Roles

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0301-Specializations.md](../0300-Characters/0301-Specializations.md) · [0801-Parties.md](0801-Parties.md) · [0803-Dungeon-Finder.md](0803-Dungeon-Finder.md) · [0405-Aggro-System.md](../0400-Gameplay/0405-Aggro-System.md)

---

## 1. Overview

Group roles (Tank, Healer, Damage) are the primary organising principle for matchmaking, party composition UI, and many encounter designs. Every specialisation maps to one or more roles.

---

## 2. Role Definitions

| Role | Responsibility | Typical Specs |
|------|----------------|---------------|
| **Tank** | Hold threat, absorb and mitigate damage, position enemies | Vanguard Warrior, Sentinel Paladin, etc. |
| **Healer** | Keep the group alive, manage resources and cooldowns | Lightbringer Paladin, Warden Cleric, Grovekeeper Druid, etc. |
| **Damage (DPS)** | Defeat enemies as quickly and cleanly as possible | All pure damage specialisations |

Some specialisations are hybrid and can fill more than one role depending on talent choice or loadout.

---

## 3. Design Rules

1. Role identity is clear in the UI (icons, party frames, nameplates).
2. Queue systems (Dungeon Finder, etc.) respect role and will not form groups that cannot complete the content under normal conditions.
3. Players can queue as multiple roles where their specialisation supports it; the system prefers to fill the most needed role.
4. Role does not restrict who a player can group with in manual parties — it only affects automated matchmaking and UI defaults.

---

## 4. Technical Notes

Role is derived from the character’s current specialisation and talent loadout at queue or invite time. Changes mid-run are handled according to the specific content’s rules (some instances allow mid-run respec, others do not).
