# 1306 — Models

## Overview
This document governs the standards and pipeline for 3D model production, complementing the specific model categories already outlined in [1103-Custom-Models.md](../1100-Client/1103-Custom-Models.md).

## Standards
* **Polycount Budgets** — tiered by asset type (player/NPC models get the highest budget, environmental clutter the lowest), reviewed against performance targets in [1208-Performance.md](../1200-Technical/1208-Performance.md).
* **Rigging & Animation** — character and creature models require a shared base rig where possible, to streamline animation reuse across similar body types (e.g. all bipedal humanoid races sharing an animation set, per [0204-Races.md](../0200-Lore/0204-Races.md)).
* **Texture Mapping** — models should use texture sets consistent with [1305-Textures.md](1305-Textures.md) rather than one-off bespoke rendering effects per model.

## Review Process
Every new model (weapon, armor piece, creature, NPC) is reviewed against [1300-Art-Style.md](1300-Art-Style.md) for silhouette clarity and stylistic consistency before being added to the content pack ([1102-Content-Pack.md](../1100-Client/1102-Content-Pack.md)).

## Ownership
The modeling pipeline is owned by the art team and tracked as part of the same quality gate as textures and icons — see [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md).


## Modular Kit Strategy

Environmental models are built as modular kits per region (wall segments, roof pieces, doorways) that can be recombined by the world team during the hand-detailing pass ([0116-World-Generation.md](../0100-World/0116-World-Generation.md)), balancing production efficiency with the "every piece placed with intent" philosophy in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).

## Creature and NPC Variation

Common NPC and creature base models support palette and minor geometry variation (scars, accessories, coloring) to avoid an army of visually identical enemies filling out a region's population, without requiring a fully unique model for every individual NPC.
