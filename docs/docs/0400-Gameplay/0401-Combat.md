# 0401 — Combat

**Project:** Elysium MMORPG
**Category:** Gameplay
**Status:** Living Document
**Related:** [0400-Game-Mechanics.md](0400-Game-Mechanics.md) · [0402-Enemy-Design.md](0402-Enemy-Design.md) · [0403-Boss-Mechanics.md](0403-Boss-Mechanics.md) · [0304-Stats.md](../0300-Characters/0304-Stats.md)

---

## 1. Overview

Elysium's combat is action-targeted (click or tab-target an enemy, then use abilities on cooldowns and resources) rather than simple native melee-swing PvP — combat feel is designed first as an MMORPG system, per [0001-Vision.md](../0000-Project/0001-Vision.md).

## 2. Core Loop

1. Target an enemy (tab-target or direct click).
2. Use abilities from the class's skill bar ([0302-Skills.md](../0300-Characters/0302-Skills.md)), constrained by cooldowns and a resource (mana, rage, energy, etc. per class).
3. Manage positioning — many enemy and boss abilities are telegraphed with ground-target indicators requiring movement to avoid.
4. Manage resources across the fight, building toward ultimate ability usage (see [0400-Game-Mechanics.md](0400-Game-Mechanics.md), Ultimate System).

## 3. Combat Identity

Each class should be visually and audibly distinct in combat — the Vanguard's screen shake and weapon-clash sound should never be mistaken for the Arcanist's projectile cast, even from across a crowded dungeon pull. See [1300-Art-Style.md](../1300-Art/1300-Art-Style.md) for the visual effects standards this depends on.

## 4. Damage & AI Interaction

* All damage runs through the formulas defined in [0304-Stats.md](../0300-Characters/0304-Stats.md).
* Enemy AI uses threat/aggro tables to determine targeting, giving tanks (Vanguard, Oathkeeper, Warden) a mechanical way to hold enemy attention — see [0405-Aggro-System.md](0405-Aggro-System.md).
* Status effects ([0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)) and elemental interactions ([0307-Elements.md](../0300-Characters/0307-Elements.md)) layer additional tactical depth onto the base loop.

## 5. Combat Roles

| Role | Responsibility | Example Classes |
| --- | --- | --- |
| Tank | Hold enemy aggro, mitigate incoming damage | Vanguard, Oathkeeper |
| Healer | Sustain the group through incoming damage | Warden, Oathkeeper |
| Damage | Maximize damage output within the fight's constraints | Arcanist, Shade, Wayfarer |

## 6. PvE vs PvP Combat Tuning

While the core ability kit is shared, certain values (crowd control duration, burst damage caps) are adjusted separately for PvP contexts to keep player-vs-player fights fair without weakening PvE boss design — see [0804-PvP.md](../0800-Multiplayer/0804-PvP.md).

## 7. Combat Feedback

Hit confirmation, damage numbers, and status icons are tuned for immediate legibility — a player should never be unsure whether their ability landed. Optional settings allow players to reduce visual clutter in large group fights (see [1109-Settings.md](../1100-Client/1109-Settings.md)).

## 8. Balancing Philosophy

Combat balance is treated as a continuous process, not a one-time pass — see [0309-Balance.md](../0300-Characters/0309-Balance.md) for the review cadence and tuning philosophy.
