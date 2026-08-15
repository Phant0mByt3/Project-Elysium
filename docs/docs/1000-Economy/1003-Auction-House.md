# 1003 — Auction House

## Overview
The Auction House is the central player-to-player marketplace, accessible from any major city ([0103-Cities.md](../0100-World/0103-Cities.md)) and, for a small listing fee, remotely via a premium convenience feature under consideration for a later update.

## Core Features
* **Listings** — sellers set a starting bid and/or buyout price, with a listing duration and small Aurum fee (an economy sink, see [1000-Economy.md](1000-Economy.md)).
* **Search & Filters** — search by item type, stats, and profession category.
* **Cross-Faction Access** — managed through the neutral Wayfarer's Guild ([0203-Factions.md](../0200-Lore/0203-Factions.md)), allowing limited cross-faction trade despite factions otherwise being siloed in parties/guilds.

## Design Rules
* Auction House data should be visible enough for players to make informed pricing decisions, discouraging predatory undercutting wars without artificially fixing prices.
* Bind-on-pickup items (most raid/dungeon drops, see [0504-Loot-Tables.md](../0500-Items/0504-Loot-Tables.md)) are not tradeable via the Auction House, keeping high-end gear progression tied to actual play rather than a pure gold purchase.

## Relationship to Trading
For direct, negotiated player-to-player exchanges outside the open market, see [1004-Trading.md](1004-Trading.md).


## Listing Fee Structure

Listing fees scale modestly with the listed price, discouraging spam-listing of unreasonably priced items while remaining a minor cost relative to a successful sale, keeping the fee primarily a currency sink rather than a meaningful barrier to participation.

## Price History and Transparency

The Auction House interface displays recent sale price history for a searched item, helping players price their own listings fairly and reducing the information asymmetry that can otherwise favor only the most dedicated market-watchers.
