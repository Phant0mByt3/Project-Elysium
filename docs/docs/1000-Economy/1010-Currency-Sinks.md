# 1010 — Currency Sinks

**Project:** Elysium MMORPG  
**Category:** Economy  
**Status:** Design Complete — Implementation Pending  
**Related:** [1009-Inflation-Control.md](1009-Inflation-Control.md) · [1001-Currency.md](1001-Currency.md) · [0515-Item-Durability.md](../0500-Items/0515-Item-Durability.md) · [0900-Housing.md](../0900-Player-Systems/0900-Housing.md)

---

## 1. Overview

Currency Sinks are the systems and costs that permanently remove Aurum (and occasionally other currencies) from the player economy. They are essential for long-term economic stability.

---

## 2. Major Sinks

| Sink | Notes |
|------|-------|
| **Repairs** | Durability loss from death and combat |
| **Training / Respec** | Talent and specialisation changes |
| **Vendor purchases** | Consumables, reagents, convenience items |
| **Crafting costs** | Optional fees or high material conversion |
| **Transmog & cosmetics** | Appearance changes and some unlocks |
| **Housing / Guild Hall** | Upkeep or upgrade costs |
| **Fast travel** | Distance-scaled portal or flight costs |
| **Auction House fees** | Listing and sale cuts |
| **Miscellaneous** | Name changes, other quality-of-life services |

---

## 3. Design Rules

1. Sinks should scale reasonably with player wealth so that both new and veteran players feel appropriate costs.
2. No single sink should feel so harsh that it discourages the associated activity.
3. New sinks are preferred over simply reducing sources when inflation pressure appears.
