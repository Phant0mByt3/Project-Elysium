# 103 — Auction House

## Overview
The Auction House is the central player-to-player marketplace, accessible from any major city ([013-Cities.md](013-Cities.md)) and, for a small listing fee, remotely via a premium convenience feature under consideration for a later update.

## Core Features
* **Listings** — sellers set a starting bid and/or buyout price, with a listing duration and small Aurum fee (an economy sink, see [100-Economy.md](100-Economy.md)).
* **Search & Filters** — search by item type, stats, and profession category.
* **Cross-Faction Access** — managed through the neutral Wayfarer's Guild ([033-Factions.md](033-Factions.md)), allowing limited cross-faction trade despite factions otherwise being siloed in parties/guilds.

## Design Rules
* Auction House data should be visible enough for players to make informed pricing decisions, discouraging predatory undercutting wars without artificially fixing prices.
* Bind-on-pickup items (most raid/dungeon drops, see [054-Loot-Tables.md](054-Loot-Tables.md)) are not tradeable via the Auction House, keeping high-end gear progression tied to actual play rather than a pure gold purchase.

## Relationship to Trading
For direct, negotiated player-to-player exchanges outside the open market, see [104-Trading.md](104-Trading.md).
