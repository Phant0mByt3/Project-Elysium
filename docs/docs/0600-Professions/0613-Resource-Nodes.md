# 0613 — Resource Nodes

**Project:** Elysium MMORPG  
**Category:** Professions  
**Status:** Design Complete — Implementation Pending  
**Related:** [0612-Profession-Materials.md](0612-Profession-Materials.md) · [0113-Biomes.md](../0100-World/0113-Biomes.md) · [0102-Regions.md](../0100-World/0102-Regions.md) · [0601-Mining.md](0601-Mining.md)

---

## 1. Overview

Resource nodes are the hand-placed or carefully managed gathering points in the world for Mining, Herbalism, Woodcutting, and related activities. Because the world is handcrafted, nodes are positioned intentionally rather than spawned by a pure procedural system.

---

## 2. Node Types

| Profession | Node Examples |
|------------|---------------|
| **Mining** | Ore veins, rich veins, special crystalline outcrops |
| **Herbalism** | Herb patches, rare blooms, aquatic plants |
| **Woodcutting** | Marked trees, fallen logs, rare ancient trunks |
| **Skinning** | (Primarily mob-based, with occasional static carcass nodes) |
| **Fishing** | Fishing pools and hotspot markers |

---

## 3. Design Rules

1. Nodes respect biome and region identity ([0113-Biomes.md](../0100-World/0113-Biomes.md)).
2. Density is higher along natural travel routes and near quest hubs so that gathering feels integrated with exploration, not a separate grind map.
3. Rich / rare nodes are uncommon and often slightly off the main path to reward curiosity (Pillar 1).
4. Nodes respawn on timers that support both casual and dedicated gatherers without creating permanent empty zones or overcrowding.

---

## 4. Technical Notes

Node state (available / depleted / respawn timer) is tracked server-side per instance. Gathering attempts validate profession skill and tool requirements before granting materials and skill-ups.
