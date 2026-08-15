# 0115 — Day Night Cycle

**Category:** World
**Status:** Living Document
**Related:** [0114-Weather-System.md](0114-Weather-System.md) · [0404-AI-Behaviour.md](../0400-Gameplay/0404-AI-Behaviour.md)

---

## 1. Overview

Elysium runs a continuous day/night cycle across the overworld, synced server-wide, contributing to the sense of a living, persistent world rather than a static backdrop.

## 2. Cycle Length

A full in-game day lasts approximately 2 real-world hours (roughly 1 hour of daylight, 1 hour of night), chosen to be long enough that time-of-day feels meaningful rather than flickering, but short enough that players regularly experience both.

## 3. Gameplay Effects

* **NPC schedules** — some NPCs have day/night routines (shops closing at night, guards changing posts), adding life to cities and villages per [0209-NPCs.md](../0200-Lore/0209-NPCs.md).
* **Enemy spawns** — certain enemies (particularly undead in the Greywater Fens) spawn more frequently or aggressively at night.
* **Rare content gating** — specific landmarks or vendors (see [0105-Landmarks.md](0105-Landmarks.md)) are only accessible at certain times of day, rewarding players who explore across the full cycle.

## 4. Visual and Atmospheric Design

Lighting, ambient sound, and even background music shift gradually across the cycle rather than snapping abruptly, coordinated with the weather system in [0114-Weather-System.md](0114-Weather-System.md) for combined atmospheric states (a rainy night in the Fens reads very differently from a clear night in the Shires).

## 5. Player-Facing Time Display

An optional HUD element shows the current in-game time, useful for players tracking time-gated content, configurable in the settings menu (see [1109-Settings.md](../1100-Client/1109-Settings.md)).

## 6. Technical Notes

The day/night cycle is server-authoritative and synchronized across all players in a shared world instance, ensuring group content and world events reference a consistent time state. Instanced content (dungeons, raids) uses a fixed lighting state appropriate to its narrative framing rather than following the live cycle.
