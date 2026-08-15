# 1007 — Market System

**Project:** Elysium MMORPG  
**Category:** Economy  
**Status:** Design Complete — Implementation Pending  
**Related:** [1003-Auction-House.md](1003-Auction-House.md) · [1000-Economy.md](1000-Economy.md) · [1004-Trading.md](1004-Trading.md) · [1008-Economic-Balance.md](1008-Economic-Balance.md)

---

## 1. Overview

The Market System is the broad player-driven and NPC-supported framework for buying and selling goods. It encompasses the Auction House, direct trading, vendor interactions, and any regional or specialised marketplaces that emerge.

---

## 2. Components

| Component | Role |
|-----------|------|
| **Auction House** | Primary asynchronous player-to-player marketplace |
| **Direct Trade** | Immediate player-to-player exchange |
| **NPC Vendors** | Fixed or rotating stock, repair, and material sinks/sources |
| **Specialised Markets** | Possible future profession or faction vendors with unique stock |

---

## 3. Design Goals

- Enable a healthy player economy without requiring constant undercutting wars or extreme complexity.
- Give gatherers and crafters reliable outlets for their production.
- Provide buyers with reasonably efficient access to gear, materials, and consumables.
- Support monitoring and intervention tools for economic health and abuse.

---

## 4. Technical Notes

Market operations are transactional and logged. Price history and volume data feed internal economy dashboards and, eventually, limited public APIs.


---

## Additional Detail: Market Data Tools

Post-launch, an optional companion website or in-client addon-equivalent tool may expose aggregated (non-personally-identifying) market trend data, helping economically-minded players make informed crafting and trading decisions without requiring third-party scraping tools.

## Regional Price Divergence

Because the Auction House ([1003-Auction-House.md](1003-Auction-House.md)) operates on a single unified market rather than per-city instances, price divergence is driven by supply and demand patterns rather than geography — see [1015-Regional-Economies.md](1015-Regional-Economies.md) for how regional material availability still creates natural specialization.
