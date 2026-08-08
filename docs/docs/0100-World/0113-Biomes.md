# 0113 — Biomes

**Project:** Elysium MMORPG  
**Category:** World  
**Status:** Design Complete — Implementation Pending  
**Related:** [0100-World.md](0100-World.md) · [0101-Continents.md](0101-Continents.md) · [0102-Regions.md](0102-Regions.md) · [1300-Art-Style.md](../1300-Art/1300-Art-Style.md) · [1210-World-Management.md](../1200-Technical/1210-World-Management.md)

---

## 1. Overview

Biomes in Elysium are authored, not generated. Each region is assigned a primary biome (and optional secondary biomes) during the design phase of [0102-Regions.md](0102-Regions.md) so that terrain, vegetation, lighting, weather, and enemy placement remain thematically consistent.

Unreal Engine’s default biome system is used only as a technical substrate; visual and gameplay identity come from the custom content pack and hand-placed features.

---

## 2. Biome Categories

| Category | Description | Example Regions |
|----------|-------------|-----------------|
| **Temperate Pastoral** | Rolling farmland, gentle hills, warm light | Southern Shires, Sunspire Hills |
| **Temperate Forest** | Dense woodland, mixed deciduous/evergreen | Wildwood Reach |
| **Wetland / Marsh** | Flooded lowlands, fog, undead-friendly | Greywater Fens |
| **Highland / Mountain** | Steep slopes, rocky outcrops, thin air | Frostgate Approach, Ironpeak Holds |
| **Volcanic / Ash** | Blackened earth, lava flows, heat haze | Ember Deeps |
| **Tundra / Steppe** | Cold open plains, sparse vegetation, strong winds | Ashenclaw Tundra |
| **Sundered / Corrupted** | Twisted terrain, residual magic scarring | Shattered Cairns |
| **Coastal** | Cliffs, beaches, tidal zones | Coastal Aurelia approaches |

Future continents introduce additional categories (ancient canopy forest for Sylvaneth, desert for Kharzul Wastes, corrupted wasteland for Nightreach).

---

## 3. Design Rules

1. Every region has one primary biome that dominates 70 %+ of its area.
2. Secondary biomes may appear at borders or in specialised sub-zones (e.g. a volcanic fissure inside a tundra region).
3. Biome choice must support the region’s level range, local conflict, and visual identity defined in the region template.
4. Transition zones between biomes are deliberately authored so that travel feels natural rather than abrupt.

---

## 4. Gameplay Impact

- **Enemy placement** — certain creature types are restricted to matching biomes (undead thrive in wetlands, fire elementals in volcanic zones).
- **Profession nodes** — Mining, Herbalism, and Woodcutting nodes are biome-gated (see [0601-Mining.md](../0600-Professions/0601-Mining.md) onward).
- **Weather & hazards** — each biome has a preferred weather profile and possible environmental hazards (see [0114-Weather-System.md](0114-Weather-System.md) and [0117-Environmental-Hazards.md](0117-Environmental-Hazards.md)).
- **Art direction** — texture sets, foliage, and colour grading are biome-specific ([1305-Textures.md](../1300-Art/1305-Textures.md), [1302-Colour-Palette.md](../1300-Art/1302-Colour-Palette.md)).

---

## 5. Technical Notes

Biome data is stored in the world templates managed by [1210-World-Management.md](../1200-Technical/1210-World-Management.md). Custom biome definitions drive temperature, humidity, and precipitation so that weather and foliage behaviour match the authored design.
