# 134 — Icons

## Overview
Icon standards for skills ([42-Skills.md](42-Skills.md)), items ([50-Weapons.md](50-Weapons.md) onward), status effects ([47-Status-Effects.md](47-Status-Effects.md)), and UI actions.

## Design Rules
* Icons must be legible at the smallest rendered size used in-game (typically a 32–40px action bar slot), with a strong silhouette readable even before color is perceived.
* Skill icons should visually hint at their effect (a shield icon for a defensive cooldown, a flame for a fire ability) rather than being purely decorative.
* Icon border color communicates rarity ([53-Loot.md](53-Loot.md)) or resource type consistently across all UI contexts.

## Categories
* **Skill Icons** — per-class, per-specialization ([41-Specializations.md](41-Specializations.md)).
* **Item Icons** — per item type and rarity tier.
* **Status Effect Icons** — buffs, debuffs, CC ([47-Status-Effects.md](47-Status-Effects.md)), color-coded by category and colorblind-safe per [116-Accessibility.md](116-Accessibility.md).
* **UI Action Icons** — menu, map, social panel icons.

## Production
Icon production follows the same pipeline and review process as other 2D assets described in [130-Art-Style.md](130-Art-Style.md).
