# 136 — Models

## Overview
This document governs the standards and pipeline for 3D model production, complementing the specific model categories already outlined in [113-Custom-Models.md](113-Custom-Models.md).

## Standards
* **Polycount Budgets** — tiered by asset type (player/NPC models get the highest budget, environmental clutter the lowest), reviewed against performance targets in [128-Performance.md](128-Performance.md).
* **Rigging & Animation** — character and creature models require a shared base rig where possible, to streamline animation reuse across similar body types (e.g. all bipedal humanoid races sharing an animation set, per [34-Races.md](34-Races.md)).
* **Texture Mapping** — models should use texture sets consistent with [135-Textures.md](135-Textures.md) rather than one-off bespoke shaders per model.

## Review Process
Every new model (weapon, armor piece, creature, NPC) is reviewed against [130-Art-Style.md](130-Art-Style.md) for silhouette clarity and stylistic consistency before being added to the resource pack ([112-Resource-Pack.md](112-Resource-Pack.md)).

## Ownership
The modeling pipeline is owned by the art team and tracked as part of the same quality gate as textures and icons — see [140-Development-Standards.md](140-Development-Standards.md).
