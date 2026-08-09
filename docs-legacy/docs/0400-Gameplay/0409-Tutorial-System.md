# 0409 — Tutorial System

**Project:** Elysium MMORPG  
**Category:** Gameplay  
**Status:** Design Complete — Implementation Pending  
**Related:** [0310-Character-Creation.md](../0300-Characters/0310-Character-Creation.md) · [0305-Leveling.md](../0300-Characters/0305-Leveling.md) · [0102-Regions.md](../0100-World/0102-Regions.md) · [0700-Quests.md](../0700-Quests/0700-Quests.md)

---

## 1. Overview

The tutorial is integrated into the opening hours of the game rather than presented as a separate, skippable mode. New players learn movement, combat, questing, and basic UI through the Southern Shires (or equivalent Duskward starting experience) while already playing the real game.

---

## 2. Goals

- Teach core controls and combat loop within the first 10–15 minutes.
- Introduce the quest system, map, and inventory without walls of text.
- Establish the tone and world of Elysium immediately.
- Avoid “tutorial island” feeling; the starting zone is a real region that experienced players may still revisit.

---

## 3. Teaching Sequence (High Level)

1. Movement and camera
2. Basic attack and first ability
3. Targeting and simple enemy pack
4. First quest accept / complete / turn-in
5. Inventory and equipment
6. Map and basic navigation
7. Introduction to the local story and the larger faction conflict

Later systems (mounts, specialisations, professions, group content) are introduced at the levels where they naturally unlock, with short contextual tooltips or quests rather than a single massive tutorial dump.

---

## 4. Design Rules

1. Never lock the player in a forced tutorial sequence that cannot be escaped if they already understand the systems.
2. Use the world and NPCs as teachers whenever possible instead of floating UI overlays.
3. Failures in the tutorial should be low-cost and educational.
4. Returning players or alts should be able to move through the opening content quickly.

---

## 5. Technical Notes

Tutorial state is tracked per character. Contextual prompts are data-driven and can be disabled in settings for experienced players. All tutorial rewards and progression are real character progression, not temporary tutorial-only items.
