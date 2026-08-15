# 0102 — Regions

**Category:** World
**Status:** Living Document
**Related:** [0101-Continents.md](0101-Continents.md) · [0103-Cities.md](0103-Cities.md) · [0106-Dungeons.md](0106-Dungeons.md)

---

## 1. Overview

Regions are the primary zone unit players experience — smaller than a continent, larger than a single city. Each region is scoped to a level band before any building begins, per [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md), Pillar 2.

## 2. Region Template

Every region should be documented with:

* **Continent & Level Range**
* **Theme / Biome** (see [0113-Biomes.md](0113-Biomes.md))
* **Dominant Faction / Race Presence**
* **Key Locations** (cities, dungeons, landmarks)
* **Local Conflict** — the small-scale story driving quests in this region
* **Notable Enemies**
* **Environmental Hazards**, if any (see [0117-Environmental-Hazards.md](0117-Environmental-Hazards.md))

## 3. Aurelia Regions

### The Southern Shires — Levels 1–10
Starting farmland, tutorial zone. Gentle terrain, low danger. Home village: Millhaven ([0104-Villages.md](0104-Villages.md)). Local conflict: minor bandit raids threatening the harvest, used to teach core combat and questing systems (see [0409-Tutorial-System.md](../0400-Gameplay/0409-Tutorial-System.md)).

### Wildwood Reach — Levels 8–16
Overgrown forest, bandit activity. Denser, more vertical terrain than the Shires. Local conflict: an organized bandit confederation using the forest cover to raid trade routes between Millhaven and Solmere.

### The Greywater Fens — Levels 14–20
Marshland, undead incursions. Home to Fenwick Crossing. Local conflict: restless dead rising from pre-Sundering burial grounds disturbed by encroaching settlement — this region's dungeon, the Drowned Chapel, resolves the arc.

### The Sunspire Hills — Levels 18–25
Rolling gold hills, Concord military presence. Local conflict: Concord logistics and training grounds preparing for the journey to Vethmoor; contains the landmark Sundered Spire.

### Solmere Capital District — Any level
Hub region surrounding the capital. Not level-gated; always safe. Functions as the social and economic center of Aurelia.

## 4. Vethmoor Regions

### Frostgate Approach — Levels 24–30
Mountain pass, contested border. The first taste of Dawnbound/Duskward conflict for players arriving from Aurelia.

### The Ember Deeps — Levels 28–36
Volcanic underground mines. Home to the Ember Foundry dungeon; local conflict centers on a rogue forge-construct uprising threatening dwarven mining operations.

### Ashenclaw Tundra — Levels 34–42
Orc clan territory, open PvP hotspots. Local conflict: clan rivalries and Duskward military buildup along the border.

### The Ironpeak Holds — Levels 38–46
Dwarven fortress-cities. Political and economic heart of Dawnbound Vethmoor.

### The Shattered Cairns — Levels 44–50
Endgame pre-raid zone, Sundering scarring. Visually distinct from the rest of Vethmoor — the ground itself shows lingering damage from the Sundering, foreshadowing Nightreach.

## 5. Region Design Process

1. Design brief drafted (theme, level range, faction, local conflict) and reviewed against neighboring regions for pacing.
2. Terrain blocked out following [0116-World-Generation.md](0116-World-Generation.md).
3. Key locations placed: at least one city or village, at least one dungeon or landmark.
4. Quest population following [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md).
5. Enemy density and level curve tuned against [0304-Stats.md](../0300-Characters/0304-Stats.md) and [0406-Difficulty-System.md](../0400-Gameplay/0406-Difficulty-System.md).

## 6. Pacing Guidelines

* No more than a 6–8 level gap between adjacent regions on the same continent, to keep the leveling curve smooth.
* Every region should take an average player 3–6 hours to fully quest through at its intended level.
* At least one region per continent should include meaningful open-world PvP relevance once the player reaches contested content (Vethmoor's border regions serve this role at launch).

## 7. Future Region Expansion

Additional regions are added as continents expand — see [0101-Continents.md](0101-Continents.md) for Sylvaneth, the Kharzul Wastes, and Nightreach, whose region breakdowns will be documented here once world-building begins on each.
