# 1405 — Naming Conventions

## Overview
Naming standards across code, assets, and in-world content, so contributors across disciplines can predict how something is named without asking.

## Code (see [1401-Coding-Standards.md](1401-Coding-Standards.md))
Standard Unreal Engine C++ conventions: PascalCase classes, camelCase methods/variables, plugin module names prefixed `elysium-` (e.g. `elysium-combat`) per [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md).

## In-World Content
* **Regions/Zones** — Descriptive two-word names reflecting theme (e.g. "Wildwood Reach," "Ashenclaw Tundra") consistent with [0102-Regions.md](../0100-World/0102-Regions.md).
* **NPCs** — First name + optional epithet/title reflecting culture ([0204-Races.md](../0200-Lore/0204-Races.md)); avoid duplicate first names within the same region without a distinguishing surname.
* **Items** — Rarity-appropriate flavor: Common/Uncommon items use plain descriptive names; Legendary/Relic items use evocative named-artifact conventions (see [0505-Legendary-Items.md](../0500-Items/0505-Legendary-Items.md), [0506-Relics.md](../0500-Items/0506-Relics.md)).

## Asset Files
Texture, model, and sound files should follow a consistent `category_subcategory_name` file naming pattern to keep the content pack ([1102-Content-Pack.md](../1100-Client/1102-Content-Pack.md)) organized as it scales past hundreds of assets.

## Enforcement
Naming inconsistencies should be flagged during the same review pass as style/quality checks in [1400-Development-Standards.md](1400-Development-Standards.md).


## Avoiding Naming Collisions

A shared, searchable naming registry (integrated with [0209-NPCs.md](../0200-Lore/0209-NPCs.md) and the item database) helps writers and designers check for naming collisions before introducing a new NPC, item, or location name, preventing confusing duplicate names across a large content set.

## Etymological Consistency

Names within a given culture draw from a consistent linguistic "feel" established during lore development ([0204-Races.md](../0200-Lore/0204-Races.md)) — human Aurelian names lean toward familiar Western-fantasy naming patterns, while dwarven and orc names follow their own distinct phonetic patterns, keeping immersion consistent even for players who notice naming patterns.
