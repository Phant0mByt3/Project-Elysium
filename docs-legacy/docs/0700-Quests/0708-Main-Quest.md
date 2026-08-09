# 0708 — Main Quest

**Project:** Elysium MMORPG  
**Category:** Quests  
**Status:** Design Complete — Implementation Pending  
**Related:** [0207-Main-Story.md](../0200-Lore/0207-Main-Story.md) · [0700-Quests.md](0700-Quests.md) · [0701-Quest-Chains.md](0701-Quest-Chains.md) · [0305-Leveling.md](../0300-Characters/0305-Leveling.md)

---

## 1. Overview

The Main Quest (also called the Main Story campaign) is the critical-path narrative that takes the player from the starting experience through the reconnection of Aurelia and Vethmoor and into the events leading to the launch raid. It is solo-completable, faction-aware, and paced to match the leveling curve.

---

## 2. Structure

The Main Quest follows the three-act structure defined in [0207-Main-Story.md](../0200-Lore/0207-Main-Story.md):

- **Act I** — Reconnection (Aurelia, levels 1–20)
- **Act II** — Fracture Lines (Vethmoor, levels 20–40)
- **Act III** — The Sunken Concord (levels 45–50, culminating in the raid)

Individual quest steps are implemented as a long quest chain (or set of closely linked chains) with clear chapter breaks and cinematic moments where appropriate.

---

## 3. Design Rules

1. The Main Quest never requires a group; all objectives are soloable.
2. Faction choice colours dialogue and framing but does not lock the player out of the critical path.
3. Side content is referenced and rewarded but never required to understand or complete the Main Quest.
4. Pacing keeps the player roughly on-level for the regions they are sent through ([0102-Regions.md](../0100-World/0102-Regions.md)).

---

## 4. Tracking & Presentation

The Main Quest has dedicated UI treatment (chapter titles, progress indicators) so players always know where they are in the story. See [0713-Quest-Tracking.md](0713-Quest-Tracking.md) and [1120-Quest-UI.md](../1100-Client/1120-Quest-UI.md).

---

## 5. Story Unlock Requirements

Major world changes require players to complete the relevant storyline.

**Example:**

A player cannot enter Post-Collision Aurelia until they complete the secret quest chain.
