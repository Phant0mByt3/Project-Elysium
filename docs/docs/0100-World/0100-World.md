# 0100 — World

**Category:** World
**Status:** Living Document
**Related:** [0101-Continents.md](0101-Continents.md) · [0200-Lore.md](../0200-Lore/0200-Lore.md) · [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md)

---

## 1. What is Elysium?

Elysium is the name of both the game and the world it takes place in — a realm that was shattered eight centuries ago in a cataclysm called **the Sundering**, and has been slowly reforming ever since. Landmasses that were once torn apart by the event are drifting back together, ancient magic is resurfacing, and the gods who once walked openly among mortals have gone silent. Players arrive during the **Age of Reclamation**, the current era in which civilizations are rebuilding and rediscovering what was lost.

The world is not a blank canvas for players to build on — it is a fully authored place with its own history, politics, and ongoing conflicts that the player steps into and influences, but does not fundamentally reshape through construction the way a sandbox title would.

---

## 2. Scale

At launch, Elysium consists of two fully realized continents — **Aurelia** (see [0101-Continents.md](0101-Continents.md)) and **Vethmoor** — each divided into multiple regions ([0102-Regions.md](0102-Regions.md)) scaled to a specific level range. Three further continents (Sylvaneth, the Kharzul Wastes, and Nightreach) are planned as post-launch expansions — see [0005-Future-Plans.md](../0000-Project/0005-Future-Plans.md).

| Metric | Launch Target |
| --- | --- |
| Continents at launch | 2 (Aurelia, Vethmoor) |
| Regions at launch | 10 (5 per continent) |
| Major cities | 3 (Solmere, Ashka Vor, Ironpeak Hold) |
| Dungeons at launch | 4, scaling to 6+ post-launch |
| Raid wings at launch | 1 |
| Level cap at launch | 50 |

---

## 3. Design Approach

Nothing in Elysium is procedurally generated. Every continent begins as a hand-drawn map (see [0112-Maps.md](0112-Maps.md)), is broken into regions with a defined theme, climate, and level band, and is then hand-built by the world team block by block. This is slower than generation but guarantees that every hill, ruin, and dungeon entrance was placed with intent — directly supporting the "every area has purpose" pillar in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).

The world-building pipeline runs, per region:

1. **Design brief** — level range, theme, dominant faction, local conflict (see the region template in [0102-Regions.md](0102-Regions.md)).
2. **Heightmap and biome pass** — base terrain shaping ([0116-World-Generation.md](0116-World-Generation.md), [0113-Biomes.md](0113-Biomes.md)).
3. **Landmark and settlement placement** — cities, villages, and landmarks blocked in before detail work ([0103-Cities.md](0103-Cities.md), [0104-Villages.md](0104-Villages.md), [0105-Landmarks.md](0105-Landmarks.md)).
4. **Hand-detailing pass** — texturing, foliage, prop placement per [1402-Building-Standards.md](../1400-Development/1402-Building-Standards.md).
5. **Quest and NPC population** — following [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md).
6. **Polish and playtest pass** — validated against Pillar 5 (Quality Over Quantity).

---

## 4. World Layers

* **Overworld** — continuous, open, shared world where exploration, world events, and world bosses happen. Persistent and shared by all players on a given server instance.
* **Instances** — dungeons ([0106-Dungeons.md](0106-Dungeons.md)) and raids ([0107-Raids.md](0107-Raids.md)), private per group, spun up on demand per [1209-Instance-System.md](../1200-Technical/1209-Instance-System.md).
* **Cities & Villages** — safe hubs for vendors, quest givers, and social play ([0103-Cities.md](0103-Cities.md), [0104-Villages.md](0104-Villages.md)).
* **Contested Zones** — overworld areas with active open-world PvP relevance, primarily in Vethmoor border regions.

---

## 5. Continuity and Connectivity

Continents connect to each other primarily through sea travel and, once unlocked, fast travel networks (see [0110-Travel.md](0110-Travel.md), [0111-Fast-Travel.md](0111-Fast-Travel.md)). Regions within a continent are geographically contiguous — a player can, in principle, walk from the Southern Shires to the Shattered Cairns without a loading screen, though doing so at low level is neither safe nor intended.

This continuity matters for immersion: Elysium avoids the "zone select screen" feeling of a lobby-based game. The world is one continuous space per continent, stitched together by the region and biome design in [0102-Regions.md](0102-Regions.md) and [0113-Biomes.md](0113-Biomes.md).

---

## 6. Tone and Atmosphere by Region Type

| Region Type | Tone | Design Emphasis |
| --- | --- | --- |
| Starting zones | Hopeful, pastoral | Gentle onboarding, low threat |
| Mid-level frontier | Tense, contested | Faction conflict, moderate danger |
| High-level border zones | Harsh, militarized | Open PvP relevance, high danger |
| Endgame / Sundering-scarred | Oppressive, alien | Raid and mythic-tier content, visual corruption |

---

## 7. See Also

[0200-Lore.md](../0200-Lore/0200-Lore.md) for the history and mythology behind the world's current state, [0201-Timeline.md](../0200-Lore/0201-Timeline.md) for the chronological account of the Sundering, and [0203-Factions.md](../0200-Lore/0203-Factions.md) for how the Dawnbound Concord and Duskward Pact shape which parts of the world are safe, contested, or hostile to a given player.

---

## 8. Ownership and Update Process

World design is owned by the World Director (see [0007-Team-Structure.md](../0000-Project/0007-Team-Structure.md)). Any change to continent count, region boundaries, or level ranges must be reflected here and in [0101-Continents.md](0101-Continents.md) / [0102-Regions.md](0102-Regions.md) before it is considered final, per the documentation-first workflow in [0008-Development-Philosophy.md](../0000-Project/0008-Development-Philosophy.md).
