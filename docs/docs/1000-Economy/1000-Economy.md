# 1000 — Economy

## Overview
Elysium's economy is player-driven wherever possible, built around Aurum ([1001-Currency.md](1001-Currency.md)) as the primary currency and the Auction House ([1003-Auction-House.md](1003-Auction-House.md)) as the primary player-to-player marketplace.

## Design Goals
* **Meaningful Aurum sinks** — repair costs, fast travel ([0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md)), consumables ([0507-Consumables.md](../0500-Items/0507-Consumables.md)), and cosmetic purchases keep currency circulating rather than accumulating indefinitely.
* **Profession relevance** — gathering and crafting professions ([0600-Professions.md](../0600-Professions/0600-Professions.md)) should be a genuine income source at every level range, not just at max level.
* **Stability** — server-wide price monitoring should inform balance adjustments to material drop rates and vendor prices, preventing runaway inflation.

## Currency Types
Covered in detail in [1001-Currency.md](1001-Currency.md), including Aurum and the rarer Sundered Shards.

## Player-to-Player Systems
* Vendors ([1002-Vendors.md](1002-Vendors.md))
* Auction House ([1003-Auction-House.md](1003-Auction-House.md))
* Direct Trading ([1004-Trading.md](1004-Trading.md))
* Mail ([1005-Mail.md](1005-Mail.md))
* Banking ([1006-Banking.md](1006-Banking.md))

## Anti-Exploitation
Gold-selling, botting, and market manipulation are treated as a security concern as much as an economic one — see [1206-Security.md](../1200-Technical/1206-Security.md) and [1207-Anti-Cheat.md](../1200-Technical/1207-Anti-Cheat.md).


## Regional Economic Variation

Material and price patterns naturally vary by region — Vethmoor's contested border regions see higher prices for combat consumables, while Aurelia's stable farmland regions see cheaper food materials — giving the economy a geographic texture beyond a single flat global market, detailed further in [1015-Regional-Economies.md](1015-Regional-Economies.md).

## Economic Health Monitoring

The live operations and design teams jointly monitor Auction House price trends, currency supply growth, and material availability post-launch, using the analytics pipeline described in [2006-Analytics.md](../2000-Operations/2006-Analytics.md) to catch inflationary or deflationary trends early — see [1009-Inflation-Control.md](1009-Inflation-Control.md) and [1008-Economic-Balance.md](1008-Economic-Balance.md) for the response process.

## Ownership

Economic design is jointly owned by the Lead Game Designer and Technical Lead, given the tight coupling between economic balance and the underlying transaction systems — see [0007-Team-Structure.md](../0000-Project/0007-Team-Structure.md).
