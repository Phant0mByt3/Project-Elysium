# 0508 — Crafting

**Category:** Items
**Status:** Living Document
**Related:** [0600-Professions.md](../0600-Professions/0600-Professions.md) · [1000-Economy.md](../1000-Economy/1000-Economy.md)

---

## 1. Overview

Crafting is the umbrella system connecting the gathering professions ([0601-Mining.md](../0600-Professions/0601-Mining.md) and its family of skills) to the production professions (Alchemy, Blacksmithing, Tailoring, and others). See [0600-Professions.md](../0600-Professions/0600-Professions.md) for the overall profession system this belongs to.

## 2. Core Loop

1. Gather raw materials in the open world via a gathering profession.
2. Learn recipes from trainers, quests, or rare drops.
3. Craft items using a production profession, consuming materials and a crafting-specific currency/time cost.
4. Sell or use the result — feeding directly into the player economy ([1000-Economy.md](../1000-Economy/1000-Economy.md)) via the Auction House ([1003-Auction-House.md](../1000-Economy/1003-Auction-House.md)).

## 3. Design Rules

* Crafted gear should be competitive with dungeon-tier drops, giving crafting professions a genuine progression role rather than being purely cosmetic or gold-focused.
* Recipes should include a mix of vendor-taught (baseline), quest-taught (thematic, one-time), and drop-taught (rare, profitable) sources.
* Crafting should support at least one profession-exclusive item type per profession (e.g. only Blacksmiths can craft plate armor) to keep professions meaningfully differentiated.

## 4. Recipe Rarity

| Recipe Source | Availability | Value |
| --- | --- | --- |
| Trainer | Always available at appropriate skill level | Baseline items |
| Vendor (rare) | Limited stock, faction-gated | Faction-flavored items |
| Quest reward | One-time, tied to a specific questline | Thematic, often BoP |
| World/dungeon drop | Random, tradeable | High-value, drives economy activity |

## 5. Crafting Quality and Specialization

Higher-skill crafters can produce items with a chance of bonus quality (an extra stat roll or slightly higher item level), giving master crafters a reputation-driven niche within the player economy beyond pure recipe access.

## 6. Enchanting

Enchanting is documented as its own related-but-distinct system — see [0509-Enchanting.md](0509-Enchanting.md).

## 7. Crafting and World Design

Gathering nodes are placed during world-building as part of the region's key-location pass (see [0116-World-Generation.md](../0100-World/0116-World-Generation.md)), ensuring each region offers materials appropriate to its biome and level range.
