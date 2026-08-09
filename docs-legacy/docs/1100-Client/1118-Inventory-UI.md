# 1118 — Inventory UI

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [0913-Inventory-System.md](../0900-Player-Systems/0913-Inventory-System.md) · [0519-Item-Storage.md](../0500-Items/0519-Item-Storage.md) · [1301-UI-Style.md](../1300-Art/1301-UI-Style.md) · [1116-Interface-Layouts.md](1116-Interface-Layouts.md)

---

## 1. Overview

The Inventory UI displays bags, equipment slots, currency, and item management controls. It is one of the most frequently used interfaces and must be both efficient and pleasant.

---

## 2. Features

- Bag grid(s) with item icons, stacks, and quality borders
- Character equipment paper-doll or slot list
- Currency display
- Sorting, filtering, and search helpers
- Drag-and-drop, right-click actions, and keyboard shortcuts
- Comparison tooltips when hovering gear

---

## 3. Design Rules

1. Item rarity and key properties are readable at a glance.
2. Drag-and-drop and context menus behave consistently with the rest of the UI.
3. The layout works at multiple UI scales and aspect ratios.
4. Full bags and important item warnings are clear without being noisy.
