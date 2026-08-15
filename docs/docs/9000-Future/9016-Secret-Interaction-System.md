# 9016 — Secret Interaction System

**Project:** Elysium MMORPG
**Category:** Future
**Status:** Unscoped Concept
**Related:** [0105-Landmarks.md](../0100-World/0105-Landmarks.md) · [0704-Achievements.md](../0700-Quests/0704-Achievements.md) · [9999-Ideas.md](9999-Ideas.md)

---

## 1. Overview

A speculative future system for deeper, more elaborate hidden interactions layered on top of the existing landmark secrets described in [0105-Landmarks.md](../0100-World/0105-Landmarks.md) — the current system rewards finding a hidden location; this concept explores rewarding a more involved *sequence* of discovery.

## 2. Concept Outline

The rough shape of the idea, as originally sketched:

* **Conditions** — a secret only becomes available under specific world or character conditions (time of day, weather state, a prior quest completed, an item in inventory) rather than being permanently present once discovered.
* **Interaction Trigger** — the player must perform a specific, non-obvious action at the location (interact with an object in a particular order, stand in a specific spot during a specific weather event) rather than a simple single-click discovery.
* **Client-Only Reveal** — the secret's existence isn't hinted at anywhere in quest text, the map, or achievement tracking until triggered, preserving genuine surprise for players who stumble onto it without following a guide.
* **Reward** — a unique, non-repeatable cosmetic or lore reward tied specifically to this discovery path.
* **Lore Connection** — every secret ties to a real piece of world lore ([0200-Lore.md](../0200-Lore/0200-Lore.md)), never existing purely as a mechanical Easter egg disconnected from the world.
* **Discovery Tracking** — once triggered, the discovery is logged to the player's journal ([0908-Journals.md](../0900-Player-Systems/0908-Journals.md)) and Collections ([0907-Collections.md](../0900-Player-Systems/0907-Collections.md)) even though it wasn't visible beforehand.

## 3. Why This Is Still a Concept, Not a Committed System

This would require dedicated scripting tooling beyond the current landmark placement pipeline ([0116-World-Generation.md](../0100-World/0116-World-Generation.md)) and a much higher per-secret production cost than a standard landmark, so it hasn't yet been scoped into [0005-Future-Plans.md](../0000-Project/0005-Future-Plans.md). It remains a promising direction worth prototyping once core world-building tooling has matured.

## 4. Relationship to Existing Systems

If pursued, this system would sit as a rare, premium-tier addition on top of — not a replacement for — the existing, more frequent landmark secrets described in [0105-Landmarks.md](../0100-World/0105-Landmarks.md), reserved for a handful of truly special, memorable discoveries per continent rather than being a common occurrence.

## 5. Next Steps

Before this can graduate to [0005-Future-Plans.md](../0000-Project/0005-Future-Plans.md), it needs: a small prototype validating the client-side trigger-without-hint technical approach, and a scoped pilot (one or two secrets) tested during Closed Alpha or Beta to gauge whether players find and enjoy them without external hints spoiling the surprise.
