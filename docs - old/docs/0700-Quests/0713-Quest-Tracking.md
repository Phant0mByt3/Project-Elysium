# 0713 — Quest Tracking

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0700-Quests.md](0700-Quests.md) · [1120-Quest-UI.md](../1100-Client/1120-Quest-UI.md) · [0112-Maps.md](../0100-World/0112-Maps.md) · [0710-Quest-Objectives.md](0710-Quest-Objectives.md)

---

## 1. Overview

Quest tracking is the set of UI and world systems that show the player what they are doing, where they need to go, and how close they are to completion. Clarity of tracking is essential to the theme-park experience.

---

## 2. Tracking Elements

| Element | Purpose |
|---------|---------|
| **Quest Log** | Full list of active, completed, and available quests |
| **Tracker Panel** | Compact on-screen list of selected objectives with progress |
| **Map Markers** | Icons on the world map and minimap for objectives and turn-in NPCs |
| **World Indicators** | In-world markers, beams, or highlights for interactable objectives |
| **Chapter / Campaign Frame** | Special treatment for Main Quest progress |

---

## 3. Design Rules

1. A player should almost never be unsure what to do next if they have an active quest.
2. Tracking can be customised (which quests are shown, minimap density) but defaults are helpful for new players.
3. Optional content is clearly distinguished from critical-path content.
4. Tracking never replaces reading quest text; it supports it.

---

## 4. Technical Notes

Quest state and objective progress are authoritative on the server. The client receives updates and renders the appropriate UI and world markers. See also [1120-Quest-UI.md](../1100-Client/1120-Quest-UI.md).
