# 1317 — Lighting Style

**Project:** Elysium MMORPG  
**Category:** Art  
**Status:** Design Complete — Implementation Pending  
**Related:** [1300-Art-Style.md](1300-Art-Style.md) · [0115-Day-Night-Cycle.md](../0100-World/0115-Day-Night-Cycle.md) · [0114-Weather-System.md](../0100-World/0114-Weather-System.md) · [1105-Shaders.md](../1100-Client/1105-Shaders.md)

---

## 1. Overview

Lighting Style defines how light and shadow express time of day, weather, interior mood, and regional atmosphere across Elysium.

---

## 2. Principles

- Daylight supports exploration clarity; night increases tension without making navigation impossible in intended paths.
- Interiors have deliberate key and fill so NPCs and interactables remain readable.
- Regional colour temperature reinforces biome and culture (warm Aurelia, cool Vethmoor highs, harsh volcanic ash light, etc.).
- Dynamic lights (spells, torches, events) are budgeted and prioritised.


---

## Additional Detail: Dynamic vs Baked Lighting

Open-world regions use a hybrid of baked lighting for static architecture and dynamic lighting for the day/night cycle ([0115-Day-Night-Cycle.md](../0100-World/0115-Day-Night-Cycle.md)) and weather ([0114-Weather-System.md](../0100-World/0114-Weather-System.md)), balancing visual fidelity against the performance requirements of a persistent open world.

## Encounter Lighting as Storytelling

Dungeon and raid encounters use deliberate, scripted lighting shifts to reinforce narrative beats and mechanic phases (a boss room darkening as an enrage phase begins), treating lighting as an active storytelling and gameplay-communication tool rather than pure ambiance.
