# 0114 — Weather System

**Project:** Elysium MMORPG  
**Category:** World  
**Status:** Design Complete — Implementation Pending  
**Related:** [0113-Biomes.md](0113-Biomes.md) · [0115-Day-Night-Cycle.md](0115-Day-Night-Cycle.md) · [0117-Environmental-Hazards.md](0117-Environmental-Hazards.md) · [0108-World-Bosses.md](0108-World-Bosses.md) · [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md)

---

## 1. Overview

Weather in Elysium is region-aware, biome-driven, and occasionally story-driven. It exists to reinforce immersion, create dynamic combat opportunities, and support specific world events and world bosses.

Weather is never purely cosmetic; certain conditions alter visibility, movement, elemental resistances, or trigger special encounters.

---

## 2. Weather Types

| Weather | Primary Biomes | Gameplay Effects |
|---------|----------------|------------------|
| **Clear** | All | Default; full visibility |
| **Light Rain** | Temperate, Wetland | Minor movement penalty on slopes; increased herbalism node density |
| **Heavy Rain / Storm** | Wetland, Coastal | Reduced visibility; lightning can strike exposed players; Maelith’s Herald world boss can spawn |
| **Fog / Mist** | Wetland, Forest | Significantly reduced view distance; stealth bonuses for Rogues |
| **Snow / Blizzard** | Tundra, Highland | Movement slow; frost resistance becomes valuable; visibility drop |
| **Ashfall / Heat Haze** | Volcanic | Periodic fire damage if unprotected; reduced healing effectiveness |
| **Sundering Storm** | Shattered / Corrupted | Rare, high-threat weather; residual Kaelgorath energy; unique loot tables for surviving |

---

## 3. Scheduling & Control

- Each region has a weighted weather schedule defined at design time.
- Weather transitions are gradual (fade over 30–90 seconds) to avoid jarring changes.
- Story or event systems can force a weather state for a limited duration (e.g. an invasion event that brings continuous ashfall).
- World bosses such as Maelith’s Herald are gated behind specific weather conditions.

---

## 4. Player Tools

- Certain consumables and class abilities provide temporary weather resistance or clear local fog.
- Inns and major cities are always considered “indoor” and ignore outdoor weather effects.
- The minimap and world map display current regional weather with a simple icon.

---

## 5. Technical Implementation

Weather is driven by a server-side plugin that:
1. Selects weather based on region + biome weights + any forced event state.
2. Broadcasts the active weather packet to clients in that instance.
3. Applies movement, damage, and visibility modifiers server-side (never trusted to the client).

See [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md) for the event-scheduling system these weather states plug into.
