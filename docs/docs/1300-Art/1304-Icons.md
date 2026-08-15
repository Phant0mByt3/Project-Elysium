# 1304 — Icons

## Overview
Icon standards for skills ([0302-Skills.md](../0300-Characters/0302-Skills.md)), items ([0500-Weapons.md](../0500-Items/0500-Weapons.md) onward), status effects ([0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)), and UI actions.

## Design Rules
* Icons must be legible at the smallest rendered size used in-game (typically a 32–40px action bar slot), with a strong silhouette readable even before color is perceived.
* Skill icons should visually hint at their effect (a shield icon for a defensive cooldown, a flame for a fire ability) rather than being purely decorative.
* Icon border color communicates rarity ([0503-Loot.md](../0500-Items/0503-Loot.md)) or resource type consistently across all UI contexts.

## Categories
* **Skill Icons** — per-class, per-specialization ([0301-Specializations.md](../0300-Characters/0301-Specializations.md)).
* **Item Icons** — per item type and rarity tier.
* **Status Effect Icons** — buffs, debuffs, CC ([0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)), color-coded by category and colorblind-safe per [1106-Accessibility.md](../1100-Client/1106-Accessibility.md).
* **UI Action Icons** — menu, map, social panel icons.

## Production
Icon production follows the same pipeline and review process as other 2D assets described in [1300-Art-Style.md](1300-Art-Style.md).


## Icon Production Volume

Given the scale of the launch content (six classes, dozens of talent nodes each, hundreds of items), icon production is planned with a modular base-icon-plus-overlay system for common variations (e.g. a base sword icon with a color/glow overlay for rarity) to keep production time sustainable without sacrificing visual distinctiveness for build-defining items.

## Class Icon Identity

Each class's ability icons share a subtle consistent visual motif (e.g. Arcanist icons favor angular, crystalline shapes; Warden icons favor organic, leaf-based shapes) reinforcing class fantasy recognition even at a glance across a crowded action bar.
