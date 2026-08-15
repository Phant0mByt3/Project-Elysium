# 1013 — Merchant System

**Project:** Elysium MMORPG  
**Category:** Economy  
**Status:** Design Complete — Implementation Pending  
**Related:** [1002-Vendors.md](1002-Vendors.md) · [1000-Economy.md](1000-Economy.md) · [0209-NPCs.md](../0200-Lore/0209-NPCs.md) · [1014-NPC-Economy.md](1014-NPC-Economy.md)

---

## 1. Overview

The Merchant System covers all NPC vendors: general goods, weapon/armour vendors, profession suppliers, repair NPCs, and specialised faction or reputation vendors. Merchants are the reliable, always-available backbone of the economy for basic needs.

---

## 2. Merchant Types

| Type | Role |
|------|------|
| **General Goods** | Consumables, basic supplies, bags |
| **Gear Vendors** | Level-appropriate white/green items, some BoE |
| **Profession Suppliers** | Reagents, tools, recipes |
| **Repair** | Durability restoration |
| **Reputation / Faction** | Exclusive gear and cosmetics gated by standing |
| **Special / Rotating** | Limited stock or event merchants |

---

## 3. Design Rules

1. Every major hub has the essential merchant services.
2. Prices are consistent with the intended gold flow at that level band.
3. Reputation vendors provide long-term goals without being the only source of competitive gear.
4. Merchants have names, personalities, and placement that support immersion ([1404-NPC-Writing-Guide.md](../1400-Development/1404-NPC-Writing-Guide.md)).


---

## Additional Detail: Traveling Merchants

Beyond static city and village vendors, occasional traveling merchant NPCs appear at world events ([0109-World-Events.md](../0100-World/0109-World-Events.md)) or during seasonal content, offering limited-time or event-exclusive goods, giving the merchant system a light dynamic dimension beyond fixed vendor lists.

## Merchant Reputation Interaction

Certain merchants offer improving discounts as a player's reputation with the relevant faction or organization increases, tying the merchant system directly into the reputation system in [0706-Reputation.md](../0700-Quests/0706-Reputation.md).
