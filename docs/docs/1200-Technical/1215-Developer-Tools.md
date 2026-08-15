# 1215 — Developer Tools

**Project:** Elysium MMORPG  
**Category:** Technical  
**Status:** Design Complete — Implementation Pending  
**Related:** [1200-Plugin-Architecture.md](1200-Plugin-Architecture.md) · [1410-Developer-Environment.md](../1400-Development/1410-Developer-Environment.md) · [1417-Development-Tools.md](../1400-Development/1417-Development-Tools.md) · [1214-Admin-Tools.md](1214-Admin-Tools.md)

---

## 1. Overview

Developer Tools support engineering and design iteration: debug commands, inspection overlays, hot-reload helpers, profiling hooks, and local simulation utilities. They are not exposed to normal players.

---

## 2. Examples

- Entity and world-partition inspectors
- Combat and threat debug displays
- Quest state manipulation for testing
- Performance profilers and tick monitors
- Data reload commands for recipes, loot tables, and dialogue

---

## 3. Design Rules

1. Dev tools are gated by permission and ideally by environment (dev/staging vs production).
2. They must not become a vector for production exploits.
3. Documentation for common tools lives alongside the coding and testing standards.


---

## Additional Detail: Content Iteration Tools

Dedicated in-editor tools allow designers to preview quest flows, test encounter mechanics in isolation, and validate loot tables without needing a full production-like server environment, significantly speeding up the content iteration loop described in [1400-Development/](../1400-Development/).

## Debug Visualization

Server-side debug visualization overlays (aggro radius, pathing nodes, spawn points) can be toggled on internal test builds, helping designers and QA diagnose issues visually rather than through logs alone.
