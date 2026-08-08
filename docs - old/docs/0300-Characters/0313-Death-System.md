# 0313 — Death System

**Project:** Elysium MMORPG  
**Category:** Characters  
**Status:** Design Complete — Implementation Pending  
**Related:** [0305-Leveling.md](0305-Leveling.md) · [0401-Combat.md](../0400-Gameplay/0401-Combat.md) · [0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md) · [0103-Cities.md](../0100-World/0103-Cities.md)

---

## 1. Overview

Death in Elysium is a setback, not a punishment spiral. The system is designed to keep players in the world and returning to the fight quickly while still giving death enough weight that players respect danger.

---

## 2. Core Rules

- On death the player becomes a spirit/ghost at the death location.
- The player may:
  - **Release** to the nearest unlocked graveyard / inn / city spirit healer, or
  - **Be resurrected** by a player with the appropriate ability (or by a spirit healer after release).
- Gear durability loss on death is modest and primarily a gold sink rather than a progress wall (see [0515-Item-Durability.md](../0500-Items/0515-Item-Durability.md)).
- No experience debt or permanent stat loss at launch.

---

## 3. Respawn & Recovery

| Location Type | Respawn Behaviour |
|---------------|-------------------|
| Open World | Nearest unlocked spirit healer / inn |
| Dungeon / Raid | Entrance or last safe checkpoint inside the instance |
| PvP / Contested | Faction-aligned spirit healer; possible corpse camping counter-measures |

After resurrection the player receives a short “Resurrection Sickness” debuff (reduced damage and healing) that fades quickly, discouraging repeated reckless deaths without being oppressive.

---

## 4. Design Goals

- Keep players in the flow of the game.
- Make group play (especially having a healer) feel valuable.
- Avoid the classic “corpse run through elite packs” frustration of older theme-park MMOs.
- Support the Hearth / Recall system ([0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md)) as a reliable “get back to safety” valve.

---

## 5. Technical Notes

Death state, corpse location, and durability changes are fully server-authoritative. The client only displays the ghost form and available release/resurrect options.
