# 1110 — Loading Screens

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [1100-Launcher.md](1100-Launcher.md) · [1300-Art-Style.md](../1300-Art/1300-Art-Style.md) · [0112-Maps.md](../0100-World/0112-Maps.md) · [0200-Lore.md](../0200-Lore/0200-Lore.md)

---

## 1. Overview

Loading screens bridge the gap between zones, instances, and login. They are an opportunity for art, lore, and atmosphere rather than pure dead time.

---

## 2. Content

- Region- or continent-appropriate key art
- Short lore tips or flavour quotes
- Progress indicator (bar or spinner)
- Optional tips for new players (controls, systems)
- Faction-aware variants where relevant

---

## 3. Design Rules

1. Loading screens should reinforce immersion and world identity.
2. Tips are helpful but never lecture; they can be disabled.
3. Art must meet the readability and style standards of [1300-Art-Style.md](../1300-Art/1300-Art-Style.md).
4. Load times are optimised so that screens are not displayed longer than necessary (see Client Optimisation).

---

## 4. Technical Notes

Loading screen assets are packaged with the content pack / client. The client selects the appropriate screen based on destination instance or continent.


---

## Additional Detail: Loading Screen Content

Loading screens rotate lore snippets, tips, and concept art relevant to the destination zone, turning an otherwise dead moment into a small piece of world-building and onboarding for newer players.

## Performance Target

Loading screen duration is actively minimized through asset streaming and preloading optimizations tracked in [1113-Client-Optimisation.md](1113-Client-Optimisation.md), since long loading screens directly undermine the immersive, seamless-feeling world the game is built around.
