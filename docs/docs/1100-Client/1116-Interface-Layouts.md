# 1116 — Interface Layouts

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [1301-UI-Style.md](../1300-Art/1301-UI-Style.md) · [1106-Accessibility.md](1106-Accessibility.md) · [1108-UI-Systems.md](1108-UI-Systems.md) · [1123-Client-Configuration.md](1123-Client-Configuration.md)

---

## 1. Overview

Interface Layouts define how the major UI elements (HUD, bags, map, quest tracker, party frames, etc.) are arranged, scaled, and customised. A good default layout is essential; advanced players may further adjust positions and scales.

---

## 2. Principles

- **Clarity first** — combat-critical information is never buried.
- **Consistent visual language** — frames, fonts, and colours follow the UI style guide.
- **Scalability** — UI scale and individual element scales support different resolutions and accessibility needs.
- **Customisation** — dragging, locking, and resetting layouts are supported without allowing complete chaos that breaks usability.

---

## 3. Default Layout Goals

- Action bars and resource displays are immediately reachable.
- Quest tracker and minimap are visible without covering key combat space.
- Party/raid frames are readable in both 5-player and larger content.
- Inventory and character sheet open in predictable, non-overlapping positions.


---

## Additional Detail: Layout Presets

Players can choose between preset UI layouts (Default, Compact, Minimal) as a starting point before further customizing individual element positions, giving new players sensible defaults while still supporting deep customization for veteran players who want to optimize their screen real estate.

## Layout Export and Sharing

UI layout configurations can be exported and shared as a simple text string, letting community members share optimized layouts (a popular raid-focused layout, for example) without requiring a full addon ecosystem.
