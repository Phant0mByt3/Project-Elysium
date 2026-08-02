# 0517 — Unique Effects

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0505-Legendary-Items.md](0505-Legendary-Items.md) · [0506-Relics.md](0506-Relics.md) · [0516-Item-Attributes.md](0516-Item-Attributes.md) · [0401-Combat.md](../0400-Gameplay/0401-Combat.md)

---

## 1. Overview

Unique effects are the non-standard mechanical behaviours that make certain items memorable: on-use abilities, procs, conditional bonuses, and build-defining powers. They are the difference between “another pair of boots” and “the boots that change how I play”.

---

## 2. Categories

| Type | Description | Typical Home |
|------|-------------|--------------|
| **On-Use** | Active ability with cooldown | Trinkets, some weapons |
| **Proc** | Chance to trigger on hit, crit, or other events | Weapons, trinkets, jewellery |
| **Conditional** | Bonus while a condition is met (low health, moving, etc.) | Various |
| **Build-Defining** | Strongly alters a rotation or talent choice | Legendary items, certain set bonuses |
| **Utility** | Non-damage effects (movement, crowd control, threat) | Various |

---

## 3. Design Rules

1. Unique effects must be readable — the player should understand what happened and why.
2. Proc rates and internal cooldowns are tuned so that effects feel exciting without flooding the combat log or UI.
3. Build-defining effects are reserved for Legendary and Relic tiers or high-end set bonuses; they are not common on blue items.
4. Effects are tested for synergy and conflict with existing class kits to avoid accidental dominance or dead combinations.

---

## 4. Technical Notes

Unique effects are implemented as scripted or data-driven behaviours inside the combat plugin. All triggers and outcomes are server-authoritative; client only plays the associated visuals and sounds.
