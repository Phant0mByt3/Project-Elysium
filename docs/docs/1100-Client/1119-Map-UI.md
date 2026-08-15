# 1119 — Map UI

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [0112-Maps.md](../0100-World/0112-Maps.md) · [0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md) · [0713-Quest-Tracking.md](../0700-Quests/0713-Quest-Tracking.md) · [1301-UI-Style.md](../1300-Art/1301-UI-Style.md)

---

## 1. Overview

The Map UI includes the world map, zone map, and minimap. It is the primary navigation and discovery interface for the handcrafted continents.

---

## 2. Features

- Zoomable world and region maps with hand-authored art
- Icons for quests, vendors, trainers, flight points, and custom points of interest
- Minimap with player heading, nearby objectives, and party members
- Fast-travel / waypoint interaction where unlocked
- Fog of war or discovery reveal for unexplored areas (if used)

---

## 3. Design Rules

1. Map art reinforces regional identity and does not look like a generic default engine map view.
2. Iconography is consistent and legible at minimap scale.
3. Players can filter icon categories to reduce clutter.
4. The map remains usable during combat (minimap especially) without demanding full attention.


---

## Additional Detail: Layered Map Information

The map UI supports toggleable information layers (quest markers, resource nodes, discovered landmarks, group member positions), letting players declutter the map to focus on exactly the information relevant to their current goal.

## Pin and Note System

Players can drop custom pins with short notes on the map for personal reference (a remembered rare node location, a landmark to revisit), a lightweight tool supporting the exploration-and-discovery play pattern central to [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).
