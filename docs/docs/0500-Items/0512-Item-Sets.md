# 0512 — Item Sets

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0501-Armour.md](0501-Armour.md) · [0503-Loot.md](0503-Loot.md) · [0107-Raids.md](../0100-World/0107-Raids.md) · [0303-Talent-Trees.md](../0300-Characters/0303-Talent-Trees.md)

---

## 1. Overview

Item sets reward collecting related pieces with progressive bonuses. They are a classic theme-park tool for giving raid and dungeon loot a clear identity and for encouraging players to complete a theme rather than cherry-picking pure stats.

---

## 2. Set Structure

- Most sets contain 2–6 pieces (typically head, shoulders, chest, gloves, legs, and sometimes a weapon or trinket).
- Bonuses unlock at 2-piece, 4-piece, and (for larger sets) 6-piece thresholds.
- Bonuses should reinforce a specialisation’s fantasy or a clear playstyle rather than giving generic “+X% damage”.

---

## 3. Design Rules

1. Set bonuses must be interesting enough that players sometimes choose a set piece over a higher item-level non-set alternative.
2. No set should be mandatory for a specialisation to function; they are power and flavour multipliers.
3. Visual cohesion is important — set pieces should look like they belong together even under transmog restrictions if the player chooses to display them.
4. Tier sets for each major raid tier are planned; dungeon sets and profession sets may also exist at lower intensity.

---

## 4. Tracking

The character sheet and a dedicated Collections UI ([0907-Collections.md](../0900-Player-Systems/0907-Collections.md)) show set progress and active bonuses.


---

## 5. Set Bonus Examples

**Vanguard Tier Set (2-piece):** reduces the cooldown of the class's primary defensive ability. **(4-piece):** the same ability now also generates a burst of threat, reinforcing the tank fantasy.

**Arcanist Tier Set (2-piece):** increases damage of the player's currently active elemental affinity ([0307-Elements.md](../0300-Characters/0307-Elements.md)). **(4-piece):** switching elemental affinity grants a brief damage window, rewarding active element-swapping play.

## 6. Set Design Cadence

A new tier set is designed alongside each new raid tier, reviewed by the Lead Game Designer against existing sets to ensure it introduces a genuinely new playstyle incentive rather than repeating a prior tier's bonus with bigger numbers.
