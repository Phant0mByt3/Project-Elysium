# 0507 — Consumables

**Category:** Items
**Status:** Living Document
**Related:** [0605-Alchemy.md](../0600-Professions/0605-Alchemy.md) · [0607-Cooking.md](../0600-Professions/0607-Cooking.md) · [1000-Economy.md](../1000-Economy/1000-Economy.md)

---

## 1. Overview

Consumables are single-use or duration-limited items that provide temporary combat or utility benefits, forming a key economic loop between the gathering/production professions and active combat.

## 2. Categories

**Potions** — instant or duration effects (healing, mana restore, temporary stat buffs); crafted via Alchemy ([0605-Alchemy.md](../0600-Professions/0605-Alchemy.md)).

**Food & Drink** — longer-duration, smaller buffs, typically consumed before a dungeon/raid pull; crafted via Cooking ([0607-Cooking.md](../0600-Professions/0607-Cooking.md)).

**Scrolls** — one-time utility effects (temporary teleport, buff duration extension); sourced from vendors or rare quest rewards.

**Bandages/Field Kits** — self-healing tools with a cast time, giving non-healer players a limited out-of-combat sustain option.

## 3. Design Rules

* Combat consumables (potions, scrolls) should share a limited number of cooldown categories to prevent stacking too many effects at once from trivializing difficulty.
* Food and potion buffs should never be mandatory for normal-difficulty content, only for Heroic/Mythic dungeons and raids ([0106-Dungeons.md](../0100-World/0106-Dungeons.md), [0107-Raids.md](../0100-World/0107-Raids.md)), to keep the leveling and casual experience approachable.
* Consumables should be a meaningful Aurum sink and profession revenue source — see [1000-Economy.md](../1000-Economy/1000-Economy.md).

## 4. Acquisition

Primarily player-crafted (Alchemy, Cooking) or vendor-purchased with basic recipes; rare/powerful consumables may be quest or drop-gated.

## 5. Consumable Tiers

| Tier | Availability | Example |
| --- | --- | --- |
| Basic | Vendor, low-level recipe | Minor Healing Potion |
| Standard | Profession-crafted, mid-level recipe | Greater Healing Potion |
| Raid-Tier | Profession-crafted, requires rare materials | Elixir of the Sunken Concord |
| Rare/Unique | Quest or drop-gated, non-craftable | Vial of Aeloria's Tears |

## 6. Cooldown Categories

To prevent consumable stacking from breaking encounter balance, potions share a shared "combat potion" cooldown category, while food buffs, scrolls, and bandages each occupy their own independent category, allowing reasonable combination without runaway power stacking.

## 7. Economic Role

Consumables represent one of the most reliable, renewable Aurum sinks in the game since they are consumed rather than retained, making Alchemy and Cooking consistently profitable professions across all stages of the game — see [1010-Currency-Sinks.md](../1000-Economy/1010-Currency-Sinks.md).
