# 0912 — Loadouts

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0301-Specializations.md](../0300-Characters/0301-Specializations.md) · [0303-Talent-Trees.md](../0300-Characters/0303-Talent-Trees.md) · [0500-Items/](../0500-Items/) · [0401-Combat.md](../0400-Gameplay/0401-Combat.md)

---

## 1. Overview

Loadouts let players save and quickly switch between different equipment, talent, and specialisation configurations. They support players who fill multiple roles or who want optimised setups for different content types (raiding, PvP, leveling, crafting).

---

## 2. What a Loadout Stores

- Specialisation
- Talent configuration
- Equipped gear (by item instance or by slot preferences)
- Optional action-bar / keybind layout (client-side preference)
- Name and icon for easy identification

---

## 3. Design Rules

1. Switching loadouts is restricted or blocked in combat and inside most instances to prevent mid-fight abuse.
2. The number of saved loadouts is generous but finite.
3. Loadout switching should be fast and reliable once the player is in a safe context.
4. Visual feedback clearly shows which loadout is active.

---

## 4. Technical Notes

Loadout definitions are stored on the character. Application of a loadout validates ownership of the referenced items and talent validity before committing changes. All swaps are server-authoritative.


---

## Additional Detail: Loadout Switching

Loadouts bundle a talent build, action bar layout, and equipment set (via the transmog and gear-swap systems) into a single saved profile, letting players switch between a raiding loadout and a PvP loadout in a few clicks rather than manually reconfiguring each component.

## Loadout Restrictions

Loadout switching is disabled during active combat and within a short cooldown after combat ends, preventing loadout-swapping from being used as an exploit to bypass intended encounter pacing.
