# 0114 — Weather System

**Category:** World
**Status:** Living Document
**Related:** [0113-Biomes.md](0113-Biomes.md) · [0115-Day-Night-Cycle.md](0115-Day-Night-Cycle.md)

---

## 1. Overview

Weather is a dynamic, biome-appropriate atmospheric system that adds visual variety and, in select cases, light gameplay impact — without becoming an intrusive survival mechanic (Elysium is not a survival game; see [0001-Vision.md](../0000-Project/0001-Vision.md)).

## 2. Weather Types by Biome

| Biome | Weather Patterns |
| --- | --- |
| Temperate Plains | Clear, light rain, overcast |
| Dense Forest | Mist, filtered rain, fog |
| Wetland / Marsh | Heavy rain, fog, occasional storms |
| Alpine / Snow | Snowfall, blizzards, clear cold |
| Volcanic | Ash fall, heat haze, occasional ember storms |
| Tundra | Snow, whiteout blizzards, aurora events |

## 3. Gameplay Impact

Weather is primarily cosmetic, but select severe weather (blizzards in Ashenclaw Tundra, ash storms in the Ember Deeps) briefly reduces visibility and is used narratively to gate certain rare spawns or trigger specific world events (see [0109-World-Events.md](0109-World-Events.md)). Weather never applies direct damage or forces players indoors — it is atmosphere first, mechanic second.

## 4. Technical Approach

Weather transitions are server-driven and synced across all players in a region for shared atmosphere during group content, cycling on semi-randomized timers biased toward biome-appropriate patterns.

## 5. Aurora and Rare Weather Events

Rare weather events (auroras over Ashenclaw Tundra, ember storms in the Ember Deeps) are visually distinct, screenshot-worthy occurrences that occasionally coincide with bonus loot or rare spawns, rewarding players who happen to be exploring when they occur.

## 6. Art and Audio Integration

Each weather state has matching ambient audio and lighting changes, coordinated between the Art and Technical teams per [1300-Art-Style.md](../1300-Art/1300-Art-Style.md) and the audio design standards in [1300-Art/](../1300-Art/).
