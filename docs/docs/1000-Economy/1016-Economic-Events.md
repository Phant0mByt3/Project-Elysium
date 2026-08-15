# 1016 — Economic Events

**Project:** Elysium MMORPG  
**Category:** Economy  
**Status:** Design Complete — Implementation Pending  
**Related:** [0109-World-Events.md](../0100-World/0109-World-Events.md) · [0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md) · [1000-Economy.md](1000-Economy.md) · [1008-Economic-Balance.md](1008-Economic-Balance.md)

---

## 1. Overview

Economic Events are temporary or seasonal occurrences that affect supply, demand, prices, or available goods. They create short-term goals for crafters and traders and add variety to the living world.

---

## 2. Examples

- A temporary surge in demand for a particular consumable during a world event or raid tier opening
- Seasonal festivals that introduce limited recipes, materials, or vendor stock
- Caravan or trade-route events that reward escort or defense with rare materials
- Limited-time reputation or currency exchange opportunities

---

## 3. Design Rules

1. Events should be telegraphed so that engaged players can prepare and participate.
2. Impact is meaningful but not so extreme that it permanently distorts the broader economy.
3. Events are used sparingly enough that they remain special.
4. Outcomes are monitored for unintended inflation or scarcity spikes.

---

## 4. Technical Notes

Economic events are driven by the same scheduling and state systems used for world events. Vendor inventories, drop tables, and recipe availability can be toggled or weighted for the duration of the event.


---

## Additional Detail: Event Types

Economic events range from small, region-scoped disruptions (a bandit raid temporarily halting a trade route) to server-wide occurrences (a rare material shortage event tied to a seasonal storyline), each designed to create temporary, interesting market dynamics rather than permanent economic damage.

## Player-Facing Communication

Significant economic events are communicated clearly through in-client notifications and, where relevant, quest or world-event framing, ensuring players understand why prices or availability have shifted rather than experiencing it as an unexplained, opaque change.
