# 0116 — World Generation

**Category:** World
**Status:** Living Document
**Related:** [0100-World.md](0100-World.md) · [1210-World-Management.md](../1200-Technical/1210-World-Management.md)

---

## 1. Overview

Despite the name, "World Generation" in Elysium refers to the authored terrain-creation pipeline, not procedural generation. This document describes how the world team turns a region design brief into finished, playable terrain.

## 2. Pipeline Stages

1. **Heightmap authoring** — base terrain shape is sculpted using external terrain-authoring tools before import into Unreal Engine, establishing broad elevation, valleys, and ridgelines matching the region's brief in [0102-Regions.md](0102-Regions.md).
2. **Biome layer pass** — texture and foliage layers are applied according to the region's assigned biome ([0113-Biomes.md](0113-Biomes.md)).
3. **Key location placement** — cities, villages, dungeon entrances, and landmarks are placed and blocked in at low fidelity to validate the region's layout and pacing.
4. **Hand-detailing pass** — props, foliage density, rock formations, and points of interest are placed by hand, following [1402-Building-Standards.md](../1400-Development/1402-Building-Standards.md).
5. **Navigation and collision pass** — navmesh generation and collision validation for both players and AI ([0404-AI-Behaviour.md](../0400-Gameplay/0404-AI-Behaviour.md)).
6. **Lighting and atmosphere pass** — baked and dynamic lighting matched to the region's tone (see [0100-World.md](0100-World.md), Section 6).

## 3. Why Not Procedural Generation

Procedural generation was explicitly rejected for the overworld because it works against Pillar 1 and Pillar 2 in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md) — a generated landscape cannot guarantee that every hill and ruin was placed with narrative or gameplay intent. Elysium's identity depends on the world feeling deliberately authored.

## 4. Tools

The world team uses external heightmap and terrain-sculpting tools to produce base terrain data, which is then imported into Unreal Engine's Landscape system for detailed, hand-authored refinement — see [1210-World-Management.md](../1200-Technical/1210-World-Management.md) for the technical import pipeline.

## 5. Iteration and Review

Regions go through at least two internal review passes — a layout review after Stage 3 and a full polish review after Stage 6 — before being considered ready for quest population, per the world-building pipeline described in [0100-World.md](0100-World.md), Section 3.

## 6. Performance Considerations

Terrain complexity is budgeted per region to maintain target frame rates across the intended range of player hardware; the Technical Lead and World Director jointly review any region exceeding its asset/prop budget before it proceeds to the detailing pass.
