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
| **Tank** | Hold threat, absorb and mitigate damage, position enemies | Vanguard (tank spec), Oathkeeper (tank spec) |
| **Healer** | Keep the group alive, manage resources and cooldowns | Oathkeeper (healer spec), Warden (healer spec) |
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


## 5. Off-Spec Queuing

Players may queue in a secondary role using an alternate talent loadout (see [0303-Talent-Trees.md](../0300-Characters/0303-Talent-Trees.md)) without fully respeccing their primary build, encouraging role flexibility especially for filling scarce Tank and Healer queue slots.

## 6. Role Representation in World Content

Outside of instanced content, role labeling is de-emphasized in the open world, since solo and small-group world content doesn't require the same strict role coverage that dungeons and raids do.
