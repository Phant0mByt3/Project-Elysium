# 0113 — Biomes

**Category:** World
**Status:** Living Document
**Related:** [0116-World-Generation.md](0116-World-Generation.md) · [0102-Regions.md](0102-Regions.md)

---

## 1. Overview

Biomes define the base terrain, foliage, and environmental palette used to hand-build each region. Every region is assigned a primary biome (and sometimes a secondary transitional biome at its borders) during the design brief stage described in [0102-Regions.md](0102-Regions.md).

## 2. Launch Biomes

| Biome | Continent(s) | Example Region |
| --- | --- | --- |
| Temperate Plains | Aurelia | The Southern Shires |
| Dense Forest | Aurelia | Wildwood Reach |
| Wetland / Marsh | Aurelia | The Greywater Fens |
| Golden Hills | Aurelia | The Sunspire Hills |
| Alpine / Snow | Vethmoor | Frostgate Approach |
| Volcanic / Underground | Vethmoor | The Ember Deeps |
| Tundra | Vethmoor | Ashenclaw Tundra |
| Sundering-Scarred | Vethmoor | The Shattered Cairns |

## 3. Biome Transitions

Borders between biomes are hand-blended rather than sharply cut, using transitional foliage and terrain textures so the world reads as continuous geography rather than a patchwork of distinct zones (see [0116-World-Generation.md](0116-World-Generation.md) for the terrain pipeline).

## 4. Biome and Gameplay Interaction

Biomes influence more than visuals:

* **Weather patterns** are biome-appropriate (see [0114-Weather-System.md](0114-Weather-System.md)).
* **Environmental hazards** vary by biome (heat in volcanic zones, cold exposure in alpine zones — see [0117-Environmental-Hazards.md](0117-Environmental-Hazards.md)).
* **Gathering nodes** for professions are biome-specific (see [0601-Mining.md](../0600-Professions/0601-Mining.md)).

## 5. Future Biomes

Sylvaneth introduces a **canopy forest** biome, the Kharzul Wastes introduce a **desert** biome, and Nightreach introduces a **corrupted wasteland** biome — each expanding this table once world-building for those continents begins (see [0101-Continents.md](0101-Continents.md)).
