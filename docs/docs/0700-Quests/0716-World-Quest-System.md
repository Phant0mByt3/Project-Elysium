# 0716 — World Quest System

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0715-Dynamic-Quests.md](0715-Dynamic-Quests.md) · [0109-World-Events.md](../0100-World/0109-World-Events.md) · [0702-Daily-Quests.md](0702-Daily-Quests.md) · [0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md)

---

## 1. Overview

World Quests are short, repeatable, location-based objectives that appear across the open world on a rotating schedule. They provide a steady stream of content for max-level and mid-to-late leveling players who want to engage with the world outside of dungeons and the Main Quest.

---

## 2. Characteristics

- Appear on the map for a limited window (hours to a couple of days).
- Objectives are concise (kill a rare, collect a set of items, complete a small event, etc.).
- Rewards focus on reputation, currency, gear upgrades, and seasonal/event currencies.
- Multiple World Quests can be active simultaneously across different regions.

---

## 3. Design Rules

1. World Quests should pull players into different parts of the map rather than concentrating everyone on a single hotspot.
2. Difficulty is tuned so that solo or small-group play is viable for most objectives.
3. Emitting too many simultaneous World Quests is avoided to prevent map clutter and decision paralysis.
4. Integration with seasonal events and world events creates variety without requiring entirely new systems.

---

## 4. Technical Notes

World Quest availability and progress are managed by the same event and quest scheduling systems used for world events and dailies. State is server-authoritative and visible on the map UI.


## 5. Reward Currency

World Quests primarily reward a dedicated endgame currency usable to purchase catch-up gear and cosmetics from a rotating vendor, giving the system a clear economic purpose distinct from dailies and weeklies.

## 6. Seasonal Integration

During seasonal events ([0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md)), World Quest density and rewards temporarily increase in event-themed regions, spotlighting seasonal content without requiring a separate quest system to be built from scratch.
