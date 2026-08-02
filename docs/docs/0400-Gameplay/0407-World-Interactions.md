# 0407 — World Interactions

**Project:** Elysium MMORPG  
**Category:** Gameplay  
**Status:** Design Complete — Implementation Pending  
**Related:** [0100-World.md](../0100-World/0100-World.md) · [0110-Travel.md](../0100-World/0110-Travel.md) · [0906-Simulated-Civilisation.md](../0900-Player-Systems/0906-Simulated-Civilisation.md) · [0700-Quests.md](../0700-Quests/0700-Quests.md)

---

## 1. Overview

World interactions are the non-combat ways players engage with the handcrafted environment: examining objects, speaking with ambient NPCs, triggering environmental storytelling, and using the world as a living space rather than a series of quest markers.

---

## 2. Interaction Types

| Type | Examples | Purpose |
|------|----------|---------|
| **Examine / Lore Objects** | Journals, plaques, statues, ruins | Deliver optional lore and achievements |
| **Ambient NPC Dialogue** | Guards, citizens, merchants with idle lines | Make cities and villages feel inhabited |
| **Environmental Storytelling** | Destroyed camps, abandoned carts, battle remnants | Reinforce regional conflict without a quest |
| **Utility Interactions** | Doors, levers, elevators, boats, flight masters | Support traversal and dungeon flow |
| **Profession Nodes** | Ore, herbs, trees, fishing spots | Gathering gameplay (see Professions) |
| **Rest / Social** | Benches, campfires, tavern seats | Encourage roleplay and downtime |

---

## 3. Design Rules

1. Every region should contain at least a handful of pure-discovery interactions that are not required by any quest (Pillar 1).
2. Interactions must be readable — the player should understand they can interact without needing a tutorial tooltip every time.
3. Critical path interactions (quest objects, dungeon levers) must be impossible to miss for a player following the main markers.
4. Interactions never permanently alter the handcrafted terrain outside of approved systems (Housing, certain event props).

---

## 4. Technical Notes

Interactions are driven by server-side triggers and data-driven dialogue/examine entries. Client displays prompts and plays animations/effects; outcomes (quest credit, item grants, door states) are always confirmed by the server.
