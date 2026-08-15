# 0407 — World Interactions

**Project:** Elysium MMORPG
**Category:** Gameplay
**Status:** Living Document
**Related:** [0400-Game-Mechanics.md](0400-Game-Mechanics.md) · [0105-Landmarks.md](../0100-World/0105-Landmarks.md)

---

## 1. Overview

World interactions are the systems governing how players interact with the environment outside of combat — gathering nodes, interactable objects, puzzle mechanisms, and environmental storytelling triggers.

## 2. Interaction Categories

* **Gathering Nodes** — resource nodes tied to gathering professions ([0601-Mining.md](../0600-Professions/0601-Mining.md)).
* **Lore Objects** — books, journals, murals that contribute to the lore system ([0209-NPCs.md](../0200-Lore/0209-NPCs.md)).
* **Mechanisms** — levers, pressure plates, and puzzle elements used in dungeons and landmark content.
* **Quest Objects** — items or triggers tied to active quests ([0700-Quests/](../0700-Quests/)).
* **Ambient Interactables** — chairs, instruments, and other non-mechanical objects that support roleplay and immersion.

## 3. Interaction Feedback

All interactable objects use a consistent highlight and prompt system so players can reliably identify what can be interacted with, avoiding the frustration of ambiguous "is this clickable" environments.

## 4. Puzzle Design Standards

Puzzle mechanisms found in dungeons and landmarks follow a consistent internal logic per encounter (lever sequences, pressure plate patterns) and are tuned to be solvable through in-world clues rather than requiring external guides, in keeping with the exploration-reward philosophy in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).

## 5. Environmental Storytelling

Scripted environmental triggers (a door that only opens after nearby lore is read, ambient sound stings tied to specific locations) are used throughout landmarks and dungeons to reinforce narrative without requiring dialogue, per the "show don't tell" principle referenced in [1403-Quest-Writing-Guide.md](../1400-Development/1403-Quest-Writing-Guide.md).

## 6. Technical Notes

Interactable objects are defined through a data-driven interaction system, allowing designers to configure new interaction types without engineering support for common cases (simple gather, simple lever, simple lore pickup) — see [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md).
