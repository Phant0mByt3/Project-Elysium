# 135 — Textures

## Overview
Texture standards for blocks, terrain, and surface materials used to realize each continent and city's visual identity within the resource pack ([112-Resource-Pack.md](112-Resource-Pack.md)).

## Resolution Standard
A consistent texture resolution (to be finalized during Phase 0, likely 32x or 64x to balance fidelity against Minecraft's block-based rendering and the performance targets in [128-Performance.md](128-Performance.md)) should be used uniformly, avoiding jarring resolution mismatches between vanilla-adjacent and custom-textured blocks.

## Regional Texture Sets
Each continent and its major cities require a dedicated texture set matching the color and material language defined in [130-Art-Style.md](130-Art-Style.md) and [132-Colour-Palette.md](132-Colour-Palette.md) — Aurelian pale stone and warm wood, Vethmoor dark granite and iron, and so on.

## Design Rules
* No vanilla Minecraft textures should ship unmodified in a player-facing zone — every visible surface should be retextured or intentionally reused as a deliberate style choice.
* Texture variation (multiple variants of a common block) should be used to avoid obvious tiling patterns across large handcrafted builds.

## Production Pipeline
Owned by the art team, reviewed against [140-Development-Standards.md](140-Development-Standards.md)'s quality bar before merging into the resource pack.
