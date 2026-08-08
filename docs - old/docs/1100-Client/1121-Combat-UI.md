# 1121 — Combat UI

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [0401-Combat.md](../0400-Gameplay/0401-Combat.md) · [0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md) · [1301-UI-Style.md](../1300-Art/1301-UI-Style.md) · [1106-Accessibility.md](1106-Accessibility.md)

---

## 1. Overview

Combat UI covers action bars, resource displays, unit frames, nameplates, cast bars, and status effect indicators — everything the player relies on in active combat.

---

## 2. Core Elements

| Element | Purpose |
|---------|---------|
| **Action Bars** | Abilities and items |
| **Player / Target Frames** | Health, resources, key auras |
| **Party / Raid Frames** | Group health and status |
| **Nameplates** | Enemy/ally identification and health |
| **Cast / Channel Bars** | Telegraphs and self-casts |
| **Buff / Debuff Icons** | Status effects with clear categorisation |

---

## 3. Design Rules

1. Critical information (player health, incoming telegraphs, major cooldowns) is prioritised and never obscured by optional elements.
2. Colour and icon design remain colourblind-safe.
3. Layout defaults work for both solo and group play; advanced customisation is available.
4. Performance of nameplates and frames is budgeted for large raid and world-event scenarios.
