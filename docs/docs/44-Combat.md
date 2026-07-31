# 44 — Combat

## Overview
Elysium's combat is action-targeted (click or tab-target an enemy, then use abilities on cooldowns and resources) rather than Minecraft's native melee-swing PvP — combat feel is designed first as an MMORPG system, per [01-Vision.md](01-Vision.md).

## Core Loop
1. Target an enemy (tab-target or direct click).
2. Use abilities from the class's skill bar ([42-Skills.md](42-Skills.md)), constrained by cooldowns and a resource (mana, rage, energy, etc. per class).
3. Manage positioning — many enemy and boss abilities are telegraphed with ground-target indicators requiring movement to avoid.

## Combat Identity
Each class should be visually and audibly distinct in combat — the Warrior's screen shake and weapon-clash sound should never be mistaken for the Mage's projectile cast, even from across a crowded dungeon pull. See [130-Art-Style.md](130-Art-Style.md) for the visual effects standards this depends on.

## Damage & AI Interaction
* All damage runs through the formulas defined in [45-Stats.md](45-Stats.md).
* Enemy AI uses threat/aggro tables to determine targeting, giving tanks (Warrior, Paladin, Druid) a mechanical way to hold enemy attention.
* Status effects ([47-Status-Effects.md](47-Status-Effects.md)) and elemental interactions ([48-Elements.md](48-Elements.md)) layer additional tactical depth onto the base loop.

## Balancing Philosophy
Combat balance is treated as a continuous process, not a one-time pass — see [49-Balance.md](49-Balance.md) for the review cadence and tuning philosophy.
