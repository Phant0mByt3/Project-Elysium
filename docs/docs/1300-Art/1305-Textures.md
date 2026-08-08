# 1305 — Textures

## Overview
Texture standards for terrain, props, and surface materials used to realize each continent and city's visual identity within the content pack ([1102-Content-Pack.md](../1100-Client/1102-Content-Pack.md)).

## Resolution Standard
A consistent texture resolution (to be finalized during Phase 0, balanced for fidelity against Unreal Engine's PBR rendering pipeline and the performance targets in [1208-Performance.md](../1200-Technical/1208-Performance.md)) should be used uniformly, avoiding jarring resolution mismatches between reused engine assets and custom-textured surfaces.

## Regional Texture Sets
Each continent and its major cities require a dedicated texture set matching the color and material language defined in [1300-Art-Style.md](1300-Art-Style.md) and [1302-Colour-Palette.md](1302-Colour-Palette.md) — Aurelian pale stone and warm wood, Vethmoor dark granite and iron, and so on.

## Design Rules
* No default Unreal Engine starter-content textures should ship unmodified in a player-facing zone — every visible surface should be custom-textured or intentionally reused as a deliberate style choice.
* Texture variation (multiple variants of a common block) should be used to avoid obvious tiling patterns across large handcrafted builds.

## Production Pipeline
Owned by the art team, reviewed against [1400-Development-Standards.md](../1400-Development/1400-Development-Standards.md)'s quality bar before merging into the content pack.
