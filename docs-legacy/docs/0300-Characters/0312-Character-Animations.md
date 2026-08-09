# 0312 — Character Animations

**Project:** Elysium MMORPG  
**Category:** Characters  
**Status:** Design Complete — Implementation Pending  
**Related:** [0300-Classes.md](0300-Classes.md) · [0401-Combat.md](../0400-Gameplay/0401-Combat.md) · [1307-Animation-Style.md](../1300-Art/1307-Animation-Style.md) · [1306-Models.md](../1300-Art/1306-Models.md)

---

## 1. Overview

Animations are a primary carrier of class identity and combat readability. Every class should be recognisable from its movement and ability animations alone, even before particle effects or UI elements are considered.

---

## 2. Animation Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| **Locomotion** | Walk, run, sprint, swim, climb, mount | Shared base with class-specific flavour |
| **Combat Stance** | Idle-in-combat, weapon ready | Distinct per weapon type and class |
| **Ability Animations** | Cast, strike, channel, finish | Must telegraph clearly for both player and observers |
| **Hit Reactions** | Light, heavy, knockback, death | Consistent weight across races |
| **Emotes & Social** | Wave, cheer, sit, dance, etc. | See [0904-Emotes.md](../0900-Player-Systems/0904-Emotes.md) |
| **Death & Resurrect** | Collapse, spirit form, return | Tied to [0313-Death-System.md](0313-Death-System.md) |

---

## 3. Design Rules

1. **Telegraph priority** — any ability that can kill or control another player (or a boss) must have a readable wind-up.
2. **Class fantasy** — a Warrior’s heavy swings feel weighty; a Mage’s casts feel precise and elemental; a Rogue’s attacks feel quick and precise.
3. **Shared rigs** — bipedal humanoid races share a common skeleton where possible to maximise animation reuse ([1306-Models.md](../1300-Art/1306-Models.md)).
4. **Performance** — animation budgets are reviewed against [1208-Performance.md](../1200-Technical/1208-Performance.md), especially in large-scale raids and world events.

---

## 4. Production Pipeline

Owned by the Art team under the Animation Style and Guidelines documents ([1307-Animation-Style.md](../1300-Art/1307-Animation-Style.md), [1318-Animation-Guidelines.md](../1300-Art/1318-Animation-Guidelines.md)). New ability animations are required before a skill is considered content-complete.
