# 0612 — Profession Materials

**Project:** Elysium MMORPG  
**Category:** Professions  
**Status:** Design Complete — Implementation Pending  
**Related:** [0600-Professions.md](0600-Professions.md) · [0613-Resource-Nodes.md](0613-Resource-Nodes.md) · [0508-Crafting.md](../0500-Items/0508-Crafting.md) · [1003-Auction-House.md](../1000-Economy/1003-Auction-House.md)

---

## 1. Overview

Profession materials are the raw and processed ingredients used by gathering and crafting professions. They form a major part of the player-driven economy and are carefully tiered to match the leveling and endgame curves.

---

## 2. Material Tiers

Materials are organised into tiers that roughly correspond to character and profession skill bands:

- **Tier 1** — Starter regions (Southern Shires, early Wildwood)
- **Tier 2** — Mid Aurelia
- **Tier 3** — Late Aurelia / early Vethmoor
- **Tier 4** — Mid-to-late Vethmoor
- **Tier 5** — Max-level / pre-raid and raid-tier materials

Each tier introduces new base materials (ores, woods, herbs, leathers, fish, etc.) and processed intermediates.

---

## 3. Design Rules

1. Materials should feel regionally distinct where possible (ash-forged iron from Ember Deeps, frost-touched herbs from Ashenclaw, etc.).
2. Stack sizes are generous to reduce inventory friction.
3. Rare variants and “rich” nodes exist to create excitement and Auction House value without making baseline crafting impossible.
4. Vendor materials exist for convenience but should never completely replace player gathering for high-end crafts.

---

## 4. Economy Interaction

Materials are one of the primary trade goods on the Auction House. Their sinks (crafting, upgrading, consumables) and sources (nodes, mob drops, quest rewards) are monitored as part of overall economic health ([1000-Economy.md](../1000-Economy/1000-Economy.md)).
