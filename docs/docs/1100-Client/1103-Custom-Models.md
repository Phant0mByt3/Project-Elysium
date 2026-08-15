# 1103 — Custom Models

## Overview
Custom 3D models used throughout Elysium's content pack ([1102-Content-Pack.md](1102-Content-Pack.md)), covering weapons, armor, NPCs, creatures, and world set-dressing beyond what default engine starter-content can express.

## Categories
* **Character Models** — race-specific player model adjustments ([0204-Races.md](../0200-Lore/0204-Races.md)) and NPC models ([0209-NPCs.md](../0200-Lore/0209-NPCs.md)).
* **Creature Models** — enemy and world boss models ([0108-World-Bosses.md](../0100-World/0108-World-Bosses.md)), designed per-region to match local bestiary themes.
* **Item Models** — weapons, armor, and accessory models ([0500-Weapons.md](../0500-Items/0500-Weapons.md) through [0502-Accessories.md](../0500-Items/0502-Accessories.md)).
* **Environmental Models** — non-block set-dressing (statues, ruins detail, foliage) used to give handcrafted regions a level of detail beyond standard block palettes.

## Pipeline
Models are produced by the art team following the standards in [1300-Art-Style.md](../1300-Art/1300-Art-Style.md) and [1306-Models.md](../1300-Art/1306-Models.md), then integrated into the content pack for distribution via the launcher.

## Technical Constraints
Model complexity and polycount budgets should be reviewed against the performance targets in [1208-Performance.md](../1200-Technical/1208-Performance.md), particularly for large-scale content like raids and world events where many models render simultaneously.


## Level of Detail (LOD) Standards

All custom models ship with multiple LOD tiers, ensuring distant or high-population scenes (world bosses, city hubs) maintain performance without requiring every player-visible model to render at full detail simultaneously.

## Reuse and Asset Libraries

Common architectural and environmental pieces are built as a reusable modular kit per region theme, balancing hand-crafted specificity (per [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md)) with realistic production timelines for a small team.
