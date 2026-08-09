# 0710 — Quest Objectives

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0700-Quests.md](0700-Quests.md) · [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md) · [0407-World-Interactions.md](../0400-Gameplay/0407-World-Interactions.md)

---

## 1. Overview

Quest objectives are the concrete tasks a player must complete to advance or finish a quest. They are written to be clear, motivated, and varied so that questing does not collapse into pure kill-or-collect repetition.

---

## 2. Objective Types

| Type | Examples |
|------|----------|
| **Kill** | Defeat a number of enemies or a specific named foe |
| **Collect / Loot** | Gather items from the world or from enemies |
| **Interact / Examine** | Use an object, read a document, speak to an NPC |
| **Escort / Defend** | Protect an NPC or location for a duration |
| **Reach / Discover** | Arrive at a location or uncover a landmark |
| **Craft / Deliver** | Create an item or turn it in to an NPC |
| **Choice** | Select a dialogue or action that branches the outcome |

---

## 3. Design Rules

1. Every objective needs a stated reason tied to the quest’s narrative or the region’s local conflict.
2. Objectives are tracked clearly in the UI with progress counts where relevant.
3. Multi-step objectives within a single quest should feel like a short arc, not a checklist of unrelated chores.
4. Fail states (escort deaths, etc.) should be recoverable without forcing a full quest restart where possible.

---

## 4. Technical Notes

Objectives are data-driven. Progress is recorded server-side and synchronised to the client for display. See [0713-Quest-Tracking.md](0713-Quest-Tracking.md) and [0717-Quest-Scripting.md](0717-Quest-Scripting.md).
