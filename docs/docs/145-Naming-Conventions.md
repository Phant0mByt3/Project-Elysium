# 145 — Naming Conventions

## Overview
Naming standards across code, assets, and in-world content, so contributors across disciplines can predict how something is named without asking.

## Code (see [141-Coding-Standards.md](141-Coding-Standards.md))
Standard Java conventions: PascalCase classes, camelCase methods/variables, plugin module names prefixed `elysium-` (e.g. `elysium-combat`) per [120-Plugin-Architecture.md](120-Plugin-Architecture.md).

## In-World Content
* **Regions/Zones** — Descriptive two-word names reflecting theme (e.g. "Wildwood Reach," "Ashenclaw Tundra") consistent with [12-Regions.md](12-Regions.md).
* **NPCs** — First name + optional epithet/title reflecting culture ([34-Races.md](34-Races.md)); avoid duplicate first names within the same region without a distinguishing surname.
* **Items** — Rarity-appropriate flavor: Common/Uncommon items use plain descriptive names; Legendary/Relic items use evocative named-artifact conventions (see [55-Legendary-Items.md](55-Legendary-Items.md), [56-Relics.md](56-Relics.md)).

## Asset Files
Texture, model, and sound files should follow a consistent `category_subcategory_name` file naming pattern to keep the resource pack ([112-Resource-Pack.md](112-Resource-Pack.md)) organized as it scales past hundreds of assets.

## Enforcement
Naming inconsistencies should be flagged during the same review pass as style/quality checks in [140-Development-Standards.md](140-Development-Standards.md).
