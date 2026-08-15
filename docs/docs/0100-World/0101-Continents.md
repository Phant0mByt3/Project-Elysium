# 0101 — Continents

**Category:** World
**Status:** Living Document
**Related:** [0100-World.md](0100-World.md) · [0102-Regions.md](0102-Regions.md) · [0005-Future-Plans.md](../0000-Project/0005-Future-Plans.md)

---

## 1. Overview

Elysium is made up of five continents, two of which are available at launch. Each continent has a distinct theme, climate, dominant races, and level range. Continents are the largest geographic unit in the game and each anchors one major arc of the main story (see [0207-Main-Story.md](../0200-Lore/0207-Main-Story.md)).

| Continent | Status | Level Range | Dominant Culture | Faction Lean |
| --- | --- | --- | --- | --- |
| Aurelia | Launch | 1–30 | Human | Dawnbound Concord |
| Vethmoor | Launch | 25–50 | Dwarf / Orc | Contested |
| Sylvaneth | Expansion 1 | 50–65 | Elf | Neutral, faction-influenced |
| Kharzul Wastes | Expansion 2 | 65–80 | Beastkin | Duskward-leaning |
| Nightreach | Expansion 3 | 80+ (endgame) | Revenant / corrupted | Neutral, threat-driven |

---

## 2. Aurelia *(Launch — Levels 1–30)*

The human heartland and the game's starting continent. Temperate plains, rolling farmland, and the capital city of **Solmere** (see [0103-Cities.md](0103-Cities.md)). Home to the Dawnbound Concord's seat of power. New characters of every race begin their journey in Aurelia's southern shires before the story sends them further afield.

**Climate:** temperate, four distinct seasons, mostly plains and low hills with pockets of dense forest and wetland.

**Geography:** bordered by coastline to the south and east, forested highlands to the north, and the Greywater Fens marking its eastern transition toward the coast where ships depart for Vethmoor.

**Narrative role:** establishes the Age of Concord's legacy, introduces the player to the Sundering's aftermath at a human scale, and sets up the ideological foundation of the Dawnbound Concord before the player ever sets foot in contested territory.

**Regions:** see the full breakdown in [0102-Regions.md](0102-Regions.md) — the Southern Shires, Wildwood Reach, the Greywater Fens, the Sunspire Hills, and the Solmere Capital District.

---

## 3. Vethmoor *(Launch — Levels 25–50)*

A continent of snow-capped highlands, deep mines, and fortified holds, shared by the Dwarven clans and Orcish tribes. Politically split between Dawnbound-aligned dwarven holds and Duskward-aligned orc clans, making it the primary early PvP frontier (see [0806-Territory-Control.md](../0800-Multiplayer/0806-Territory-Control.md)).

**Climate:** cold, mountainous, with active volcanic zones in its southern reaches contrasting with glacial tundra in the north.

**Geography:** a single large landmass dominated by a central mountain range, split roughly down the middle into dwarven-held western holds and orc-held eastern tundra, with a heavily contested border strip running north to south.

**Narrative role:** the first continent where the player directly experiences the Dawnbound/Duskward conflict as an active, contested reality rather than as history — most of the continent's questing is framed around the border conflict.

**Regions:** Frostgate Approach, the Ember Deeps, Ashenclaw Tundra, the Ironpeak Holds, and the Shattered Cairns — see [0102-Regions.md](0102-Regions.md).

---

## 4. Sylvaneth *(Planned — Expansion 1)*

The elven forest continent — ancient, vertical, and half-swallowed by an enormous world-tree canopy. Its design leans heavily into verticality, with settlements and pathways built into and between the branches of the world-tree rather than purely on the forest floor. See [1502-Expansion-Story-Structure.md](../1500-Expansions/1502-Expansion-Story-Structure.md).

**Design intent:** the first continent to break from Aurelia and Vethmoor's largely ground-plane traversal, introducing new travel mechanics (canopy paths, tree-lift networks) that build on [0110-Travel.md](0110-Travel.md).

---

## 5. Kharzul Wastes *(Planned — Expansion 2)*

A scorched desert continent of beastkin nomad clans and buried pre-Sundering ruins. See [1503-Expansion-World-Design.md](../1500-Expansions/1503-Expansion-World-Design.md).

**Design intent:** heavy emphasis on buried Age of Concord ruins as dungeon and landmark content, tying directly into [0214-Ancient-Civilisations.md](../0200-Lore/0214-Ancient-Civilisations.md) and [0215-Ancient-Archivarium.md](../0200-Lore/0215-Ancient-Archivarium.md).

---

## 6. Nightreach *(Planned — Expansion 3, endgame-focused)*

A continent still visibly warped by the Sundering, home to Kaelgorath's remaining corruption and the Revenant race's origin. See [1504-Expansion-Feature-Planning.md](../1500-Expansions/1504-Expansion-Feature-Planning.md).

**Design intent:** the endgame-focused continent, gated behind reaching the level cap on prior continents, framed as the culmination of the long-term main story arc referenced in [9004-Long-Term-Story.md](../9000-Future/9004-Long-Term-Story.md).

---

## 7. Structure Per Continent

Each continent document (this file's per-continent sections, expanding over time) should define:

* **Theme and climate**
* **Level range**
* **Dominant faction presence**
* **Major cities**
* **Its role in the main story**
* **Its relationship to the continents that came before it**, so the world feels like one connected place rather than disconnected level-gated maps

Regional-level detail belongs in [0102-Regions.md](0102-Regions.md); city-level detail in [0103-Cities.md](0103-Cities.md).

---

## 8. Inter-Continental Travel

Continents are connected by sea routes and, at higher levels, mage-portal networks unlocked through story progression (see [0111-Fast-Travel.md](0111-Fast-Travel.md)). A player cannot fast-travel to a continent they have not yet unlocked through the main story, preventing high-level players from skipping earlier world-building content entirely and low-level players from wandering into content far above their level unprepared.

---

## 9. Design Consistency Checklist

When adding a new continent to this document, confirm it:

* Has a clear thematic identity distinct from all existing continents.
* Has a defined level range that extends the leveling curve in [0305-Leveling.md](../0300-Characters/0305-Leveling.md) without large overlapping gaps.
* Ties into at least one existing faction, race, or lore thread rather than existing in isolation.
* Has been reviewed against [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md), particularly Pillar 2 (Every Area Has Purpose).
