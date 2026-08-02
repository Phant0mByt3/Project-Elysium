# 0115 — Day Night Cycle

**Project:** Elysium MMORPG  
**Category:** World  
**Status:** Design Complete — Implementation Pending  
**Related:** [0114-Weather-System.md](0114-Weather-System.md) · [0109-World-Events.md](0109-World-Events.md) · [0202-Gods.md](../0200-Lore/0202-Gods.md) · [0906-Simulated-Civilisation.md](../0900-Player-Systems/0906-Simulated-Civilisation.md)

---

## 1. Overview

Elysium runs a continuous day-night cycle that is shared across all open-world instances of a continent. The cycle exists to support immersion, NPC routines, certain world events, and a small number of time-gated activities.

The cycle is deliberately slower than real time so that players experience meaningful stretches of day and night without feeling rushed.

---

## 2. Timing

| Period | Approximate Duration (real time) | In-Game Feel |
|--------|----------------------------------|--------------|
| Dawn | 15–20 min | Soft golden light, NPCs beginning daily routines |
| Day | 60–75 min | Full brightness, peak activity in cities and roads |
| Dusk | 15–20 min | Warm decline, taverns filling |
| Night | 45–60 min | Reduced ambient light, increased undead/nocturnal activity in certain regions |

Total cycle ≈ 2.5–3 real hours. Exact timings are tunable per continent if needed.

---

## 3. Gameplay Effects

- **Visibility** — night reduces ambient light; torches, lanterns, and certain class abilities become more valuable.
- **Enemy behaviour** — some creature types become more aggressive or only spawn at night (especially in Greywater Fens and Shattered Cairns).
- **NPC routines** — vendors, guards, and citizens follow simple day/night schedules (see [0906-Simulated-Civilisation.md](../0900-Player-Systems/0906-Simulated-Civilisation.md)).
- **World events** — a subset of dynamic events and world-boss windows are time-of-day gated.
- **Religious flavour** — Solthar-aligned locations feel stronger at midday; Nyxara-aligned locations feel stronger at midnight.

---

## 4. Player Tools

- Hearthstones and inns always provide full indoor lighting regardless of outside time.
- Certain consumables and class abilities grant temporary night vision or light sources.
- The minimap displays a simple sun/moon icon indicating current period.

---

## 5. Technical Notes

Day-night state is authoritative on the server and synchronised to all clients in the instance. Individual players cannot advance or pause the cycle; it is a shared world property. Instance servers for dungeons and raids may optionally freeze time or run an independent cycle if the encounter design requires it.
