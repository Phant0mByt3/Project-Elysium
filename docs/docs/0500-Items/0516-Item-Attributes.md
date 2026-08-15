# 0516 — Item Attributes

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0304-Stats.md](../0300-Characters/0304-Stats.md) · [0500-Weapons.md](0500-Weapons.md) · [0501-Armour.md](0501-Armour.md) · [0502-Accessories.md](0502-Accessories.md) · [0309-Balance.md](../0300-Characters/0309-Balance.md)

---

## 1. Overview

Item attributes are the numerical and mechanical properties that items grant when equipped or used. They are the primary bridge between the item system and the character stat framework defined in [0304-Stats.md](../0300-Characters/0304-Stats.md).

---

## 2. Attribute Categories

| Category | Examples | Notes |
|----------|----------|-------|
| **Primary Stats** | Strength, Intellect, Agility, Stamina | Scale with item level and armour type |
| **Secondary Stats** | Critical Strike, Haste, Mastery, Versatility | Subject to diminishing returns at high values |
| **Defensive** | Armor, Resistances, Avoidance | Primarily on armour and shields |
| **Weapon** | Weapon damage, attack speed, type | Determines auto-attack and ability scaling |
| **Special / Unique** | On-use effects, procs, set bonuses, Legendary powers | See [0517-Unique-Effects.md](0517-Unique-Effects.md) and Legendary/Relic docs |

---

## 3. Design Rules

1. Item level is the main driver of raw power; secondary stats and unique effects provide build identity.
2. No single secondary stat should dominate all itemisation; balance work in [0309-Balance.md](../0300-Characters/0309-Balance.md) keeps options open.
3. Attributes are always shown clearly on the tooltip with comparison to currently equipped gear.
4. Random affixes (if used) are constrained so that the worst possible roll is still usable and the best roll is exciting but not mandatory.

---

## 4. Technical Notes

Attribute packages are data-driven. The server calculates final character stats from equipped items + talents + buffs; the client displays the results but does not own the authoritative values.


---

## 5. Secondary Stat Diminishing Returns

Secondary stats (Critical Strike, Haste, Mastery, Versatility) use a soft diminishing-returns curve past certain thresholds, preventing a single stat from being stacked to the exclusion of all others and keeping itemization decisions interesting throughout progression.

## 6. Attribute Budget by Item Level

Total attribute value scales predictably with item level, allowing designers and players alike to reason about relative item power at a glance even before reading a full tooltip.
