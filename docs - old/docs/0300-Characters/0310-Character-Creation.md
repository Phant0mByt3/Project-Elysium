# 0310 — Character Creation

**Project:** Elysium MMORPG  
**Category:** Characters  
**Status:** Design Complete — Implementation Pending  
**Related:** [0300-Classes.md](0300-Classes.md) · [0204-Races.md](../0200-Lore/0204-Races.md) · [0203-Factions.md](../0200-Lore/0203-Factions.md) · [0311-Character-Customisation.md](0311-Character-Customisation.md) · [1100-Launcher.md](../1100-Client/1100-Launcher.md)

---

## 1. Overview

Character creation is the player’s first sustained contact with Elysium’s identity. It must feel like stepping into a living world rather than filling out a form. The flow is deliberately ordered: Race → Faction → Class → Appearance → Name → Confirmation.

---

## 2. Creation Flow

1. **Race Selection**  
   Player chooses from the six launch races (Human, High Elf, Dwarf, Orc, Beastkin, Revenant). Each race card shows a short lore blurb, default faction lean, and racial passive summary. Race does **not** restrict class choice.

2. **Faction Selection**  
   Dawnbound Concord or Duskward Pact. Faction choice determines starting story framing, city access, and PvP allegiance. Players may choose against their race’s statistical lean.

3. **Class Selection**  
   One of the eight launch classes. Each class presents its fantasy, available specialisations (unlocked later), and primary roles. A short “how this class feels” combat preview is desirable but not required for MVP.

4. **Appearance**  
   See [0311-Character-Customisation.md](0311-Character-Customisation.md). Full customisation of face, body, hair, markings, and starting outfit colours within racial limits.

5. **Name**  
   Free-text name with server-side filters for length, forbidden terms, and basic uniqueness. Titles are earned later, not chosen here.

6. **Confirmation & Tutorial Entry**  
   Player is placed into the appropriate starting experience (Southern Shires for most Concord characters, equivalent Duskward tutorial for Pact characters).

---

## 3. Design Rules

- No permanent, irreversible decisions beyond race and faction at creation. Class is permanent; specialisation and talents are respeccable.
- The UI should feel diegetic where possible (old parchment, forged frames) consistent with [1301-UI-Style.md](../1300-Art/1301-UI-Style.md).
- Creation must work entirely offline/local until the player confirms and the launcher authenticates the new character with the account service ([1204-Authentication.md](../1200-Technical/1204-Authentication.md)).

---

## 4. Technical Notes

Character data is written to the central database only after final confirmation. Incomplete creation sessions are discarded. The launcher handles the presentation layer; the server validates the final payload.
