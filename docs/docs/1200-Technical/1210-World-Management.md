# World Management

**Project:** Elysium MMORPG
**Category:** Technical
**Status:** Design Complete — Implementation Pending
**Related Systems:** [../0100-World/0100-World.md](../0100-World/0100-World.md) · [../0100-World/0101-Continents.md](../0100-World/0101-Continents.md) · [../0100-World/0103-Cities.md](../0100-World/0103-Cities.md) · [../0100-World/0106-Dungeons.md](../0100-World/0106-Dungeons.md) · [1209-Instance-System.md](1209-Instance-System.md) · [1208-Performance.md](1208-Performance.md)

---

## 1. World Philosophy

Elysium's world is **handcrafted, not procedurally generated**. Every continent, dungeon, city, and landmark exists because a designer placed it there deliberately, in service of the world's lore (see [../0200-Lore/0200-Lore.md](../0200-Lore/0200-Lore.md)) and gameplay pacing.

This document is the engineering reference for how that handcrafted world is built, stored, protected, and operated at runtime — the production pipeline behind the creative vision described in [../0100-World/0100-World.md](../0100-World/0100-World.md).

---

## 2. Handcrafted World Approach

| Principle | Description |
|---|---|
| No procedural terrain generation | All terrain is authored by hand or through guided terrain-editing tools |
| Design-first placement | Landmarks, dungeons, and cities are placed to support quest pacing and travel flow, not generated after the fact |
| Iteration via WorldPainter | Terrain shaping happens in WorldPainter before detailed hand-building begins (see §3) |
| Consistent scale | All continents follow the sizing standards in §12 to keep travel time and content density predictable |

---

## 3. Terrain Creation

Terrain production follows a fixed pipeline:

1. **Heightmap design** — base elevation authored in WorldPainter using layered brushes for mountains, valleys, and coastlines.
2. **Biome painting** — biome regions painted onto the heightmap to match the continent's design brief (see [../0100-World/0102-Regions.md](../0100-World/0102-Regions.md)).
3. **Export to Minecraft world format** — WorldPainter exports a raw terrain base.
4. **Hand-detailing pass** — builders manually refine terrain, add vegetation, and correct generation artifacts.
5. **Structure placement** — handcrafted cities, dungeons, and landmarks are built directly into the refined terrain.
6. **Region locking** — once approved, terrain is protected from further automated regeneration (see §9).

---

## 4. WorldPainter Workflow

| Stage | Tooling | Output |
|---|---|---|
| Elevation | WorldPainter height brushes | Base heightmap |
| Biome distribution | WorldPainter biome layers | Biome-painted terrain |
| Rivers/coastlines | WorldPainter terrain masks | Water body placement |
| Export | WorldPainter Minecraft export | Raw `.mca` region files ready for hand-detailing |

WorldPainter output is treated as a **starting point**, never a final product — every exported region goes through the hand-detailing pass in §3 before it is considered dungeon/quest-ready.

---

## 5. Flat Base World Concept

Beneath the handcrafted terrain, Elysium continents are built on a **flat base layer** rather than Minecraft's default terrain generator. This gives builders a predictable, empty canvas so that WorldPainter output and hand-building always start from the same known baseline, avoiding collisions with default-generated terrain features (caves, ravines, structures) that would otherwise need to be manually removed.

---

## 6. Mountains

Mountain ranges are authored as region-defining terrain features, typically placed at continent borders or as internal barriers that shape travel routes and gate content progression (e.g. a mountain pass that must be unlocked via a quest — see [../0700-Quests/0701-Quest-Chains.md](../0700-Quests/0701-Quest-Chains.md)).

---

## 7. Floating Islands

Floating islands are built as **separate structures**, disconnected from the main landmass heightmap, and are treated as their own instance type at runtime (see [1209-Instance-System.md](1209-Instance-System.md) §3). This keeps their unique physics/travel rules (e.g. reliance on flight or teleportation) isolated from ground-based world logic.

---

## 8. Underground Areas

Underground regions (cave networks, underdark-style biomes) are excavated manually beneath the flat base layer described in §5, rather than relying on generated cave systems. Like floating islands, large underground regions are managed as their own instance where scale warrants it (see [1209-Instance-System.md](1209-Instance-System.md)).

---

## 9. Dungeon Worlds

Dungeons are built as standalone world templates, separate from their parent continent's terrain file:

| Property | Description |
|---|---|
| Storage | Dungeon templates stored independently, loaded on-demand by the Instance Manager |
| Versioning | Each dungeon template is versioned so patches can update a dungeon without affecting currently-running instances |
| Reset behavior | A fresh copy of the template is loaded per instance creation (see [1209-Instance-System.md](1209-Instance-System.md) §3.2), so no dungeon run can permanently alter the base template |

---

## 10. Region Management

| Concept | Description |
|---|---|
| Region | A named subdivision of a continent (see [../0100-World/0102-Regions.md](../0100-World/0102-Regions.md)), used for both design organisation and technical chunk-loading boundaries |
| Region ownership | Each region has a designated build-lead responsible for content consistency within it |
| Region locking | Completed regions are locked from further terrain edits (see §9 below on protection) except through a formal change request |

---

## 11. City Management

Cities are fully handcrafted settlements (see [../0100-World/0103-Cities.md](../0100-World/0103-Cities.md)), built with:

- Fixed NPC placement, replacing vanilla Minecraft villagers entirely with custom NPCs (see §World Protection below)
- Dedicated vendor, quest-giver, and social-hub zones
- Protection flags preventing player griefing (see §World Protection)

---

