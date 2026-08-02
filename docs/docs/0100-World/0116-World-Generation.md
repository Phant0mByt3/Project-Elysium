# 0116 — World Generation

**Project:** Elysium MMORPG  
**Category:** World  
**Status:** Design Complete — Implementation Pending  
**Related:** [0100-World.md](0100-World.md) · [0113-Biomes.md](0113-Biomes.md) · [1210-World-Management.md](../1200-Technical/1210-World-Management.md) · [0001-Vision.md](../0000-Project/0001-Vision.md)

---

## 1. Philosophy

Elysium does **not** use runtime procedural world generation.

Every continent, region, mountain, river, and cave is authored offline using a combination of WorldPainter heightmaps, biome painting, and extensive hand-detailing by the World Building team. The resulting world templates are then loaded by the Instance Manager as static (or versioned) bases.

This document exists to make the “no procedural generation” rule explicit and to describe the offline production pipeline.

---

## 2. Offline Production Pipeline

1. **Concept sketch** — rough regional layout in [0112-Maps.md](0112-Maps.md).
2. **Heightmap authoring** — WorldPainter elevation brushes for mountains, valleys, coastlines.
3. **Biome painting** — WorldPainter biome layers matching the region’s assigned biomes ([0113-Biomes.md](0113-Biomes.md)).
4. **Export** — raw Minecraft region files.
5. **Hand-detailing** — builders refine terrain, add vegetation, correct artifacts, place landmarks and structure shells.
6. **Structure finalisation** — cities, dungeons, villages, and quest-critical geometry are completed.
7. **Protection & versioning** — region is locked; world template is versioned and stored for the Instance System ([1209-Instance-System.md](../1200-Technical/1209-Instance-System.md)).

---

## 3. What Is Explicitly Forbidden

- Runtime terrain generation of any kind (caves, ravines, structures, ore veins).
- Vanilla Minecraft world generators or custom noise-based generators for player-facing continents.
- Any system that would allow the world to “grow” or change shape after a region is locked.

Resource nodes (ore, herbs, trees) are pre-placed or managed by profession systems, never generated on the fly in a way that alters terrain.

---

## 4. Exceptions (Controlled)

- **Dungeon & Raid templates** — loaded as fresh copies per instance; the base template itself remains static.
- **Event overlays** — temporary props or barriers for world events may be spawned and later removed, but the underlying terrain is never modified permanently.
- **Housing plots** — player or guild housing areas are the only locations where limited player building is permitted (see [0900-Housing.md](../0900-Player-Systems/0900-Housing.md)).

---

## 5. Rationale

Handcrafted worlds guarantee that every hill, ruin, and vista was placed with intent. This directly supports Pillar 1 (Exploration is Always Rewarding) and Pillar 2 (Every Area Has Purpose) from [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md). It is slower than procedural generation, but the resulting world is the primary reason players will forget they are inside Minecraft.
