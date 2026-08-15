# 0907 — Collections

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0903-Cosmetics.md](0903-Cosmetics.md) · [0901-Mounts.md](0901-Mounts.md) · [0902-Pets.md](0902-Pets.md) · [0704-Achievements.md](../0700-Quests/0704-Achievements.md) · [0513-Transmog-System.md](../0500-Items/0513-Transmog-System.md)

---

## 1. Overview

Collections is the unified UI and data layer that tracks everything a player has unlocked for cosmetic and completionist purposes: mounts, pets, appearances, toys, titles, and similar account- or character-bound unlocks.

---

## 2. Tracked Categories

| Category | Notes |
|----------|-------|
| **Mounts** | Ground and (later) flying |
| **Pets** | Companion pets |
| **Appearances / Transmog** | Armour and weapon looks |
| **Toys & Utility Cosmetics** | Fun and social items |
| **Titles** | Earned prefixes/suffixes |
| **Emotes** | Unlockable expressions |
| **Other** | Future categories as needed |

---

## 3. Design Rules

1. Collecting should feel rewarding on its own; many unlocks have no combat power.
2. Progress is visible and filterable so players can chase specific goals.
3. Account-wide unlocks are preferred where it increases satisfaction without harming character identity.
4. New content regularly adds to existing collections rather than creating disconnected trackers.

---

## 4. Technical Notes

Collection state is stored primarily at account level (with character-specific exceptions where required). The client queries and displays the data; unlock events are emitted by the systems that grant the items.


---

## Additional Detail: Collection Categories

Beyond mounts, pets, and transmog, the Collections system tracks toy-like novelty items, rare housing decor, and profession mastery badges, giving completionists a single unified account-wide checklist spanning every collectible system in the game.

## Rarity-Weighted Completion Score

Collection completion is weighted by item rarity rather than pure count, so tracking down a handful of genuinely rare collectibles contributes meaningfully more to a player's completion score than a large volume of common items, keeping the score a fair signal of dedication.