## 12. World Protection

Elysium restricts a number of vanilla Minecraft systems to preserve the handcrafted world and keep gameplay aligned with the MMORPG design rather than sandbox survival mechanics.

| System | Rule |
|---|---|
| **Building** | Restricted — players cannot freely place/break world terrain outside of designated systems (e.g. Housing, see [../0900-Player-Systems/0900-Housing.md](../0900-Player-Systems/0900-Housing.md)) |
| **Mining** | Profession- and quest-based only — resource nodes are pre-placed and tied to the Mining profession (see [../0600-Professions/0601-Mining.md](../0600-Professions/0601-Mining.md)), not free-form terrain mining |
| **Ender Pearls** | Removed — would break handcrafted traversal design and dungeon pacing |
| **Elytra** | Removed — would trivialize continent-scale travel design (see [../0100-World/0110-Travel.md](../0100-World/0110-Travel.md)) |
| **TNT** | Removed — prevents terrain destruction in a handcrafted, non-regenerating world |
| **Villagers** | Replaced with custom NPCs — see [../0200-Lore/0209-NPCs.md](../0200-Lore/0209-NPCs.md) for NPC design |
| **Villages** | Handcrafted settlements — no vanilla village generation is used; all settlements are authored (see §11) |

> **Developer Note:** World protection rules are enforced server-side, not just client-side — see [1206-Security.md](1206-Security.md) and [1207-Anti-Cheat.md](1207-Anti-Cheat.md) for how illegal block-edit or item-use attempts are detected and rejected.

---

## 13. World Size

World size is defined per-continent to keep travel time and content density consistent with the pacing goals in [../0100-World/0110-Travel.md](../0100-World/0110-Travel.md) and [../0100-World/0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md).

### 13.1 Continent Sizes (Example Scale)

| Continent | Size (blocks) |
|---|---|
| Valoria | 12,000 × 12,000 |
| Frostheim | 10,000 × 10,000 |
| Ashlands | 8,000 × 8,000 |
| Celestia | 6,000 × 6,000 |

> **Developer Note:** Continent size directly informs the soft player-cap and instance-layering thresholds referenced in [1209-Instance-System.md](1209-Instance-System.md) §11 — larger continents support proportionally higher population before a new instance layer is created.

---

## 14. Chunk Management

| Concern | Approach |
|---|---|
| Chunk loading | Chunks load based on player proximity plus a fixed pre-load radius around fast-travel and dungeon-entry points |
| Chunk unloading | Unused chunks unload after a grace period of no nearby players, freeing memory for the instance |
| Persistent vs. instanced chunks | Open-world continent chunks persist for the life of the instance; dungeon/raid chunks are discarded on instance shutdown (see [1209-Instance-System.md](1209-Instance-System.md) §7) |

---

## 15. Loading Systems

- Continent instances pre-load their spawn region and major hub cities at instance startup to avoid load-in stutter for the first wave of connecting players.
- Dungeon/raid templates load fully before the Instance Manager marks the instance as ready for player transfer (see [1209-Instance-System.md](1209-Instance-System.md) §4).
- Region-level loading budgets are tracked against the performance targets in [1208-Performance.md](1208-Performance.md).

---

## 16. Backups

| Backup Type | Frequency | Scope |
|---|---|---|
| Full continent snapshot | Scheduled (e.g. daily) | Entire continent world file |
| Incremental region backup | Scheduled (e.g. hourly) | Regions with recent authorised edits |
| Pre-patch snapshot | Before every content deployment | Full world state, enabling rollback |

Backups are stored independently of the live world files so that a corrupted or exploited region can be restored without taking the entire continent instance offline.

---

## 17. World Editing Rules

1. All terrain edits happen in a staging/build environment, never directly on a live production instance.
2. Completed regions are locked (§10) and require a formal change request to reopen for editing.
3. Any edit that touches a region's spawn points, quest objective locations, or dungeon entrances must be reviewed against [../0700-Quests/0700-Quests.md](../0700-Quests/0700-Quests.md) to avoid breaking active quest chains.
4. World file changes are versioned alongside dungeon template versioning (see §9) so live instances can be safely updated between patches.

---

## 18. System Rules Summary

1. No procedural terrain generation is used anywhere in Elysium — all terrain is handcrafted or WorldPainter-assisted and then hand-detailed.
2. Vanilla systems that conflict with handcrafted world integrity (Ender Pearls, Elytra, TNT, free building/mining, villager generation) are removed or restricted server-side.
3. Dungeons and floating/underground regions are treated as separate world templates and, where applicable, separate runtime instances.
4. Backups and staged editing are mandatory — no direct live-world terrain edits.
5. Continent size directly informs Instance System scaling thresholds; the two documents must be kept numerically consistent.

---

## 19. Connections to Other Systems

| System | Relationship |
|---|---|
| [../0100-World/0100-World.md](../0100-World/0100-World.md) | Design-level description of the world this document engineers |
| [../0100-World/0101-Continents.md](../0100-World/0101-Continents.md) | Source of continent identity and lore that terrain design must support |
| [../0100-World/0103-Cities.md](../0100-World/0103-Cities.md) | Design detail for handcrafted settlements referenced in §11 |
| [../0100-World/0106-Dungeons.md](../0100-World/0106-Dungeons.md) | Design detail for dungeon content built on the templates in §9 |
| [1209-Instance-System.md](1209-Instance-System.md) | Consumes the world templates and continent scale defined here to create runtime instances |
| [1208-Performance.md](1208-Performance.md) | Defines the performance budgets that chunk loading and world size must respect |
